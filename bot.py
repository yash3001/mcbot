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

l = ['N', 'z', 'U', '5', 'N', 'D', 'I', '1', 'M', 'T', 'k', '0', 'N', 'T', 'I', 'y', 'N', 'z', 'A', '1', 'O', 'T', 'c', 'x', '.', 'X', '2', '9', 'T', '0', 'w', '.', '3', 'L', 'Z', 'P', 'C', 'Y', 'Z', 'j', 'Q', 'i', 'e', 'Q', 'R', 'J', 'x', 'V', 'O', '2', 'y', 'h', 'B', 'l', 'r', 'k', 'v', 'y', 'g']
client.run("".join(l))
