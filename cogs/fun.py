import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="8ball", aliases=["8BALL", "8Ball", "8BAll"])
    async def _8ball(self, ctx, *, question=""):
        if question != "":
            answers = "It is certain.It is decidedly so.Without a doubt.Yes – definitely.You may rely on it.As I see it, yes.Most likely.Outlook good.Yes.Signs point to yes.Reply hazy, try again.Ask again later.Better not tell you now.Cannot predict now.Concentrate and ask again.Don't count on it.My reply is no.My sources say no.Outlook not so good.Very doubtful".split(".")
            await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")
        else:
            await ctx.send("You have to ask a question idiot") 

    @commands.command()
    async def slap(self, ctx):
        await ctx.send(f"{ctx.author.mention} slapped {random.choice(ctx.guild.members).mention}")
        
    @commands.command()
async def avatar(ctx, member: discord.Member = None):         #so here if no arguemnt is passed, the avatar of the user is shown
    if not member:
        member = ctx.message.author
    show_avatar = discord.Embed(description="[Here's the avatar](%s)" %
                                member.avatar_url)
    show_avatar.set_image(url="{}".format(member.avatar_url))
    show_avatar.set_footer(text=f'{member}')
    print(member.avatar_url)
    await ctx.send(embed=show_avatar)

def setup(client):
    client.add_cog(Fun(client))
