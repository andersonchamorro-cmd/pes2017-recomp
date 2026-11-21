# Prueba visual Android — 21/11/2026

**Estado:** validación visual **parcial aprobada**; pendiente juego completo y guardado.

## Evidencia recibida
El usuario instaló la salida privada `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk` y compartió tres capturas del menú de selección de equipos en Xiaomi Mi 10T. Las capturas son archivos privados del usuario, no se suben al repositorio público.

| Recurso | Resultado visible |
| --- | --- |
| Ligue 2 BKT (emb_0068_l) | Logotipo nuevo visible, sin anomalías perceptibles |
| LaLiga Hypermotion (emb_0067_l / emb_0071_l) | Logotipo nuevo visible, sin anomalías perceptibles |
| Liga Portugal (emb_0014_l) | Logotipo nuevo visible, sin anomalías perceptibles |
| Serie BKT (emb_0069_l / emb_0072_l) | **Pendiente captura o prueba explícita** |
| EFL Championship | Variante previa sin reemplazar, corresponde a emblema real |
| Nombres de menú | **Sin cambios**: aparecen nombres genéricos (p. ej., English League, Spanish 2nd Division, Portugal League) |

## Rendimiento mostrado en las capturas

- Indicador: **60 FPS** durante visualización de menús.
- Tiempo por fotograma: **16,7–16,8 ms**.
- Temperatura del indicador superpuesto: **53–54 °C**.
- Estas son **tres lecturas puntuales**; no representan una medición de FPS durante partidos, ni permiten atribuir el origen exacto de la temperatura.

## Verificaciones pendientes antes de designar el parche «estable»

1. Inspeccionar Serie BKT en el menú y, si procede, las variantes de emblemas.
2. Jugar un partido completo y comprobar imagen/sonido/retorno al menú.
3. Comprobar Liga Máster, guardar y volver a cargar una partida de prueba.
4. Confirmar FPS y temperatura durante el partido frente a la versión anterior con los mismos ajustes.
5. Mantener copia original para restauración si aparece cualquier anomalía.

## Siguientes etapas

- Se inventariaron **68 imágenes de emblemas de competiciones**, incluidas variantes, en `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk`.
- Para cambiar **nombres de competiciones** no basta editar `dt15`: primero hay que localizar el campo de texto en `dt10` o en los paquetes de idioma y demostrar qué recursos leen los menús. Sin ese análisis, no hacer parches especulativos.
- Para actualizar **copas**, priorizar los logos originales proporcionados por el usuario o fuentes legítimas verificables; no inventar iconografía.
- No editar simultáneamente `dt10`, `dt15` y los recursos de marcador: lotes separados y reversibles.
- No publicar archivos completos del juego ni marcas de terceros en GitHub público.
