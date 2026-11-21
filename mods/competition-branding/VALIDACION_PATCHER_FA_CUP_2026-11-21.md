# Prueba de integridad del parcheador CPK — 21 noviembre 2026

El script `mods/competition-branding/tools/patch_competition_logo.py` permite reemplazar exactamente un logo de competición `emblemLc` en una **copia** del `dt15`, sin sobrescribir el archivo de entrada.

## Prueba de identidad realizada

- **Entrada:** `dt15_x36_LOTE04_LOGOS_AUTENTICOS.cpk` (último lote instalado por el usuario).
- **Logo de prueba:** copia binaria extraída de su propio `emb_0015_l.png` (FA Cup); no es un logo nuevo.
- **Operación:** reconstrucción del archivo reemplazando la entrada por exactamente los mismos bytes.
- **Resultado:** `cmp` binario **idéntico** a la entrada; **PASS**.
- **SHA-256 tanto de entrada como de salida:** `853d9cdb40cf22525877231544d8670cf2b6150ad667de83544cf1f4533bee98`.
- **Tamaño total en ambos:** 246746371 bytes.
- **Recursos totales:** 2784.
- **Recursos ajenos a la entrada objetivo preservados:** 2783/2783.
- **Validaciones completadas:** encabezado CPK, TOC, PNG objetivo, todos los recursos restantes y tamaño total.
- **Advertencia:** prueba técnica con imagen idéntica; no demuestra que un logo nuevo funcione ni que no cambie el rendimiento en Android.

Los archivos temporales de la prueba fueron eliminados. No se publicaron CPK ni logos.

## Próxima tarea

Utilizar el original de Emirates FA Cup preparado por el flujo `.github/workflows/fetch-domestic-cup-logos.yml`, verificar visualmente que coincide con la identidad 2026/27, elegir una variante 256×256 indexada que quepa en el espacio disponible de `emb_0015_l.png` y crear el siguiente CPK como nueva copia. No designarlo estable sin prueba del usuario en el teléfono.
