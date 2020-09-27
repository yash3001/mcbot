import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game("with your mind"))
        print("Bot is ready")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} just joined the server")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} just left the server") 

def setup(client):
    client.add_cog(Events(client))
