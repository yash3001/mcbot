import discord
from  discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = ["Mc ", "mc ", "mC ", "MC "])

@client.command()
async def load(ctx, extension=""):
    if extension != "":
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} loaded")
    else:
        await ctx.send("You have to provide the name of the extension")

@client.command()
async def unload(ctx, extension=""):
    if extension != "":
        client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} unloaded")
    else:
        await ctx.send("You have to provide the name of the extension")

@client.command()
async def reload(ctx, extension=""):
    if extension != "":
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} reloaded")
    else:
        await ctx.send("You have to provide the name of the extension")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("NzU5NDI1MTk0NTIyNzA1OTcx.X29T0w.q_y5upSuS3vj0y1Oo76LiyJCrSI")
