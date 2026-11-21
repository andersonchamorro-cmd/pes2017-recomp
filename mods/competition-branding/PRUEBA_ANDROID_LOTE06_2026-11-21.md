# Prueba visual Android — Lote 06, 21/11/2026

**Estado: logos de Copa del Rey y Supercopa de España VERIFICADOS EN MENÚS; partido y guardado pendientes.**

El usuario instaló `dt15_x36_LOTE06_COPA_REY_SUPERCOPA_AUTENTICAS.cpk` en Xiaomi Mi 10T y envió dos capturas: selector de categoría por país en ESPAÑA y selector de competición con los cuatro torneos de España.

## Observaciones respaldadas por capturas

| Comprobación | Resultado |
| --- | --- |
| Copa del Rey — `emb_0017_l.png` | Logo auténtico visible en ambos menús; legible, no recortado |
| Supercopa de España — `emb_0074_l.png` | Logo auténtico visible en ambos menús; legible, no recortado |
| LaLiga y LaLiga Hypermotion | Emblemas anteriores continúan visibles |
| Textos de nombres | Siguen genéricos, «Spanish Cup», «Spanish Super Cup», «Spanish League», «Spanish 2nd Division»; no se tocaron recursos de texto |
| FPS primera / segunda captura | **60 / 60** |
| Tiempo por fotograma primera / segunda captura | **16,8 / 16,6 ms** |
| Temperatura de superposición primera / segunda captura | **48 / 59 °C**. No es posible inferir componente o temperatura de la batería con estas imágenes |
| Errores gráficos visibles | Ninguno en las dos capturas; se ven cuatro entradas correctas |

## Contenido técnico del lote

- Entrada acumulativa: `dt15_x36_LOTE05_FA_CUP_AUTENTICA.cpk`, SHA-256 `03cbeb18fc847873a711c733f1ec8fbfa03d60d5688803f07e1310f12004f3c2`
- Salida probada por usuario: `dt15_x36_LOTE06_COPA_REY_SUPERCOPA_AUTENTICAS.cpk`, SHA-256 `c47883f6093dcdc786cf6a83e41d1a2116afb147a76a7d6fea74c2cbb0b78761`
- **2 cambios en 2784 entradas; 2782 idénticas al lote anterior** según validación estructural.
- No se tocó `dt10`, plantillas, marcadores, guardados ni ejecutable.

## Pruebas pendientes y estabilidad

Esta es una **aprobación visual y de navegación del menú**, no una declaración de 60 FPS sostenidos en partidos ni una prueba de partidas guardadas. Sigue pendiente:

1. Partido completo, regreso al menú y comparación de rendimiento con la versión anterior.
2. Guardado/carga de Liga Máster usando una partida de prueba.
3. Observar la lectura de temperatura durante el partido, especialmente si persiste una cifra cercana a 59 °C.
4. Mantener un respaldo local de la última versión funcional antes de instalar siguiente lote.

**Siguiente versión:** partir exclusivamente de este lote 06 y limitarse a 2–4 emblemas verificados para las copas de Italia/Francia/Países Bajos/Portugal. No subir archivos de juego ni imágenes de marcas al repositorio público.
