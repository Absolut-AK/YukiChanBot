import asyncio
from guild import guildSignup
import discord
from discord.ext import commands
from jsonDatabase import *
from DiscordPetShop import Inventory
from StarterClass import starterClass
from profileStats import profileStats, inventory
from quests import guess, coinFlip
from location import locations
from guild import guildSignup
client = discord.Client()
client = commands.Bot(command_prefix='-')

#commands
@client.command()
async def petshop(ctx):
    await ctx.send(Inventory)
    await ctx.message.author
@client.command()
async def p(ctx):
    id = ctx.message.author.id
    embed = discord.Embed(title="Profile", description=profileStats(id))
    await ctx.send(embed=embed)
@client.command()
async def starter(ctx):
    check(id)
    firstUser = ctx.message.author.id
    embed = discord.Embed(title="StarterClasses", description=
    '''
    🙤Swordsman
    \t-Swordsman, are more durable, and more balanced class.\n
    🙤Archer
    \t-Archer, are more faster and are better against bosses.\n
    🙤Mage
    \t-Mage, are stronger against multiple enemies, and it is the slowest class.\n
    Write your desired class, this can't be changed in the future for free!	(─‿‿─)
    ''')
    await ctx.send(embed=embed)
    try:
        msg = await client.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author and 
        message.channel == ctx.channel)
    except asyncio.TimeoutError:
        await ctx.message.delete()
    await ctx.send(starterClass(msg, firstUser))
@client.command()
async def quests(ctx):
    embed = discord.Embed(title="Way to Earn Coin", description=
    '''
    🙤Free For Everyone:
    \t-guesser
    \t-coinflip
    \t(On Progress)\n
    🙤Guilds only:
    \t(On Progress)\n
    🙤Casino only:
    \t(on Progress)
    ''')
    await ctx.send(embed=embed)
@client.command()
async def cf(ctx, ammount=0, HorT=None):
    id = ctx.message.author.id
    if getDataValue(id, 'coin') >= 10 and  getDataValue(id, 'coin') >= ammount:
        HorT = HorT.lower()
        if ammount < 10  or ammount > 100 or HorT == None:
            await ctx.send("Choose your bet(min 10, max 100) and guessing side(-coinflip 10 tails or heads)")
        elif HorT == 'heads' or HorT == 'tails':
            await ctx.send(coinFlip(ammount, HorT, id))
        else:
            await ctx.send("Choose your bet(min 10, max 100) and guessing side(-coinflip 10 tails or heads)")
    else:
        await ctx.send("You don't have enough coins. <(￣︶￣)>")

@client.command()
async def g(ctx, gNum=0, diff=0):
    id = ctx.message.author.id
    if getDataKey(id, 'class'):
        if gNum == None or diff == None:
            await ctx.send("Choose a number and 1 out of what(-guesser 10 10(min 10 no max), this an example, the user picked 10 and it is 1-100) o(≧▽≦)o")
        elif gNum > 0 and diff > 9:
            await ctx.send(guess(gNum, diff, id))
        else:
            await ctx.send("Choose a number and 1 out of what(-guesser 10 10(min 10 no max), this an example, the user picked 10 and it is 1-100) ٩(｡•́‿•̀｡)۶")
    else:
        await ctx.send("Please choose a class first. (≧◡≦)")
@client.command()
async def guild(ctx):
    id = ctx.message.author.id
    if getDataKey(id, 'guild'):
        pass
    else:
        await ctx.send("Hello, do you want to buy the guild pass for 100 coins? y/n")
        try:
            msg = await client.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author and 
            message.channel == ctx.channel)
        except asyncio.TimeoutError:
            await ctx.message.delete()
        await ctx.send(guildSignup(id, msg))

@client.command()
async def f(ctx, location=None):
    id = ctx.message.author.id
    if location != None:
        text = locations(id, location)
    else:
        await ctx.send("You didn't pick a location, do -find (location) ex. forest")
    await ctx.send(text)
@client.command()
async def sell(ctx, item):
    pass
@client.command()
async def i(ctx):
    id = ctx.message.author.id
    await ctx.send(inventory(id))
client.run('ODQ2NTg1MDMyMTg5NTQyNDEw.YKxpwA.zUSGN7_vFNV7xIVV69Ulss1AdoE')