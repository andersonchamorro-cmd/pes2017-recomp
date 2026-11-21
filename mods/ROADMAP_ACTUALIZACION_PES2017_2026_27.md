# PES 2017 Android — roadmap consolidado del proyecto

Actualizado: **21 de noviembre de 2026**. 
Repositorio: `andersonchamorro-cmd/pes2017-recomp`. 
Rama de documentación/experimentos actuales: `feature/competition-logos-20261121`.
Dispositivo objetivo: **Xiaomi Mi 10T 5G, Snapdragon 865, 6 GB de RAM, Android 12**.

## Objetivo y reglas no negociables

Transformar progresivamente PES 2017 (Xbox 360 recompilado para Android) en una edición actualizada, visualmente cercana a EA Sports FC 26, con licencias reales, identidad gráfica y más adelante competiciones, clubes, jugadores y plantillas 2026/27. Preferencia expresa del usuario: **no degradar FPS, estabilidad, memoria o temperatura por una mejora cosmética**. El juego ya funciona y por ello cada cambio debe ser incremental y reversible. Objetivo aproximado: **50–60 FPS**, conservar los **60 FPS visibles en menús** como referencia, no como evidencia de partida completa.

- Cada nuevo parche parte de la **última versión acumulativa aprobada por el usuario**, no del original ni de una base más antigua.
- Copia de seguridad local de CPK(s) y partidas; archivo privado + SHA-256 + manifiesto de recursos e IDs; comparaciones byte a byte; arranque/partido/guardado/FPS en Android; solo después promover a estable.
- Mantener `main` y versiones anteriores intactas durante experimentos.
- En el repositorio público guardar **documentos, hashes, mapas y herramientas reproducibles**, no `default.xex`, CPK completos del juego ni logos de terceros sin licencia de distribución.
- No alterar simultáneamente motor, `dt10`, `dt15` y UI/marcadores en una misma prueba.

## Orden acordado

| Etapa | Alcance | Estado al 21-11-2026 |
| --- | --- | --- |
| 0. Base jugable y controles | Port Android / validaciones de estabilidad; controlador Xbox jugador 1 tratado en rama separada | El usuario ya juega; corrección del mando separada; no mezclar con mods de ligas |
| 1. Licenciar clubes de ligas existentes, **base 2016/17** | Nombres (`dt10` / `Team.bin`), escudos (`dt15`), IDs correctos | Lotes generados; unos probados visualmente, otros solo validados estructuralmente. No hay prueba integral de todos |
| 2A. **Logos originales de competiciones** | Ligas principales y segundas, luego copas, supercopas, torneos continentales/internacionales, selecciones; recursos gráficos `emblemLc` | **EN CURSO**. Último parche de seis recursos visible en menú; pendiente Serie B, partido y guardado |
| 2B. **Nombres reales de competiciones en el menú** | Reemplazar English League, Italian League, Spanish 2nd Division, Portugal League, etc. **solo al localizar y verificar dónde se almacenan los textos** | Pendiente. Logo y nombre son recursos distintos; NO inventar un parche `dt10` sin inspección |
| 3. **Marcadores TV por competición** | Piloto Premier League; si funciona, Champions, LaLiga, Europa League, Serie A y demás | Pendiente: debe descubrirse qué recursos usan marcadores y si selección automática por competición es posible. No prometerla antes de verificar |
| 4. Remodelación de ligas **2026/27** | Ascensos/descensos, estructura e IDs de ligas/equipos; diseñar y validar uso de ligas genéricas | PLANEADO. No modificar todavía. Reservas propuestas: **PEU → Bundesliga, PLA → Liga BetPlay de Colombia, PAS → Saudi Pro League**. Liga MX y MLS a estudiar con otros espacios |
| 5. Plantillas 2026/27 y datos deportivos | Fichajes, jugadores, dorsales, estadísticas, equipos, calendarios y asignación a ligas | PLANEADO, **después** de resolver IDs/divisiones; requiere pruebas con Liga Máster y guardados |
| 6. Identidad visual de clubes y jugadores | Kits/uniformes 2026/27, caras, balones y eventualmente estadios: prioridad a recursos ligeros, experimentos aislados | PLAN FUTURO, no implementado |
| 7. QA continua | Control de FPS, calentamiento, errores gráficos, CPK intactos, reversión, guardado/carga | APLICAR EN TODAS LAS ETAPAS, no es un lote único |

**Prioridad de ligas:** clubes y competiciones importantes/comerciales, incluyendo **Liga BetPlay colombiana** como requisito del usuario; 50–60 FPS si es posible. La reasignación PEU/PLA/PAS es plan tentativo, **no cambio instalado**. Antes de reestructurar ligas, verificar compatibilidad con las partidas.

## Historial concreto de la fase 1 — licencias de clubes

| Lote | Ligas | Trabajo y alcance |
| --- | --- | --- |
| Piloto | Premier, Chelsea / Manchester United / Manchester City | Prueba de 3 nombres reales en `Team.bin`, después 3 escudos por ID y tamaños 128/256 |
| Premier | 20 equipos | Nombres/escudos corregidos y probados visualmente en parte |
| LaLiga | 20 equipos | 18 equipos requerían cambios; 2 ya licenciados |
| Lote 03 | Serie A (20), Ligue 1 (20) | 2 clubes ficticios de Serie A corregidos (Juventus y Sassuolo); Ligue 1 ya licenciada |
| Lote 04 (**de clubes**) | Championship (24), Segunda española (22) | 46 nombres y 92 PNG de escudos |
| Lote 05 (**de clubes**) | Eredivisie (18), Portugal (18) | Eredivisie ya licenciada; 16 clubes portugueses corregidos |
| Lote 06 (**de clubes**) | Serie B italiana (22), Ligue 2 (20) | 22 clubes italianos corregidos; Ligue 2 ya licenciada |

**Balance de liga: 204 clubes cubiertos en 10 ligas.** Los documentos contabilizan aproximadamente **124 clubes con correcciones nuevas** y 80 ya licenciados; 204 no significa que se sustituyeran 204 escudos. La fase 1 conserva estructura/plantillas y nombres de la temporada base 2016/17.

Las guías anteriores están en `mods/team-branding/`. Los estados "generado / validado" no significan automáticamente "probado por el usuario".

## Avances de la fase 2 — logos de competiciones

- Logos de Premier, LaLiga, Serie A, Ligue 1 y Eredivisie: se reportaron funcionando visualmente en conversaciones anteriores.
- Última prueba: `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk`, derivado del `dt15_x36(1).cpk` aportado por el usuario; **6 PNG modificados de 2784** y 2778 recursos preservados byte a byte.
- Cuatro diseños suministrados por el usuario: **Liga Portugal, LaLiga Hypermotion, Ligue 2 BKT, Serie BKT**.
- El usuario instaló el último CPK y aportó tres capturas: Liga Portugal, LaLiga Hypermotion y Ligue 2 BKT visibles a **60 FPS / 16,7–16,8 ms en menús**, temperatura indicada **53–54 °C**. Serie BKT no aparece en esas capturas, aunque el cambio está en el CPK.
- EFL Championship: su emblema real previo no se reemplazó en el último lote. Evitar logos inventados.
- **Quedan**: inspeccionar el resto de las 68 entradas de logos (incluidas variantes), confirmar identidad oficial de las que falten; prioridad a ligas reales, copas nacionales, supercopas, Champions League/Europa League, internacionales y selecciones. Luego localizar y modificar nombres oficiales del menú en un lote aparte.
- **Quedan pruebas**: partido completo, comparar FPS con mismos ajustes, comprobar Liga Máster/guardado; no afirmar estabilidad plena solo por las 3 capturas de selección.

Documentos asociados:
- `mods/competition-branding/LOTE01_COMPETICIONES_SEGUNDAS_2026-11-21.md`
- `mods/competition-branding/lote01_competiciones_manifest.json`
- `mods/competition-branding/PRUEBA_ANDROID_VISUAL_2026-11-21.md`

**Advertencia de nombres de lotes:** "lote 04" existe tanto en `team-branding` (Championship/Segunda de clubes) como en archivo de competiciones actual `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk`. Son hitos distintos.

## Siguiente acción segura y necesidades de archivos

1. **Mantener el `dt15` actual que funciona.** No volver al original.
2. Documentar/corroborar Serie BKT, un partido completo, Liga Máster y FPS.
3. Identificar dentro de los 68 recursos los logos de ligas/copas/selecciones todavía incorrectos. Sustituir únicamente los confirmados, preferentemente PNG oficiales aportados por el usuario, respetando dimensiones/paleta/transparencia.
4. Para nombres del menú, inspeccionar el **`dt10_x36.cpk` actual** y, si allí no figuran, el paquete de idioma correspondiente: se requiere el binario correcto, no sirven supuestos.
5. Preparar piloto de marcador TV de **Premier** solo tras descubrir recursos/activación real, sin alterar el CPK estable de escudos ni prometer cambio automático por liga antes de medirlo.
6. Dejar la actualización deportiva 2026/27 para después de la identidad gráfica de competiciones/scoreboards y de preservar compatibilidad con partidas.

Documentación actualizada a partir de las conversaciones del usuario y de registros técnicos del propio repositorio; no se han cambiado archivos de juego en este commit.
