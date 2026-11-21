# Prueba visual Android — Emirates FA Cup — 21/11/2026

**Resultado: APROBADA en menús; validación de partido y guardados PENDIENTE.**

El usuario instaló el parche acumulativo privado `dt15_x36_LOTE05_FA_CUP_AUTENTICA.cpk` y compartió dos capturas de PES 2017 en Xiaomi Mi 10T.

## Observaciones directas de las capturas

| Elemento | Comprobación |
| --- | --- |
| Emirates FA Cup | Nuevo logo rojo con trofeo y texto Emirates FA CUP aparece en «Select Competition» con England Cup seleccionado |
| Segundo menú | Nuevo logo también aparece en «Competition List» dentro de ENGLAND |
| Premier League | Logo previo sigue visible |
| EFL Championship | Escudo previo sigue visible |
| FPS mostrados | **60** en ambas capturas |
| Tiempo de fotograma mostrado | **16,6 ms** en ambas |
| Temperatura mostrada en superposición | **52 °C y 48 °C**, respectivamente |
| Otros errores gráficos visibles | No observados en las capturas |
| Texto del menú | Sigue siendo «England Cup», y otras etiquetas genéricas siguen; no se han cambiado datos de texto |

## Correspondencia técnica

- Parche privado de entrada: `dt15_x36_LOTE05_FA_CUP_AUTENTICA.cpk`.
- SHA-256: `03cbeb18fc847873a711c733f1ec8fbfa03d60d5688803f07e1310f12004f3c2`.
- Única entrada reemplazada: `common/render/symbol/emblemLc/emb_0015_l.png`.
- Validación binaria previa: CPK de 2.784 recursos, **2.783 preservados exactamente**; tamaño total sin cambios.

## Pendiente para considerar estable

1. Jugar un partido completo de una competición y comparar FPS con misma configuración que versión previa.
2. Confirmar regreso al menú y ausencia de cierres o texturas erróneas.
3. Verificar guardado/carga de una partida de prueba de Liga Máster, sin arriesgar partida principal.
4. Conservar copia de seguridad del `dt15` funcional.

**No se reportan pruebas en partido ni de guardado/carga; no inferirlas a partir de imágenes de menús.**

## Siguiente fase

Revisar Coppa Italia (`emb_0016_l.png`) y Copa del Rey (`emb_0017_l.png`) con logos originales auténticos y validar uno por lote. Actualización de nombres de competiciones es un proyecto distinto que requiere identificar recursos de texto. Mantener CPK acumulativo del lote 05 como la **última base confirmada visualmente en menús**, sin declararlo todavía plenamente estable.

No se incorporan imágenes del usuario, logos de terceros o binarios del juego al repositorio Git público.
