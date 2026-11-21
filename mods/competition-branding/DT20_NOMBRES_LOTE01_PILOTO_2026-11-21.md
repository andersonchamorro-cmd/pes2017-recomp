# PES 2017 Android — piloto de nombres de ligas 01 (inglés)

**Fecha:** 21 noviembre 2026. **Estado:** CPK generado y **verificado binariamente**. **Prueba visual y FPS en Xiaomi Mi 10T: pendiente.**

## Base y salida (archivos privados, no incluidos en GitHub)

| Campo | Valor |
|---|---|
| Archivo original aportado por usuario | `dt20_eng_x36.cpk` |
| SHA-256 original | `2f33c53cc6adcfd5e34298d4a9213be0ec41e7625b6994883203a22239c6142e` |
| CPK piloto entregado | `dt20_eng_x36_NOMBRES_LOTE01_PILOTO.cpk` |
| SHA-256 piloto | `a0b3f2532124733ee660105b99e276e7a4d3a3a5956ccd38a294bd037df7403a` |
| Tamaño total entrada/salida | **368184 bytes** |
| Entradas TOC | **5** |
| Recursos modificados | **1**: `eng/string/all.str` |
| Recursos intactos | **4**, comparados byte por byte |
| Tamaño del recurso modificado antes/después | 282648 → 280369 bytes |
| Tamaño descomprimido de `all.str` | **844784 bytes**, sin cambios |
| Capacidad de ranura | 284672 bytes |

## Las tres sustituciones de texto

| Original visible | Destino piloto | Ocurrencias cambiadas | Posiciones en `all.str` descomprimido |
|---|---|---:|---|
| `English League` | `Premier League` | 5 | 517241, 664565, 669534, 670131, 747977 |
| `Italian League` | `Serie A` | 5 | 517276, 664622, 669563, 670160, 748016 |
| `Portugal League` | `Liga Portugal` | 2 | 517868, 748042 |

Las cadenas fueron encontradas realmente en `eng/string/all.str` descomprimido desde el `dt20_eng_x36.cpk` del usuario. No se editaron etiquetas arbitrarias ni se alteraron IDs de `dt10`.

## Método técnico de bajo riesgo

1. Se inspeccionó el contenedor CRI CPK, su encabezado y tabla `TOC`; se localizaron 5 recursos, incluidos `all.str` y `staff_list.str`.
2. `all.str` utiliza envoltorio `WESYS` (cabecera big endian) y payload `zlib/deflate`. Se descomprimió, validando tamaño de 844784 bytes.
3. Se localizaron 12 ocurrencias en 3 etiquetas. Las tres sustituciones se hicieron conservando la **longitud exacta de cada campo de texto** y el **offset original de todos los terminadores NUL**. Las dos etiquetas más cortas se rellenaron con espacios finales; la copia fuente no fue modificada.
4. Se recomprimió con deflate optimizado tipo **Zopfli** para conservar el tamaño requerido. Nuevo recurso 280369 bytes, menor que los 282648 originales y el espacio máximo 284672.
5. Se actualizó exclusivamente el tamaño del registro `all.str` en la TOC cifrada, sustituyendo el recurso dentro de su ranura original y dejando las demás en su lugar.
6. Verificación independiente: se extrajo de nuevo `all.str` desde el CPK final y confirmó recuentos exactos de `Premier League` ×5, `Serie A` ×5, `Liga Portugal` ×2; los tres textos anteriores desaparecieron. Cabecera original y otros 4 recursos se compararon byte por byte, coincidiendo exactamente.
7. **No hay prueba funcional en Android aún**. La sustitución de cadenas comprimidas no demuestra por sí sola que el juego las muestra en todos los menús; comprobarlo en el dispositivo.

## Instalación/rollback

1. Conservar respaldo privado de `dt20_eng_x36.cpk` anterior.
2. Cerrar completamente el juego.
3. Renombrar `dt20_eng_x36_NOMBRES_LOTE01_PILOTO.cpk` a **`dt20_eng_x36.cpk`**.
4. Reemplazar **solo** `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/dt20_eng_x36.cpk`.
5. Abrir los menús: Inglaterra (Premier League), Italia (Serie A), Portugal (Liga Portugal). Verificar texto sin recortes, FPS, navegación y una partida.
6. Si hay error, cerrar y restaurar `dt20_eng_x36.cpk` original. No modificar `dt10`, `dt15` ni `saves`.

## Plan posterior

Tras confirmar visualmente piloto, continuar cambiando nombres de copas/divisiones ya reales en lotes pequeños. **NO renombrar** PEU, PLA, PAS como Bundesliga, Colombia o Liga MX hasta sustituir clubes e IDs y validar estructura. Los reemplazos acordados son `PEU → Bundesliga`, `PLA → Liga BetPlay`, `PAS → Liga MX`.

**GitHub público guarda solo informe, nombres de recursos, código y hashes. NO contiene archivos CPK, textos originales completos ni recursos propietarios.**
