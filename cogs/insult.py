import discord
from discord.ext import commands
import random

class Insult(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def insult(self, ctx, *, name = " "):
        if name == " ":
            await ctx.send("Please provide a name as well")
    
        else:
            curses_0 = "Chutiya.Jhaat ka baal.Lowde jesi shakal ka.Madarchod.Gaand ka dhakan.Kamina.Tharki.Behen ka lauda.Chut ka maindak.Hijra.Choot ka baal.Chullu bhar muth mein doob mar.Bhen ka taka.Kutte ka tatta.Gand Ka Khatmal.Tatto ke saudagar".split(".")
            curses_1 = "gaandu.bhosdike.lodu.suwar ki aulad.randi baj.sust lund ki padaish.mera muh me le.betichod.choot ka bhoot.choot ka pakoda.apni gaand mein muthi daalta hai.apna lund choosta hai.teri gaand main kute ka lund.tu kutte ke poot, teri maa ki choot".split(".")
            random_choice = random.choice([0,1])
            if random_choice:
                await ctx.send(f"{name} {random.choice(curses_1)}")
            else:
                await ctx.send(f"{random.choice(curses_0)} {name}")

def setup(client):
    client.add_cog(Insult(client))
