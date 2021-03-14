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

    @commands.command(aliases=["whois"])
    async def userinfo(ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                              title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Roles:", value="".join([role.mention for role in roles[1:]])) #ignores the @everyone role because....it pings all..so instead append if wanted or remove the [1:] part and let it remain as @@everyone :p
        embed.add_field(name="Highest Role:", value=member.top_role.mention)
        print(member.top_role.mention)
        await ctx.send(embed=embed) 


def setup(client):
    client.add_cog(Utility(client))
