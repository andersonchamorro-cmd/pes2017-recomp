# Lote 06 — Italian 2nd Division / Serie B + Ligue 2 (base 2016/17)

**Estado: generados y validados a nivel de archivo; sin prueba aún en Android**.

## Composición

- **Serie B (22 equipos):** todos los nombres y escudos eran ficticios. Se prepararon 22 nombres reales y 44 imágenes PNG para los tamaños 128 y 256.
- **Ligue 2 (20 equipos):** los veinte nombres y escudos ya estaban licenciados; no se cambiaron.
- Se han preservado todas las correcciones anteriores: Premier, LaLiga, Serie A, Ligue 1, Championship, Segunda española, Eredivisie y Liga Portugal.
- No se han alterado las posiciones de jugadores, plantillas, calendarios, divisiones, el juego ejecutable, ni los nombres/logos del menú de competiciones.

## Correspondencia exacta (ID de equipo PES 2017)

| ID | Original | Nombre del lote |
|---:|---|---|
| 317 | MA ZEBRA | ASCOLI PICCHIO FC |
| 4141 | ALVEGIARO | US AVELLINO |
| 319 | BAGNARONI | FC BARI 1908 |
| 4232 | CM YELLOW RED | BENEVENTO CALCIO |
| 187 | BRUTIE | BRESCIA CALCIO |
| 4075 | ER WHITE RED | CARPI FC |
| 1362 | ER BLACK WHITE | AC CESENA |
| 1920 | DL CRIMSON | AS CITTADELLA |
| 4234 | TI YELLOW BLUE | FROSINONE CALCIO |
| 4076 | LITOLIZANO | US LATINA CALCIO |
| 2377 | PM BLUE WHITE | NOVARA CALCIO |
| 4240 | PRASTOGNA | AC PERUGIA CALCIO |
| 4241 | TO BLUE BLACK | AC PISA 1909 |
| 2612 | PAILAMUDOVELI | FC PRO VERCELLI 1892 |
| 4244 | CM BURGUNDY | US SALERNITANA |
| 4923 | ER SKY BLUE | SPAL 2013 |
| 1600 | SPREMONESE | SPEZIA CALCIO |
| 331 | TECCARINA | TERNANA CALCIO |
| 4077 | DREPANUMESE | TRAPANI CALCIO |
| 336 | DL BLUE | HELLAS VERONA FC |
| 337 | VOCCHAIONI | VICENZA CALCIO |
| 4230 | LR WHITE BLUE | VIRTUS ENTELLA |

La lista de nombres sigue la nomenclatura usada en 2016/17, sin caracteres acentuados para preservar compatibilidad ASCII. Las imágenes provienen del repositorio de emblemas `JoseArroyave/football-logos`; pueden representar diseños modernos y **no necesariamente el escudo histórico exacto**.

## Archivos acumulativos privados (no almacenados en GitHub)

| Archivo | SHA-256 | Bytes |
|---|---|---:|
| `dt10_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_PORTUGAL_SERIEB_NOMBRES.cpk` | `3af02253e90f0a0aac2ce54e057abb8c4006f109c7410ff1dca4bf4f02fd441a` | 1176820 |
| `dt15_x36_PREMIER_LALIGA_SERIEA_CHAMP_SEGUNDA_PORTUGAL_SERIEB_ESCUDOS.cpk` | `82dacac84a5a1338860648039f6d2d9461be6f851e9eb71984d07b64a30fbfd4` | 246664649 |

**Fuentes de entrada del lote 05:**

- `dt10` SHA256 `68e509e63d164d81c6717bab3608153b68ea1804171c3792aa2a61657a49f238`
- `dt15` SHA256 `65768169d1f7c85c0db5f5310c143fcac870571da90caa6c224636f5787705a1`

## Verificaciones completadas

1. El fichero `Team.bin` conserva su estructura de 501 registros de 1.400 bytes. El ID de equipo en el registro coincide en los 22 casos.
2. Los cambios de texto están limitados a los 22 campos de nombre y cada nombre original aparece una vez.
3. El contenedor CPK del `dt10` preserva exactamente los otros 155 recursos.
4. El contenedor CPK del `dt15` reemplaza **44 PNG** para 22 IDs, con resoluciones correctas (128x128 y 256x256), modo indexado y transparencia.
5. Los restantes **2.740 recursos** del `dt15` son byte a byte iguales al lote anterior.
6. Se verificaron los valores `TocOffset`, `ContentSize`, `EnabledPackedSize`, `EnabledDataSize`, tamaños y contenido de cada entrada.
7. La estrategia de actualización de CPK es *append-only* para nuevos blobs y edición del TOC; conserva los originales sin modificar físicamente y evita cambiar posiciones de recursos ajenos.

**No probado aún:** arranque, carga de equipos, partidas guardadas y FPS del port `com.pes2017.recomp` en Xiaomi Mi 10T.

## Procedimiento de prueba

1. Cerrar completamente PES 2017.
2. Copiar ambos archivos actuales `dt10_x36.cpk` y `dt15_x36.cpk` fuera de `Android/data` para poder restaurarlos.
3. Renombrar ambos CPK nuevos a sus nombres originales y reemplazarlos en `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`.
4. Comprobar Ascoli, Benevento, Bari, SPAL, Hellas Verona y Trapani en la Serie B.
5. Comprobar que la Ligue 2 sigue licenciada (Lens y Strasbourg) y que siguen correctos Porto, Chelsea y Juventus.
6. Cargar un partido y probar guardar/cargar Liga Máster.
7. Si el juego falla, cerrar y restaurar los **dos** CPK del lote 05.

## Referencias

- https://pes.football/news/pravilnye_nazvanija_vsekh_ne_licenzirovannykh_komand_v_pes_2017_spisok/2016-08-31-3348
- https://parchespes2017.blogspot.com/2016/10/team-list-id-pes-2017.html
- https://www.player.it/guide/241611-pes-2017-come-aggiungere-nomi-e-maglie-delle-squadre-senza-licenza.html

Los SVG originales se prepararon mediante GitHub Actions en `.github/workflows/fetch-serieb-crests.yml`, sin subir archivos CPK del juego al repositorio.
