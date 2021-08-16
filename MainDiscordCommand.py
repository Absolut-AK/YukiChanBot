import discord
from discord.ext import commands
from jsonDatabase import check
from DiscordPetShop import Inventory
from StarterClass import starterClass
client = discord.Client()
client = commands.Bot(command_prefix='-')

#commands
@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def p(ctx):
    username = ctx.message.author.id
    await ctx.send(username)
@client.command()
async def c(ctx):
    userid = ctx.message.author.id
    await ctx.send(check(userid))
@client.command()
async def petshop(ctx):
    await ctx.send(Inventory)
    await ctx.message.author
@client.command()
async def profile(ctx):
    id = ctx.message.author.id
@client.command()
async def starter(ctx):
    embed = discord.Embed(title="StarterClasses", description=
    '''
    •Swordsman
        -Swordsman are more durable, and more balanced class.
    •Archer
        -Archer are more faster and are better against bosses.
    •Mage
        -Mage are stronger against multiple enemies, and it is the slowest class.
    ''')
    await ctx.send(embed=embed)
    msg = await client.wait_for("message")
    await ctx.send(starterClass(msg, ctx.message.author.id))
    

client.run('ODQ2NTg1MDMyMTg5NTQyNDEw.YKxpwA.zUSGN7_vFNV7xIVV69Ulss1AdoE')