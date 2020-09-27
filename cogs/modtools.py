import discord
from discord.ext import commands

class Modtools(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")
    
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")
    
    @commands.command()
    async def unban(self, ctx, *, member):
        unban = False
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
    
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                unban = True
                await ctx.send(f"Unbanned {user.mention}")
                break
        
        if not unban:
            await ctx.send("Either the given username/discriminator is incorrect or the user is not banned")


def setup(client):
    client.add_cog(Modtools(client))
