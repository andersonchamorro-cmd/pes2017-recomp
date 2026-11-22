# PES 2017 Android — Piloto 03: franja de marcador Xbox 360 en `game2dEngF.bin`

**Fecha:** 21 de noviembre de 2026 (sesión de madrugada). **Estado:** CPK acumulativo de logo/nombres NO modificado; solo nuevo `dt11` experimental construido **desde el `dt11` original**. Validado en dos pasadas estructurales; prueba Android de apariencia/FPS **pendiente**.

## Contexto y prueba del usuario: el piloto 02 no consiguió cambiar el marcador visible

El usuario aportó **7 nuevas capturas de Liga Máster** tras el piloto 02:

| Pantalla | FPS |
| --- | ---: |
| Calendario de Liga Máster | 60 |
| Alineaciones | 48 |
| Presentación de estadio | 28 |
| Banner del saque inicial | 30 |
| Marcador activo 0:49 | 59 |
| Marcador activo 2:10 | 60 |
| Marcador activo 4:29 | 52 |

La franja de goles **ARS 0-0 MAN** permaneció visualmente **azul**, sin distinguirse el cambio morado del piloto 02. **No considerar el 02 aprobado por diseño**, ni concluir mejora o degradación real de FPS a partir de capturas puntuales.

## Hallazgo del tercer piloto

Se encontró una coincidencia geométrica mucho más convincente con la franja en **`common/menu/licence/game2dEngF.bin`**:
- Su atlas `tex000` contiene **tres placas azules separadas por dos ranuras diagonales transparentes**, como las de los lados ARS / 0-0 / MAN en la captura del usuario.
- Debajo aparece el gráfico **PES2017 de la animación inicial**, que ya sabemos que es normal; permanece sin modificar.
- **Corrección técnica importante**: la textura TXDT tipo `0x15` empaqueta los 4 bytes de cada píxel en orden **ARGB: [A,R,G,B]**, no RGBA. El piloto 02 anterior trató la secuencia como RGBA, por lo que su validación de "alfa intacto" era incorrecta aunque no hubiera errores aparentes en las capturas; **en el nuevo piloto se ha comprobado explícitamente el verdadero byte alfa [0] y no se modifica**.
- La coincidencia geométrica de tres secciones es muy prometedora, **pero aún no se ha comprobado en el motor Android que este recurso esté seleccionado para esa liga**. La hipótesis se validará con una sola prueba visual específica.

## CPK nuevo, privado, para instalar solamente tras respaldo

| Campo | Valor |
| --- | --- |
| CPK base privado aportado por el usuario | `dt11_x36.cpk` |
| SHA-256 base | `e20bbb24907ad7143e403fdbb1c3dad1fb5eabe24b4d95189829f18f42b1c030` |
| Archivo piloto privado | `dt11_x36_MARCADOR_PILOTO03_ENGF_MORADO_FC26.cpk` |
| SHA-256 piloto | `769e3786af10ff8e7016c015bd908d2fab0531e3d400e726b5a1cd855885c6d6` |
| Bytes contenedor antes / después | **160987324** (sin cambios) |
| Recursos CPK | **751** |
| Modificados | **1**: `common/menu/licence/game2dEngF.bin` |
| Recursos intactos byte por byte | **750/750** |
| Tamaño comprimido del recurso original → nuevo | **166771 → 163531 bytes** |
| Capacidad de la ranura | **167936 bytes** |
| TXDT objetivo | `tex000`, **268×136, ARGB `0x15`** |
| Tamaño LZ original → nuevo | **28777 → 26591 bytes** |
| Píxeles modificados | **6042** en las tres placas de resultado de la banda superior |
| Canal alfa real | **idéntico en todos los píxeles** |
| Sprites debajo de la fila 28, logo PES2017, animaciones | **idénticos byte por byte** |
| Segunda textura del mismo TXP2 | **sin cambios** |

### Método y garantía técnica

1. Se leyó la cabecera y TOC CRI CPK con el decodificador para Xbox 360 y se identificó exclusivamente `game2dEngF.bin`.
2. WESYS/zlib decodificado; TXP2 (admite 12 bytes de padding final en el paquete original). Se identificó `tex000` comprimido con legacy LZ.
3. Se decodificó `TXDT` ARGB, se modificaron **solo los canales [1:4] RGB** de la banda superior y se dejó intacto el byte [0] alfa, la geometría, las separaciones diagonales y las imágenes de intro.
4. Se eligió violeta oscuro y pequeño acento turquesa, con degradado vertical suave de 28 píxeles. Es un **piloto del HUD**, no una reproducción exacta de todos los elementos del video de referencia.
5. Se recomprimió legacy LZ, se comparó el resultado descomprimido bit a bit con la textura editada, y se preservaron las posiciones y tamaños originales del paquete TXP2 mediante relleno en la ranura.
6. Se actualizó exclusivamente la TOC de `game2dEngF.bin` y se verificó CPK final con 751 entradas, 750 no objetivo byte a byte idénticas, longitud original intacta y SHA-256 final.
7. La segunda verificación extrajo **otra vez** el CPK original y modificado, decodificó WESYS y LZ, confirmó que solo cambió el recurso esperado, que la textura `268×136` conserva el alfa, que los sprites de intro desde fila 28 son iguales y que la segunda textura `tex001` no cambió.

## Rendimiento y límites de este piloto

- La edición **sustituye únicamente colores existentes de un atlas**, no añade texturas, formatos, dimensiones, animaciones ni elementos de dibujado. **Bajo riesgo de sobrecarga**, pero **sin garantía absoluta de 60 FPS** sin medir en Xiaomi Mi 10T.
- El objetivo es **el marcador durante el juego**, no el menú de Liga Máster ni la presentación previa. Esta última se deja intacta porque la secuencia tiene caídas de ~25–30 FPS en las capturas.
- No se ha modificado el reloj, texto, resultado dinámico ni asignación automática por competición.
- El video original del usuario https://www.youtube.com/watch?v=GkhXEpaUHqU no pudo inspeccionarse directamente: la coincidencia es una **aproximación de color y geometría disponible**, NO equivalencia exacta con ese video.
- Cualquier cambio a `game2dEngF` puede afectar otros torneos que empleen ese HUD. No se sabe aún si el motor selecciona una interfaz distinta por competición.

## Prueba y recuperación Android

1. Conservar en carpetas diferentes copia del `dt11_x36.cpk` instalado (piloto 02) **y del original**.
2. **Cerrar el juego**. Renombrar `dt11_x36_MARCADOR_PILOTO03_ENGF_MORADO_FC26.cpk` a `dt11_x36.cpk` y reemplazar solo ese archivo en `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
3. Entrar en **la misma partida de Liga Máster**, Arsenal vs. Manchester United, y comprobar el marcador arriba a la izquierda entre los minutos 2 y 5, comparando el tono violeta de las tres placas y la lectura del reloj/resultado.
4. Comparar los FPS durante el juego activo frente a aproximadamente **52–60 FPS** de las capturas actuales. Distinguir de las presentaciones, que bajan a 25–30 FPS en el juego original.
5. Ante glitch, HUD invisible, corrupción o empeoramiento notable de FPS, salir y restaurar el `dt11` original. No tocar `dt10`, `dt15`, `dt20`, `saves/`, `save_backups/`.
6. **No solicitar nuevas pruebas de los pilotos 01/02**: ya hay suficiente evidencia de que ambos fallaron a nivel visual.

## GitHub

No subir ni distribuir los CPK o contenidos gráficos propiedad de terceros a GitHub público; publicar únicamente códigos/hashes/informes.
