# PES 2017 LaLiga 2016/17 — escudos acumulativos

**Estado:** contenedor reconstruido y validado estructuralmente; falta probarlo en el Xiaomi.

## Archivo de partida y salida

- Base: `dt15_x36_PREMIER_LEAGUE_20_ESCUDOS.cpk` (incluye 20 escudos de la Premier).
- SHA-256 de base: `1a054c92d4e8364767e925a8773caf959b1210735fc50b0086108282243a5dd3`.
- Salida privada: `dt15_x36_PREMIER_Y_LALIGA_40_ESCUDOS.cpk`.
- SHA-256 de salida: `5b3064f5ac194d4d1949349554c253ba75a9c9a83a8442e1bb16845b43545efc`.
- Salida: **245225593 bytes**, 2784 recursos.
- Archivos sustituidos: **36 PNG** (18 equipos, dos resoluciones); otros **2748 recursos byte por byte idénticos**.
- Se conservaron los escudos de los 20 clubes ingleses, incluidos los tres iniciales; los de FC Barcelona y Atlético de Madrid no fueron modificados.

## IDs de clubes españoles, verificados contra tabla de PES 2017

| ID | Equipo |
|---|---|
| 4145 | Deportivo Alavés |
| 258 | Athletic Club |
| 195 | Celta de Vigo |
| 111 | Deportivo La Coruña |
| 4146 | SD Eibar |
| 259 | RCD Espanyol |
| 1765 | Granada CF |
| 364 | UD Las Palmas |
| 4272 | CD Leganés |
| 260 | Málaga CF |
| 263 | CA Osasuna |
| 194 | Real Betis |
| 109 | Real Madrid |
| 196 | Real Sociedad |
| 265 | Sevilla FC |
| 363 | Sporting de Gijón |
| 110 | Valencia CF |
| 267 | Villarreal CF |

**Atención:** una tabla pública antigua repite por error el ID 4146 en Real Sociedad; el identificador correcto es **196**, corroborado por PES Master y una segunda lista.

Fuentes: https://pes-files.ru/pro_evolution_soccer_2017_id_komand y https://www.pesmaster.com/pv-blue-white/pes-2017/team/196/

Las 18 imágenes se obtuvieron mediante el flujo `.github/workflows/fetch-laliga-logos.yml` usando los SVG de `JoseArroyave/football-logos`. Los escudos se conservan en el archivo privado de prueba del usuario; no se han incluido archivos del juego ni los escudos en los commits públicos.

## Cómo probar

1. Cerrar PES 2017 completamente.
2. Conservar una copia del `dt15_x36.cpk` actualmente funcional en Download.
3. Renombrar el CPK nuevo a `dt15_x36.cpk`.
4. Reemplazar el archivo de la instalación activa bajo `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
5. **No tocar `dt10_x36.cpk`**, donde están los nombres reales de Premier y LaLiga.
6. Probar Real Madrid, Real Sociedad, Athletic Club, Valencia, y los escudos de la Premier; después un partido y Liga Máster.
7. Ante fallo, cerrar PES y restaurar el anterior `dt15_x36.cpk`.

**No cambia** la leyenda «Spanish League» ni el logotipo de la competición. Esos recursos se investigarán por separado.
