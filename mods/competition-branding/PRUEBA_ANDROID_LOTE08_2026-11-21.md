# PES 2017 Android — verificación visual del lote 08 (21/11/2026)

**Estado:** tres logos nuevos visibles y menú funcional en Xiaomi Mi 10T. **FPS de partido, estabilidad prolongada y guardado/carga pendientes.**

## Evidencia aportada por el usuario

Tres capturas de la pantalla `Select Competition` después de instalar el archivo acumulativo privado `dt15_x36_LOTE08_KNVB_SUPERCUP_PORTUGAL_FC26.cpk`:

| País/pantalla | Recurso modificado | Resultado en captura | FPS | Tiempo de fotograma | Temperatura del indicador |
| --- | --- | --- | ---: | ---: | ---: |
| Países Bajos | `emb_0019_l.png`, KNVB Beker (Netherlands Cup) | Nuevo escudo romboidal oscuro visible, sin cuadro blanco | 60 | 16,6 ms | 51 °C |
| Italia | `emb_0076_l.png`, EA SPORTS FC Supercup | Trofeo celeste y base azul visibles, sin cuadro blanco | 59 | 16,8 ms | 53 °C |
| Portugal | `emb_0020_l.png`, Taça de Portugal | Logo multicolor y letras visibles, sin cuadro blanco; el texto todavía parece pequeño y de contraste limitado | 60 | 16,6 ms | 53 °C |

Las capturas también muestran que los emblemas previos de Serie A, Coppa Italia, Serie B y Liga Portugal siguen apareciendo.

**Observaciones de calidad:** el logo italiano de Supercopa parece pequeño en su casilla, y el de Taça de Portugal conserva letras finas de difícil lectura; no obstante ambos se renderizan. El emblema de `Dutch Super Cup` sigue presentando un rectángulo blanco y una identidad visual antigua; **no formó parte del lote 08**. Los nombres del menú siguen genéricos, porque todavía no se editaron sus cadenas de texto.

## Verificación de alcance

- CPK privado de salida: `dt15_x36_LOTE08_KNVB_SUPERCUP_PORTUGAL_FC26.cpk`
- SHA-256: `54949b7f610ab3b0cf371b68c83cc19d482b01c6e53e2bbabbb1c33940707547`
- Tamaño: **246746371 bytes**
- **3 de 2784** recursos modificados respecto al lote 07B; **2781 idénticos byte a byte** según el análisis estructural previo.
- La prueba visual confirma que esos tres recursos aparecen y que el menú conserva fluidez; no demuestra que los 59–60 FPS sean sostenidos durante el partido.

## Decisión para el siguiente lote

1. Tomar el **lote 08 como última base visualmente comprobada en menú**, sin borrar el respaldo del lote 07B.
2. **Prioridad sugerida:** logos originales y sin fondo de otras supercopas nacionales, comenzando por Dutch Super Cup/Johan Cruyff Schaal, luego Francia y Portugal, pero **solo después de verificar la identidad exacta de la temporada 2026/27 y los IDs internos**.
3. Considerar en un lote separado un ajuste conservador de escalado para EA FC Supercup (se ve pequeño) y contraste de Taça de Portugal. No aumentar resolución ni añadir texturas 4K.
4. Mantener lotes de **2–4 recursos como máximo** y compararlos byte por byte contra el CPK previo; preservar FPS y rollback.
5. Para corregir nombres como `Netherlands Cup`, `Italian Super Cup`, `Portugal Cup`, investigar antes el archivo de texto correspondiente (`dt10`/idiomas); no mezclar cambios de texto y PNG.
6. Se solicita en futuras pruebas comprobar partido completo, retorno al menú y guardado/carga de prueba para evaluar estabilidad real.

**No subir capturas del usuario, CPK comerciales ni marcas a Git público.** Aquí únicamente se registra evidencia y metadatos técnicos.
