# Fase 2A — Copas nacionales, piloto 01: Emirates FA Cup (2026/27)

**Estado: CPK acumulativo generado y verificado estructuralmente; prueba en Android pendiente.**

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
- El SVG se recuperó y cotejó visualmente con el logotipo auténtico 2026/27. Se convirtió en PNG indexado con transparencia y se integró en una copia del último CPK acumulativo. El resultado superó pruebas binarias completas.

## Único cambio realizado

1. Reemplazar exclusivamente `emb_0015_l.png` dentro del `dt15` acumulativo actual.
2. Mantener intactos **2.783 recursos** y los otros campos de TOC.
3. Confirmar dimensiones, transparencia, integridad PNG, tamaño máximo del espacio disponible en CPK y SHA-256 antes/después.
4. Mantener `dt10`, plantillas, marcadores y demás recursos sin modificaciones.
5. Guardar respaldo del `dt15` actual, antes de probar el siguiente parche.
6. Probar el logo de FA Cup en el menú, arrancar partido de copa, regresar a menú, Liga Máster y FPS frente a las mismas opciones.

**El nuevo CPK está técnicamente preparado, pero NO es versión estable hasta que el usuario pruebe en Android.**

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


## Resultado concreto del parche — 21/11/2026

| Campo | Valor |
| --- | --- |
| CPK privado preparado | `dt15_x36_LOTE05_FA_CUP_AUTENTICA.cpk` |
| Archivo de partida | `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk` |
| SHA-256 de partida | `853d9cdb40cf22525877231544d8670cf2b6150ad667de83544cf1f4533bee98` |
| SHA-256 de salida | `03cbeb18fc847873a711c733f1ec8fbfa03d60d5688803f07e1310f12004f3c2` |
| Bytes del contenedor | `246746371`, igual que la base |
| Recurso modificado | `common/render/symbol/emblemLc/emb_0015_l.png` |
| PNG original → nuevo | 17612 → **8242 bytes** |
| Formato de nuevo logo | 256×256, PNG indexado (P), 128 colores, con transparencia |
| PNG SHA-256 | `2fd4e3889f9127492a6dbe4a003b2b65283fa1e98767a76b226e19190fc81732` |
| SHA-256 de SVG de origen | `c03088a51865b089d0965f71e61d2e7f2f2b6b534c6e9e974e0c771039db5283` |
| Procedencia del SVG | `mierzida/FLP_forBBK`, commit `cd7043224e00c85fe1d2a0437003de2b96425b39` |
| Validación de recursos ajenos | **2783 de 2783 idénticos** |
| Comprobación de TOC, encabezado y PNG nuevo | **APROBADA** |
| Comprobación visual en Android y FPS | **PENDIENTE** |

El CPK se entregó directamente en la conversación, pero **no se subió a GitHub** (se conserva la norma de no alojar datos propietarios del juego). El manifiesto JSON de la prueba está en `mods/competition-branding/lote02_fa_cup_manifest.json`.

### Instalación segura

1. Salir completamente del juego.
2. Respaldar el `dt15_x36.cpk` **actualmente instalado y funcionando** fuera de la carpeta del juego.
3. Renombrar el lote 05 a `dt15_x36.cpk` y sustituir únicamente ese archivo.
4. Verificar la FA Cup en el menú; después comprobar las competiciones del lote previo para detectar regresiones.
5. Jugar un partido, comprobar FPS, regreso al menú y, si se usa, carga/guardado de Liga Máster en una partida de prueba.
6. Si aparece cualquier anomalía, cerrar y restaurar el `dt15` respaldado.

**En ningún momento se han tocado** `dt10`, plantillas, marcadores, ejecutable ni los otros 2783 recursos dentro de `dt15`.
