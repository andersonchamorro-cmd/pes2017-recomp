# PES 2017 Android — análisis real del dt10 para fase 2B de nombres

Fecha: 21/11/2026.

## Archivo recibido del usuario y validación
- Archivo binario PRIVADO: `dt10_x36(1).cpk` (el instalado actualmente, copia del usuario).
- SHA-256: `3af02253e90f0a0aac2ce54e057abb8c4006f109c7410ff1dca4bf4f02fd441a`.
- Tamaño: **1 176 820 bytes**.
- CPK válido: encabezado CRI, tabla TOC descifrable, **156 entradas**.
- Los datos interiores WESYS/zlib se leyeron y descomprimieron verificando el tamaño declarado.
- `common/etc/pesdb/Competition.bin`: **61 registros** de 32 bytes, identificadores *internos* como `ENGLAND_D1_LEAGUE`, `ITALY_D1_LEAGUE`, `PORTUGAL_D1_LEAGUE`.
- Otras tablas presentes: `CompetitionEntry.bin`, `CompetitionKind.bin`, `CompetitionRegulation.bin`, `Team.bin`, archivos de equipos/jugadores y categorías. No alterar estos datos para cambiar textos de menú.

## Hallazgo decisivo
La búsqueda en los recursos **descomprimidos** y en los datos brutos, probando UTF-8/ASCII, UTF-16LE y UTF-16BE, **NO encontró** estas cadenas que sí aparecen en los menús Android:

- `English League`
- `Italian League`
- `Portugal League`
- `England Cup`
- `Spanish League`
- `French Cup`
- `English 2nd Division`
- `Spanish 2nd Division`

Estas etiquetas **no están presentes como texto editable directamente** en este CPK. Cambiar `ENGLAND_D1_LEAGUE` por `Premier League` sería incorrecto: el primero es una **clave interna** que otras tablas referencian, no la etiqueta visible del menú. Hacerlo podría introducir bugs en competiciones y Liga Máster.

El archivo **NO se modificó** y no se generó un falso CPK de nombres. La base de emblemas del usuario **Lote 10** permanece intacta.

## Ubicación verificada como candidata para las cadenas visibles
Los mapas de archivos de PES 2017 para Xbox 360 y el README del proyecto de recompilación confirman que `dt10` contiene la base de datos y los paquetes `dt20_*` contienen los recursos de idioma/localización:
- https://foro.pesoccerworld.com/viewtopic.php?p=2086004
- https://github.com/andersonchamorro-cmd/pes2017-recomp (README incluye `dt20_*` como paquetes instalados).

Siguiente archivo a inspeccionar en **esta misma versión del juego**: **`dt20_eng.cpk`**, o si no está, el paquete `dt20_use.cpk` u otro `dt20_*` correspondiente al idioma inglés usado en Android. No afirmar que una cadena concreta está en un recurso interno sin examinarlo.

## Siguiente ejecución segura
1. Recibir el paquete `dt20_*` correcto; inventariar y localizar las cadenas exactas en sus recursos `.str` o equivalentes.
2. Identificar IDs y formato de cadenas, editar **máximo 3 nombres** en copia, confirmar referencias, tamaños, codificación y integridad de recursos no objetivo.
3. Pilotar nombres `English League → Premier League`, `Italian League → Serie A` y `Portugal League → Liga Portugal`, tras comprobar patrocinadores y compatibilidad del cuadro del menú.
4. Conservar la copia de cada CPK y probar en Android los tres nombres; solo después ampliar a otras copas. 
5. Las ligas ficticias **PEU → Bundesliga**, **PLA → Liga BetPlay** y **PAS → Liga MX** no deben renombrarse sin sustituir primero clubes y estructura.

**Estado:** análisis de dt10 completado y documentado; **piloto de nombres bloqueado hasta recibir el paquete de idioma**, no por un error de integridad.

No publicar CPK, nombres de jugadores, datos del juego ni assets externos en Git público.
