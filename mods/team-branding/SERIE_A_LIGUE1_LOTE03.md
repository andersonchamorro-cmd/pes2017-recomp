# Paquete 03: Serie A + Ligue 1 — nombres y escudos

**Estado:** CPKs acumulativos creados y verificados estructuralmente; aún NO probados en el Xiaomi. Se conservan los cambios previos de Premier League y LaLiga.

## Resultado de las capturas del usuario

- **Ligue 1:** los 20 nombres y los 20 emblemas ya son reales en esta edición de PES 2017. Se mantienen tal como están.
- **Serie A:** los dos únicos clubes de la primera división con nombres/escudos ficticios son:
  - `PM BLACK WHITE` → `JUVENTUS FC` (PES 2017 ID 120)
  - `SANSAGIULO` → `US SASSUOLO CALCIO` (ID 1919)
- Las 18 entradas restantes de la Serie A ya aparecen identificadas correctamente en las capturas.
- Se usa el logo con la «J» de Juventus para ir acercando la presentación al estilo FC 26; el origen de los logos está en un repositorio externo, no se han subido gráficos al historial Git.

Fuentes: https://parchespes2017.blogspot.com/2016/10/team-list-id-pes-2017.html y https://www.psu.com/news/pes-2017-all-real-team-names-for-editing/

## Artefactos privados producidos en la conversación

| CPK | SHA-256 | Tamaño |
|---|---|---|
| `dt10_x36_PREMIER_LALIGA_SERIEA_NOMBRES.cpk` | `c5dd268ac0a3846106204b50668b2fdfe4bd86f87751631ed5592ad782cfd7bb` | 1 138 688 bytes |
| `dt15_x36_PREMIER_LALIGA_SERIEA_ESCUDOS.cpk` | `d5e59d9a75e62cb32f1d393e57ec00df5ad05ebfc7feca0ed78e45518e50d45a` | 245 248 742 bytes |

Bases verificadas para construir el nuevo paquete:

- `dt10_x36_PREMIER_Y_LALIGA_NOMBRES_2016_17.cpk`: `a17345dc25c91e4f338d0bd6cf2b49cbdf47f3579ed8a67470a687c6181dadd1`
- `dt15_x36_PREMIER_Y_LALIGA_40_ESCUDOS.cpk`: `5b3064f5ac194d4d1949349554c253ba75a9c9a83a8442e1bb16845b43545efc`

## Comprobaciones realizadas

- `Team.bin` conserva su tamaño descomprimido; dos campos de nombre modificados, el resto del contenido idéntico tras aplicar esas dos sustituciones.
- Los otros 155 recursos del `dt10` siguen intactos y el contenedor se abre correctamente.
- `dt15`: se sustituyen solamente cuatro PNG: `emblem_0120_f.png`, `emblem_0120_f_l.png`, `emblem_1919_f.png`, `emblem_1919_f_l.png`.
- PNG de 128 y 256 px con transparencia y paleta; formato e índice verificables.
- Los **otros 2.780 recursos** del `dt15` coinciden exactamente, byte a byte, con el anterior paquete Premier+LaLiga.
- Se mantiene el motor gráfico y no se tocan jugadores, estadísticas, divisiones, ligas o partidas.

## Instalación / retroceso

1. Salir completamente del juego.
2. Asegurar respaldo fuera de Android/data de los `dt10_x36.cpk` y `dt15_x36.cpk` que funcionan.
3. Renombrar **los dos CPK nuevos** con los nombres originales `dt10_x36.cpk` y `dt15_x36.cpk`.
4. Copiarlos a `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/` reemplazando únicamente esos dos archivos.
5. Probar Juventus y Sassuolo, luego Real Madrid, Tottenham y Chelsea, y guardar/cargar Liga Máster.
6. Si el juego falla, cerrar y restaurar ambos archivos desde la copia de seguridad.

## Pendiente

Nombres y logos de la competición (por ejemplo «Italian League» → «Serie A») **NO están incluidos**: pertenecen a recursos de interfaz diferentes, aún sin mapear/validar.

Los nombres, escudos y plantillas de 2026/27, ascensos y descensos quedan para una fase posterior.
