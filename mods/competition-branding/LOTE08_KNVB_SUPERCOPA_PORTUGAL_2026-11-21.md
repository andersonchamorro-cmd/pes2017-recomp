# PES 2017 Android — Lote 08: KNVB, Supercoppa EA FC y contraste Portugal

**Fecha de creación:** 21 de noviembre de 2026. **Estado:** CPK acumulativo terminado, con validación estructural y comparación binaria **aprobadas**. Pruebas Android en menús, partidos y partidas **pendientes**.

## Objetivo y versión base

Continuar la fase 2A de identidad visual, priorizando logos auténticos transparentes, sin rectángulos blancos y con la resolución preexistente del juego (256×256). El usuario aprobó visualmente los tres logos transparentes del lote 07B en los menús Android a 60 FPS, pero pidió mejorar la legibilidad del nombre de Taça de Portugal.

| Campo | Valor |
| --- | --- |
| Entrada | `dt15_x36_LOTE07B_TRANSPARENTE_FC26.cpk` |
| SHA-256 entrada | `10778afa0f01507edc62eb5940caf51a2a66eaa10520fae538b67d8b42fe140c` |
| Salida nueva | `dt15_x36_LOTE08_KNVB_SUPERCUP_PORTUGAL_FC26.cpk` |
| SHA-256 salida | `54949b7f610ab3b0cf371b68c83cc19d482b01c6e53e2bbabbb1c33940707547` |
| Tamaño de entrada y salida | 246746371 bytes (235,3 MiB) |
| Recursos dentro del contenedor | 2784 |
| Recursos modificados | 3 |
| Recursos preservados sin alterar los bytes | 2781 |

## Tres entradas modificadas

| Competición | Nombre interno `emblemLc` | Bytes anterior → nuevo | SHA-256 de PNG nuevo |
| --- | --- | --- | --- |
| Copa neerlandesa (KNVB Beker, emblema de competición sin marcas de patrocinio) | `emb_0019_l.png` | 14935 → **5272** | `4cf1b810f75ecbbd84d8f24c81a4dcec145cd691712c31805bb50ee1deed5fc0` |
| Supercopa italiana (EA SPORTS FC Supercup) | `emb_0076_l.png` | 10634 → **6871** | `9bf22925a30d27c9e432f4e3fef6734bfd04d850e3830e558edfcf7dfe59d5e9` |
| Taça de Portugal — mejora de contraste tipográfico | `emb_0020_l.png` | 7945 → **8319** | `a09f413b364cbfadba5153bcd975f0000cf3aff2eee38a8ef5cac41639346bb4` |

## Origen y fidelidad de la identidad

- **Copa neerlandesa:** emblema oscuro con copa plateada, versión sin logotipos de patrocinadores, descargado de `https://assets.football-logos.cc/logos/netherlands/1500x1500/knvb-cup.f193b5c6.png` (PNG 1500×1500; SHA-256 `1f0db9598a417f202bf0d65d389d1f9268b259631425c190f139784525c87732`). No hay datos publicitarios ni vínculos de apuestas en el paquete final: solo el escudo deportivo.
- **Supercopa de Italia:** composit logo EA SPORTS FC Supercup, publicado originalmente por Lega Serie A (App oficial) en 2023 y conservado en Wikimedia Commons: `https://upload.wikimedia.org/wikipedia/commons/5/56/Ea-sports-fc-supercup-%282023-2024%29.png` (215×373, SHA-256 `ce8beb259f6853bcf2dfa2ed08ca2b2a7f9d4c6c0bc83a33fa166d8eb2c37054`). Lega Serie A sigue denominando el torneo `EA SPORTS FC Supercup` en 2026/27: `https://www.legaseriea.it/supercoppa/index`. **No se afirma que esta variante gráfica reproducida de 2023 sea idéntica en todos los detalles al manual de marca 2026/27.**
- **Portugal:** se preservó el PNG del lote 07B; únicamente en la línea del texto blanco **TAÇA DE PORTUGAL** se añadió un borde de grafito de 1 píxel y baja opacidad, bajo las letras existentes. No se cambió el trazado del emblema ni se insertó fondo blanco.

Ambas imágenes externas fueron recuperadas en un job aislado de GitHub Actions, utilizando una rama técnica distinta. No se subió ninguno de los logos al historial Git público.

## Preparación de PNG

- Los tres PNG nuevos se guardaron a resolución **256×256** y formato indexado `P`, con alfa y transparencia.
- Para Italia se retiró el fondo blanco del archivo de origen y se conservaron las letras blancas que son parte del rectángulo azul del patrocinador EA FC.
- Para el logo de copa neerlandesa se conservaron proporciones, alfa y la insignia original.
- Se comprobó cómo se ven en menús claros/grises y azules, sin crear cuadros blancos de fondo.
- Ningún PNG excedió el espacio reservado por su entrada en el CPK.

## Validación técnica y pruebas pendientes

Las modificaciones se aplicaron secuencialmente a copias mediante `patch_competition_logo.py`. La validación independiente final comparó todas las entradas de la versión anterior contra la nueva: **solo `emb_0019_l.png`, `emb_0020_l.png` y `emb_0076_l.png` son diferentes; las restantes 2781 son idénticas**. Cabecera, TOC, número de recursos y tamaño total permanecen íntegros.

Pendiente: abrir el menú de Países Bajos, el de Italia (Supercopa) y el de Portugal (Copa), comprobar aparición exacta de cada imagen, jugar partido completo y verificar FPS/temperatura y guardado/carga de prueba. Un CPK estructuralmente válido **no certifica rendimiento sostenido**.

## Instalación y vuelta atrás

1. Guardar una copia local aparte del `dt15_x36.cpk` actualmente instalado y funcionando (lote 07B).
2. Salir del juego y reemplazar exclusivamente ese `dt15` por el archivo nuevo renombrado a `dt15_x36.cpk`.
3. Revisar las tres competiciones y controles de regresión (Premier, FA Cup, Copa del Rey, Ligue 2, etc.).
4. Si ocurre un fallo, cerrar el juego y restaurar la copia del CPK anterior.

**Sin cambios** en `dt10`, ejecutable, guardados, equipos, nombres de competiciones o marcadores. No fusionar a la rama `main` ni designar estable antes de la aprobación del usuario.

**Política GitHub:** solo scripts, hashes y documentación; no publicar archivos completos del juego ni logos externos.
