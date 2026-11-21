# PES 2017 Android — Inventario de nombres de competición visibles y comienzo de fase de textos
Fecha: 21 noviembre 2026

## Evidencia visual confirmada por el usuario

El usuario aportó **siete capturas** de «Select Competition» / «Competition List» con: Inglaterra, Francia, Italia, Países Bajos, España, Portugal y Otros. En ellas hay **23 entradas visibles** en total (4+2+4+2+4+3+4). El selector también muestra Brasil, Argentina, Chile, PEU, PLA, PAS e internacionales, pero **no se expandieron esas categorías**: no afirmar un inventario global completo.

| País/categoría | Cadena textual visible, tal como aparece en el juego | Nombre oficial orientativo a verificar | Estado de nombres |
| --- | --- | --- | --- |
| Inglaterra | English League | Premier League | Pendiente |
| Inglaterra | England Cup | Emirates FA Cup | Pendiente |
| Inglaterra | English 2nd Division | EFL Championship | Pendiente |
| Inglaterra | English Super Cup | FA Community Shield | Pendiente |
| Francia | French Cup | Coupe de France Crédit Agricole | Pendiente |
| Francia | French Super Cup | Trophée des Champions | Pendiente |
| Italia | Italian League | Serie A Enilive | Pendiente |
| Italia | Italian Cup | Coppa Italia Frecciarossa | Pendiente |
| Italia | Italian 2nd Division | Serie BKT | Pendiente |
| Italia | Italian Super Cup | EA SPORTS FC Supercup | Pendiente |
| Países Bajos | Netherlands Cup | KNVB Beker | Pendiente |
| Países Bajos | Dutch Super Cup | Johan Cruijff Schaal | Pendiente |
| España | Spanish League | LALIGA EA SPORTS | Pendiente |
| España | Spanish Cup | Copa del Rey | Pendiente |
| España | Spanish 2nd Division | LALIGA HYPERMOTION | Pendiente |
| España | Spanish Super Cup | Supercopa de España | Pendiente |
| Portugal | Portugal League | Liga Portugal Betclic | Pendiente |
| Portugal | Portugal Cup | Taça de Portugal Generali Tranquilidade | Pendiente |
| Portugal | Portuguese Super Cup | Supertaça Cândido de Oliveira | Pendiente |
| Otros | Club International Cup | **No renombrar automáticamente** | Requiere mapeo |
| Otros | South American Championship | **No renombrar automáticamente** | Requiere mapeo |
| Otros | KONAMI Cup | Conservar nombre/licencia ficticia hasta conocer ID | Requiere mapeo |
| Otros | KONAMI League | Conservar nombre/licencia ficticia hasta conocer ID | Requiere mapeo |

Las denominaciones de destino son **candidatas**, no modificaciones efectuadas ni equivalencias verificadas de forma exhaustiva para temporada 2026/27. Confirmar patrocinios y longitud de cadenas (recortes de UI) antes de modificar.

## Observaciones y estado técnico

- Se observó en las capturas rendimiento de menú 59–60 FPS, tiempos de 16,6–17,0 ms por fotograma. Estas lecturas puntuales no certifican rendimiento de partidos ni estabilidad total.
- La vista de Inglaterra sigue mostrando «English League» a pesar de tener el emblema actualizado Premier League. Lo mismo sucede para las demás competiciones; **logo PNG no modifica el texto**.
- Último CPK de emblemas técnicamente preparado: `dt15_x36_LOTE10_PORTUGAL_SUPERCUP_FC26.cpk`, SHA-256 `1cf59eaa551ba4c8c78178ea38d96fd0841100bf7b3114b457c37d1f0651a8f8`. Verificaciones binarias de 3 entradas cambiadas y 2781 intactas. Las capturas apoyan su funcionamiento **en menús** y sugieren buen estado visual, no prueba de todos los recursos.
- **El paquete binario actual de texto `dt10_x36.cpk` no está montado en el entorno de trabajo**. Se ha buscado en archivos visibles y Library sin recuperar ese binario. No es correcto prometer un CPK modificado de nombres hasta recibir y mapear la ubicación real de cadenas, que podrían estar en recursos de idioma u otro CPK.

## Plan de edición de nombres sin introducir errores

1. Solicitar al usuario su `dt10_x36.cpk` **actual**, sin reinstalar ni copiar otro parche.
2. Examinar índice/TOC, hashes y recursos de localización; comprobar si contiene las cadenas visibles. Si no, localizar el archivo de idioma realmente usado antes de pedir otro CPK.
3. Crear **piloto de 3 nombres de liga** con valores oficiales verificados, respetando la longitud/codificación/formato de las cadenas. Guardar copia del paquete inicial.
4. Validar nuevo archivo binariamente, confirmando que los recursos ajenos permanezcan idénticos. Probar tres menús en Android. Abortar o revertir si hay recortes, caracteres extraños o problemas de carga.
5. Solo después ampliar el conjunto a las demás entradas mapeadas, con tandas de máximo 3 y un archivo final acumulativo.
6. Los cuatro torneos de «Otros» no se relabelan como torneos reales sin tener clara la semántica/IDs y cómo afectan juego/Liga Máster.
7. Evitar mezclar cambios de nombres con más modificaciones de logos o marcadores en el mismo lote.

El usuario aportó capturas en chat; no se cargan imágenes personales al repositorio. Únicamente inventario derivado, documentación, hashes y código.
