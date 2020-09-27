import discord
from discord.ext import commands

class Modtools(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == ctx.guild.owner:
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member.mention}")
        else:
            await ctx.send("You are not authorised to kick someone")
    
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == ctx.guild.owner:
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member.mention}")
        else:
            await ctx.send("You are not authorised to ban someone")
    
    @commands.command()
    async def unban(self, ctx, *, member):
        if ctx.author == ctx.guild.owner:
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
        else:
            await ctx.send("You are not authorised to unban someone")

def setup(client):
    client.add_cog(Modtools(client))
