# PES 2017 Android — Lote 06: Copa del Rey y Supercopa de España

**Fecha:** 21/11/2026 · **Estado:** CPK acumulativo **verificado binariamente**, **pendiente de prueba en Android**.

## Decisión de alcance y prioridad
Para conservar la estabilidad ya confirmada en las capturas del último lote, limitar este parche a **DOS competiciones** en un solo CPK: Copa del Rey y Supercopa de España. Coppa Italia, Coupe de France, KNVB Beker y Taça de Portugal se mantienen sin cambios por ahora: se han identificado sus logos antiguos, pero no se inyectan versiones sin arte original plenamente comprobado.

El emblema de Copa del Rey es el diseño auténtico **sin el patrocinador MAPFRE**. La competición en 2026/27 se denomina Copa del Rey MAPFRE, pero este lote no agrega ni simula el logotipo comercial de MAPFRE. El diseño de Supercopa de España procede igualmente de un SVG vectorial real. Se preservan proporciones y colores en un recuadro blanco para mostrar correctamente los detalles oscuros en los menús de PES 2017.

## Archivo de partida y destino (archivos PRIVADOS, no incluidos en Git)

| Dato | Valor |
| --- | --- |
| Entrada | `dt15_x36_LOTE05_FA_CUP_AUTENTICA.cpk` |
| SHA-256 entrada | `03cbeb18fc847873a711c733f1ec8fbfa03d60d5688803f07e1310f12004f3c2` |
| Salida acumulativa | `dt15_x36_LOTE06_COPA_REY_SUPERCOPA_AUTENTICAS.cpk` |
| SHA-256 salida | `c47883f6093dcdc786cf6a83e41d1a2116afb147a76a7d6fea74c2cbb0b78761` |
| Tamaño entrada y salida | **246746371 bytes** |
| Cantidad recursos en CPK | **2784** |
| Recursos modificados | **2** |
| Recursos intactos byte a byte | **2782** |
| Logo FA Cup del lote 05 | **preservado** |

## Recursos modificados (solo PNG dentro de dt15)

| Copa | Archivo dentro del CPK | Antes → después | PNG SHA-256 |
| --- | --- | --- | --- |
| Copa del Rey | `common/render/symbol/emblemLc/emb_0017_l.png` | 16525 → 5251 bytes | `c26e552c204593f5487c12938f5e3c198af76641e0a8a1844df009ebb173d3f2` |
| Supercopa de España | `common/render/symbol/emblemLc/emb_0074_l.png` | 5283 → 4865 bytes | `bdbc57e160398664ae560034bee20cadcfdc41e735ffc68b010d3d1966fc0851` |

**Formato:** PNG 256×256, paleta indexada (P), transparencia, margen interno y fondo blanco para que los detalles oscuros sean legibles tanto sobre fondos claros como oscuros. Misma resolución que los PNG reemplazados: no se introducen texturas 4K o recursos pesados.

## SVG auténticos de entrada

Ambos se obtuvieron para uso privado desde un espejo público de logos reales, **sin incorporarlos al repositorio**:

- Copa del Rey: `mierzida/FLP_forBBK` commit `cd7043224e00c85fe1d2a0437003de2b96425b39`, `public/assets/logos/spain/copa-del-rey.svg` — SHA-256 `aaced486308a2e1b2763fb7b20b7a06861b95b3c5101bca3d1d82875a7391fe7`.
- Supercopa de España: misma revisión, `public/assets/logos/spain/supercopa-de-espana.svg` — SHA-256 `82bfc2c6628d8037b744698a36036ee16b7b3b11c515b5ba5a7ed5a483ea364d`.

Fuentes oficiales para validar las identidades actuales: [RFEF Copa del Rey](https://rfef.es/es/competiciones/copa-de-sm-el-rey), [RFEF Supercopa](https://rfef.es/es/competiciones/supercopa-de-espana). Los SVG provienen de un archivo de terceros; no se atribuye su distribución a la RFEF.

## Validación estructural terminada

1. Se generaron candidatos PNG de 16/32/64/128/256 colores; se eligieron los de mejor compatibilidad/tamaño bajo el espacio disponible en cada recurso.
2. Los dos PNG se integraron secuencialmente mediante `mods/competition-branding/tools/patch_competition_logo.py`, usando exclusivamente copias.
3. Cada etapa volvió a leer los recursos y verificó el encabezado, la TOC y los demás archivos byte a byte.
4. Una última comparación del CPK final contra el lote 05 verificó: **solo 2 cambios**, longitud idéntica, 2782 recursos intactos y el logo anterior de FA Cup idéntico.
5. No se cambió `dt10`, `dt11`, nombres de ligas, plantillas, marcadores, binarios, partidas guardadas ni el APK.

## Instalación y control de rendimiento

1. **Respaldar el `dt15_x36.cpk` funcional actual** fuera de la carpeta del juego. Nunca borrarlo.
2. Cerrar PES 2017 completamente.
3. Descargar el nuevo CPK privado, renombrar a `dt15_x36.cpk` y reemplazar **solo** ese archivo.
4. Comprobar Copa del Rey y Spanish Super Cup en menús de competiciones. La etiqueta genérica de texto no cambia.
5. Revisar FA Cup, LaLiga Hypermotion, Liga Portugal y Serie BKT como controles de regresión.
6. Entrar en un partido y verificar carga, FPS y cierre/retorno al menú; comparar contra la misma configuración. Comprobar guardado/carga de una partida de prueba si se utiliza Liga Máster.
7. Si ocurre cualquier fallo, cerrar PES y restaurar el `dt15` anterior.

**No afirmar que los FPS son 60 con el nuevo parche ni promover a «estable» hasta que el usuario lo confirme en su Xiaomi.** Un CPK bien formado no garantiza compatibilidad funcional.

## Continuación

Siguiente tanda, **después de esta prueba**: Coppa Italia Frecciarossa, Coupe de France Crédit Agricole y otras copas; solo con archivos de origen auténticos y verificados, sin superar tres/cuatro competiciones por lote para limitar regresiones.

Solo se guardan documentos, código, hashes y mapas en GitHub público; **no se publican logos de terceros ni CPK del juego**.
