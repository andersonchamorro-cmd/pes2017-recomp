# PES 2017 Android — competiciones, lote de logos (21/11/2026)

> **Estado: VALIDACIÓN ESTRUCTURAL COMPLETA; PRUEBA EN ANDROID PENDIENTE.**
> No sustituir la versión estable hasta que el usuario compruebe arranque, escudos, partidas y FPS.
> Este lote de logos de competición es distinto de los lotes 04–06 previos de **escudos de clubes**.

## Procedencia y alcance

- Base: `dt15_x36(1).cpk`, suministrada por el usuario como archivo actual.
- Archivo privado generado: `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk`.
- Se modifican **solo seis entradas PNG** de `common/render/symbol/emblemLc/`, conservando la integridad de otros 2.778 recursos.
- Se usan cuatro logos entregados por el usuario: Liga Portugal, LaLiga Hypermotion, Ligue 2 BKT y Serie BKT. **EFL Championship no se modifica** hasta disponer de un archivo oficial verificado.
- Los nombres de menús, marcadores, `dt10`, bases de equipos, plantillas, guardados y ejecutable no se modifican.
- Los logos provienen de imágenes del usuario; no se afirma que correspondan a la temporada vigente sin revisión independiente.

## Hashes de archivos privados (NO almacenar en Git público)

| Archivo | Tamaño (bytes) | SHA-256 |
| --- | ---: | --- |
| `dt15_x36(1).cpk` (entrada) | 246746371 | `e610ef7128eeabcc48b8422004950fa0d81004eef205beefbf0ed66a158841ae` |
| `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk` (salida) | 246746371 | `853d9cdb40cf22525877231544d8670cf2b6150ad667de83544cf1f4533bee98` |

## Recursos exactos

| Competición | Archivo PNG reemplazado | Tamaño anterior → nuevo (bytes) |
| --- | --- | --- |
| Liga Portugal | `emb_0014_l.png` | 2994 → 3696 |
| Segunda española, LaLiga Hypermotion | `emb_0067_l.png`, `emb_0071_l.png` | 4399 → 4480 (cada uno) |
| Ligue 2 BKT | `emb_0068_l.png` | 3331 → 2296 |
| Serie BKT | `emb_0069_l.png`, `emb_0072_l.png` | 5335 → 5008 (cada uno) |

La modificación se realiza *in place* sobre copia del CPK existente, actualizando el índice TOC de las seis entradas. El contenedor final tiene 2.784 entradas, conserva su longitud y el resto de recursos conserva sus datos binarios. **Eso no prueba que el juego sea funcional ni que los FPS permanezcan iguales**.

## Material PNG original de entrada (privado, no subir al repositorio)

| Archivo | SHA-256 |
| --- | --- |
| `liga-portugal-seeklogo.png` | `ba3d7a9768d6b5a4b2777287f6c39580afd83c7170a38069603127c7bc9c0b37` |
| `laliga-hypermotion-seeklogo.png` | `b8379dd75bbc102ae985a382e679fd2839a9b2ae73485e36014b95d931b34588` |
| `ligue-2-bkt-seeklogo.png` | `57fa0a0ada89906b5fdcab64e78c88d2bcf118c96c234e6aa33dc5889980543d` |
| `serie-b-2018-logo.png` | `f9f73024b9d22e7f6fe8feb9d0557d56c1c4e270b226da0ba4eba0d82bbe62c2` |

## Criterios para confirmar en Xiaomi Mi 10T

1. Guardar una copia independiente del **CPK actual que sí funciona** antes de instalar el parche.
2. Cerrar el juego completamente; reemplazar solo `dt15_x36.cpk` por esta salida renombrada.
3. Comprobar visualmente las cuatro competiciones, especialmente que cada logo corresponda a su liga. Comprobar Premier, Chelsea y Serie A como controles de regresión.
4. Entrar a un partido, volver al menú y confirmar que no hay cierres ni texturas incorrectas.
5. Comprobar acceso, guardado y carga de Liga Máster. No iniciar una partida nueva sobre la única copia del guardado importante.
6. Comparar los FPS y la estabilidad con la misma resolución y ajustes de la versión previa. La inspección binaria no mide rendimiento.
7. Ante cualquier anomalía, cerrar el juego y **restaurar la copia original del dt15**.

**Promoción a estable:** solo después de confirmación explícita del usuario. No actualizar `main` ni sobreescribir la rama previa de nombres/escudos hasta entonces.

## Política de GitHub

Este repositorio público conserva exclusivamente **documentación, hashes, manifest y código de herramientas**. No subir CPK del juego, imágenes de marcas o escudos de terceros, ni datos comerciales. Los archivos privados permanecen en posesión del usuario. Se trabaja en rama nueva para conservar intactos los lotes anteriores.
