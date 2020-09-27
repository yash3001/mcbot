import discord
from discord.ext import commands

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! ... Lol, just kidding, bot's latency is {round(self.client.latency * 1000)}ms")
    
    @commands.command()
    async def servername(self, ctx):
        await ctx.send(f"{ctx.guild.name}")

def setup(client):
    client.add_cog(Utility(client))
