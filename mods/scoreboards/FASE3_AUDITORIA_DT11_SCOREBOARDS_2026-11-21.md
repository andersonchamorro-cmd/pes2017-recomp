# Fase 3 — auditoría real de los marcadores PES 2017 Android (Xbox 360 recompilado)

**Fecha:** 21/11/2026. **Estado:** Recursos localizados, descompresión e inventario validados; **NO se ha creado ningún parche ni modificado ningún archivo del juego**.

## Cierre visual de nombres (fase 2B)
El usuario instaló `dt20_eng_x36_TODOS_NOMBRES_OFICIALES_FC26.cpk` y aportó **9 capturas** de Inglaterra, Francia, Italia, Países Bajos, España, Portugal, Argentina, Chile y Copa do Brasil. Se muestran nombres y logos; FPS de **59–60**, sin defectos de texto evidentes. El nombre largo `Supertaça Cândido de Oliveira` entra en la caja del menú. No equiparar menús con prueba de partido o guardados. Esta versión queda **aprobada visualmente en menús**; no volver a cambiar dt20 sin necesidad.

## Archivo real de scoreboard localizado

`dt11_x36.cpk` **fue subido por el usuario en una conversación anterior** y recuperado de su Biblioteca, sin solicitar nueva carga.

| Campo | Valor |
| --- | --- |
| SHA-256 | `e20bbb24907ad7143e403fdbb1c3dad1fb5eabe24b4d95189829f18f42b1c030` |
| Tamaño | **160987324 bytes** (~153,53 MiB) |
| Archivo CPK | **CRI CPK de Xbox 360**, encabezado y TOC decodificados |
| Entradas TOC | **751** |
| Recursos relacionados con HUD, `game2d`, `licenceTexture` | **55** investigados |
| Envoltorio de esos BIN | **WESYS + zlib**, con tamaño descomprimido validado |
| Contenedor interior | **TXP2**, con objetos `afp_*.apk` |

### Entradas precisas de interés

| Recurso dentro del CPK | Tamaño comprimido | Posible función |
| --- | ---: | --- |
| `common/menu/licence/game2dPes.bin` | 91230 bytes | HUD / marcador genérico |
| `common/menu/licence/licenceTexturePes.bin` | 80538 bytes | Atlas de texturas del HUD genérico |
| `common/menu/licence/game2dPesLayout.bin` | 1836 bytes | Layout del HUD genérico |
| `common/menu/licence/game2dEngF.bin` | 166771 bytes | HUD específico de competición inglesa |
| `common/menu/licence/licenceTextureEngF.bin` | 41872 bytes | Atlas de marcadores de competición inglesa |
| `common/menu/licence/game2dUcl.bin` | 121464 bytes | HUD Champions League |
| `common/menu/licence/game2dUel.bin` | 114476 bytes | HUD Europa League |
| `common/menu/licence/game2dUsc.bin` | 120430 bytes | HUD Supercopa UEFA |
| `common/menu/licence/game2dAcl.bin` | 63569 bytes | HUD torneo asiático |
| `common/menu/licence/game2dCcl.bin` | 57470 bytes | HUD torneo adicional del juego |
| `common/menu/general/game2d.bin` | 76137 bytes | Base HUD/interfaz 2D |

**Evidencia de contenidos internos:** el BIN de texturas genéricas `licenceTexturePes.bin` contiene los objetos `hudTexPes-scoreBase`, `hudTexPes-plateFull`, `hudTexPes-plateSmall`, `hudTexPes-plateTop`, `hudTexPes-gradationSmall`, `hudTexPes-gradationBar`, `hudTexPes-card-0`, `hudTexPes-card-1` y otros. `licenceTextureEngF.bin` contiene `licenceTextureEngF-iconScore-0`, `licenceTextureEngF-pkScore-0`, `licenceTextureEngF-plate0-0` y demás elementos.

**Control negativo:** se inventariaron los **2784 recursos** del `dt15_x36_LOTE10_PORTUGAL_SUPERCUP_FC26.cpk` y NO aparecen `game2dPes.bin`, `licenceTexturePes.bin`, ni rutas `common/menu`. Por tanto, **los marcadores NO deben modificarse en dt15** (se conserva lote 10 de logos). Tampoco deben tocarse dt10 (datos de equipos) ni dt20 (nombres ya aprobados).

## Interpretación y límite técnico

- **Verificado en este CPK Xbox 360:** las interfaces de puntuación y sus texturas existen como `TXP2` dentro de archivos `BIN`; no son PNGs sueltos, por lo que el parcheador de logos no aplica.
- En herramientas públicas de modding PES 2017 para PC, `game2dPes.bin` y `licenceTexturePes.bin` son archivos usados para el marcador y geometría del HUD. Fuentes generales: https://www.peshdpatch.com/2017/06/pes-2017-scoreboard-editor-v1-by-devil-cold52.html ; https://www.ultigamerz.com/2017/01/how-to-edit-pes-2017-scoreboard.html ; https://foro.pesoccerworld.com/viewtopic.php?p=2101160
- **No afirmar todavía que cada liga puede elegir un marcador diferente solo reemplazando estos BIN**: hay un marcador PES genérico y algunos paquetes licenciados, pero el mapa liga-ID → HUD no está verificado. La selección dinámica por liga puede requerir examinar la lógica de selección en el ejecutable recompilado o un gancho en el runtime; no editar IDs al azar.

## Próximo piloto sin arriesgar estabilidad

1. Conseguir una **captura del marcador durante un partido** (por ejemplo Premier League / amistoso con equipos ingleses): tiempo, resultado, nombres de clubes; otra de Champions o FA Cup si el HUD cambia. No sirve el menú previo al partido.
2. Identificar visualmente qué elementos del HUD corresponden a cada objeto de textura y cómo se muestra la selección por competición.
3. Probar **un marcador moderno y legible**, con costo de textura similar, reutilizando tamaño y compresión de cada textura dentro del atlas (sin aumentar memoria); primero en copia de `dt11_x36.cpk`.
4. Escribir validador TXP2 y reemplazo que garantice mismas entradas y formatos y no altera tamaños fuera de la ranura. Extraer nuevamente desde parche y comparar 750 entradas ajenas byte a byte.
5. Verificar fps/menú/partido y pruebas de retorno y guardado con el usuario. Volver al CPK original ante cualquier error.
6. Solo después verificar si se puede **asignar un marcador diferente a cada competición** mediante assets seleccionados por el motor o, si no, mediante un pequeño cambio aislado del runtime (requiere evaluación y prueba).

## Fases futuras del proyecto
- Fase 4: PEU→Bundesliga, PLA→Liga BetPlay, PAS→Liga MX, estructura/IDs/clubes reales 2026/27 antes de nombres.
- Fase 5: Plantillas y fichajes 2026/27.
- Fase 6: Uniformes y acabado gráfico FC26.

No subir ni redistribuir archivos CPK o recursos gráficos propietarios de PES a GitHub público.
