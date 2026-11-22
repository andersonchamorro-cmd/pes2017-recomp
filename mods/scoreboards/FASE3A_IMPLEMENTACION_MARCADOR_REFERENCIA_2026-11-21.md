# PES 2017 Android — Fase 3A: desarrollo del marcador exacto de referencia

**Fecha:** 21/11/2026 (continuación técnica). **Estado:** implementación de geometría y estado **C++17 comprobada en PC**. Todavía **NO** hay un APK ni CPK instalable que reproduzca esta disposición en el móvil.

## Diseño solicitado y verificado en captura del usuario

La referencia visual aportada muestra **panel izquierdo color del equipo (celeste en MNC), panel central púrpura con 0 [escudo león Premier League] 0, panel derecho rojo para MNU y pequeña placa púrpura inferior con el reloj 0:57**. El objetivo NO es incrustar una imagen fija: los textos, goles y tiempo deben provenir del partido REAL, actualizándose durante Liga Máster. No modificar menús ni pantallas ajenas. La presentación inicial es opcional y secundaria debido a caídas previas a 25–29 FPS.

El usuario confirmó disponibilidad de PC para herramientas y aportó su `dt11_x36.cpk` original previamente.

## Trabajo concreto efectuado en este turno

Se creó y compiló un módulo de geometría **sin dependencias de juego ni bibliotecas de terceros**:
- `scoreboard_layout.h`: estructuras `GameState`, `Style`, `Layout`, interfaz gráfica `Sink` y `Render`. Acepta abreviaturas, resultado, segundos de partido, colores por equipo y bandera de partido activo; dibuja **cuatro placas 2D**, cinco etiquetas y un logo existente.
- `test_scoreboard_layout.cpp`: pruebas de posiciones de rectángulos, recuentos de elementos, abreviaturas, reloj `0:57` y `90:00`, texto de goles y bloqueo fuera de partido.
- Verificación: compilación `g++ -std=c++17 -O2 -Wall -Wextra -Werror` y ejecución de pruebas con resultado **PASS**.
- Paquete de código privado de sesión para el usuario: `PES2017_PREMIER_HUD_MODULO_NATIVO_FASE3A.zip`, SHA-256 **`3da4427f4c59f554e3348cf79ad31f6432b6b76aa8d8b2ba87d00db691b82bbe`**. Este paquete **no es instalable en el juego** y no debe usarse para reemplazar CPK.

## Por qué se requiere integración nativa

- Los **pilotos 01 y 02** de textura CPK cambiaron el RGB de atlas PES, **sin cambiar la franja azul permanente** `ARS 0–0 MAN`. El éxito binario no demuestra un diseño visible. No generar otro CPK coloreando atlas a ciegas.
- El diseño solicitado **mueve el reloj debajo** de los goles, introduce un escudo central y cambia posiciones y composiciones: modificar únicamente píxeles de texturas comprimidas **no mueve los controles del HUD**.
- El port Xbox 360 Android procede de una recompilación C++ del ejecutable, con un renderizador Vulkan y código abierto en este repositorio. Puede ser necesario un pequeño gancho del renderer/HUD o modificar layout AFP. La vía de integración se debe comprobar antes de intentar compilar APK.
- El **Sider.exe de PES2017 PC es una herramienta para la edición Windows**, no un plugin listo para cargar en `com.pes2017.recomp` de Android. No instalar software de PC a ciegas ni prometer compatibilidad.

## Dependencia concreta siguiente

**Archivo privado solicitado al usuario:** `default.xex` actual, carpeta `Android/data/com.pes2017.recomp/files/PES 2017 BY MUSTAFA GAMERS/`, ~**30,98 MB** según su captura. Necesario para confirmar la versión ejecutable y mapear las estructuras/funcciones reales de partido y HUD (marcador, tiempo y competición). El APK de recompilación se solicitaría **después** únicamente si la vía nativa lo exige; no pedir varios archivos de antemano.

No subir `default.xex` ni otras partes propietarias del juego a GitHub. No alterar partidas ni `dt10`, `dt15` (logos lote10), `dt20` (nombres unificados), ni `dt11` en este momento.

## Criterios de aceptación del futuro mod instalable

1. Todos los elementos se ven con el layout solicitado, no solo un cambio de color.
2. El reloj actualiza durante la Liga Máster sin depender del reloj del teléfono.
3. Los goles y abreviaturas varían correctamente con el juego.
4. El HUD azul original no queda debajo o superpuesto.
5. Sin nuevo vídeo, animaciones costosas, OCR en tiempo real ni texturas de gran tamaño.
6. Prueba A/B a FPS comparables en un partido, más retorno al menú y guardado/carga de Liga Máster antes de declarar la implementación lista.

**No afirmar CPK, APK, FPS o reproducción del diseño terminados hasta comprobarlos en Android.**
