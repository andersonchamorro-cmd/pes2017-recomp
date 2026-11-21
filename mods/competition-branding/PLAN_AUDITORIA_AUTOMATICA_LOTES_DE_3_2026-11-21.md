# PES 2017 Android — plan de compilación acumulativa en tandas de tres

**Fecha: 21-11-2026. Estado: auditoría actual completada; no hay un nuevo CPK final verificado en Android.**

## Solicitud del usuario
Preparar todas las competiciones que realmente necesiten corrección mediante tandas de **hasta 3 cambios**, haciendo un control de calidad interno en cada tanda, integrando cada lote sobre el anterior y entregando **un solo CPK acumulativo al final**. Mantener la fidelidad de los logos a la temporada 2026/27, la estética moderna tipo FC26 y los FPS actuales sin cambios innecesarios.

## Inventario real y alcance
- Se revisó directamente el CPK **Lote 09** presente en el contenedor, tamaño 246746371 bytes, SHA-256 `2ef902c9c0874360f719ad167e6f6dbf17f1644d43e0ba46736589992199dfcd`.
- Dentro de los 2784 recursos del CPK hay **68 emblemas gráficos** en `common/render/symbol/emblemLc`.
- **68 recursos no equivalen a 68 competiciones reales**: incluyen variantes de Champions/Europa League/AFC, varias entradas duplicadas de copa internacional y emblemas de ligas/copas genéricas o ficticias (PEU/PLA/PAS, etc.).
- No reemplazar sin autorización conceptual las ligas genéricas por competiciones reales mientras no se finalice el mapeo deportivo de la fase 4.
- Algunos logos actuales ya son auténticos (Premier, LaLiga, FA Cup, varias competiciones UEFA y regionales); conservarlos si se mantienen vigentes y legibles.

## Problema confirmado al auditar el Lote 09
El lote 09 conserva estructura CPK correcta; reemplazó únicamente:
- `emb_0075_l.png`: Trophée des Champions
- `emb_0077_l.png`: Johan Cruijff Schaal
- `emb_0078_l.png`: Supertaça Cândido de Oliveira

**Sin embargo, las tres nuevas imágenes son completamente opacas**: canal alfa mínimo/máximo 255/255 y cuatro esquinas opacas. Esto crea rectángulos negros/blancos/grises en las casillas. Es contrario a la preferencia explícita del usuario de **no tener cuadros de fondo**.

**Decisión QA:** el lote 09 **no está aprobado visualmente**; no usar como base definitiva ni declararlo «sin bugs» antes de rehacerlo con transparencia real. **Última base comprobada por capturas de usuario: Lote 08**, `dt15_x36_LOTE08_KNVB_SUPERCUP_PORTUGAL_FC26.cpk`, SHA-256 `54949b7f610ab3b0cf371b68c83cc19d482b01c6e53e2bbabbb1c33940707547`, 246746371 bytes.

## Procedimiento estricto por cada tanda (máximo tres)

1. Comprobar fuente oficial/auténtica vigente e ID exacto; no alterar recursos ajenos o competencias ficticias sin mapeo.
2. Preparar cada logo PNG **256×256, indexado, con transparencia alfa auténtica**, sin fondos ni bordes opacos en las esquinas; revisar manualmente sobre fondo gris, azul y oscuro del menú.
3. Comparar el tamaño del PNG nuevo con la capacidad disponible de la entrada en el CPK; abortar ante desbordamiento.
4. Copiar el **último CPK acumulativo técnicamente aprobado**, nunca el original, a un nombre nuevo e inmutable.
5. Sustituir 1–3 PNG. En cada paso validar encabezado, TOC, recuento de 2784 recursos, extracción de PNG, IDs, offsets y el contenido de todas las entradas ajenas a la tanda.
6. Hacer **revisión independiente final** del lote: exactamente los N recursos esperados cambiados; los demás idénticos byte a byte; longitud de contenedor inalterada; SHA-256 de entrada y salida; manifiesto con fuente y cambios.
7. Rechazar lote si cualquier comprobación falla. Conservar versión anterior y registro de causa.
8. Al terminar todos los logos legítimos verificables, realizar auditoría final del CPK acumulativo: comparar con Lote 08, lista total de recursos modificados, PNG e integridad, sin cambios en datos de jugadores o partidos.
9. Entregar **solo el CPK acumulativo final** para la instalación del usuario; conservar respaldo/rollback del Lote 08.

## Límite imprescindible de lo que se puede verificar sin el Xiaomi

Las validaciones en PC prueban la integridad binaria y calidad de los PNG; **no pueden simular fielmente la recompilación Android ni medir FPS, partidas guardadas, estabilidad durante partidos o cambios de memoria del Xiaomi Mi 10T**. Para llamar «estable en el teléfono» al último CPK se requiere **una prueba final del usuario**, por lo menos menús de diferentes competiciones y partido completo, retorno y si se utiliza Liga Máster guardado/carga de prueba. No garantizar 100% ausencia de bugs antes de esa validación.

## Informe local de la auditoría
`PES2017_AUDITORIA_LOTE09_Y_PLAN_LOTES_DE_3.json` (JSON de inspección local) y `PES2017_LOTE09_INVENTARIO_GENERAL.png` (lámina de las 68 entradas). Esos archivos **no se incorporan como CPK al repositorio Git**.

Los logos de origen tienen derechos de sus titulares: GitHub público solo contiene scripts, decisiones de mapeo, documentación y hashes.
