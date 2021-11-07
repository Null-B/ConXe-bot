import discord 
from discord.ext import commands

class example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('bot yes')

    @commands.command()
    async def pongf(self, ctx):
        await ctx.send ('a')


def setup(client):
    client.add_cog(example(client))