# PES 2017 Android — Fase 3, piloto 01: cambio seguro de la base del marcador genérico

**Fecha:** 21 de noviembre de 2026 (sesión que continuó después de medianoche UTC).  
**Estado:** **CPK creado, verificado estructural y binariamente.** Prueba de marcador en Android **pendiente**. No se debe declarar que el marcador aparece o funciona durante un partido hasta que el usuario lo compruebe.

## Contexto y objetivo

El usuario compartió las capturas de Arsenal vs. Manchester United en modo Liga Máster: el marcador activo de PES2017 está arriba a la izquierda y el indicador de rendimiento en esa pantalla señaló **53 FPS**, frente a 58 en menú y 24–29 en escenas de presentación. Se eligió un piloto visual mínimo para evitar sobrecargar GPU/CPU: teñir solamente la **base del HUD genérico** de un azul verdoso oscuro a un violeta oscuro inspirado en la identidad Premier League.

**Atención:** No es un marcador Premier League completo ni una selección automática por competición. `game2dPes.bin` / `licenceTexturePes.bin` son genéricos, por lo que el color puede afectar otros encuentros que empleen este HUD. La geometría, el texto de goles/reloj y el selector de ligas permanecen intactos.

## Entrada, salida y hashes

| Campo | Valor |
| --- | --- |
| Base original `dt11_x36.cpk` | SHA-256 **`e20bbb24907ad7143e403fdbb1c3dad1fb5eabe24b4d95189829f18f42b1c030`** |
| Archivo privado generado | `dt11_x36_MARCADOR_PILOTO01_MORADO_FC26.cpk` |
| SHA-256 generado | **`834693d35d0db1c7b352303401b819d9c7a00fd03cc0d3567a60d627254ecbbb`** |
| Tamaño CPK original/generado | **160987324 bytes**, idéntico |
| Entradas | **751** |
| Entradas modificadas | **1** |
| Entradas preservadas byte a byte | **750 de 750** |
| Recurso modificado | `common/menu/licence/licenceTexturePes.bin` |
| Tamaño del recurso anterior / nuevo | **80538 → 80539 bytes** |
| Capacidad disponible | **81920 bytes** |

## Hallazgo técnico y parche aplicado

1. Extracción desde el TOC CPK Xbox360, validando firma, nombres, offsets y tamaños.
2. `licenceTexturePes.bin`: WESYS + zlib, con `TXP2` a offset 48.
3. TXP2: 2 atlas; primer atlas `tex000` con wrapper LZ de 161435 bytes, que se decodifica a un `TXDT` de **1044544 bytes**, 1024×1020 píxeles en DXT5.
4. En la tabla de regiones se identificó **`hudTexPes-scoreBase`** con coordenadas de atlas `[888,0,964,40]` (textura de 76×40 sobre alineación DXT5, 75×39 según límite de semipíxeles del contenedor).
5. El bloque de color en la región se repite 190 veces, pero su compresión LZ hace referencia a solamente **4 bytes literales originales** del flujo. Un análisis completo de dependencias demostró que esos cuatro literales afectan **exclusivamente a los endpoints RGB565 del área de scoreBase** y a ninguna otra región, cabecera, alfa o selector.
6. Se modificaron solo esos **4 bytes** dentro del WESYS descomprimido, para transformar los colores DXT5 de `09460125` a `40ec2849` (endpoints RGB565 de tonos morados oscuros). La descompresión completa del atlas modificado se comparó con el original: cambiaron **exactamente 760 bytes de endpoints DXT5**, todos dentro de la región autorizada, y cero bytes ajenos.
7. El WESYS modificado se recomprimió con zlib nivel 9 en **80539 bytes**, sin sobrepasar el slot de 81920. La TOC CPK se actualizó solo para ese registro. El tamaño total del CPK permanece constante.
8. Se extrajo el parche una vez reempacado y se validaron header, TOC, 751 archivos, bytes de los 750 no objetivo y contenido del recurso editado.
9. **Verificación independiente posterior:** el WESYS descomprimido original y nuevo difieren exactamente en las posiciones `[1569,1570,1571,1572]`, y el TXDT nuevo se descomprime correctamente con extremos RGB565 `40ec2849`.

## Seguridad y límites

- Se creó **un nuevo CPK**, sin modificar el original.
- `dt10_x36.cpk`, `dt15_x36.cpk` **lote 10**, `dt20_eng_x36.cpk` **nombres unificados**, `saves` y `save_backups` no se modificaron.
- La vista previa es una representación real de **la región de atlas scoreBase**, no una captura real de partido y no predice el color final si el juego combina texturas de otra manera.
- El cambio no añade texturas, no incrementa resolución, no modifica animaciones ni lógica de juego. **No equivale a medición del rendimiento o compatibilidad del runtime en Android**.
- No se hizo selección `id_competicion → hud`; se requiere trabajo adicional para un marcador genuinamente diferente por liga.

## Instalación y prueba Android

1. En el teléfono, **cerrar PES 2017**. Guardar una **copia del `dt11_x36.cpk` original** en otra carpeta, manteniendo `dt15`, `dt20` y las partidas intactas.
2. Descargar `dt11_x36_MARCADOR_PILOTO01_MORADO_FC26.cpk`, renombrarlo a **`dt11_x36.cpk`** y sustituir **solo** ese archivo bajo `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
3. Abrir un partido de Premier League / Liga Máster y entrar al **juego activo**, cuando se ve `ARS 0-0 MAN` y el reloj arriba a la izquierda (no una pantalla de menú, alineaciones o presentación).
4. Confirmar que sigue visible el reloj, marcador de goles y clubes, comprobar **color, legibilidad y FPS**. Si hay fallo de carga, menú negro, HUD invisible, corrupción o bajada apreciable de rendimiento, cerrar y restaurar `dt11_x36.cpk` original.
5. Solo si el usuario aprueba el piloto, investigar selección por competición para incorporar diseños propios por liga. No prometer que este cambio ya moderniza el HUD completo.

## Restricciones del repositorio

No subir CPK ni el atlas comercial al repositorio. Conservar solo documentación de cambios, hashes, procedimientos y scripts que no contengan assets del juego.
