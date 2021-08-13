import discord
from database import ids, profile
from discord.ext import commands
from jsonDatabase import check
from DiscordPetShop import Inventory

client = discord.Client()
client = commands.Bot(command_prefix='-')

#commands
@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def p(ctx):
    username = ctx.message.author.id
    if ids(username):
        await ctx.send(username)
@client.command()
async def c(ctx):
    userid = ctx.message.author.id
    await ctx.send(check(userid))
@client.command()
async def petshop(ctx):
    await ctx.send(Inventory)
    await ctx.message.author
    

client.run('ODQ2NTg1MDMyMTg5NTQyNDEw.YKxpwA.zUSGN7_vFNV7xIVV69Ulss1AdoE')