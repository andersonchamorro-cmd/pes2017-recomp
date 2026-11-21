#!/usr/bin/env python3
"""Safe single-logo patcher for PES 2017 Xbox 360 CRI CPK emblemLc assets.

Private, user-owned game archives only. No copyrighted game data included.
The script never modifies the input and checks every unrelated TOC entry and byte sequence.
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import struct
from pathlib import Path
from PIL import Image

FMT = {0:('>B',1), 2:('>H',2), 4:('>I',4), 6:('>Q',8), 8:('>f',4)}
DIRECTORY = 'common/render/symbol/emblemLc'

def crypt(data):
    state=0x5f
    out=bytearray(data)
    for i in range(len(out)):
        out[i]^=state
        state=(state*0x15)&0xff
    return bytes(out)

def read_utf(handle,offset,signature):
    handle.seek(offset)
    sig,zero,size=struct.unpack('<4sIQ',handle.read(16))
    if sig!=signature: raise ValueError(f'CPK section signature mismatch at {offset}: {sig!r}')
    raw=handle.read(size)
    plain=raw if raw.startswith(b'@UTF') else crypt(raw)
    if plain[:4]!=b'@UTF': raise ValueError('Cannot decode CPK UTF table')
    _,bodylen,rows_off,strings_off,data_off,table_name,ncols,row_size,nrows=struct.unpack('>4sIIIIIHHI',plain[:32])
    base=8
    def get_string(off):return plain[base+strings_off+off:].split(b'\0',1)[0].decode('utf-8')
    def value(stream,tp):
        if tp in FMT: return struct.unpack(FMT[tp][0],stream.read(FMT[tp][1]))[0]
        if tp==10: return get_string(struct.unpack('>I',stream.read(4))[0])
        if tp==11:
            off,count=struct.unpack('>II',stream.read(8))
            return plain[base+data_off+off:base+data_off+off+count]
        raise ValueError(f'Unsupported CPK field type {tp}')
    cols=[]; stream=io.BytesIO(plain[32:])
    for _ in range(ncols):
        spec,off=struct.unpack('>BI',stream.read(5))
        mode,tp=spec>>4,spec&15
        const=value(stream,tp) if mode==3 else None
        cols.append((get_string(off),tp,mode,const))
    rows=[]
    for i in range(nrows):
        row_stream=io.BytesIO(plain[base+rows_off+row_size*i:base+rows_off+row_size*(i+1)])
        rows.append({name:(const if mode==3 else value(row_stream,tp) if mode==5 else None)
                     for name,tp,mode,const in cols})
    return {'rows':rows,'cols':cols,'offset':offset,'raw':raw,'plain':plain,'rows_off':rows_off,'row_size':row_size,'encrypted':not raw.startswith(b'@UTF')}

def hash_file(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for data in iter(lambda:f.read(8*1024*1024),b''):
            h.update(data)
    return h.hexdigest()

def patch(source,logo,target,resource):
    source,logo,target=map(Path,(source,logo,target))
    if not source.is_file() or not logo.is_file():raise FileNotFoundError('Input CPK or PNG not found')
    if source.resolve()==target.resolve():raise ValueError('Refusing to overwrite original input')
    if not resource.startswith('emb_') or '/' in resource or not resource.endswith('_l.png'):
        raise ValueError('Resource must be a single CPK competition emblem filename')
    new_bytes=logo.read_bytes()
    with Image.open(io.BytesIO(new_bytes)) as im:
        im.load()
        if im.size!=(256,256) or im.mode!='P':
            raise ValueError(f'Expected indexed 256 x 256 PNG, got {im.size} {im.mode}')
        if im.format!='PNG':raise ValueError('Expected a real PNG file')
    with source.open('rb') as fin:
        header=read_utf(fin,0,b'CPK ')
        toc_off=header['rows'][0]['TocOffset']
        toc=read_utf(fin,toc_off,b'TOC ')
        rows=toc['rows']
        if len(rows)!=2784:raise ValueError(f'Unexpected CPK resource count: {len(rows)}')
        if toc['row_size']!=28 or [x[0] for x in toc['cols']][:4]!=['DirName','FileName','FileSize','ExtractSize']:
            raise ValueError('TOC layout not recognized; abort before writing')
        matches=[(i,r) for i,r in enumerate(rows) if r['DirName']==DIRECTORY and r['FileName']==resource]
        if len(matches)!=1:raise ValueError(f'Ambiguous or missing resource {resource}: {len(matches)} matches')
        index,old=matches[0]
        by_offset=sorted(rows,key=lambda r:r['FileOffset'])
        pos=next(i for i,r in enumerate(by_offset) if r is old)
        next_off=by_offset[pos+1]['FileOffset'] if pos+1<len(rows) else source.stat().st_size-0x800
        capacity=next_off-old['FileOffset']
        if len(new_bytes)>capacity:raise ValueError(f'New asset {len(new_bytes)} > free slot {capacity} bytes')
        original_png_off=old['FileOffset']+0x800
        fin.seek(original_png_off);original_data=fin.read(old['FileSize'])
        if not original_data.startswith(b'\x89PNG\r\n\x1a\n'):raise ValueError('Original resource is not a PNG')
        mutable=bytearray(toc['plain'])
        row_packed_offset=8+toc['rows_off']+index*toc['row_size']+8
        if struct.unpack_from('>II',mutable,row_packed_offset)!=(old['FileSize'],old['ExtractSize']):
            raise ValueError('TOC size field did not match expected resource')
        struct.pack_into('>II',mutable,row_packed_offset,len(new_bytes),len(new_bytes))
    temp=target.with_suffix(target.suffix+'.incomplete')
    if temp.exists():raise FileExistsError('Temporary file already exists: '+str(temp))
    try:
        shutil.copyfile(source,temp)
        with temp.open('r+b') as fout:
            fout.seek(original_png_off);fout.write(new_bytes)
            fout.seek(toc_off+16);fout.write(crypt(mutable) if toc['encrypted'] else mutable)
        with source.open('rb') as fin, temp.open('rb') as fout:
            nh=read_utf(fout,0,b'CPK ')
            nr=read_utf(fout,toc_off,b'TOC ')['rows']
            if nh['rows']!=header['rows'] or len(nr)!=len(rows):raise ValueError('Header or resource count changed')
            for i,(r,newr) in enumerate(zip(rows,nr)):
                fin.seek(r['FileOffset']+0x800)
                fout.seek(newr['FileOffset']+0x800)
                if i==index:
                    if (newr['FileSize'],newr['ExtractSize'])!=(len(new_bytes),len(new_bytes)):
                        raise ValueError('Updated TOC lengths incorrect')
                    if fout.read(newr['FileSize'])!=new_bytes:raise ValueError('Target resource content mismatch')
                else:
                    if r!=newr or fin.read(r['FileSize'])!=fout.read(newr['FileSize']):
                        raise ValueError('Untargeted resource changed: '+str(r['FileName']))
        if temp.stat().st_size!=source.stat().st_size:raise ValueError('The CPK container size changed')
        os.replace(temp,target)
    finally:
        if temp.exists():temp.unlink()
    return {'input':source.name,'input_sha256':hash_file(source),'output':target.name,'output_sha256':hash_file(target),
            'resource':DIRECTORY+'/'+resource,'old_bytes':len(original_data),'new_bytes':len(new_bytes),
            'total_resources':len(rows),'unchanged_resources':len(rows)-1,
            'container_bytes':target.stat().st_size,'validation':'PASSED: TOC, logo, all other entries byte-for-byte'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',required=True,type=Path,help='Last known-good cumulative dt15_x36.cpk')
    p.add_argument('--logo',required=True,type=Path,help='Indexed 256x256 PNG that will replace one resource')
    p.add_argument('--output',required=True,type=Path,help='New CPK to write; input never overwritten')
    p.add_argument('--resource',default='emb_0015_l.png',help='Exact competition logo filename')
    args=p.parse_args()
    print(json.dumps(patch(args.input,args.logo,args.output,args.resource),indent=2))
if __name__=='__main__':main()
