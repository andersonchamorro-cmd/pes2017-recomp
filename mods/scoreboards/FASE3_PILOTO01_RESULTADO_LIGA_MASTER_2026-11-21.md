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
