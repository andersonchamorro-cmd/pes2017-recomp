# Fase 3 — capturas reales del marcador de Premier League, mapa TXP2 y control de FPS

**Fecha:** 21/11/2026. **Estado:** 5 capturas de partidos analizadas, 5 recursos BIN Xbox 360 descomprimidos y comparados; **parche de marcador no generado todavía**, porque no está validada la reinyección TXP2. No sobrescribir el juego del usuario sin un paquete auténticamente verificable.

## Imágenes recibidas y mediciones visuales del indicador del juego

| Captura | Pantalla | FPS | ms/frame | Temperatura mostrada |
| --- | --- | ---: | ---: | ---: |
| `146699.jpg` | Liga Máster: menú principal (Arsenal) | 58 | 17,2 | 55 °C |
| `146700.jpg` | Antes de partido: alineaciones Arsenal–Manchester United | 29 | 34,5 | 58 °C |
| `146701.jpg` | Introducción del estadio/presentación central | 24 | 40,9 | 53 °C |
| `146702.jpg` | Inicio del encuentro, banner inferior grande | 51 | 19,8 | 62 °C |
| `146703.jpg` | **Partido activo**: ARS 0-0 MAN, minuto 1:01 | **53** | **18,9** | 59 °C |

**Importante:** el rendimiento dentro del partido no equivale a los 59–60 FPS de menús. Apreciamos 51–53 FPS en dos instantes de juego y caídas de 24–29 durante escenas previas; son capturas puntuales, no prueba prolongada, ni prueban que los mods sean la causa. Priorizar un HUD compacto y reutilizar texturas sin subir resolución, animaciones o efectos.

## Identificación de regiones en pantalla

- **Marcador vivo:** esquina superior izquierda; franja oscura/azul de baja altura, abreviaturas `ARS` / `MAN`, resultado `0-0`, reloj.
- **Presentación del estadio:** panel grande centrado con escudos y logos PES2017. **Es distinta** del marcador vivo y no se debe modificar como si fuera la misma textura.
- **Banner inferior al comenzar partido:** otra tarjeta gráfica con equipos, estadio y competición; mantener fuera del primer piloto.
- Controles superpuestos y medidor FPS de la aplicación Android ocupan bordes superiores/laterales; no ampliar el HUD hasta taparlos.

## Fuentes técnicas recuperadas y comprobadas

`dt11_x36.cpk` ya aportado por el usuario y materializado desde Biblioteca.
- SHA-256: `e20bbb24907ad7143e403fdbb1c3dad1fb5eabe24b4d95189829f18f42b1c030`.
- Tamaño: 160987324 bytes; TOC: 751 entradas.
- `common/menu/licence/game2dPes.bin`, BIN WESYS + zlib, **91230 bytes comprimido, 164224 descomprimido**, contiene `game2d_score`, `game2d_scoreDemo`, `hudTexPes-score-0` y otros objetos de la animación/posicionamiento del marcador.
- `common/menu/licence/licenceTexturePes.bin`, BIN WESYS + zlib, **80538 → 199920 bytes**, contiene `hudTexPes-scoreBase`, `hudTexPes-plateSmall`, `hudTexPes-plateFull`, `hudTexPes-plateTop`, `hudTexPes-gradationSmall`, `hudTexPes-gradationTop`, `hudTexPes-card-0` etc.
- `common/menu/licence/game2dPesLayout.bin`, **1836 → 3104 bytes**, layout.
- `common/menu/licence/game2dEngF.bin`, **166771 → 466208 bytes**; `common/menu/licence/licenceTextureEngF.bin`, **41872 → 48400 bytes**; empaquetados para competición inglesa especial, **no asumir** que se utilizan en Premier League.
- Los 5 BIN fueron **re-descomprimidos desde los datos originales y comparados exactamente con las extracciones previas** (5/5 coincidencias). Los BIN desempaquetados contienen **TXP2 a desplazamiento 48**.
- Los paquetes son de **Xbox 360**, no PNG extraíbles directamente. Las herramientas de modding de PC pueden servir de referencia conceptual, pero no garantizan que los archivos reempaquetados funcionen en el motor Android recompilado.

Referencias externas de procedimiento:
- https://www.ultigamerz.com/2017/01/how-to-edit-pes-2017-scoreboard.html
- https://www.peshdpatch.com/2017/06/pes-2017-scoreboard-editor-v1-by-devil-cold52.html

## Plan técnico de primer piloto

1. Mantener los `dt10_x36.cpk` (equipos/IDs), `dt15_x36.cpk` (logos L10), `dt20_eng_x36.cpk` (nombres unificados) y `saves/` **intactos**.
2. Validar primero un **roundtrip sin cambios** de los bloques TXP2/apk y WESYS, comparando cada byte de vuelta, incluido el formato de textura de Xbox 360, sus mips, swizzling y referencias. No intentar modificar PNG directamente en los BIN comprimidos.
3. Localizar el mapa exacto `game2d_score` → `hudTexPes-scoreBase` y **asegurar que el CPK de Premier usa el HUD genérico PES**; si ese recurso es global para varias ligas, un cambio unilateral afectaría a todas, y se requiere un método de selección por competición.
4. Primera sustitución **visual mínima**: colores/placas de Premier League inspirados en una estética de retransmisión moderna, manteniendo mismo tamaño de atlas y HUD liviano; sin sumar grandes texturas ni efectos. Solo copia del CPK `dt11_x36.cpk`, **jamás in place**.
5. Verificar la TOC, descompresión y reinyección, todos los 751 recursos y que los **749 recursos ajenos a los 2 objetivos** mantengan bytes idénticos.
6. Probar un partido de Premier League en Android: navegación de menús, marcador al menos en primer/segundo tiempo, FPS antes/después, retorno a menú, save/load. Si falla, restaurar copia original inmediatamente.
7. Solo tras el piloto, diseñar variantes **LaLiga, Serie A, Bundesliga, Liga BetPlay, Liga MX** según el soporte real del motor, evitando fingir marcadores por competición si no hay selector dinámico.

**Limitación actual:** sin reempaquetador TXP2 Xbox 360 validado y sin comprobación del selector liga→HUD, **no hay parche seguro para instalar**. El usuario ya aportó la captura y `dt11`; **no pedirle de nuevo esos archivos**.

Respetar copyright: **no subir CPK ni texturas propietarias** a GitHub público. Documentar solo recursos, método y hashes.
