# Premier League 2016/17 — paquete de 20 escudos (piloto)

**Estado:** nuevo archivo dt15 creado y validado en estructura; **todavía no probado dentro del juego**.

- Fuente: dt15 aportado por el usuario; se utilizó como base la versión privada con tres escudos ya comprobados en Android.
- ID de los 15 equipos faltantes: 105, 177, 179, 204, 205, 207, 378, 382, 395, 396, 398, 399, 1589, 1909, 4071.
- Dos variantes PNG por equipo: 128x128 y 256x256.
- Nombres identificados contra la lista [PES 2017 team IDs](https://pes-files.ru/pro_evolution_soccer_2017_id_komand).
- Logos obtenidos para uso local desde [JoseArroyave/football-logos](https://github.com/JoseArroyave/football-logos), `logos/england/`.
- No se han subido los logos ni los archivos binarios del juego al repositorio; el flujo de GitHub Actions generó un artefacto temporal para descargarlos, sin incorporarlos al historial Git.
- Nuevo CPK privado de prueba: 244932985 bytes, SHA-256 `1a054c92d4e8364767e925a8773caf959b1210735fc50b0086108282243a5dd3`.
- Comparación de recursos: 30 modificados, 2754 idénticos respecto al dt15 con Chelsea, Manchester United y Manchester City ya funcionales. Se mantienen intactos esos seis recursos anteriores.
- **Solo modificación de escudos**; no cambia nombres, equipos, plantillas, kits, gameplay ni ejecutable.

## Instalación segura

1. Cerrar el juego completamente.
2. Conservar copia de seguridad del `dt15_x36.cpk` activo fuera de `Android/data`.
3. Renombrar el nuevo `dt15_x36_PREMIER_LEAGUE_20_ESCUDOS.cpk` a `dt15_x36.cpk`.
4. Sustituir únicamente el `dt15_x36.cpk` en el directorio activo que contiene `default.xex`.
5. Dejar sin cambios el `dt10_x36.cpk` de nombres reales que ya funciona.
6. Comprobar menú, un partido y Liga Máster antes de considerar la prueba aprobada.
7. Si ocurre un cierre o fallo, salir del juego y restaurar el `dt15_x36.cpk` respaldado.

**Advertencia:** los escudos son marcas de sus respectivos clubes. El contenedor se preparó solamente para probar la copia del juego del usuario.
