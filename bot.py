import discord
from  discord.ext import commands
import random

client = commands.Bot(command_prefix = "mc ")

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

@client.command(name="8ball", aliases=["8BALL", "8Ball", "8BAll"])
async def _8ball(ctx, *, question=""):
    if question != "":
        answers = "It is certain.It is decidedly so.Without a doubt.Yes – definitely.You may rely on it.As I see it, yes.Most likely.Outlook good.Yes.Signs point to yes.Reply hazy, try again.Ask again later.Better not tell you now.Cannot predict now.Concentrate and ask again.Don't count on it.My reply is no.My sources say no.Outlook not so good.Very doubtful".split(".")
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")
    else:
        await ctx.send("You have to ask a question idiot")

@client.command()
async def insult(ctx, *, name = " "):
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

@client.command()
async def slap(ctx, *, reason=""):
    if reason != "":
        await ctx.send(f"{ctx.author} slapped {random.choice(ctx.guild.members)}. Reason *{reason}*")
    else:
        await ctx.send("You can't just slap someone for no reason")

@client.command()
async def servername(ctx):
    await ctx.send(f"{ctx.guild.name}")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
async def unban(ctx, *, member):
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


client.run("NzU5NDI1MTk0NTIyNzA1OTcx.X29T0w.Fza69ORtAhRUtjQJXO-6H0Tg6so")
