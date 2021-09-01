import os, asyncio, time, requests, json
from datetime import datetime, date, time, timezone

import discord
from discord import Embed, Member, message
from discord.ext import commands, tasks
from itertools import cycle

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix=".")
client.remove_command('help')
status = cycle(["Hey if you wnat help use .help🌑", "Hey Welcome🌒", "moon🌓.", "use prefix \".\" for commands🌔", "chese🌕", "help the dev - pls🌖", "go to github🌗", "thanks for useing \"Your mom Bot\" hope you have a good time useing it🌘"])

#✅
@client.event
async def on_ready():
    change_presence.start()

    print ("\n----------------------------------")
    print (f'Logged in as: {client.user.name}')
    print (f'With ID: {client.user.id}.')
    print ("----------------------------------\n")

async def on_message(message):
    word_list = ['cheat', 'cheats', 'hack', 'hacks', 'internal', 'external', 'ddos', 'denial of service']

    if message.author == client.user:
        return

    messageContent = message.content
    if len(messageContent) > 0:
        for word in word_list:
            if word in messageContent:
                await message.delete()
                await message.channel.send('Do not say that!')
        
    messageattachments = message.attachments
    if len(messageattachments) > 0:
        for attachment in messageattachments:
            if attachment.filename.endswith(".dll"):
                await message.delete()
                await message.channel.send("No DLL's allowed!")
            elif attachment.filename.endswith('.exe'):
                await message.delete()
                await message.channel.send("No EXE's allowed!")
            else:
                break
    print("some one has sent a bad message")

@tasks.loop(seconds=1200)
async def change_presence():
    await client.change_presence(activity = discord.Game(next(status)))

@commands.Cog.listener()
async def on_member_join(self, member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(color=0xff0000)
            embed.add_field(
                name="Welcome!",
                value=f"{member.mention} has joined the server!",
                inline=False
            )
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

@commands.Cog.listener()
async def on_member_remove(self, member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(color=0xff0000)
            embed.add_field(
                name="Good bye!",
                value=f"{member.mention} has left the server!",
                inline=False
            )
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

#✅
@client.command()
@commands.has_permissions(kick_members = True)
async def ping(ctx):
    embed = discord.Embed(
        title = f'{round(client.latency * 1000)}ms',
        description = "**Pong!**",
        color = discord.Color.green()
    )
    await ctx.send(embed=embed)
    print("some has ping")


#✅
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user) 
async def hi (ctx):
    await ctx.send("Hi")

    print("hi has been sent")

    
#✅
@client.command()
async def website(ctx):
    embedVar = discord.Embed(title="The Website", url="https://websever-for-replit.kemalsptkemal.repl.co", description="This is the Website for the Bot you can find many thing there like update and contributor's ", color=0x006eff)
    embedVar.set_footer(text="go there if you want")
    await ctx.channel.send(embed=embedVar)

    print("Website comand has run")

#✅
@client.command()
async def bot(ctx):
    await ctx.channel.send("https://github.com/Null-B/Your_mom_bot")

    print("The github has sent")

#✅
@client.command()
async def bot_web(ctx):
    await ctx.channel.send("here is the repo- https://github.com/Null-B/websever-for-replit \n and the Real website- https://websever-for-replit.kemalsptkemal.repl.co")

    print("The github websever repo has been sent")

#✅
@client.command()
async def dev(ctx):
    await ctx.channel.send("https://github.com/Null-B\n He is the person that coded this bot")

    print("The dev has been sent")

#✅
@client.command()
async def dev_helpers(ctx):
    embed=discord.Embed(title="Helpers for the Bot", description="These are the helpers for this bot \n They have done some contributions to the bot", color=0xd69200)
    embed.add_field(name="https://github.com/PH-KDX", value="PH-KDX has helped with tidying up the code", inline=True)
    embed.set_footer(text="if you want to help out got to the github https://github.com/Null-B/Your_mom_bot")
    await ctx.send(embed=embed)

    print("The dev_helpers has been sent")

#✅
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
    if amount > 100:
        embed = discord.Embed(
            title = 'Please enter a smaler amount than 100',
            description = "you canot enter a biger amount than 100",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        await ctx.channel.purge(limit=2)

    elif amount == 0:
        embed = discord.Embed(
            title = 'you must enter a positive amount',
            description = "",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        
        time.sleep(1)
        await ctx.channel.purge(limit=2)

    else:    
        await ctx.channel.purge(limit=amount)
        print(f"{amount} message have been cleared")



#❌
@client.event
async def on_kick_error(ctx, error, member : discord.Member):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title = f'{member.name} You cant do that',
            description = "You need to have \"manage_messages\" perms to use this comand",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)

#fix this❌
@clear.error
async def clear_errrors(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Pleas send a vaid Int")

#✅
#add info to this
@client.command()
async def Help(ctx):
    embed=discord.Embed(title="**Here is some help to the Bot**", description="you can find more help on the commands page (insert commands page url)", color=0xff0000)
    embed.add_field(name="A", value="D", inline=True)
    embed.add_field(name="B", value="E", inline=True)
    embed.add_field(name="C", value="F", inline=True)
    embed.set_footer(text="INSERT SOMETHING")
    await ctx.send(embed=embed)

    print("The help embed has been sent")

#✅
@client.command()
async def invite(ctx):
    link = await ctx.channel.create_invite(max_age = 300)
    embed = discord.Embed(
        title = f'{link}',
        description = f'This link will expire in 5 minutes',
        color = discord.Color.blue()
    )
    await ctx.send(embed=embed)

    print("\"Invite\" has been sent")

#✅
@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)

    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    link = await ctx.channel.create_invite(max_age = 300)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description="Here you go for the information",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name="Invite Link", value=link, inline=True)

    await ctx.send(embed=embed)

    print("\"Serverinfo\" has been sent")


class DuratiohConverter(commands.Converter): 
    async def convert(self, ctx, argument): 
        amount = argument[:-1] 
        unit = argument[-1] 

        if amount.isdigit() and unit in ['s', 'm']:
            return (int(amount), unit) 
        raise commands.BadArgument(message='Not a valid duration') 

#✅
@client.command()
@commands.has_permissions(kick_members = True, ban_members = True )
async def tempban(ctx, member: commands.MemberConverter, duration: DuratiohConverter):
    multiplier = {'s': 1,'m': 60}
    amount, unit = duration 

    await ctx.guild.ban(member)

    embed = discord.Embed(
            title = f'{member} has been banned for',
            description = f'has been banned for **{amount}{unit}**',
            color = discord.Color.green()
            )

    await ctx.send(embed=embed)
    await asyncio.sleep(amount * multiplier[unit]) 
    await ctx.guild.unban(member)

    print(f"Tempban has been issued to \"{member}\"")




#✅
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, * , reason = "No reason provided"):
    embed = discord.Embed(
        title = f'You have been kicked form {ctx.guild.name}.',
        description = f'Because {reason}',
        icon = ctx.guild.icon,
    )
    await member.send(embed=embed)
    await member.kick(reason=reason)

    print(f"kick has been issued to \"{member}\"")



#✅
@client.command()
@commands.has_permissions(kick_members = True, ban_members = True)
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:

        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="You cannot ban yourself", value="so stop trying", inline=True)
        await ctx.channel.send(embed=embed)

        return
    if reason == None:
        reason = "No reason specified for your Ban"

    link = await ctx.channel.create_invite()

    embed1=discord.Embed(color=0xff0000)
    embed1.add_field(name=f"You have been banned from {ctx.guild.name} for \"{reason}\"", value=f"you can apply for a unban here - (LINK for the unban apply)", inline=True)
    embed1.add_field(name = "When you do get unbaned use this link below", value=f"{link}" , inline=True)
    
    await member.send(embed=embed1)
    await ctx.guild.ban(member, reason=reason)
    
    timestamp = datetime.now()
    time = (timestamp.strftime(r"%I:%M %p %d/%m/%y"))

    embed2=discord.Embed(color=0x00b3ff)
    embed2.add_field(name=f"{member} is Banned!", value=f"{time} by {ctx.author.name}", inline=True)
    await ctx.channel.send(embed=embed2)

    print(f"ban has been issued to \"{member}\"")

#✅
@client.command()
@commands.has_permissions(kick_members = True, ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user) 
            
            embed=discord.Embed(color=0x00b3ff)
            embed.add_field(name=f"{member} is Unbanned!", value=f"Welcome back {user.mention}. \n try not to get baned again", inline=True)
            await ctx.channel.send(embed=embed)
            return

    print(f"user has \"{member}\" been  unband")

@client.command()
async def ayay (ctx):
    await ctx.channel.send("Please enter a ayah nuber :")

    ayah_Number = await client.wait_for("message")


    print (ayah_Number)    

    url = f"http://api.alquran.cloud/v1/ayah/{ayah_Number}/en.asad"


#need some work ❌
@client.command()
async def echo(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(
            title = 'Please tell me what you wnat me to say...',
            description = 'This request will timeout in 1 minute',
        )
    sent = await ctx.channel.send(embed=embed)

    try:
        msg = await self.bot.wait_for(
            "message",
            timeout = 60,
            check = lambda message: message.author == ctx.author
                               and message.channel == ctx.channel
        )
        
        if msg:
            await sent.delete()
            await msg.delete()
            await ctx.channel.send(msg)

    except asyncio.TimeoutError:
        await sent.delete()

        embed = discord.Embed(
            title = 'Canceleing due to timeout.',
            description = 'deleteing after 10 seconds',
        )
        await ctx.guild.send(embed=embed, deleat_after=10)


#✅
@client.command()
async def dm(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    embed_a = discord.Embed(
        title = 'What do you want to send?',
        description = 'pleas be kind to others 😄',
        color = discord.Color.blue()
    )
    embed1 = await ctx.send(embed=embed_a)

    def check(m):
        return m.author.id == ctx.author.id

    message = await client.wait_for("message", check=check)
    await embed1.delete()
    embed_b = discord.Embed(
        title = f'Message has been sent to {member}',
        description = 'now wait for a response',
        color = discord.Color.green()
    )
    await ctx.send(embed=embed_b)

    embed_c = discord.Embed(
        title = f'{ctx.author.name}has sent you a message:\n {message.content}',
        description = 'why not send him a response?',
        color = discord.Color.green()
    )
    await member.send(embed=embed_c)   

    print(f"\"Dm\" has been sent by {member}") 


#need some work ❌
@client.command()
async def ayah(ctx):

    def check(msg):
        return ctx.message.content

    try:
        embed = discord.Embed(
            title = 'Please tell us a a ayah Number',
            description = 'these are the valid ayah Numbers: ',
        )
        await ctx.send(embed=embed)

        ayah_number = await client.wait_for("message", check=check, timeout=30) 
        await ctx.send(ayah_number)
        # await ctx.channel.purge(limit=2)
    except asyncio.TimeoutError:
        await ctx.delete()
        await ctx.send("Sorry, you didn't reply in time!")


        embed = discord.Embed(
            title = 'Canceleing due to timeout.',
            description = 'deleteing after 10 seconds',
        )
        await ctx.guild.send(embed=embed, deleat_after=10)


    response = requests.get(f"http://api.alquran.cloud/v1/ayah/{ayah_number}/en.asad")
    json_data = json.loads(response.text)
    ayah = (json_data)

    """
    embed = discord.Embed(
            title = 'you must enter a positive amount',
            description = "",
            color = discord.Color.red()
        )
    """

    await ctx.channel.send(ayah)

    print("Ayah has been sent successfully")


@client.command()
async def some(ctx):
    await ctx.send(f"y or n")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in ["y", "n"]

    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == "y":
        await ctx.send("You said yes!")
    else:
        await ctx.send("You said no!")



client.run(TOKEN)