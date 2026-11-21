# PES 2017 Android — Lote 09B: supercopas sin fondos rectangulares

**Fecha:** 21-11-2026  
**Estado:** CPK acumulativo construido y **verificado estructuralmente**. Prueba Android de menús/partido/guardados **pendiente**.

## Motivo de corrección

El usuario instaló `Lote 09` y aportó capturas de seis países: Francia, Países Bajos y Portugal mostraban **fondos negros/blancos** detrás de los emblemas de Supercopa. El PNG del 09, aun con tamaño y cabecera correctos, tenía **alfa opaco en las esquinas**, por lo que no cumplía el requisito de emblemas sin fondo y estética cercana a FC26.

Se partió del **Lote 08 probado por el usuario en Android**, no del Lote 09 defectuoso. Las fuentes gráficas de los tres emblemas se aislaron de los fondos opacos del raster de referencia, conservando geometría y colores; el de Portugal conserva el trofeo y un rótulo simple para lectura en menú. Se transformaron a PNG en modo paleta con canal alfa realmente transparente. La nueva vista previa es del archivo PNG extraído/decodificado, y se comprobó la transparencia en las cuatro esquinas.

## Identificación binaria

| Campo | Valor |
| --- | --- |
| Entrada | `dt15_x36_LOTE08_KNVB_SUPERCUP_PORTUGAL_FC26.cpk` |
| SHA-256 de entrada | `54949b7f610ab3b0cf371b68c83cc19d482b01c6e53e2bbabbb1c33940707547` |
| Salida privada entregada | `dt15_x36_LOTE09B_SUPERCOPAS_SIN_FONDOS_FC26.cpk` |
| SHA-256 de salida | `f7625ce5d4c436c868932bc39a21fa64cb1d32ad1ae8ffa653c2f3e2fad42cc6` |
| Tamaño idéntico al de la entrada | **246746371 bytes** |
| Total de entradas | **2784** |
| Entradas modificadas | **3** |
| Entradas preservadas byte a byte | **2781** |

### Recursos (solo `dt15_x36.cpk`)

| Copa | Recurso | Antes → después | SHA-256 PNG final |
| --- | --- | ---: | --- |
| Trophée des Champions (Francia) | `common/render/symbol/emblemLc/emb_0075_l.png` | 4548 → 6049 bytes | `67c73ed106d84983336181300fe035bbb7c5b7a04208803bdfeb6d73fe91b5d9` |
| Johan Cruijff Schaal (Países Bajos) | `common/render/symbol/emblemLc/emb_0077_l.png` | 4971 → 5920 bytes | `17d1549810abb256c31188fff024a8483257e109e1bcfd2059cafc36fb214112` |
| Supertaça Cândido de Oliveira (Portugal) | `common/render/symbol/emblemLc/emb_0078_l.png` | 7728 → 5818 bytes | `515afc4af14da47a8a409075e936ba0e8d725358b34cea2ee155fe05b8891742` |

Los tres están a 256×256 píxeles, PNG indexado con transparencia real, y **alpha=0 en cada una de las cuatro esquinas** tras recargar el archivo desde disco.

## Protocolo de control de calidad

1. El SHA-256 del CPK base coincidió con la versión anteriormente verificada.
2. Se procesaron los rasters auténticos ya recuperados para retirar exclusivamente el fondo opaco, cuidando colores y trazos.
3. Se comprobaron las tres imágenes sobre fondo gris claro, selección azul y fondo oscuro, y se rechazaron las primeras versiones con transparencia falsa.
4. Cada PNG cumplió el límite de tamaño de su entrada: 6144/6144/8192 bytes respectivamente.
5. Se introdujeron los cambios **uno por uno** con el parcheador del proyecto, sin sobrescribir entrada.
6. Se inspeccionó el encabezado, tabla TOC, 2784 recursos y cada entrada; **solo 3 archivos cambiaron**, los 2781 restantes permanecieron idénticos byte a byte, con tamaño total idéntico.
7. **Pendiente:** validar menús de Francia, Países Bajos y Portugal en el Xiaomi, y en otro momento FPS dentro de un partido completo y guardado/carga de una partida de prueba.

### Nota de contraste

En los menús muy oscuros, las letras negras/grises de Francia y Portugal tienen contraste limitado; se preservó la identidad original sin pintar cuadros ni añadir efectos de alto coste. Esta limitación debe examinarse visualmente en Android si se muestra ese menú, pero no implica error del contenedor.

## Instalación segura

1. Guardar respaldo local del `dt15_x36.cpk` actual (el lote 09 puede contener cuadros; conservar también el lote 08 estable).
2. Cerrar el juego completamente.
3. Cambiar nombre del nuevo archivo a `dt15_x36.cpk`; reemplazar solamente ese archivo.
4. Abrir Francia, Países Bajos y Portugal, inspeccionar rectángulos de fondo, tamaño y FPS mostrados.
5. Si aparece un fallo, salir y restaurar el lote 08; no se tocan otros CPK, partidas, motor ni marcadores.

No subir CPK completos ni logos de terceros al repositorio público; guardar únicamente manifiestos, hashes y procedimientos.
