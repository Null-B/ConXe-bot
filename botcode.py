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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('$yes'):
        await message.channel.send("is mall")




client.run(TOKEN)