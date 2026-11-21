# Fase 2A — Copas nacionales, piloto 01: Emirates FA Cup (2026/27)

**Estado: logo de referencia localizado y preparación reproducible registrada. No existe aún CPK nuevo probado.**

## Estado anterior confirmado

- Entrada acumulativa: `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk`
- SHA-256: `853d9cdb40cf22525877231544d8670cf2b6150ad667de83544cf1f4533bee98`
- Tamaño: **246746371 bytes**; contiene 2784 recursos.
- Prueba visual en Android de Ligue 2 BKT, LaLiga Hypermotion y Liga Portugal: **60 FPS en tres menús**, sin errores visibles.
- Serie BKT aún no tiene captura individual. No hay prueba integral del partido y partidas en el último lote.
- No sobrescribir, revertir ni modificar este archivo estable de referencia.

## Inventario localizado en el `dt15`

- **FA Cup (England Cup):** `common/render/symbol/emblemLc/emb_0015_l.png` (256×256, indexado, PNG), **17612 bytes** en el CPK previo.
- El recurso actual presenta un logo antiguo de `FOOTBALL ENGLAND CUP`. El nombre y el icono son elementos de presentación distintos.
- El diseño oficial 2026/27 de **The Emirates FA Cup** usa un trofeo estilizado con el texto **Emirates FA CUP**, en rojo o blanco según el fondo.
- La identificación del diseño fue cotejada contra el material oficial publicado por The FA en noviembre de 2026: https://www.thefa.com/-/media/thefacom-new/files/competitions/2026-27/emirates-fa-cup/emirates-fa-cup-where-to-watch---first-round-proper.ashx .
- Página oficial de la competición: https://www.thefa.com/competitions/thefacup .

## Obtención de logo (no se suben marcas al Git público)

- Fuente SVG de una copia pública de la identidad: `mierzida/FLP_forBBK`, `public/assets/logos/england/emirates-fa-cup.svg`. Procedencia indicada en el propio proyecto: football-logos.cc. **No es un archivo entregado directamente por The FA; su equivalencia gráfica se revisa visualmente antes de instalar.**
- Flujo de trabajo: `.github/workflows/fetch-domestic-cup-logos.yml`.
- Objetivo: generar un PNG original a **256×256** (modo paleta P + transparencia), conservando la proporción y con variantes de 32/64/128/256 colores para escoger por calidad y tamaño.
- El flujo entrega **artefactos temporales privados de GitHub Actions**, sin publicar el logo en el historial Git. No distribuye código comercial ni datos de juego.
- El resultado aún debe validarse, descargarse y compararse con la imagen oficial antes de integrarlo en el CPK acumulativo.

## Único cambio previsto

1. Reemplazar exclusivamente `emb_0015_l.png` dentro del `dt15` acumulativo actual.
2. Mantener intactos **2.783 recursos** y los otros campos de TOC.
3. Confirmar dimensiones, transparencia, integridad PNG, tamaño máximo del espacio disponible en CPK y SHA-256 antes/después.
4. Mantener `dt10`, plantillas, marcadores y demás recursos sin modificaciones.
5. Guardar respaldo del `dt15` actual, antes de probar el siguiente parche.
6. Probar el logo de FA Cup en el menú, arrancar partido de copa, regresar a menú, Liga Máster y FPS frente a las mismas opciones.

**No declarar “completado” hasta verificar el PNG y preparar el parche, ni “estable” hasta la prueba en Android.**

## Copas siguientes por orden sugerido

| ID interno | Competición identificada en PES 2017 | Próxima comprobación |
| --- | --- | --- |
| 15 | English Cup → Emirates FA Cup | **Piloto actual** |
| 16 | Italian Cup → Coppa Italia | Verificar identidad actual y logo oficial |
| 17 | Spanish Cup → Copa del Rey | Verificar identidad actual y logo oficial |
| 18 | French Cup → Coupe de France | Verificar identidad actual y logo oficial |
| 19 | Dutch Cup → KNVB Beker | Verificar identidad actual y logo oficial |
| 20 | Portuguese Cup → Taça de Portugal | Verificar identidad actual y logo oficial |
| 73–79 | Supercopas nacionales | Lote posterior, con cada ID comprobado |
| 2–4 | UEFA Champions, Europa League, Super Cup | Conservar logotipos si siguen vigentes; cambiar solo con pruebas y fuente contrastada |
| 33–36 | Copas continentales genéricas | **NO sustituir por competiciones reales sin resolver los IDs y su uso** |

## Control de riesgos

- Las capturas de menú prueban que ciertos recursos se muestran; **no prueban que los FPS se mantengan durante todos los partidos**.
- No instalar ninguna versión si el contenido de la imagen no corresponde al logo oficial vigente.
- No publicar archivos CPK del juego, ni copiar marcas de terceros a un repositorio público.
- Si la fuente de logos falla o el ZIP de Actions no está disponible, **no fabricar un PNG aproximado**: mantener la versión actual hasta contar con un SVG/PNG fiable.
