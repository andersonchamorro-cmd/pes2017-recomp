# Estado verificable de los parches acumulativos — 21 nov 2026

Este documento identifica los archivos locales que el usuario ya probó o debe probar. **No contiene archivos comerciales del juego**.

| Archivo | SHA-256 | Estado |
|---|---|---|
| dt10_x36_PREMIER_Y_LALIGA_NOMBRES_2016_17.cpk | a17345dc25c91e4f338d0bd6cf2b49cbdf47f3579ed8a67470a687c6181dadd1 | nombres Premier y LaLiga visibles en capturas del usuario |
| dt15_x36_PREMIER_LEAGUE_20_ESCUDOS.cpk | 1a054c92d4e8364767e925a8773caf959b1210735fc50b0086108282243a5dd3 | escudos Premier visibles en capturas |
| dt15_x36_PREMIER_Y_LALIGA_40_ESCUDOS.cpk | 5b3064f5ac194d4d1949349554c253ba75a9c9a83a8442e1bb16845b43545efc | reconstrucción comprobada en estructura; falta prueba real en teléfono de los escudos españoles |

## Reglas para ampliar las ligas

1. Trabajar sobre el **último archivo validado**, nunca volver al original para generar un parche acumulativo.
2. Registrar para cada equipo el **ID real de PES 2017**, nombre ficticio, nombre real, liga, estado y fuente comprobada. No fiarse de un nombre si puede repetirse en otro club.
3. Si el club será sustituido durante 2026/27 (PEU, PLA, PAS), **reservar ID y escudo sin cambiarlos todavía**.
4. Para cada cambio de `dt10`: modificar únicamente los nombres previstos dentro de `Team.bin`; verificar que los demás recursos y datos de jugadores permanecen idénticos.
5. Para cada cambio de `dt15`: comprobar PNG original y nuevo, ID, resolución, transparencia y que los recursos no objetivo mantienen sus bytes.
6. No confundir el **nombre/escudo de un club** con la **etiqueta/logo de una competición**: habrá que localizar el recurso correspondiente en el juego antes de modificarlo.
7. Mantener un respaldo por versión, un hash SHA-256 y una lista explícita de cambios. No distribuir el juego completo en el repositorio.
8. Las pruebas en Android requieren validar: menú, selección, partido, Liga Máster, guardar/cargar y rendimiento/temperatura; ninguna verificación binaria sustituye esas pruebas.

## Pendiente en la próxima tanda

- Confirmación visual del parche de escudos de LaLiga que ya se generó.
- Inventario fiable de equipos y nombres de las demás ligas existentes.
- Verificar la compatibilidad del modo Liga Máster antes de reestructurar divisiones.
- Separar la actualización 2026/27 de nombres y escudos: ascensos, plantillas, fichajes y calendarios serán otra fase.
