#!/usr/bin/env python3
"""Build 1-4 cup logo replacements safely, from a verified PES 2017 Lote 06 CPK.

User-owned CPK + user-approved 256x256 PNG images are required inputs.
The script does not distribute game data or third-party logo files.
"""
import argparse
import json
import tempfile
from pathlib import Path
from shutil import copyfile
from PIL import Image

from patch_competition_logo import patch, hash_file, read_utf, DIRECTORY

EXPECTED_BASE_SHA = "c47883f6093dcdc786cf6a83e41d1a2116afb147a76a7d6fea74c2cbb0b78761"
EXPECTED_BASE_BYTES = 246746371

TARGETS = {
    "coppa_italia": "emb_0016_l.png",
    "coupe_de_france": "emb_0018_l.png",
    "knvb_beker": "emb_0019_l.png",
    "taca_de_portugal": "emb_0020_l.png",
}

def get_rows(path):
    with path.open("rb") as h:
        header = read_utf(h, 0, b"CPK ")
        toc = read_utf(h, header["rows"][0]["TocOffset"], b"TOC ")
    return ({r["FileName"]: r for r in toc["rows"] if r["DirName"] == DIRECTORY},
            len(toc["rows"]))

def extract_bytes(path, row):
    with path.open("rb") as h:
        h.seek(row["FileOffset"] + 0x800)
        return h.read(row["FileSize"])

def build(source, output, logodir, requested, allow_identity=False):
    source, output, logodir = map(Path, (source, output, logodir))
    if not 1 <= len(requested) <= 4:
        raise ValueError("Only 1-4 distinct cup logos per batch")
    if len(set(requested)) != len(requested) or set(requested)-set(TARGETS):
        raise ValueError("Unknown or duplicate logo ID")
    if source.resolve() == output.resolve():
        raise ValueError("The original input must never be overwritten")
    if source.stat().st_size != EXPECTED_BASE_BYTES or hash_file(source) != EXPECTED_BASE_SHA:
        raise ValueError("Input CPK must match the user-tested Lote 06 SHA-256")
    baseline, n = get_rows(source)
    if n != 2784:
        raise ValueError("Unexpected CPK resource count")
    for key in requested:
        p = logodir / (key + ".png")
        if not p.exists():
            raise FileNotFoundError("Missing vetted logo: " + str(p))
        b = p.read_bytes()
        with Image.open(p) as im:
            im.load()
            if im.format != "PNG" or im.mode != "P" or im.size != (256, 256):
                raise ValueError("Expected indexed 256x256 PNG: " + str(p))
        if b == extract_bytes(source, baseline[TARGETS[key]]) and not allow_identity:
            raise ValueError("Asset is identical to the current logo: " + str(p))
    if output.exists():
        raise FileExistsError("Refusing to overwrite " + str(output))
    stages = []
    with tempfile.TemporaryDirectory(prefix="pes17_cup_batch_") as td:
        td = Path(td)
        prev = source
        for i, key in enumerate(requested):
            temp = td / f"step{i}.cpk"
            stages.append(patch(prev, logodir/(key+".png"), temp, TARGETS[key]))
            prev = temp
        copyfile(prev, output)
    result, count = get_rows(output)
    if count != n or output.stat().st_size != source.stat().st_size:
        raise AssertionError("CPK size or resource count changed")
    changed = [name for name, old in baseline.items()
               if old != result[name] or extract_bytes(source, old) != extract_bytes(output, result[name])]
    expected = {TARGETS[key] for key in requested}
    if set(changed)-expected:
        raise AssertionError(f"Modified extra resources: {changed}")
    if set(changed) != expected and not allow_identity:
        raise AssertionError(f"Required logo changes missing: {changed}")
    return {"status": "BINARY_VERIFIED_ANDROID_TEST_PENDING",
            "input": source.name, "output": output.name,
            "input_sha256": hash_file(source), "output_sha256": hash_file(output),
            "bytes": output.stat().st_size,
            "resources_total": n, "modified_resources": changed,
            "unmodified_resources_bytewise": n-len(changed),
            "batch_steps": stages}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--logos", type=Path, required=True)
    parser.add_argument("--cups", nargs="+", required=True, choices=list(TARGETS))
    args = parser.parse_args()
    print(json.dumps(build(args.input, args.output, args.logos, args.cups), indent=2))
