import os
import json
import requests
import random
from discord import Client, Intents, Embed, Status, Game
from discord.ext import comands

# from webserver import keep_alive
from dotenv import load_dotenv
load_dotenv()

# discord bot client settings
TOKEN = os.getenv("TOKEN")
INTENTS = Intents.default()
INTENTS.members = True

# client / bot comad
client = Client(
    command_prefix="!",
    intents=INTENTS
    )

client2 = comands.bot(
    command_prefix = '!'
)

# Ready message
@client.event
async def on_ready():
    await client.change_presence(
        status=Status.online,
        activity=Game(
            "check my code here-https://github.com/Null-B/bot"
            )
        )
    print (f'Logged in as: {client.user.name}')
    print (f'With ID: {client.user.id}')

# Json for the inspire fucntion
async def random_quote_gen():
    url = "https://quotejoy.p.rapidapi.com/list-sources"

    headers = {
        'x-rapidapi-key': "ab103f1da6mshbf05334d9149fc7p1a58d4jsn76e86d802108",
        'x-rapidapi-host': "quotejoy.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    quote = (response)
    print (response.text)
    return (quote)


#add a func for random emojis

#inspire foramt
async def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = (f"{json_data[0]['q']} \n\n **{json_data[0]['a']}**")

    return (quote)

# inspire but with embed
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





# kick/ban
# @client.commands
# async def kick(ctx, member : client.Member, *, reason=None):
#     await member.kick(reason=reason)

# @client.command
# async def ban(ctx, member : client.Member, *, reason=None):
#     await member.ban(reason=reason)



# make a bd with ph qouths

# join / leave fucntions 
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(
                color=0x4a3d9a
                )
            embed.add_field(
                name="Welcome",
                value=f"{member.mention} has joined {member.guild.name}",
                inline=False
                )
            embed.set_image(
                url=("https://newgitlab.elaztek.com/NewHorizon-Developme"
                     "nt/discord-bots/Leha/-/raw/master/res/welcome.gif")
                )
            await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(
                color=0xdeb110
                )
            embed.add_field(
                name="Welcome",
                value=f"{member.name} has left {member.guild.name}",
                inline=False
                )
            embed.set_image(
                url=("https://newgitlab.elaztek.com/NewHorizon-Developme"
                     "nt/discord-bots/Leha/-/raw/master/res/goodbye.gif")
                )
            await channel.send(embed=embed)


# in dev
list_of_greetings = ["Hello!" , "It’s nice to meet you.", "Hi!" , "G’day!", "Howdy!", "Hey", "Hey there", "What’s up?", "sup", "Yo"]

random_greetings = random.shuffle(list_of_greetings)
print(random_greetings)

# add image to the invite
# @client.command
#     async def yes():
#         if message.content.startswith('$invite'):
#             embedVar = Embed(
#                 title="Server Invite",
#                 description="Here is the invite",
#                 color=0x04b4db
#                 )
#             embedVar.add_field(
#                 name="*https://discord.gg/Tehtfh6gwz*",
#                 value="**you can use this invite to join**",
#                 inline=False)
#             await message.channel.send(embed=embedVar)

client2.command() 
async def server(cxt):
    name= str(cxt.guild.name) 
    discription = str(cxt.guild.description) 

    owner =  str(cxt.guild.ouner)
    id = str(cxt.guild.id) 
    region = str(cxt.guild.region) 
    memberCout = str(cxt.guild.member_cout)
    icon = str(cxt.guild.icon_uri) 

    embed = Embed(
        title = name + "Severe information",
        description = discription(),
    )
    embed.set_thumbnail(url = icon)
    embed.add_field(name = "owner", value = owner, inline=True)
    embed.add_field(name = "Sever ID", value = id, inline=True)
    embed.add_field(name = "Region", value = region, inline=True)
    embed.add_field(name = "Member Cout", value = memberCout, inline=True)

    await cxt.send(embed=embed) 

@client.event
async def on_message(message):
    if message.content.startswith('$help'):
        embedVar = Embed(
            title="Commands",
            description="dont forget to use the \"$\" to use the comands",
            color=0x00ff00
            )
        embedVar.add_field(
            name="Hi commands",
            value="$hi / $hello / $sup",
            inline=False
            )
        embedVar.add_field(
            name="More commands",
            value="$inspire - for a inspirational quote\n\n$quote - to get a different type of quote  \n\n$invite - for the invite sever link \n\n  ",
            inline=False
            )
        await message.channel.send(embed=embedVar)


    # hi commands
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!😀')

    if message.content.startswith('$hi'):
        await message.channel.send('eyyyy😀')

    if message.content.startswith('$sup'):
        await message.channel.send('sup my dued😀')

    # inspiration
    if message.content.startswith('$inspire'):
        quote = await get_quote()
        await message.channel.send(quote)

    # if message.content.startswith('$comad'):
    #     quote = await get_quote_embed()
    #     await message.channel.send(quote)

    if message.content.startswith('$quote'):
        quote = await random_quote_gen()
        await message.channel.send(quote)

# keep_alive()

client.run(TOKEN)
