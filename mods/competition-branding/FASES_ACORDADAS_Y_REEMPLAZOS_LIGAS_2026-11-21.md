# PES 2017 Android — recuperación del plan original de fases y sustituciones
**Fecha:** 21/11/2026. **Origen:** decisiones anteriores con el usuario (no inferir sustituciones adicionales).

## Las tres ligas ficticias que acordamos reemplazar

| Ranura existente PES 2017 | Destino acordado | Prioridad | Estado |
|---|---|---|---|
| **PEU League** | **Bundesliga de Alemania** | Alta | **Planificado; sin cambios instalados** |
| **PLA League** | **Liga BetPlay DIMAYOR (Colombia)** | **Obligatoria y prioritaria** | **Planificado; sin cambios instalados** |
| **PAS League** | **Saudi Pro League (Arabia Saudita)** | Alta | **Planificado; sin cambios instalados** |

Para PAS se consideró previamente la **Süper Lig turca**, pero se eligió finalmente **Saudi Pro League**. **Liga MX** y **MLS** se discutieron como candidatas adicionales, pero **NO** se les asignó ninguna ranura ni se confirmó eliminar otra liga. No presentarlas como decisiones cerradas.

## Ligas a conservar y actualizar, no eliminar
- Premier League y EFL Championship (Inglaterra).
- LaLiga y LaLiga Hypermotion (España).
- Serie A y Serie B (Italia).
- Ligue 1 y Ligue 2 (Francia).
- Eredivisie (Países Bajos).
- Liga Portugal.
- **Liga brasileña, argentina y chilena**: conservarlas, revisar sus logos y plantillas en su momento, no confundirlas con sustituciones.

## Fases del proyecto acordadas

1. **Fase 2A:** Logos y emblemas de clubes y competiciones. Lotes conservadores, CPK acumulativo, fuente auténtica, alfa transparente y revisión de integridad; última base visualmente probada en menús: **Lote 10**. No afirmar que todas las ligas de Brasil, Argentina, Chile, PEU/PLA/PAS y Others estén ya corregidas.
2. **Fase 2B:** Nombres oficiales de ligas, copas y competiciones, manteniendo fidelidad de cada ranura; localizar recursos de idioma o texto (p. ej. `dt10_x36.cpk` u otros), no confundir PNG con datos de texto. El usuario quiere empezar los nombres después del trabajo principal de logos.
3. **Fase 3:** Marcadores y elementos visuales específicos de la competición, empezando por las principales, sin cargar innecesariamente la GPU.
4. **Fase 4:** **Reemplazar PEU→Bundesliga, PLA→Liga BetPlay, PAS→Saudi Pro League** y actualizar estructura de ligas, clubes, ascensos/descensos y temporada **2026/27**. **Esta fase aún no ha sido instalada**. Antes de alterar equipos/IDs y Liga Máster requiere auditoría de tablas, número de clubes por ranura y compatibilidad.
5. **Fase 5:** Plantillas, fichajes y actualizaciones deportivas de 2026/27.
6. **Fase 6:** Resto de acabado gráfico inspirado en FC 26 (uniformes y elementos estéticos), sin alterar estabilidad.

Fases 2B/3/4 pueden requerir ajustes del orden de ejecución para evitar mostrar los nombres nuevos de Bundesliga, Colombia y Arabia Saudita mientras sus ranuras todavía tengan los clubes ficticios de PEU/PLA/PAS. **Nunca renombrar los tres torneos antes de hacer el reemplazo real de sus clubes y estructura.**

## Restricciones acordadas
- Mantener idealmente entre **50 y 60 FPS** en Xiaomi Mi 10T (Android 12, 6 GB RAM).
- Respaldo previo de cada CPK; preservar archivos originales y guardados.
- Verificar estructura, TOC, tamaños, rutas, hashes y cada entrada no modificada; grupos de hasta tres sustituciones por lote.
- Prueba visual de menús Android y, antes de decir «estable», pruebas de partido completo, retorno al menú, guardado/carga.
- Mantener informes/manifiestos en GitHub, **no publicar los archivos de juego ni imágenes de terceros**.
