#Moduals
import discord
import os
from dotenv import load_dotenv
load_dotenv()

#deps
TOKEN = os.getenv("TOKEN")
PREFIX = '!'
INTENTS = discord.Intents.default()

#client
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)

#reddy message
@client.event
async def on_ready():
    await client . change_presence(status=discord. Status . idle, activity=discord .Game("check my code here-https://github.com/Null-B/bot " ))
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

#users join/leave /log
client.event
async def on_memberjoin(member,message): 
    print(f'member has joined a server. ') 
    await message.channel.send(member,'member has joined a server.')

async def on_member_remove(member,message): 
    print(f'member has left a server.' )
    await message.channel.send(member,'member has left a server.')


#comands

@client.event
async def on_message(message):
    #help
 
    @client.event
    async def on_message(message):

        #embed help list
        if message.content.startswith('$help'):
                embedVar = discord.Embed(title="Comads", description="dont forget to use the \"$\" to use the comands", color=0x00ff00)
                embedVar.add_field(name="Hi comads", value="$hi / $hello / $sup", inline=False)
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

client.run(TOKEN)