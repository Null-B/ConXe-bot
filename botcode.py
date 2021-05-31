import os, json, requests
from tkinter.font import BOLD
from dotenv import load_dotenv
from discord import Client, Intents, Embed, Status, Game
from discord.ext import commands
import discord
# from websever import keep_aliveO
load_dotenv()

#deps
TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix = "!")
INTENTS = Intents.default()
INTENTS.members = True

#client
client = Client(intents=INTENTS)



async def random_qotegen2():
    url = "https://quotejoy.p.rapidapi.com/list-sources"

    headers = {
        'x-rapidapi-key': "ab103f1da6mshbf05334d9149fc7p1a58d4jsn76e86d802108",
        'x-rapidapi-host': "quotejoy.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    quote2 = (response)
    print(response.text)
    return (quote2)

    



async def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = (f"{json_data[0]['q']} \n\n **{json_data[0]['a']}**")

    return(quote)


# async def get_quote_embed():
#     response = requests.get("https://zenquotes.io/api/random")
#     json_data = json.loads(response.text)

#     quote_formated= (f"{json_data[0]['q']}  {json_data[0]['a']}")

#     quote_embed = quote_formated
#     print (quote_embed)

#     # embed = Embed(color=0x4a3d9a)
#     # embed.add_field.name="Quote", value = 
    


#     print(quote_embed)
#     return(embed)

#reddy message
@client.event
async def on_ready():
    await client.change_presence(status= Status.online, activity= Game("check my code here-https://github.com/Null-B/bot " ))
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

#kick/ban
# @client.comands() 
# async def kick(ctx, member : discord.Member, *, reason=None):
#     await member.kick(reason=reason) 

# @client.comands()
# async def ban(ctx, member : discord.Member, *, reason=None):
#     await member.ban(reason=reason) 



#comands
#join moment this goood
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(color=0x4a3d9a)
            embed.add_field(name="Welcome", value=f"{member.mention} has joined {member.guild.name}", inline=False)
            embed.set_image(url="https://newgitlab.elaztek.com/NewHorizon-Development/discord-bots/Leha/-/raw/master/res/welcome.gif")
            await channel.send(embed=embed)

#leave moment fix this
@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(color=0xdeb110)
            embed.add_field(name="Welcome", value=f"{member.name} has left {member.guild.name}", inline=False)
            embed.set_image(url="https://newgitlab.elaztek.com/NewHorizon-Development/discord-bots/Leha/-/raw/master/res/goodbye.gif")
            await channel.send(embed=embed)

@client.event
async def on_message(message):

    if message.content.startswith('$help'):
            embedVar = Embed(title="Comads", description="dont forget to use the \"$\" to use the comands", color=0x00ff00)
            embedVar.add_field(name="Hi comads", value="$hi / $hello / $sup", inline=False)
            embedVar.add_field(name="more comads", value="$inspire "+ " $invite", inline=False)
            await message.channel.send(embed=embedVar)
#add image to the invite
    if message.content.startswith('$invite'):
        embedVar = Embed(title="Comads", description="Here is the invite", color=0x04b4db)
        embedVar.add_field(name="*https://discord.gg/Tehtfh6gwz*", value="**you can use this invite to join**", inline=False)
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

    
    #inspiration 
    if message.content.startswith('$inspire'):
        quote = await get_quote()
        await message.channel.send(quote) 

    # if message.content.startswith('$comad'):
    #     quote = await get_quote_embed()
    #     await message.channel.send(quote)

    if message.content.startswith('$qoute'):
        qoute2 = await random_qotegen2()
        await message.channel.send(qoute2)
# keep_aliveO()
client.run(TOKEN)