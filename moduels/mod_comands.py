import discord, asyncio, datetime
from discord import ctx
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


class DuratiohConverter(commands.Converter): 
    async def convert(self, ctx, argument): 
        amount = argument[:-1] 
        unit = argument[-1] 

        if amount.isdigit() and unit in ['s', 'm']:
            return (int(amount), unit) 
        raise commands.BadArgument(message='Not a valid duration') 

#✅
@commands.command()
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
@commands.command()
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
@commands.command()
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
@commands.command()
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

    
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        await ctx.send("template command")


def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))