# Piloto de nombres: Premier + España e Italia

Estado: **CPK de prueba construido sobre el dt10 original del usuario**, pendiente de prueba en el dispositivo. Los recursos comerciales no se suben a GitHub.

- Premier League 2016/17: conservar 18 correcciones anteriores.
- España: 17 nombres ficticios con equivalencias verificadas contra el alias `Team.bin` (tanto primera como segunda división en la base).
- Italia: 10 nombres ficticios con equivalencias verificadas, incluyendo equipos de Serie B.
- No se han cambiado nombres de ligas, logos de ligas, escudos adicionales ni divisiones.
- El nuevo CPK conserva la estructura original (1 138 688 bytes y 156 recursos) y 155 recursos binarios intactos.
- Se utiliza `mods/team-branding/crear_parche_laliga_serie_a_piloto.py` solamente con `dt10_x36.cpk` original del propietario.
- Para probar: cerrar juego, respaldar dt10 vigente, renombrar el CPK privado descargado a `dt10_x36.cpk`, sustituir solo dt10 en directorio activo. No cambiar dt15 de Premier. Si el juego falla, restaurar dt10 anterior.
- Próximo: inventariar cada liga en captura y verificar IDs y nombres actuales antes de convertir los escudos de España e Italia; estudiar recursos de logotipos y nombres de competiciones por separado.
