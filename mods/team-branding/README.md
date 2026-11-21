# PES 2017 Android (Xbox 360) — nombres y escudos: piloto seguro

**Estado: preparación; NO hay todavía un parche de escudos ni de nombres instalado.**

Objetivo: conservar la base jugable de 2016/17 y corregir únicamente **nombres e insignias** de clubes no licenciados. En una etapa posterior, si funciona y se guarda bien, actualizar equipos y plantillas (por ejemplo 2026/27). Este trabajo va en una rama separada que incluye la corrección del mando Xbox jugador 1.

## Bases verificadas

- El port recompila el ejecutable de Xbox 360 edición europea, no la edición PC. Los mods de PC no son intercambiables directamente.
- Los datos originales se importan al teléfono desde archivos `.cpk`; el ejecutable `default.xex` debe conservarse.
- La comunidad de PES 2017 de Xbox 360 identifica los nombres de clubes en la base de datos (`dt10`) y los símbolos/logotipos en recursos (`dt15`); las **rutas y nombres reales de la instalación Android deben confirmarse antes de extraer o reemplazar cualquier archivo**.
- Según una prueba comunitaria publicada en noviembre de 2026, los assets de un parche de PC pueden adaptarse a este port, a veces mediante conversión binaria de endianess y texturas. No existe aún una herramienta reproducible demostrada para esta adaptación.

Fuentes:
- https://github.com/dzakyraf/pes2017-recomp
- https://foro.pesoccerworld.com/viewtopic.php?p=2086004
- https://www.reddit.com/r/AndroidNativePorts/comments/1xrd6z7/got_pte_patch_60_pc_working_with_dzakyrafs_pes/
- https://pes.football/news/pravilnye_nazvanija_vsekh_ne_licenzirovannykh_komand_v_pes_2017_spisok/2016-08-31-3348

## Primera prueba de bajo riesgo (sin parches binarios)

1. Mantener respaldada, en Download u otra carpeta externa, la carpeta original `files` del juego. No editar el respaldo.
2. En el juego, `Extras > Edit`, intentar cambiar solamente el nombre de **LONDON FC → Chelsea FC**, **MAN RED → Manchester United** y **MAN BLUE → Manchester City**. Si la opción no aparece o queda bloqueada, registrar ese resultado y NO forzar cambios.
3. Salir del editor, cerrar y reabrir PES, verificar que se mantengan los tres nombres; probar también Liga Máster si procede.
4. Volver al estado anterior si hay fallos. Esta prueba confirma el método de edición/guardado de nombres, **no** la compatibilidad de escudos ni de CPK.

## Segunda prueba: escudos originales

Se requiere inspeccionar el inventario real de archivos de `Android/data/com.pes2017.recomp/files/game` (sin subir 6.7 GB a un repositorio público). Extraer y estudiar **solo una muestra** del contenedor de emblemas del propio juego mediante herramientas compatibles y sobre COPIAS LOCALES.

- Usar para el primer piloto Chelsea, Manchester United y Manchester City (IDs de club en `team-mapping-2016-17.csv`).
- Confirmar formato de archivo, dimensiones, canal alfa, asignación a ID, compresión y bytes de orden de Xbox 360.
- Probar que los nuevos símbolos aparecen tanto en selección de equipos como en juego y Liga Máster, sin cierres ni error de guardado.
- Automatizar un respaldo y reversión antes de modificar o reconstruir archivos originales `.cpk`.
- No publicar en el repositorio público archivos del juego ni logotipos de terceros sin el permiso correspondiente.

## Criterios para ampliar al resto

- El juego abre y se puede jugar al menos un partido.
- Los tres nombres persisten después del reinicio.
- Tres escudos corresponden al ID correcto de cada club.
- Guardado y carga en Liga Máster funcionan.
- Rendimiento y temperatura se mantienen razonablemente similares a la versión sin parche.

## Precaución sobre compatibilidad

Los parches tradicionales de Xbox 360 pueden requerir `DpFileList.bin`, packs `.cpk` y un formato de guardado de consola que el port **no ha documentado como compatible**. No copiar esos archivos directamente al directorio del juego ni reemplazar `.cpk` sin determinar primero su ruta y formato en el teléfono.
