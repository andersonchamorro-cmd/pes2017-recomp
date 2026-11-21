# Lote 04 — Championship + Spanish Segunda 2016/17

**Estado:** generado y verificado estructuralmente; **pendiente de prueba dentro del port de Android**.

Partimos de las últimas versiones acumulativas que el usuario había confirmado para Premier League, LaLiga y Serie A. Comparamos las 8 capturas de English 2nd Division y Spanish 2nd Division con una tabla de IDs de PES 2017 y dos listas históricas de nombres. **No se cambian fichajes ni divisiones; temporada base 2016/17.**

## Cambios

- `dt10_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_NOMBRES.cpk`: 24 nuevos nombres de Championship + 22 de Segunda española = **46 nombres**.
- `dt15_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_ESCUDOS.cpk`: **92 PNG** reemplazados (128px y 256px para cada uno de 46 clubes).
- No alterados los 155 recursos restantes del `dt10`, ni los 2692 recursos restantes del `dt15`.
- Todos los nombres de las tres ligas anteriores y sus PNG permanecieron sin cambios.
- Los escudos se procesaron desde `JoseArroyave/football-logos` mediante el flujo temporal `.github/workflows/fetch-segundas-crests.yml` sin alojar los binarios del juego o imágenes en el historial Git.
- **Los nombres y logotipos de las competiciones en el menú no fueron modificados**: requieren localizar otros recursos de UI.

## Huellas SHA-256 y tamaños

| Archivo privado | SHA-256 | Bytes |
|---|---|---:|
| dt10_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_NOMBRES.cpk | `8a55d53d557ab9a10792b6041553f7a600993fabef049fe5b3bcccd355df0468` | 1138688 |
| dt15_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_ESCUDOS.cpk | `a0e597f06eb3eb107b3f44f0986f231ccd9d264ad3203f9b06aef94c7d3a37df` | 246052251 |

Bases anteriores:

- `dt10` SHA-256 `c5dd268ac0a3846106204b50668b2fdfe4bd86f87751631ed5592ad782cfd7bb`
- `dt15` SHA-256 `d5e59d9a75e62cb32f1d393e57ec00df5ad05ebfc7feca0ed78e45518e50d45a`

## Validación realizada

1. Todos los nombres antiguos estaban presentes exactamente una vez en el campo correspondiente de `Team.bin`; se han sustituido sin variar tamaño de registros ni base de jugadores.
2. Se conservaron los otros 155 recursos del `dt10` byte por byte.
3. Se localizaron los 92 PNG esperados mediante los IDs correctos, sin duplicados ni archivos ausentes.
4. Se reconstruyó el índice TOC y se verificó el contenido PNG, la paleta, la transparencia y la resolución.
5. Los otros 2692 recursos del `dt15` permanecieron idénticos, incluidos los escudos acumulativos anteriores.
6. **La compatibilidad con partidas guardadas y los FPS en Android requieren una prueba del usuario**.

## Instalación y reversión

1. Cerrar completamente PES.
2. Guardar copia de seguridad **de ambos** `dt10_x36.cpk` y `dt15_x36.cpk` instalados actualmente, fuera de `Android/data`.
3. Renombrar ambos CPK nuevos a sus nombres originales.
4. Reemplazar ambos dentro de `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
5. Probar Aston Villa, Leeds United, Newcastle United, Cádiz, Real Valladolid y Rayo Vallecano; verificar también Chelsea, Real Madrid y Juventus.
6. Comprobar un partido y el guardado/carga de Liga Máster.
7. Si hay un fallo, cerrar PES y restaurar **ambos** archivos respaldados.

Fuentes de mapeo de equipos:

- https://parchespes2017.blogspot.com/2016/10/team-list-id-pes-2017.html
- https://pes.football/news/pravilnye_nazvanija_vsekh_ne_licenzirovannykh_komand_v_pes_2017_spisok/2016-08-31-3348
