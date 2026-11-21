# PES 2017 Android — Lote 07B: corrección de transparencia (21-11-2026)

**Estado:** archivo acumulativo CPK terminado y verificado binariamente. **Pendiente prueba de menús/partidos y FPS en Xiaomi Mi 10T**.

## Motivo

En la prueba Android del lote 07 el usuario mostró que Coppa Italia, Coupe de France y Taça de Portugal cargaban correctamente a **60 FPS en el menú**, pero aparecían sobre **rectángulos blancos** que no armonizaban con la presentación solicitada (lo más cercana posible a EA Sports FC 26 sin aumentar recursos ni sacrificar estabilidad). Se realizó únicamente la corrección estética de las transparencias, sin tocar nombres, plantillas, marcadores, motor ni otros logos.

## Base y resultado privados

| Campo | Valor |
| --- | --- |
| CPK de entrada | `dt15_x36_LOTE07_COPPA_FRANCIA_PORTUGAL.cpk` |
| SHA-256 de entrada | `fff16a5633c8df17a52c875f9f6db79b1d4fcfcb7615d39b4597c0bcd18ee140` |
| CPK corregido | `dt15_x36_LOTE07B_TRANSPARENTE_FC26.cpk` |
| SHA-256 corregido | `10778afa0f01507edc62eb5940caf51a2a66eaa10520fae538b67d8b42fe140c` |
| Tamaño CPK en ambas versiones | **246746371 bytes**, idéntico |
| Entradas CPK totales | **2784** |
| Entradas corregidas | **3** |
| Entradas preservadas byte a byte | **2781/2781** |

## Archivos exactos reemplazados

| Competición | Ruta dentro del `dt15` | Antes → después | SHA-256 PNG corregido |
| --- | --- | ---: | --- |
| Coppa Italia Frecciarossa | `common/render/symbol/emblemLc/emb_0016_l.png` | 4256 → **6765 bytes** | `95ca7338c09e01a40f08ef7c5823f222bd4e3ed703f8987d2ee798e4b4de6846` |
| Coupe de France Crédit Agricole | `common/render/symbol/emblemLc/emb_0018_l.png` | 6357 → **7423 bytes** | `017b9b2131807e16ed15f1f46230fa60852d682efe72b75df56abe6367fa18ed` |
| Taça de Portugal Generali Tranquilidade | `common/render/symbol/emblemLc/emb_0020_l.png` | 4626 → **7945 bytes** | `597b9f005790c70477e3e04be9e1609aa8723d07aee67ae81bd9b2c235416877` |

## Cómo se corrigieron los PNG

- Se recuperaron los **PNG de origen** desde un artefacto temporal de GitHub Actions en una rama técnica. Esos originales permanecieron fuera del historial público. Los hashes de fuente están en el manifiesto original del lote 07.
- **Francia y Portugal:** se partió de su PNG original RGBA con transparencia alfa y se reescaló preservando esa transparencia.
- **Coppa Italia:** el original era un PNG **opaco blanco** de 600×600; se separó matemáticamente el blanco exterior y de los huecos del emblema, manteniendo el texto blanco **dentro del rectángulo rojo FRECCIAROSSA**.
- Los tres recursos finales son **PNG indexados de 256×256 con alfa** (paleta de 256 colores). Se preservaron marcas, proporciones y colores; no se inventaron nuevos logos ni se añadieron texturas grandes.
- Se comprobó su apariencia sobre **fondos grises, azules y oscuros**. Algunos textos azul marino tienen menor contraste sobre fondos muy oscuros, pero se priorizó conservar los logos originales, evitando un cuadro blanco o reestilizaciones agresivas.

## Prueba estructural terminada

Cada una de las tres imágenes fue reemplazada de manera secuencial utilizando `mods/competition-branding/tools/patch_competition_logo.py`, partiendo de **una copia** del lote 07. En cada paso se comprobaron la cabecera, la TOC, el PNG y todas las entradas ajenas al recurso objetivo.

Una comparación final independiente del CPK previo con la revisión confirmó **solo tres entradas diferentes**, 2781 archivos sin cambios, longitud total idéntica y transparencias correctas en los tres PNG.

## Instalación y prueba Android (pendiente)

1. Cerrar completamente PES 2017.
2. Guardar **una copia fuera de la carpeta del juego** del `dt15_x36.cpk` funcional actual (lote 07).
3. Renombrar `dt15_x36_LOTE07B_TRANSPARENTE_FC26.cpk` a `dt15_x36.cpk` y reemplazar exclusivamente ese archivo.
4. Abrir las copas de Italia, Francia y Portugal; verificar ausencia de rectángulos blancos y visibilidad de los textos en el menú gris/azul.
5. Revisar FA Cup, Copa del Rey, Supercopa de España, Liga Portugal y otras ligas para descartar regresiones.
6. Entrar a un partido completo y observar estabilidad/FPS. Probar carga/guardado en Liga Máster usando copia de prueba, sin arriesgar partidas principales.
7. Ante cualquier error, salir y restaurar el `dt15` del lote 07.

**No declarar estabilidad ni FPS sostenidos sin las pruebas del usuario.** Aunque las imágenes tienen la misma resolución, el efecto en Android debe comprobarse.

**Política del repositorio:** sólo documentación, hashes y código, nunca los CPK completos ni marcas de terceros sin autorización de redistribución.
