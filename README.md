## Especificaciones

Van a tener que armar un bot de Discord que se pueda comunicar con una API que ustedes prefieran. Los requisitos son:
- Al entrar al Servidor, el bot debe poder mandar un mensaje por privado al usuario saludando y describiendo su funcion.
- El bot debe tener a lo menos tres comandos (que usen el decorador `@bot.command()`) que permitan al usuario hacer uso de la API.

Armen un `README.md` con lo siguiente:

```markdown
# Discord Bot + API

Alumno: Apellido y nombre
Curso: Curso
Materia: Redes y Protocolos

```

## Consideraciones

- Tienen la documentacion de `discord.py` en este [link](https://discordpy.readthedocs.io/en/stable/api.html).
- Si no encuentran una API que les interese, pueden usar esta de [COVID-19](https://documenter.getpostman.com/view/10808728/SzS8rjbc).

## Como entregar

Pongan el `bot.py` y `README.md` en una carpeta y corran:

```
git init
git add README.md bot.py
git commit -m "Initial commit"
git checkout -b ryp/2021/discord+api
git push https://github.com/trq20/USERNAME.git ryp/2021/discord+api
```
