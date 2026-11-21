# PES 2017 Android — Lote 10, Portugal/Italia (21-11-2026)

**Estado: CPK acumulativo generado y verificado binariamente; Android todavía no probado.**

Base: `dt15_x36_LOTE09B_SUPERCOPAS_SIN_FONDOS_FC26.cpk`, SHA-256 `f7625ce5d4c436c868932bc39a21fa64cb1d32ad1ae8ffa653c2f3e2fad42cc6`.

Salida privada entregada al usuario: `dt15_x36_LOTE10_PORTUGAL_SUPERCUP_FC26.cpk`, SHA-256 `1cf59eaa551ba4c8c78178ea38d96fd0841100bf7b3114b457c37d1f0651a8f8`.

Ambos CPK: **246746371 bytes**. Total: **2784** entradas. Modificadas exactamente **3**; **2781** verificadas byte a byte e idénticas.

## Mejoras individuales

| Competición | Recurso `emblemLc` | Antes → después | PNG SHA-256 |
| --- | --- | ---: | --- |
| Liga Portugal | `emb_0014_l.png` | 3696 → 3667 bytes | `65acc0368e77be39d87c06fac78db300d920ba2e2602f4c6c5af22a1201f0dd5` |
| Taça de Portugal | `emb_0020_l.png` | 8319 → 8038 bytes | `cd3f00d070d87f93d73073da072f8cecb39e86ffe3e3cc560c878738bc2b5f33` |
| EA SPORTS FC Supercup (Italia) | `emb_0076_l.png` | 6871 → 8458 bytes | `f14e8588887c05062f4bdba8861a6beb2615ea30838bb7e8ce206c06e7f417ae` |

- **Liga Portugal:** se preservó **cada uno de los píxeles y colores existentes** del logo original, añadiendo una línea de separación marfil de 1 píxel solo en el borde exterior semitransparente. Se reutilizó una ranura sin utilizar de la paleta original para caber en el espacio del CPK de 4096 bytes. Mejora contraste del logo azul marino sobre menú azul.
- **Taça de Portugal:** únicamente se oscurecieron píxeles de la línea de patrocinio verde, que perdía legibilidad sobre fondo gris; no se alteró el diseño del trofeo ni el texto rojo.
- **Supercopa italiana:** se incrementó uniformemente su escala alrededor de 7,5 %, conservando proporciones, textura 256×256 y su logo real anterior.

## Verificaciones técnicas realizadas

1. SHA-256 de la base coincidió exactamente con el lote 09B aprobado visualmente por el usuario.
2. Cada nueva imagen es PNG de paleta indexada, 256×256, con alfa transparente real (0 en las cuatro esquinas).
3. Los tres PNG quedaron por debajo de la capacidad disponible de las entradas del CPK.
4. Las modificaciones fueron secuenciales sobre copias del CPK; entrada original intacta.
5. Validación independiente: las 2784 entradas se compararon, incluyendo tablas y datos. **Solo cambiaron los 3 recursos esperados; los otros 2781 son byte a byte idénticos.**
6. Cabeceras, tabla TOC, tamaños y total de bytes preservados. No se tocó `dt10`, nombres, equipos, marcadores, guardados o ejecutable.
7. La vista previa fue probada sobre gris claro y azul de menú antes de empacar. **No se afirma que los FPS se mantengan sin prueba Android**.

## Instalación, rollback y prueba del usuario

1. Mantener **copia externa del último `dt15_x36.cpk` funcional** (lote 09B).
2. Salir de PES; descargar lote 10, renombrar a `dt15_x36.cpk` y reemplazar exclusivamente ese archivo.
3. Inspeccionar logos de `Portugal League`, `Portugal Cup` y `Italian Super Cup` en menús.
4. Validar logos anteriores, partida completa, retorno a menú y prueba de guardado/carga de Liga Máster si aplica.
5. Si aparece error, cerrar PES y restaurar la copia anterior. No clasificar como estable hasta que el usuario lo apruebe.

## Fase siguiente: nombres oficiales

El usuario pidió comenzar los nombres reales justo después del lote 10. **El PNG y la cadena de texto son recursos distintos**. Primero localizar el contenido del `dt10_x36.cpk` instalado o archivos de idioma, sin modificar a ciegas. Empezar con un piloto de 3 nombres (`English League`, `Italian League`, `Portugal League`) después de respaldar archivos y mapear las referencias exactas.

Los archivos CPK y las marcas privadas NO se suben al repositorio público de GitHub. Solo hashes/documentación/herramientas.
