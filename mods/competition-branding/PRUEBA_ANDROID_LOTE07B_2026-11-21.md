# PES 2017 Android — Lote 07B, verificación visual con transparencia

**Fecha:** 21/11/2026. **Resultado: APROBADO en los menús de Francia, Italia y Portugal.** Prueba de partido completo, guardado/carga y rendimiento sostenido **pendiente**.

## Evidencia recibida del usuario

Tres capturas del Xiaomi Mi 10T después de instalar `dt15_x36_LOTE07B_TRANSPARENTE_FC26.cpk`. En los tres menús los logos nuevos se integran directamente sobre el fondo del juego sin el rectángulo blanco observado en el lote 07.

| Pantalla | Logo | FPS | Fotograma | Temperatura indicada |
| --- | --- | ---: | ---: | ---: |
| Francia | Coupe de France Crédit Agricole | 60 | 16,8 ms | 51 °C |
| Italia | Coppa Italia Frecciarossa | 60 | 16,7 ms | 54 °C |
| Portugal | Taça de Portugal Generali Tranquilidade | 60 | 16,7 ms | 49 °C |

No se observan fallos ni recortes evidentes de los tres logos. Los datos de FPS y temperatura son **lecturas puntuales en menús**, no métricas de partido completo ni diagnóstico de temperatura de batería.

### Observación visual para la siguiente iteración

El texto **"TAÇA DE PORTUGAL"** de la identidad gráfica portuguesa es blanco y de poco contraste sobre el gris claro del menú. El símbolo tricolor es legible; no conviene restaurar fondo blanco. Si se mejora, hacer solo un tratamiento mínimo de contraste/contorno sobre las letras, sin alterar el trazado ni agregar textura, y comprobarlo como parche separado o junto al próximo lote de pocos recursos.

Los textos genéricos ("French Cup", "Italian Cup", "Portugal Cup") permanecen sin cambios: son diferentes de los logos del `dt15`.

## Versión de referencia

- Archivo privado instalado: `dt15_x36_LOTE07B_TRANSPARENTE_FC26.cpk`
- SHA-256: `10778afa0f01507edc62eb5940caf51a2a66eaa10520fae538b67d8b42fe140c`
- Tamaño: 246746371 bytes
- 2784 entradas del CPK; 3 modificadas frente a lote 07 y 2781 preservadas.
- La confirmación visual en el teléfono autoriza tomar esta versión como la **base de menús funcionales** para el siguiente lote. No implica prueba completa de estabilidad.

## Siguiente paso propuesto

Conservar copia del lote 07B. Actualizar un máximo de 2–4 recursos auténticos por lote; priorizar contraste legible del logo portugués, comprobar estado de KNVB Beker y supercopas nacionales, o avanzar a localizar los textos oficiales de competición en su paquete correspondiente. Mantener pruebas de regresión (logos antiguos, FIFA/UEFA si corresponde, menú, partido, partidas) y hashes en GitHub.

No subir capturas privadas del usuario, logos de terceros ni CPK comerciales al repositorio público.
