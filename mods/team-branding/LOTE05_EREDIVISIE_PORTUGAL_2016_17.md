# Lote 05 — Eredivisie y Liga Portugal (temporada base 2016/17)

**Estado:** parches acumulativos de nombres/escudos construidos y **verificados estructuralmente**; requieren prueba de compatibilidad en el Xiaomi Mi 10T. No se reemplazaron recursos de interfaz ni datos deportivos.

## Análisis de capturas

- **Eredivisie:** 18 equipos visibles, todos con nombres y emblemas reales; **no modificar**.
- **Portugal League:** 18 equipos; SL Benfica (191) y Sporting CP (193) ya licenciados. **16 clubes** con nombre y escudo ficticios.
- El FC Porto original aparece como `DL BLUE WHITE` (ID 192); no confundir con CD Feirense, que es `DL AZURE BLUE` (ID 2385).

## Identificadores y correspondencias

| PES ID | Ficticio | Nombre nuevo |
|---:|---|---|
| 2380 | ARIMELCAO | FC AROUCA |
| 1973 | BLEMOTAO | CF OS BELENENSES |
| 4323 | BORFECAO | BOAVISTA FC |
| 1974 | BRESIGNE | SC BRAGA |
| 4085 | TM BLUE RED | GD CHAVES |
| 2383 | ESTRALPAO | GD ESTORIL PRAIA |
| 2385 | DL AZURE BLUE | CD FEIRENSE |
| 1976 | MASEADEIRA | CS MARITIMO |
| 2388 | MERASZILHO | MOREIRENSE FC |
| 1944 | NARDIMCOL | CD NACIONAL |
| 1978 | PODEFTEZA | FC PACOS DE FERREIRA |
| 192 | DL BLUE WHITE | FC PORTO |
| 1979 | ROVANECHE | RIO AVE FC |
| 2614 | BA YELLOW GREEN | CD TONDELA |
| 1804 | VISICUTAO | VITORIA SC GUIMARAES |
| 1981 | VERFOLCAO | VITORIA FC SETUBAL |

Nombres se almacenan como ASCII en `Team.bin` para conservar la codificación del port. Las grafías en portugués con acentos se muestran sin diacríticos por esta limitación deliberada.

## Resultados privados

| Archivo | SHA-256 | Bytes |
|---|---|---:|
| `dt10_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_PORTUGAL_NOMBRES.cpk` | `68e509e63d164d81c6717bab3608153b68ea1804171c3792aa2a61657a49f238` | 1138688 |
| `dt15_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_PORTUGAL_ESCUDOS.cpk` | `65768169d1f7c85c0db5f5310c143fcac870571da90caa6c224636f5787705a1` | 246359253 |

Bases anteriores verificadas:

- `dt10`: `8a55d53d557ab9a10792b6041553f7a600993fabef049fe5b3bcccd355df0468`
- `dt15`: `a0e597f06eb3eb107b3f44f0986f231ccd9d264ad3203f9b06aef94c7d3a37df`

## Aseguramiento de calidad

1. **16 nombres:** cada cadena ficticia apareció una sola vez en el lugar esperado de `Team.bin`; coincidencia total de contenido excepto las 16 sustituciones.
2. El tamaño de `Team.bin` descomprimido permanece en 701400 bytes; compresión, índices y TOC del `dt10` pasan validación.
3. Se conservaron byte a byte los **155 recursos ajenos a Team.bin** en `dt10`.
4. **32 PNG de escudos**: PNG válidos de paleta y transparencia, 128px y 256px, IDs comprobados y sin duplicados.
5. Se conservaron byte a byte los restantes **2752 recursos del `dt15`**, incluidos todos los emblemas de Premier, LaLiga, Serie A, Championship y Segunda.
6. No se tocaron ligas, jugadores, fichajes, categorías, calendarios ni el motor gráfico.
7. No se ha probado el juego en el teléfono ni se ha comprobado el guardado de Liga Máster con esta versión.

Origen visual de los 16 SVG: `JoseArroyave/football-logos`. Flujo temporal GitHub Actions `.github/workflows/fetch-portugal-crests.yml`, que no incorpora binarios comerciales al repositorio.

Mapeo validado contra:

- https://parchespes2017.blogspot.com/2016/10/team-list-id-pes-2017.html
- https://pes.football/news/pravilnye_nazvanija_vsekh_ne_licenzirovannykh_komand_v_pes_2017_spisok/2016-08-31-3348

## Instalación y recuperación

1. Cerrar el juego.
2. Guardar copias **de los dos** `dt10_x36.cpk` y `dt15_x36.cpk` en Download.
3. Renombrar cada archivo descargado al nombre original.
4. Sustituir exclusivamente los dos archivos en `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
5. Verificar FC Porto, Feirense, Boavista, SC Braga, Tondela, Vitória Guimarães y Vitória Setúbal. Comprobar equipos anteriormente corregidos.
6. Probar un partido y guardar/cargar Liga Máster.
7. Si falla, cerrar el juego y restaurar ambos CPK respaldados.

**Pendiente en fase UI:** «Portugal League» → logo/nombre de la liga real; su recurso se encuentra fuera de los PNG de escudos de clubes.
