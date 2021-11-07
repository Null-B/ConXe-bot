import discord, time
from discord import ctx
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

#✅
@commands.command()
@commands.has_permissions(kick_members = True)
async def ping(ctx):
    embed = discord.Embed(
        title = f'{round(commands.latency * 1000)}ms',
        description = "**Pong!**",
        color = discord.Color.green()
    )
    await ctx.send(embed=embed)
    print("some has ping")

#✅
@commands.command()
@commands.cooldown(1, 30, commands.BucketType.user) 
async def hi (ctx):
    await ctx.send("Hi")

    print("hi has been sent")

    
#✅
@commands.command()
async def website(ctx):
    embedVar = discord.Embed(title="The Website", url="https://websever-for-replit.kemalsptkemal.repl.co", description="This is the Website for the Bot you can find many thing there like update and contributor's ", color=0x006eff)
    embedVar.set_footer(text="go there if you want")
    await ctx.channel.send(embed=embedVar)

    print("Website comand has run")

#✅
@commands.command()
async def bot(ctx):
    await ctx.channel.send("https://github.com/Null-B/Your_mom_bot")

    print("The github has sent")

#✅
@commands.command()
async def bot_web(ctx):
    await ctx.channel.send("here is the repo- https://github.com/Null-B/websever-for-replit \n and the Real website- https://websever-for-replit.kemalsptkemal.repl.co")

    print("The github websever repo has been sent")

#✅
@commands.command()
async def dev(ctx):
    await ctx.channel.send("https://github.com/Null-B\n He is the person that coded this bot")

    print("The dev has been sent")

#✅
@commands.command()
async def dev_helpers(ctx):
    embed=discord.Embed(title="Helpers for the Bot", description="These are the helpers for this bot \n They have done some contributions to the bot", color=0xd69200)
    embed.add_field(name="https://github.com/PH-KDX", value="PH-KDX has helped with tidying up the code", inline=True)
    embed.set_footer(text="if you want to help out got to the github https://github.com/Null-B/Your_mom_bot")
    await ctx.send(embed=embed)

    print("The dev_helpers has been sent")

#✅
@commands.command()
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
@commands.event
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
@commands.command()
async def help(ctx):
    embed=discord.Embed(title="**Here is some help to the Bot**", description="you can find more help on the commands page (insert commands page url)", color=0xff0000)
    embed.add_field(name="A", value="D", inline=True)
    embed.add_field(name="B", value="E", inline=True)
    embed.add_field(name="C", value="F", inline=True)
    embed.set_footer(text="INSERT SOMETHING")
    await ctx.send(embed=embed)

    print("The help embed has been sent")

#✅
@commands.command()
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
@commands.command()
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


    
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        await ctx.send("template command")


def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))