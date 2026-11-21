# PES 2017 Android — lote 02 acumulativo de nombres oficiales

**21 noviembre 2026. Estado: parche creado y verificado binariamente. Falta prueba de Android.**

## Confirmación del lote 01

El usuario instaló el primer `dt20_eng_x36.cpk` modificado y envió **3 capturas** que muestran correctamente **Premier League**, **Serie A** y **Liga Portugal** en las pantallas de selección de ligas, incluyendo un menú Home/Away. El contador indicaba **60 FPS** y ~**16,7 ms/fotograma**, sin evidencias de recortes ni corrupción visible. **No implica prueba de partido completo o guardado**.

## Lote 02: segundo grupo de 3 nombres

| Texto anterior del juego | Nombre 2026/27 elegido | Recurso y offset original |
| --- | --- | --- |
| `English 2nd Division` | **Sky Bet Championship** | `eng/string/all.str` @ 748380 |
| `Italian 2nd Division` | **Serie BKT** | `eng/string/all.str` @ 748431 |
| `Spanish 2nd Division` | **LALIGA HYPERMOTION** | `eng/string/all.str` @ 748401 |

Fuentes oficiales de nombres:
- EFL: https://www.efl.com/news/2026/january/12/efl-kick-off-dates-confirmed-for-2026-27-season/ (Sky Bet Championship)
- Lega B: https://www.legab.it/seriebkt/calendario (Serie BKT 2026/27)
- LALIGA: https://www.laliga.com/en-US/laliga-hypermotion (LALIGA HYPERMOTION 2026/27)

## Identificación e integridad

| Campo | Valor |
| --- | --- |
| Base privada del lote 01 (confirmado visualmente) | `dt20_eng_x36_NOMBRES_LOTE01_PILOTO.cpk` |
| SHA-256 base | `a0b3f2532124733ee660105b99e276e7a4d3a3a5956ccd38a294bd037df7403a` |
| Salida privada entregada | `dt20_eng_x36_NOMBRES_LOTE02_SEGUNDAS_DIVISIONES.cpk` |
| SHA-256 salida | `29f3beac0f91f3f4c336e586f407c4c31ec0d4592b89fd80f5a10600af4e0ccd` |
| Tamaño total | **368184 bytes**, igual |
| Recursos en CPK | **5** |
| Recurso modificado respecto al lote 01 | Solo **`eng/string/all.str`** |
| Recursos intactos byte a byte | **4/4** |
| Recurso comprimido antes/después | 280369 → **280338 bytes** |
| Capacidad de espacio en CPK | **284672 bytes** |
| Tamaño descomprimido antes/después | **844784 bytes**, igual |

Las sustituciones son **del mismo tamaño que la cadena antigua**, con espacios finales solo cuando la etiqueta nueva es más corta. Se conserva el desplazamiento de los terminadores NUL. `Spanish 2nd Division Playoffs` es **otra etiqueta distinta**, que no se alteró por coincidencia parcial del nombre: se ha usado comparación de **cadena completa terminada en NUL**.

Un segundo proceso independiente volvió a extraer ambas versiones desde los CPK y comprobó que:
1. Solo las tres etiquetas autorizadas son distintas en el recurso descomprimido.
2. Los 3 nombres del lote 01 siguen idénticos.
3. Otros 4 recursos, cabecera/tabla TOC y tamaño del CPK no tienen cambios inesperados.
4. El recurso WESYS/zlib se descomprime y el nuevo contenido coincide exactamente.
5. No se modificaron `dt10_x36.cpk`, `dt15_x36.cpk`, equipos, identificadores ni partidas.

## Cómo probar y revertir

1. Respaldar el `dt20_eng_x36.cpk` instalado (lote 01) fuera de la carpeta de instalación.
2. Cerrar el juego, renombrar el nuevo lote 02 a `dt20_eng_x36.cpk` y reemplazar únicamente ese archivo.
3. Examinar la selección Home/Away y los menús de competiciones de Inglaterra, Italia y España, verificando **Sky Bet Championship**, **Serie BKT** y **LALIGA HYPERMOTION**; observar cualquier corte de texto y FPS.
4. Si hay errores, cerrar PES y restaurar lote 01, sin alterar `dt15` y las carpetas `saves` / `save_backups`.

**Estado de prueba Android del lote 02: pendiente.** No afirmar FPS real del lote 02 hasta recibir capturas del usuario.

## Plan de fases sin cambios

Continuar lotes cortos de nombres para otras ligas/copas. Ligas ficticias todavía NO renombradas: **PEU→Bundesliga**, **PLA→Liga BetPlay**, **PAS→Liga MX**. Estas sustituciones requieren antes transformar equipos y estructura del campeonato.

No se publican CPK ni datos del juego en GitHub público; solo procedimientos, recursos editados y hashes.
