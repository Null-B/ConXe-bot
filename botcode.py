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

    @client.event
    async def on_message(message):

        if message.content.startswith('$help'):
            embedVar = discord.Embed(title="Comads", description="dont forget to use the \"$\" to use the comands", color=0x00ff00)
            embedVar.add_field(name="Hi comads", value="$hi / $hello / $sup", inline=False)
            embedVar.add_field(name="$penis", value="to be sus", inline=False)
            embedVar.add_field(name="$haram", value="to see what is haram", inline=False)
            # embedVar.add_field(name="Field2", value="hi2", inline=False)
            # embedVar.add_field(name="Field2", value="hi2", inline=False)
            # embedVar.add_field(name="Field2", value="hi2", inline=False)
            # embedVar.add_field(name="Field2", value="hi2", inline=False)
            await message.channel.send(embed=embedVar)

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