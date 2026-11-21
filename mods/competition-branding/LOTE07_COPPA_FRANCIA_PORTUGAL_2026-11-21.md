# PES 2017 Android — Lote 07: Coppa Italia, Coupe de France y Taça de Portugal

**Fecha:** 21 noviembre 2026 · **Estado:** tres logos auténticos **integrados en CPK acumulativo y verificados estructuralmente**. **Pendiente prueba en Android**.

## Base y salida

- Base **ya probada en menús** por el usuario: `dt15_x36_LOTE06_COPA_REY_SUPERCOPA_AUTENTICAS.cpk` (SHA-256 `c47883f6093dcdc786cf6a83e41d1a2116afb147a76a7d6fea74c2cbb0b78761`).
- Salida privada de esta conversación: `dt15_x36_LOTE07_COPPA_FRANCIA_PORTUGAL.cpk` (SHA-256 `fff16a5633c8df17a52c875f9f6db79b1d4fcfcb7615d39b4597c0bcd18ee140`).
- Ambos CPK: **246746371 bytes**, **2784 recursos**.
- **3 entradas cambiadas / 2781 intactas** según la comparación binaria final.
- `dt10`, plantillas, Liga Máster, marcadores, APK y otros CPK no se modificaron.

## Cambios concretos

| Copa | Entrada de `dt15` | Antes → después | PNG SHA-256 |
| --- | --- | ---: | --- |
| Coppa Italia Frecciarossa (Italia) | `common/render/symbol/emblemLc/emb_0016_l.png` | 13598 → **4256 bytes** | `7564419bd5d58f80f13ba595028b7551db09f8696e099d66ac7922d70a9ae514` |
| Coupe de France Crédit Agricole (Francia) | `common/render/symbol/emblemLc/emb_0018_l.png` | 24645 → **6357 bytes** | `cc3ca4a971b6b51c9144d34183d7785bc7d20cea1bc6caad05bf4f657c341f7d` |
| Taça de Portugal Generali Tranquilidade (Portugal) | `common/render/symbol/emblemLc/emb_0020_l.png` | 10806 → **4626 bytes** | `0120dab2f4b8f964e378d2da43959e267c6313b8cfb1175375d33d88e611ba83` |

Los tres logos fueron obtenidos como PNG originales, optimizados a 256×256 píxeles indexados (256 colores), preservando proporciones. Se añadieron márgenes blancos de presentación, como en lotes anteriores.

## Fuentes y contraste

- Coppa Italia: `https://images.seeklogo.com/logo-png/54/1/coppa-italia-logo-png_seeklogo-547524.png`. Se cotejó la identidad con Lega Serie A (2026/27): `https://www.legaseriea.it/coppa-italia/index`.
- Coupe de France: `https://assets-eu-01.kc-usercontent.com/00700616-e4fb-015d-9378-ef41bc76ccc9/6d5174ac-29d2-47c9-a3ba-d0c7faaad120/Coupe_de_France_logo.png`. Se cotejó la identidad con la FFF 2026/27: `https://lfpl.fff.fr/wp-content/uploads/sites/20/2026/11/CDF-Bonus-Exploit.pdf`.
- Taça de Portugal: `https://cdn-img.zerozero.pt/img/logos/edicoes/188527_imgbank_.png`. Se cotejó el logo con documentos de la FPF y material de temporada 2026/27: `https://publicidade.rtp.pt/wp-content/uploads/2026/11/Proposta-Comercial_4a-e-5a-Eliminatoria-Taca-de-Portugal-2026_2027_atualizada.pdf`.
- Espejos públicos verificados: **las imágenes proceden de medios o portales de terceros, no de descargas directas facilitadas por las federaciones**.
- Los PNG originales no se almacenan en el historial del repositorio público. La conversión se realizó en una ejecución aislada de GitHub Actions y se recuperó como artefacto temporal. Código en la rama técnica `feature/lote07-official-assets-20261121`.

## Proceso de calidad

1. Hash de la base aprobado antes de modificar.
2. Descarga independiente de PNG desde fuentes verificadas y análisis de formato y dimensiones.
3. Conversión a PNG indexado 256×256; todas las imágenes caben en el espacio de las entradas del CPK.
4. Tres modificaciones secuenciales con `patch_competition_logo.py`.
5. **Dos verificaciones:** durante cada paso se compararon todos los recursos no objetivo; después se volvieron a comparar las 2784 entradas contra el lote 06 con un verificador independiente.
6. Conteo final exacto: `emb_0016_l.png`, `emb_0018_l.png`, `emb_0020_l.png` cambiados; los otros **2781 sin cambios**.
7. CPK no se hizo más grande, no hay cabecera/TOC corrupto y todas las imágenes nuevas decodifican.
8. **Pendientes:** comprobar en Android aparición de las tres copas, rendimiento durante un partido, regreso al menú y guardado/carga.

## Por qué la cuarta copa queda fuera

KNVB Beker (**`emb_0019_l.png`**) se **conserva sin cambios**, porque no se pudo verificar con suficiente confianza una versión gráfica vigente y apropiada. No se inventa un emblema para completar una cuota numérica.

## Instalación y recuperación

**Conservar copia de seguridad del `dt15_x36.cpk` actualmente instalado**; cerrar el juego; renombrar el nuevo archivo de lote 07 a `dt15_x36.cpk` y reemplazar solamente ese CPK. Inspeccionar las copas de Italia, Francia y Portugal en los dos menús. Si aparecen errores, restaurar la copia de seguridad del lote 06. Mantener el mismo ajuste gráfico para comparar FPS.

La revisión en menús del lote 06 documentó 60 FPS, **no una prueba de FPS en partido para el lote 07**. No promover el lote 07 a estable hasta la confirmación del usuario.
