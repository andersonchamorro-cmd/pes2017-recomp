# PES 2017 Android — Fase 3A: marcador piloto 02, placa de juego (sin cambio de menús)

**Fecha:** 21 de noviembre de 2026, Colombia.  
**Estado:** **CPK generado y verificado en dos pasadas independientes.** Prueba visual y de FPS en Liga Máster en el teléfono **pendiente**.

## Petición del usuario y alcance estrictamente priorizado

El usuario quiere un marcador **parecido al de su video de referencia**, y valora por encima de todo **no perder FPS**. El aspecto de menús e interfaz de Liga Máster **no le interesa**. Opcionalmente se modificaría la tarjeta de presentación del partido únicamente cuando pueda hacerse sin empeorar rendimiento. Se evita meter modificaciones extra por estética.

**Referencia visual compartida:** https://www.youtube.com/watch?v=GkhXEpaUHqU  
El video no pudo inspeccionarse fotograma a fotograma desde el entorno de investigación; por tanto **NO** se afirma haber igualado su geometría ni estilo exacto. El piloto 02 modifica la apariencia de una placa real del HUD con paleta moderna violeta oscuro/turquesa; no es marcador completo estilo video ni cambio automático por competición.

**No se tocó la presentación inicial**, porque el usuario observó 25–29 FPS durante esa secuencia, frente a ~50–55 FPS en varias capturas del partido activo. Los logos PES2017 de animación inicial permanecen intactos.

## Importancia respecto al piloto 01

El piloto 01 cambiaba `licenceTexturePes.bin`, región `hudTexPes-scoreBase`, sin que el tono morado se hiciera perceptible en las capturas de los minutos 1:53 y 2:57. Las nuevas capturas revelan que el marcador sigue azul. Por eso se decidió **partir del `dt11_x36.cpk` original** e intervenir **`game2dPes.bin`**, en la textura real que contiene el gran sprite horizontal del marcador y dos placas menores, manteniendo intocables los sprites de PES2017 y WinnerEleven2017.

## Identificación del binario

| Campo | Valor |
| --- | --- |
| Base privada del usuario | `dt11_x36.cpk` |
| SHA-256 de entrada | `e20bbb24907ad7143e403fdbb1c3dad1fb5eabe24b4d95189829f18f42b1c030` |
| Piloto privado generado | `dt11_x36_MARCADOR_PILOTO02_FC26_LIGERO.cpk` |
| SHA-256 de salida | `18e3491e960098683260260ac3e14f652d19596fcdd3fd4e1f02a9e3c1c4b3ba` |
| Tamaño contenedor antes / después | **160987324 bytes** |
| Recursos en el CPK | **751** |
| Recurso modificado | **`common/menu/licence/game2dPes.bin`** |
| Recursos preservados byte por byte | **750/750** |
| Tamaño del recurso editado antes/después | 91230 → **88704 bytes** |
| Capacidad de ranura CPK | 92160 bytes |

## Modificación exacta

1. Se extrajo `game2dPes.bin` y se descomprimió **WESYS/zlib**.
2. Se identificó TXP2 con **dos texturas**. El atlas `tex000` contiene `TXDT` RGBA, **248×222 píxeles** (0x15, 4 bytes por píxel).
3. En ese atlas se recolorearon *solo los píxeles RGB* del sprite de placa horizontal arriba y dos placas pequeñas abajo: violeta oscuro de alto contraste con borde turquesa. El alfa de absolutamente todos los píxeles se conservó.
4. Se omitieron expresamente sprites de logo `PES2017`, `WinningEleven2017`, iconos laterales y la segunda textura `tex001`.
5. Se implementó y verificó compresión **legacy LZSS** para volver a incluir todo el atlas. `tex000` pasó de **46001 a 43695 bytes** comprimidos. La descompresión de la nueva textura coincide exactamente con los píxeles recoloreados; misma resolución, mismos buffers y formato.
6. Se actualizaron los **dos campos de tamaño** del registro `tex000` dentro de TXP2; **no se desplazaron offsets** ni la segunda textura y el tamaño total del TXP2 quedó idéntico.
7. Se recomprimió el WESYS y se cambió únicamente su registro en la TOC del CPK; nuevo WESYS de **88704 bytes**, por debajo de la capacidad reservada de 92160.
8. El encabezado, la tabla TOC, las 751 entradas, los datos originales de los otros **750 recursos** y el tamaño total del CPK se cotejaron byte por byte.
9. **Auditoría independiente**: volvieron a extraerse la nueva y la vieja versión para comparar píxeles RGB y el alfa. **16025 píxeles cambiaron RGB**, cero cambios de alfa; los sprites de PES2017 y los otros iconos se mantuvieron intactos. El SHA-256 coincide con lo documentado.
10. **No se añadieron nuevas texturas, elementos de interfaz, animaciones, geometría del reloj ni draw calls**. Esto minimiza el impacto potencial, pero **NO garantiza FPS idénticos sin probar en Android**.

## Estado realista de la apariencia

- La vista previa documenta **el atlas real**, no la captura final del marcador durante el partido.
- Se espera que el color sea visible en las placas que use `game2dPes.bin`, pero **la selección interna exacta y mezcla del HUD requieren la prueba Android**. Si la placa no se ve cambiada, debemos localizar el sprite realmente activo en vez de repetir pruebas del mismo material.
- **No se implementó selección por competición**: es una edición del **HUD PES genérico** y puede verse en otros torneos.
- **No se intentó reproducir directamente el código, texturas o sistemas Sider de mods PC**, porque la versión del usuario es Xbox 360 recompilada para Android.
- La presentación previa del enfrentamiento se dejó fuera por prioridad de rendimiento, tal como autorizó el usuario.

## Instalación / rollback en Liga Máster

1. Antes de modificar nada, hacer copia del `dt11_x36.cpk` actualmente instalado (piloto 01 u original) y conservar también el **original** en una carpeta aparte.
2. **Cerrar completamente PES 2017**.
3. Descargar el piloto 02, renombrarlo exactamente a **`dt11_x36.cpk`**.
4. Sustituir **únicamente** ese archivo en `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
5. Abrir una **partida de Liga Máster existente**, jugar Premier League y comprobar específicamente la franja del marcador arriba a la izquierda entre los minutos 1:30 y 3:00, no solo los menús o la animación inicial.
6. Revisar legibilidad de marcador y reloj, posibles tintes defectuosos, FPS durante la jugabilidad normal frente a los **~50–55 FPS previos en instantes comparables**. Probar una transición de vuelta al menú; no pisar `saves` ni `save_backups`.
7. Si el HUD no funciona, se corrompe o aparecen bajadas anormales de FPS, cerrar el juego y **restaurar el dt11 original o el último estable**, sin afectar dt10/dt15/dt20.

**Estado Android:** NO PROBADO. **Estado binario:** verificado.  
No distribuir CPK ni arte propietario en GitHub público; solo documentación y manifiestos.
