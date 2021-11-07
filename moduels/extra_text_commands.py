import discord, asyncio
from discord import ctx
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot



#need some work ❌
@commands.command()
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
@commands.command()
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

    message = await commands.wait_for("message", check=check)
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
@commands.command()
async def ayah(ctx):

    def check(msg):
        return ctx.message.content

    try:
        embed = discord.Embed(
            title = 'Please tell us a a ayah Number',
            description = 'these are the valid ayah Numbers: ',
        )
        await ctx.send(embed=embed)

        ayah_number = await commands.wait_for("message", check=check, timeout=30) 
        await ctx.send(ayah_number)
        # await ctx.channel.purge(limit=2)
    except asyncio.TimeoutError:
        await ctx.delete()
        await ctx.send("Sorry, you didn't reply in time!")

    
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        await ctx.send("template command")


def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))