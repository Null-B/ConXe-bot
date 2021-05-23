import discord
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = '!'
INTENTS = discord.Intents.default()
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
#comands
#
@client.event
async def on_message(message):
    #help
    if message.author == client.user:
        return
    
    if message.content.startswith("$help"):
        await message.channel.send("don forget to use   \"$\"    to use these comads\n\nhelp     -    for all comads \n \nhello      /    hi     /   sup \n\npenis    -   for      🍆\n\nharam-     🐖 ")
    #hi comands
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!😀')

    if message.content.startswith('$hi'):
        await message.channel.send('eyyyy😀')

    if message.content.startswith('$sup'):
        await message.channel.send('sup my dued😀')
    
    #new

    elif message.content.startswith('$penis'):
        await message.channel.send("🍆")

    elif message.content.startswith('$haram'):
        await message.channel.send("🐖")




client.run(TOKEN)