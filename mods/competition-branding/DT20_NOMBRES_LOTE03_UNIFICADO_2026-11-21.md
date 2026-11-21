# PES 2017 Android — Lote 03 unificado: nombres reales de ligas, copas y supercopas

**Fecha:** 21/11/2026. **Estado:** CPK armado y verificado con dos comprobaciones independientes. **Prueba funcional Android: pendiente.**

El usuario aprobó con 3 capturas el **lote 02** de nombres, donde **Sky Bet Championship**, **Serie BKT** y **LALIGA HYPERMOTION** aparecen a 60 FPS y sin recortes en los menús de selección. Solicitó reunir todos los nombres pendientes en **un solo CPK acumulativo**, sin más lotes de tres.

## Archivos del lote unificado

| Campo | Valor |
| --- | --- |
| Base ya probada visualmente | `dt20_eng_x36_NOMBRES_LOTE02_SEGUNDAS_DIVISIONES.cpk` |
| SHA-256 entrada | `29f3beac0f91f3f4c336e586f407c4c31ec0d4592b89fd80f5a10600af4e0ccd` |
| Salida entregada privadamente | `dt20_eng_x36_TODOS_NOMBRES_OFICIALES_FC26.cpk` |
| SHA-256 salida | `83db345a1bff6c2e57976ca13ef13bd43987c22cb655b118c7dd41f769513150` |
| Tamaño fuente/salida | **368184 bytes** |
| Recursos CPK | **5** |
| Recurso modificado | `eng/string/all.str` |
| Entradas CPK ajenas intactas | **4/4** byte a byte |
| STR grupos indexados | **202/202**, recreados con offsets, cantidades y longitudes de cadenas válidas |
| Registros STR | **11188/11188** |
| Registros textuales realmente cambiados | **44** (Lcx1C: 10; Onml1W: 21; TermpesC: 13) |
| Bytes WESYS comprimidos | 280338 → **279595** |
| Capacidad reservada | **284672** bytes |
| Bytes STR descomprimidos | 844784 → **844768** |

## Nombre oficial (o tradicional reconocido) aplicado a cada ranura del juego

### Ligas
- `Spanish League` → **LALIGA EA SPORTS**.
- `Argentine League`, `Argentinean League` y `Argentinian League` → **Liga Profesional** (solo las etiquetas de Liga Máster y pantallas correspondientes; el formato de clubes/torneo no se ha alterado).
- `Chilean League` → **Liga de Primera**.
- `French League` → **Ligue 1**, `Dutch League` → **Eredivisie**, `Portuguese League` → **Liga Portugal**, `Brazilian League` → **Brasileirão** (estos cuatro especialmente en lista de ligas, filtros y frases «Current Club»).
- La etiqueta ya correcta `CAMPEONATO BRASILEIRO` no se cambia.
- Se conservan los seis nombres **ya aprobados**: Premier League, Serie A, Liga Portugal, Sky Bet Championship, Serie BKT y LALIGA HYPERMOTION.

### Copas
- `England Cup` → **Emirates FA Cup**
- `Italian Cup` → **Coppa Italia**
- `Spanish Cup` → **Copa del Rey**
- `French Cup` → **Coupe de France**
- `Netherlands Cup` → **KNVB Beker**
- `Portugal Cup` → **Taça de Portugal**
- `Brazilian Cup` → **Copa do Brasil**
- `Argentinean Cup` → **Copa Argentina**
- `Chilean Cup` → **Copa Chile**

### Supercopas
- `English Super Cup` → **FA Community Shield**
- `Spanish Super Cup` → **Supercopa de España**
- `French Super Cup` → **Trophée des Champions**
- `Italian Super Cup` → **EA SPORTS FC Supercup**
- `Dutch Super Cup` → **Johan Cruijff Schaal**
- `Portuguese Super Cup` → **Supertaça Cândido de Oliveira**
- `Argentine Super Cup` → **Supercopa Argentina**

### Playoffs de ascenso
- `English Promotion Play-off` → **Championship Play-offs**
- `Spanish 2nd Division Playoffs` → **LALIGA HYPERMOTION Play-offs**
- `Italian Promotion Play-off` → **Serie B Play-offs**

## Notas de alcance y compatibilidad
- En este lote, `all.str` necesitaba **cadenas de longitud variable** por las denominaciones auténticas, algo que los lotes 01/02 evitaron por cautela.
- Se reconocieron formalmente los grupos PES STR y cada una de sus 11188 etiquetas con **ID, longitud de bytes, longitud de caracteres Unicode y desplazamiento**. Una reconstrucción **sin cambios** reprodujo el archivo original **byte por byte**, antes de autorizar ninguna edición.
- Se reconstruyeron solo **3 grupos** de textos y se actualizaron correctamente las referencias/offsets de grupos que cambiaron de ubicación. Tras el parche, todas las 202 secciones y sus 11188 cadenas fueron decodificadas de nuevo sin pérdidas, manteniendo los 11144 registros no objetivo idénticos semánticamente.
- El envoltorio WESYS/zlib se volvió a comprimir y cabe dentro del espacio fijo del CPK; cabecera, TOC y otros 4 recursos sin corrupción.
- **No se cambiaron `dt10_x36.cpk`, `dt15_x36.cpk`, los jugadores, clubes, archivos de guardado ni IDs de torneos.**
- **No se renombraron competiciones ficticias:** PEU League / Cup / Super Cup, PLA League / Cup / Super Cup, PAS League / Cup / Super Cup, KONAMI League y KONAMI Cup, ni `Club International Cup` o `South American Championship`, que requieren mapeo. Sustituciones futuras acordadas: **PEU→Bundesliga; PLA→Liga BetPlay; PAS→Liga MX**. Primero deben instalarse equipos y estructura.

## Nombres de patrocinio y contexto de temporada
Los nombres básicos o comerciales se eligieron para que fueran **reconocibles y legibles en el menú** sin añadir publicidad de patrocinadores que no fuera parte de la competición. Las denominaciones exactas pueden variar por temporada, por lo que se consultaron autoridades de 2026/27:
- Italia, EA SPORTS FC Supercup y Coppa Italia: https://www.legaseriea.it/supercoppa/index
- España, Supercopa: https://rfef.es/es/noticias/competiciones-masculinas/supercopa
- Inglaterra, FA Community Shield: https://www.thefa.com/news/2026/aug/14/where-to-watch-fa-community-shield-20261408
- Francia, Trophée des Champions / Coupe de France: https://www.lfp.fr/article/la-lfp-et-decathlon-devoilent-le-ballon-du-trophee-des-champions-2026
- Países Bajos: https://www.knvb.nl/competities/overige-competities/johan-cruijff-schaal
- Portugal, temporada 2026/27: https://www.fpf.pt/DownloadDocument.ashx?id=26802
- Chile, Liga de Primera: https://www.anfp.cl/categorias/liga-de-primera/
- Brasil, Copa do Brasil: https://www.cbf.com.br/futebol-brasileiro/noticias/copa-do-brasil/profissional/copa-do-brasil-quinta-fase-comeca-com-promessa-de-grandes-jogos

## Protocolo Android obligatorio para aprobar funcionalmente

1. **Respaldo** del `dt20_eng_x36.cpk` instalado, que es el Lote 02 ya comprobado.
2. Cerrar PES 2017, descargar el nuevo lote unificado y renombrar a `dt20_eng_x36.cpk`.
3. Reemplazar **solamente** ese CPK en `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
4. Probar **España → LALIGA EA SPORTS / Copa del Rey / Supercopa de España**, **Inglaterra → FA Community Shield / Emirates FA Cup**, **Francia → Trophée des Champions**, **Portugal → Supertaça Cândido de Oliveira**, **Italia → EA SPORTS FC Supercup**, **Países Bajos → Johan Cruijff Schaal**, y las copas sudamericanas. Confirmar que no se truncan nombres largos, no hay caracteres extraños y la carga no se bloquea.
5. En Home/Away verificar que siguen apareciendo Premier League, Serie A, Liga Portugal, Sky Bet Championship, Serie BKT, LALIGA HYPERMOTION, y probar selección de equipos, un partido y vuelta al menú.
6. Restaurar el lote 02 si un nombre se corta o la interfaz falla; evitar sobreescribir `saves` y `save_backups`.

**No afirmar que funciona a 60 FPS en Android hasta recibir capturas.** La verificación binaria no equivale a una prueba del parser concreto del videojuego o de la distribución final.

GitHub público: solo documentación, hashes y manifiestos, **nunca copiar binarios del videojuego ni las tablas completas**.
