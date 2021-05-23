import discord
import os
from dotenv import load_dotenv
TOKEN = os.getenv("TOKEN")
PREFIX = '!'
INTENTS = discord.Intents.default()
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

print(TOKEN)
# client.run(TOKEN)