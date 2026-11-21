# Lote 07 — Fuentes verificadas y construcción automática (21/11/2026)

**Estado: NO HAY UN NUEVO CPK LISTO PARA INSTALAR.** Se verificaron visualmente los logos actuales y se elaboró un generador local autónomo, probado con PNG de ensayo. **No se declara completado el parche de logos reales** porque el entorno actual no pudo descargar los bytes PNG de los enlaces externos.

## Base de referencia inalterada

- Lote 06: `dt15_x36_LOTE06_COPA_REY_SUPERCOPA_AUTENTICAS.cpk`
- SHA-256: `c47883f6093dcdc786cf6a83e41d1a2116afb147a76a7d6fea74c2cbb0b78761`
- Tamaño: 246746371 bytes; 2784 recursos.
- El usuario comprobó visualmente Copa del Rey y Supercopa de España en dos menús Android a 60 FPS. En una lectura se mostraron 59 °C; sin prueba integral durante partido.

## Verificación de identidades (2026/27)

1. **Coppa Italia Frecciarossa**: confirmada contra Lega Serie A `https://www.legaseriea.it/coppa-italia/index`; PNG de espejo con el mismo diseño en `https://images.seeklogo.com/logo-png/54/1/coppa-italia-logo-png_seeklogo-547524.png`. Entrada de juego: `emb_0016_l.png`, capacidad 14336 bytes.
2. **Coupe de France Crédit Agricole**: confirmada contra documento FFF 2026/27 `https://lfpl.fff.fr/wp-content/uploads/sites/20/2026/11/CDF-Bonus-Exploit.pdf`; PNG de espejo cotejado: `https://images.seeklogo.com/logo-png/67/1/coupe-de-france-de-football-logo-png_seeklogo-675478.png`. Entrada: `emb_0018_l.png`, capacidad 26624 bytes.
3. **KNVB Beker**: un PNG identificado representa una identidad *histórica*, no queda confirmado como logotipo vigente 2026/27. No modificar el recurso `emb_0019_l.png` todavía.
4. **Taça de Portugal**: se identificó la versión 2026/27 de la FPF/Generali Tranquilidade, pero un PNG localizado no contiene toda la identidad gráfica legible y no se ha obtenido un original íntegro. No modificar `emb_0020_l.png` todavía.

## Preparación funcional local

Se creó un ZIP entregado al usuario **en la conversación**: `PES2017_LOTE07_GENERADOR_AUTOMATICO.zip` (7.5 kB; SHA-256 `7dac4eb874b63393b9a0353f5b9def94a8f62deb31e2b308bcbde13f63d5ac02`), que contiene:
- `crear_lote07.py` — descarga dos PNG desde las URLs indicadas, valida contenido y dimensiones, los optimiza a 256×256 PNG de paleta, verifica capacidad de ranuras y crea una copia acumulativa solo con Coppa Italia y Coupe de France.
- `patch_competition_logo.py` — lector/patcheador CPK con comparaciones binarias.
- `LEEME.txt` — pasos breves con copia de seguridad obligatoria.

**Prueba local (con imágenes de ensayo, NO las descargadas):** el generador realizó dos sustituciones con nuevos PNG de ensayo y verificó exactamente 2782 de 2784 recursos intactos; produjo CPK nuevo sin tocar su base. Los archivos temporales de la prueba fueron destruidos. Esto es QA del código, **NO prueba de logos originales descargados ni estabilidad en Android**.

## Paso para completar

La descarga remota de imágenes no está habilitada en el contenedor actual (error de descarga/conectividad). La herramienta puede ejecutar la descarga al correr en PC con Internet y Python+Pillow usando la copia privada del lote 06, sin que el usuario busque logos. Exigir verificación visual local y en Android tras generar. Si falta un PNG, la herramienta detiene el proceso sin sobreescribir ningún CPK.

Ni logos ni CPK del juego se publican en GitHub. No alterar la versión estable instalada. No inventar resultados o hashes de un lote que todavía no se ha construido con los originales.
