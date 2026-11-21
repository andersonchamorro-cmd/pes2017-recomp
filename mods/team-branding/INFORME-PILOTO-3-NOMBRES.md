# Prueba local de nombres de clubes — PES 2017 Android (Xbox 360)

Estado: **CPK generado; comprobaciones binarias correctas; funcionamiento en Android no probado**.

## Archivo analizado

- Archivo aportado por el usuario: `dt10_x36.cpk`, 1 138 688 bytes
- SHA-256 del original: `2320dea228b668284a7d8ec394d34868694214d990a44fe2133ce7b60f797ef7`
- Contenedor CRI CPK: 156 recursos
- Recurso modificado: `common/etc/pesdb/Team.bin`
- `Team.bin` comprimido con WESYS/zlib, 28 792 bytes originalmente, 701 400 bytes descomprimido
- Mapa de modificaciones de prueba:

| Antes | Después |
|---|---|
| LONDON FC | CHELSEA FC |
| MAN RED | MANCHESTER UNITED |
| MAN BLUE | MANCHESTER CITY |

En la copia original de Team.bin, cada una de las tres cadenas principales aparece exactamente una vez. Se reemplazaron en campos fijos, preservando la longitud descomprimida y la estructura restante. La compresión del recurso quedó en 28 589 bytes y cabe sin desplazar otros recursos.

## Verificaciones realizadas

- CPK de salida conserva el tamaño total de 1 138 688 bytes
- Tabla TOC revalidada y 156 referencias conservadas
- Los otros 155 recursos extraídos permanecen byte por byte idénticos a los originales
- Recurso Team.bin modificado se descomprime correctamente y sus datos coinciden con los esperados
- Metadatos EnabledPackedSize/EnabledDataSize actualizados de forma consistente con el archivo original
- SHA-256 del CPK modificado: `17080bb0ed816eec35ed6da3adc25e39392cd648729eded8ed0f0ca3178d722e`

El binario modificado se entregó únicamente al usuario, en la conversación. **No subir archivos comerciales del juego a este repositorio público.**

## Prueba en el teléfono

1. Salir de PES 2017 por completo.
2. Conservar respaldado el `dt10_x36.cpk` original en Download u otra ubicación ajena a `Android/data`.
3. Copiar el archivo de prueba al directorio del juego que actualmente contiene `default.xex` y `dt10_x36.cpk`, después de renombrarlo exactamente a `dt10_x36.cpk`.
4. Abrir PES y revisar los tres nombres en selección de equipos. Comprobar si los datos de edición guardados prevalecen sobre la base CPK.
5. Probar un partido y luego guardado/carga de Liga Máster.
6. Ante cualquier error, cerrar PES y restaurar el `dt10_x36.cpk` original.

**No hay escudos nuevos en este piloto.** Para escudos hay que analizar `dt15_x36.cpk` u otros contenedores de imágenes antes de intentar modificaciones.

## Referencias técnicas

- Contenedor CRI CPK y tablas @UTF: https://github.com/the4chancup/pes-file-tools
- Proyecto del port de Android: https://github.com/dzakyraf/pes2017-recomp
- Referencia sobre las tablas Team.bin de PES 2017: https://www.pesoccerworld.com/descargar/team-editor-manager-2017-v2-4-by-lagun-2-4966.html
