# PES 2017 Android — Resultado visual del piloto 01 del marcador en Liga Máster

**Fecha de prueba:** 21/11/2026 (hora local Colombia).  
**Contexto esencial confirmado por el usuario:** **todas sus pruebas se realizan desde una partida de Liga Máster existente**, NO desde amistosos ni un modo de partido rápido.

## Capturas recibidas del piloto 01

| Pantalla Liga Máster (Arsenal vs Manchester United) | Imagen | FPS | Frametime | Temperatura |
|---|---|---:|---:|---:|
| Alineaciones previas | `146712.jpg` | 44 | 22,8 ms | 54 °C |
| Presentación del estadio | `146713.jpg` | 27 | 36,5 ms | 55 °C |
| Saque inicial/banda inferior | `146714.jpg` | 52 | 19,2 ms | 56 °C |
| Partido activo, marcador ARS 0-0 MAN minuto 0:50 | `146715.jpg` | **59** | **17,1 ms** | **57 °C** |

Los cuatro estados cargaron y renderizaron la interfaz sin errores gruesos evidentes. **El CPK piloto no impidió entrar a un partido desde Liga Máster.** Esto constituye una prueba visual positiva de arranque/navegación/partido, **no** una prueba de guardado/carga o estabilidad prolongada.

### Comparación con capturas del dt11 previo

Antes: alineaciones 29 FPS, presentación 24, saque inicial 51, partido activo (min. 1:01) 53 FPS. Después: 44, 27, 52, 59 respectivamente. **No interpretar como mejora causal:** distintos instantes, escenas, temperatura y condiciones; se necesitan pruebas comparables de 5–10 min y perfiles FPS si se decide medir.

**Diferencia gráfica:** el CPK piloto buscaba teñir `hudTexPes-scoreBase` (región DXT5 en TXP2) de azul oscuro a violeta. En la captura del minuto 0:50, el marcador se ve mayormente azul oscuro y **no se aprecia con claridad el violeta**; no afirmar éxito visual de la recoloración aún. Aparece una etiqueta `PES2017` bajo el marcador durante el minuto 0:50; no aparece en la captura anterior del 1:01. Puede formar parte de una animación transitoria de presentación del HUD, no atribuirla al parche sin una prueba del mismo intervalo y archivo original.

## Conclusión y próximos pasos prudentes

- **Compatible visualmente con el inicio de partido de Liga Máster hasta 0:50** en el teléfono del usuario, **no aprobado todavía en cuanto a color**.
- Solicitar o revisar una captura del HUD con reloj 2:00–5:00, para asegurar que la etiqueta `PES2017` desaparece normalmente y observar el color real tras la transición inicial. No necesita reinstalar nada para esta prueba.
- **No producir nuevo dt11** hasta confirmar el recurso realmente dibujado por el HUD durante el partido y la distinción de `game2dPes` frente a la animación previa. Si el endpoint modificado permanece oculto, ensayar una región realmente visible con cambios igualmente mínimos.
- El entorno obligatorio para todos los pilotes futuros es **Liga Máster existente**, con criterios prioritarios de estabilidad de guardados, temporada, competiciones y volver al menú. Evitar iniciar temporada nueva, alterar IDs, plantillas o calendario sin pruebas de compatibilidad.
- `dt10` (database), `dt15` (lote 10 logos), `dt20` (nombres unificados), `saves` y `save_backups` permanecen sin modificación en esta fase.
- Ligas ficticias que se reemplazarán en fase 4: PEU→Bundesliga, PLA→Liga BetPlay, PAS→Liga MX. Requerir especial precaución con la partida de Liga Máster ya iniciada.

## Aclaración confirmada directamente por el usuario

El usuario confirmó expresamente que la etiqueta **PES2017** que aparecía temporalmente debajo del marcador a los 0:50 del partido **sí es la animación inicial normal**, no un fallo del piloto. Se cierra esta incidencia: **no solicitar nueva captura para investigar ese logo**. Queda pendiente únicamente comprobar si el cambio de color violeta del elemento `scoreBase` es visible y diseñar un HUD completo con una selección por competición técnicamente validada; la captura actual sigue mostrando el azul predominante.


## Segunda validación del usuario — siete capturas, hasta 2:57 de Liga Máster

Se recibieron siete capturas adicionales del **mismo entorno de pruebas, Liga Máster Arsenal–Manchester United**, con el piloto `dt11_x36_MARCADOR_PILOTO01_MORADO_FC26.cpk` instalado. El usuario pidió revisar el resultado.

| Vista | FPS | ms | °C indicados |
| --- | ---: | ---: | ---: |
| Menú principal de Liga Máster | 60 | 16,7 | 54 |
| Alineaciones previas | 48 | 21,0 | 54 |
| Presentación del estadio | 25 | 40,3 | 53 |
| Saque inicial | 48 | 20,7 | 55 |
| Juego activo 0:42 | 55 | 18,2 | 57 |
| Juego activo 1:53 | 54 | 18,4 | 56 |
| Juego activo 2:57 | 50 | 19,8 | 57 |

**Observación inequívoca:** a los 0:42 se muestra el rótulo efímero `PES2017` bajo el marcador, pero **desaparece de forma normal** en las capturas de 1:53 y 2:57. El usuario previamente confirmó que se trata de una animación inicial, **no** un fallo.

**Evaluación visual:** el indicador superior izquierdo `ARS 0-0 MAN` y el reloj son funcionales, sin defectos evidentes, pero **la franja visible continúa siendo predominantemente azul**. No hay evidencia suficiente de que el cambio a violeta en los endpoints de `hudTexPes-scoreBase` haya alterado el área visual dominante. El piloto se considera **funcional en los primeros 2:57 del partido, pero NO aprobado como mejora gráfica FC26**.

**Rendimiento:** las capturas muestran entre 50 y 55 FPS en juego activo, con escenas previas 25–48 FPS. No atribuir la variación al piloto (condiciones/escenas no controladas). No afirmar que el piloto restaura 60 FPS sostenidos.

### Acción siguiente sin riesgos innecesarios

1. **No crear otro CPK cambiando colores al azar**. Verificar qué regiones del atlas TXP2 contienen la **placa azul realmente visible** y cómo las compone `game2dPes.bin`. El área `hudTexPes-scoreBase` original modificada podría corresponder a una capa secundaria o invisible en la pantalla capturada.
2. Preparar **comparaciones visuales de regiones** con las capturas reales y, solo después, un cambio localizado en la región realmente usada. Conservar dimensiones, tipo DXT5, estructura TXP2 y compresión validada.
3. Recordar: el HUD PES genérico puede afectar **varias ligas**. La asignación de marcador independiente a Premier League, LaLiga, Serie A, Bundesliga, Liga BetPlay y Liga MX **NO** está probada ni implementada. No prometer que este piloto da marcadores diferenciados.
4. **El usuario no necesita volver a tomar una captura del logo de animación** ni enviar `dt11` otra vez. Antes de cualquier nueva modificación, preservar el `dt11` original y dejar intactos `dt15`, `dt20`, y sobre todo `saves`/`save_backups`.
