# Fase 2A — Lote 07, cuatro copas nacionales

Fecha: **21/11/2026**

**Estado: preparación de fuentes y herramienta completa; NO hay nuevo CPK todavía.** No se deben proclamar logos integrados sin contar con sus imágenes auténticas verificadas.

## Base aprobada visualmente (capturas de usuario)

`dt15_x36_LOTE06_COPA_REY_SUPERCOPA_AUTENTICAS.cpk` · **246746371 bytes** · SHA-256 `c47883f6093dcdc786cf6a83e41d1a2116afb147a76a7d6fea74c2cbb0b78761`.

Dos capturas de selección de competiciones muestran Copa del Rey, Supercopa de España, LaLiga y LaLiga Hypermotion correctas a 60 FPS (16,8 y 16,6 ms; temperatura mostrada 48 y 59 °C). La estabilidad en partidos y guardado/carga sigue pendiente; usar este CPK como base, no como prueba de FPS sostenidos.

## Cuatro sustituciones previstas (máximo 4 por lote)

| País | Competición real | Recurso exacto `dt15` | Logo PNG original de entrada |
| --- | --- | --- | --- |
| Italia | Coppa Italia Frecciarossa | `emb_0016_l.png` | `coppa_italia.png` |
| Francia | Coupe de France Crédit Agricole | `emb_0018_l.png` | `coupe_de_france.png` |
| Países Bajos | KNVB Beker (identidad de la competición, preferiblemente sin logo de patrocinador) | `emb_0019_l.png` | `knvb_beker.png` |
| Portugal | Taça de Portugal Generali Tranquilidade | `emb_0020_l.png` | `taca_de_portugal.png` |

**Fuentes y corroboración visual que deben usarse antes de descargar el material:**

- **Italia:** material de la competición en sitio oficial de Lega Serie A, https://www.legaseriea.it/coppa-italia/index ; símbolo tricolor sobre `COPPA ITALIA` y `FRECCIAROSSA`. Una fuente de imagen referencial es `https://images.seeklogo.com/logo-png/54/1/coppa-italia-logo-png_seeklogo-547524.png`; es un espejo, no una descarga oficial de Lega.
- **Francia:** la FFF indica que la identidad de la Coupe de France Crédit Agricole sustituye la anterior desde 2025/26: https://lbfc.fff.fr/simple/nouvelle-charte-coupe-de-france-credit-agricole/ . Imagen referencial `https://images.seeklogo.com/logo-png/67/1/coupe-de-france-de-football-logo-png_seeklogo-675478.png`, que deberá cotejarse con FFF.
- **Países Bajos:** KNVB Beker, emblema de la competición sin redirigir al usuario a servicios de apuestas. Fuente referencial de logotipo https://football-logos.cc/netherlands/knvb-cup/ ; no se empleará el logo histórico si no coincide con la identidad deseada y actual.
- **Portugal:** la Federação Portuguesa de Futebol confirma el diseño actual de la Taça de Portugal Generali Tranquilidade en material oficial 2026/27 (https://publicidade.rtp.pt/wp-content/uploads/2026/11/Proposta-Comercial_4a-e-5a-Eliminatoria-Taca-de-Portugal-2026_2027_atualizada.pdf), con símbolo geométrico verde y rojo. Imagen referencial `https://cdn-img.zerozero.pt/img/logos/edicoes/188527_imgbank_.png` (2025/26; comprobar correspondencia exacta 2026/27 antes de instalar).

**Estado de los binarios de fuentes:** Se identificaron referencias gráficas y sitios oficiales, pero no se obtuvieron cuatro PNG originales en el contenedor de trabajo. Por esta razón **no se generó ni se instaló ningún `dt15` nuevo**. La seguridad tiene prioridad a fabricar logos aproximados o alterar los originales sin comprobar su identidad.

## Herramienta para construir lote acumulativo

- `mods/competition-branding/tools/build_cups_batch.py`: acepta máximo cuatro PNG indexados 256×256, verifica SHA-256 del lote 06, aplica un cambio por paso, valida todos los recursos no objetivo y jamás sobreescribe la entrada.
- Depende de `patch_competition_logo.py` en la misma carpeta.
- Se verificó una **prueba de identidad de cuatro pasos** con los cuatro PNG antiguos, extraídos del CPK de partida; SHA-256 de salida fue exactamente `c47883f6093dcdc786cf6a83e41d1a2116afb147a76a7d6fea74c2cbb0b78761`, igual que la entrada. No existen aún logos nuevos instalables: el test comprueba el proceso, no el contenido gráfico actualizado.
- Los parámetros de la herramienta solo admiten los cuatro recursos aprobados; se rechazan versiones con longitud o hash de base diferentes.
- Ninguna imagen original o archivo del juego se sube al repositorio público.

## Próxima ejecución

Conseguir cuatro fuentes originales verificadas, convertirlas individualmente a 256×256, paleta indexada y transparencia con calidad aceptable, y comprobar su tamaño dentro de cada ranura de CPK. Si una no cumple, se omite esa copa y se registra el motivo en vez de forzar la instalación. Generar un único CPK nuevo sobre lote 06, registrar hashes y probar en Android. Conservar respaldo y monitorizar FPS y temperaturas, especialmente el valor 59 °C mostrado en una captura.

No actualizar `dt10`, nombres ni marcadores en este lote.
