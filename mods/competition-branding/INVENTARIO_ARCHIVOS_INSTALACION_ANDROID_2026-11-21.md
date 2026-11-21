# PES 2017 Android — inventario de archivos instalado (capturas del usuario)

**Fecha:** 21/11/2026. **Origen:** cuatro capturas del explorador de Android con el contenido de la instalación. Los nombres y tamaños son **visibles en pantalla**, no inspección binaria de los CPK. Carpetas de la ruta `Android/data/com.pes2017.recomp/files/`.

## Ubicación y protección de datos del usuario

- Directorio de datos de app `Android/data/com.pes2017.recomp/files/`.
- Carpeta de recursos de juego: `PES 2017 BY MUSTAFA GAMERS/` (**40 elementos**, según el explorador).
- Carpetas externas a recursos del juego, **no modificar**: `saves/` (5 elementos), `save_backups/` (5 elementos).
- Archivos auxiliares: `game.log`, `launcher.log`, `shader_cache.bin`; no alterarlos para actualizar logos o textos.

## Archivo principal y CPK visibles en carpeta del juego

- `default.xex` (~30,98 MB).
- `dt00_x36.cpk` (~12,79 MB).
- `dt10_x36.cpk` (~1,12 MB) — el usuario ya compartió una copia que fue analizada en la fase de nombres; contiene `Competition.bin` y otras tablas deportivas, NO cadenas visibles de menús.
- `dt11_x36.cpk` (~153,52 MB).
- `dt12_x36.cpk` (~589,33 MB).
- `dt13_x36.cpk` (~22,83 MB).
- `dt15_x36.cpk` (~235,31 MB) — archivo de emblemas; acumulado Lote 10, ya probado en menús.
- `dt16_x36.cpk` (~4,24 MB).
- `dt17_x36.cpk` (~120,79 KB).
- `dt18_x36.cpk` (~12,83 MB).
- `dt19_x36.cpk` (~1,20 MB).
- **`dt20_eng_x36.cpk` (~359,55 KB)** — siguiente archivo a solicitar para el piloto de **nombres oficiales**, coincidencia exacta del nombre en instalación.
- `dt20_fra_x36.cpk` (~371,55 KB).
- `dt20_ger_x36.cpk` (~379,55 KB).
- `dt20_ita_x36.cpk` (~361,55 KB).
- `dt20_nld_x36.cpk` (~369,55 KB).
- `dt20_rus_x36.cpk` (~431,55 KB).
- `dt20_tur_x36.cpk` (~371,55 KB).
- `dt30_x36.cpk` (~248,74 MB).
- `dt32_x36.cpk` (~260,62 MB).
- `dt33_x36.cpk` (~47,20 MB).
- `dt34_x36.cpk` (~182,66 MB).
- `dt35_x36.cpk` (~96,87 MB).
- `dt36_x36.cpk` (~1,44 GB).
- `dt40_all.cpk` (~175,38 MB).
- `dt41_eng_all.cpk` (~473,14 MB).
- `dt41_fra_all.cpk` (~428,82 MB).
- `dt41_ger_all.cpk` (~495,77 MB).
- `dt41_ita_all.cpk` (~453,05 MB).
- `dt42_x36.cpk` (~64,63 KB).
- **`dt43_eng_x36.cpk` (~235,79 KB)** — **segundo candidato** en inglés en caso de que `dt20_eng_x36.cpk` no contenga los textos.
- `dt43_fra_x36.cpk` (~237,55 KB).
- `dt43_ger_x36.cpk` (~223,12 KB).
- `dt43_ita_x36.cpk` (~209,04 KB).
- `dt44_all.cpk` (~835,12 MB).
- `dt70_x36.cpk` (~426,23 MB).
- `dt90_x36.cpk` (~1,32 MB).
- `nxeart` (~744 KB).
- `su2008d200_00000000` (~8,03 MB).
- Carpeta `$SystemUpdate`.

El listado anterior reproduce solamente **nombres visibles** y tamaños aproximados del explorador; **no afirmar que los otros archivos tienen un contenido específico aún no inspeccionado**.

## Acción siguiente de la fase 2B (nombres oficiales)

**Solicitar `dt20_eng_x36.cpk` exacto**, no `dt20_eng.cpk`. Al recibirlo, inventariar tabla de contenido, examinar recursos, comprobar presencia y representación de `English League`, `Italian League` y `Portugal League`. Si faltan, pedir **`dt43_eng_x36.cpk`** como candidato siguiente. No solicitar los dos de antemano si solo se necesita el primero. No reemplazar identificadores internos de `dt10`.

El plan principal de sustitución de ligas se mantiene: `PEU → Bundesliga`, `PLA → Liga BetPlay`, `PAS → Liga MX`. No instalar el nombre antes de convertir correctamente equipos/IDs y estructura.

## Restricciones permanentes
- **No borrar ni sobrescribir `saves` ni `save_backups`**, ni parches `dt15` del usuario.
- En fase de nombres, modificar únicamente el CPK de idioma realmente responsable de cadenas, conservando respaldo, conteo de entradas y hashes, verificando prueba en Android.
- No subir archivos de juego/CPK ni assets de terceros al repositorio público; guardar solo inventario y documentación.
