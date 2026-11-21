# PES 2017 Xbox 360 Android — investigación de escudos dt15

**Estado:** extracción y reconstrucción verificadas; **escudos reales todavía pendientes de recibir y de probar en el teléfono**. Mantener intacta la copia original.

## Archivo recibido e inspeccionado

- Nombre: `dt15_x36.cpk`
- Tamaño en bytes: **244603008** (233,27 MiB)
- SHA-256: `c51851bc2a94c64d6be9788bdc8583e4dab731336d671d4cb8508a5dec116c33`
- Formato: CRI CPK con tablas @UTF cifradas y **2784 recursos**.
- Ruta interna: `common/render/symbol/flag/`
- Las versiones pequeñas de los escudos son PNG indexados (P) de 128 × 128 y las grandes son PNG de 256 × 256, con transparencia.

| Equipo | ID | Archivo 128 × 128 | Archivo 256 × 256 |
| --- | --- | --- | --- |
| Manchester United | 0100 | `emblem_0100_f.png` | `emblem_0100_f_l.png` |
| Chelsea | 0102 | `emblem_0102_f.png` | `emblem_0102_f_l.png` |
| Manchester City | 0173 | `emblem_0173_f.png` | `emblem_0173_f_l.png` |

**Correspondencia visual verificada** contra los PNG extraídos del archivo aportado por el usuario: se observan los escudos ficticios 'Man Red', 'London FC' y 'Man Blue'.

## Prueba de reconstrucción

Se realizó una prueba **sin distribuir imágenes comerciales** usando las propias imágenes ficticias extraídas del archivo recibido y reconstruidas en formato PNG con Pillow.

- Se creó un archivo CPK de prueba de 244653746 bytes, con las seis imágenes indexadas reasignadas.
- Se volvió a abrir la tabla CPK/TOC y se validaron posiciones, tamaños y PNG.
- Se compararon los datos binarios de los otros **2778 recursos**: todos son idénticos al original.
- Los únicos cambios de la tabla TOC corresponden a los seis PNG; las nuevas imágenes fueron agregadas al final del CPK, con offsets alineados a 2048 bytes y metadatos de tamaño actualizados.
- El CPK de prueba con las imágenes ficticias fue descartado; no se entrega al usuario como parche de escudos reales.
- Esto es una **validación estructural**, no una validación de que el port cargue los nuevos recursos.

## Próximo paso

Para crear el parche privado de la prueba de tres equipos, hacen falta las **tres imágenes de escudo reales**, preferentemente PNG con fondo transparente, aportadas por el usuario o con derechos adecuados. Se producirán seis PNG (128 y 256 px), se inyectarán en una copia del archivo y se verificará la integridad del resto.

**No cargar ni distribuir el dt15 original ni los emblemas propietarios en repositorios públicos.** Las marcas de los clubes son marcas registradas y pueden estar sujetas a derechos de autor.

Al probar: salir de PES; guardar una copia del dt15 original fuera de Android/data; reemplazar solo el dt15 de la instalación activa; verificar tres escudos, un partido, reinicio y guardado/carga; restaurar el original ante cualquier fallo.

Fuente general del formato CPK: https://github.com/the4chancup/pes-file-tools/blob/master/lib/pes_file_tools/cpk.py
