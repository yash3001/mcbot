import discord
from  discord.ext import commands
import random

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} just joined the server")

@client.event
async def on_member_remove(member):
    print(f"{member} just left the server")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! ... Lol, just kidding, bot's latency is {round(client.latency * 1000)}ms")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    answers = "It is certain.It is decidedly so.Without a doubt.Yes – definitely.You may rely on it.As I see it, yes.Most likely.Outlook good.Yes.Signs point to yes.Reply hazy, try again.Ask again later.Better not tell you now.Cannot predict now.Concentrate and ask again.Don't count on it.My reply is no.My sources say no.Outlook not so good.Very doubtful".split(".")
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")

@client.command()
async def insult(ctx, name):
    curses_0 = "Chutiya.Jhaat ka baal.Lowde jesi shakal ka.Madarchod.Gaand ka dhakan.Kamina.Tharki.Behen ka lauda.Chut ka maindak.Hijra.Choot ka baal.Chullu bhar muth mein doob mar.Bhen ka taka.Kutte ka tatta.Gand Ka Khatmal".split(".")
    curses_1 = "gaandu.bhosdike.lodu.suwar ki aulad.randi baj.sust lund ki padaish.mera muh me le.betichod.choot ka bhoot.choot ka pakoda.apni gaand mein muthi daalta hai.apna lund choosta hai.teri gaand main kute ka lund.tu kutte ke poot, teri maa ki choot".split(".")
    random_choice = random.choice([0,1])
    if random_choice:
        await ctx.send(f"{name} {random.choice(curses_1)}")
    else:
        await ctx.send(f"{random.choice(curses_0)} {name}")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

client.run("NzU5NDI1MTk0NTIyNzA1OTcx.X29T0w.Fza69ORtAhRUtjQJXO-6H0Tg6so")
