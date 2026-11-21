# LaLiga 2016/17 — primer parche de nombres

Se verificaron los 20 equipos de la primera división española con las capturas del usuario y la lista histórica de nombres de PES 2017. **Barcelona** y **Atlético de Madrid** ya tienen nombre real; los demás usan nombres ficticios.

El CPK de prueba para uso privado se generó usando como base el `dt10_x36.cpk` ya modificado con los nombres de la Premier League. Preserva esos cambios y modifica únicamente las 18 cadenas correspondientes a LaLiga en `common/etc/pesdb/Team.bin`.

Archivo privado de prueba: `dt10_x36_PREMIER_Y_LALIGA_NOMBRES_2016_17.cpk`.
SHA-256: `a17345dc25c91e4f338d0bd6cf2b49cbdf47f3579ed8a67470a687c6181dadd1`.
Tamaño: 1,138,688 bytes. El CPK pasó inspección estructural de 156 recursos, con solamente `Team.bin` modificado.

| Nombre PES 2017 | Nombre real de 2016/17 |
|---|---|
| PV SKY BLUE WHITE | DEPORTIVO ALAVES |
| PV WHITE RED | ATHLETIC CLUB |
| GA CYAN | CELTA DE VIGO |
| GA BLUE WHITE | DEPORTIVO LA CORUNA |
| PV BLUE RED | SD EIBAR |
| CT BLUE WHITE | RCD ESPANYOL |
| AN RED WHITE | GRANADA CF |
| CN YELLOW BLUE | UD LAS PALMAS |
| MD BLUE WHITE | CD LEGANES |
| AN CYAN WHITE | MALAGA CF |
| NC RED | CA OSASUNA |
| AN GREEN WHITE | REAL BETIS |
| MD WHITE | REAL MADRID |
| PV BLUE WHITE | REAL SOCIEDAD |
| AN WHITE RED | SEVILLA FC |
| AS RED WHITE | SPORTING GIJON |
| ED WHITE ORANGE | VALENCIA CF |
| ED YELLOW | VILLARREAL CF |

Referencias de correspondencia (revisar si el juego tiene parches previos): https://www.vrutal.com/videojuegos/3087979/los-epicos-nombres-de-los-equipos-de-la-liga-en-pes-2017 y https://www.pesgaming.com/forums/threads/names-pes-2017-real-club-names.100553/

**Pendiente**: 18 escudos reales, emblema y nombre de la competición (localizar sus recursos y probar), partido, Liga Máster y guardado. No se ha modificado la asignación de divisiones ni las plantillas 2026/27. No subir los archivos comerciales de juego al repositorio público.
