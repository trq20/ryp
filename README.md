## Especificaciones

Usar el módulo `discord.py` para programar un bot de Discord que por lo menos:

- Sea capaz de contestar a algún comando específico (como `!help` o `!kick`).
- Salude a cada persona que se conecte al servidor con un mensaje personalizado y taggeando al usuario.

Agreguen cualquier otra funcionalidad que quieran o crean conveniente.

## Como instalar el módulo

Pueden hacerlo desde la terminal, corriendo:

```
pip install discord.py
```

## Como crear el bot

- Vayan primero al [Developer Portal](https://discord.com/developers/applications) de Discord, donde van a tener que loguearse.
- En `Applications`, creen una nueva aplicación y luego en `General Information` van a ver un `APPLICATION ID`, luego van a usarlo para invitar al bot al servidor que creen.
- En `Bot`, creen uno nuevo y tomen nota del `TOKEN`. **NUNCA** lo publiquen o cualquier otra persona podría usar su bot. 
- En la misma sección, van a ver una lista de permisos. Clickeen los que quieran darle al bot dentro del servidor y tomen nota del `PERMISSIONS INTEGER`.

Ahora pueden invitar al bot a su servidor. Pueden usar este link:

```
https://discord.com/oauth2/authorize?client_id=APPLICATION_ID&permissions=PERMISSIONS_INTEGER&scope=bot
```

Reemplacen `APPLICATION_ID` y `PERMISSIONS_INTEGER` con los propios de su bot.

## Consideraciones

- Para dudas sobre lo que quieren que su bot haga, recuerden revisar la documentación oficial de [discord.py](https://discordpy.readthedocs.io/en/stable/api.html).
- Algunas clases que les pueden ser útiles revisar en la documentación son: `Client`, `Message`, `Reaction`, `Member` y `TextChannel`.
- Recuerden que para que el bot se conecte, tienen que correr el programa como `python bot.py`.
