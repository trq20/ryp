import discord

client = discord.Client()

@client.event                           # Decorador
async def on_ready():                   # Se dispara cuando el bot se conecta
    print('We have logged in as {0.user}'.format(client))

@client.event                           # Decorador
async def on_message(message):          # Se dispara cada vez que llega un mensaje
    if message.author == client.user:   # Evitar contestar los mensajes del propio bot
        return

    if message.content.startswith('$hello'):  # Revisa si el mensaje es un comando valido
        await message.channel.send('Hello!')  # Del mensaje, obtiene el chanal de texto y envia un mensaje

client.run('your token here')
