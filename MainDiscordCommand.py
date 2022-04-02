import asyncio

from discord import team
from guild import guildSignup
import discord
from discord.ext import commands
from jsonDatabase import *
from DiscordPetShop import Inventory
from StarterClass import starterClass
from profileStats import profileStats, inventorys
from quests import guesser, coinFlip
from location import locations
from guild import guildSignup
from levelSystem import *
from petShop import petShops, buyPets
from Shops import *
from lootFromDungeon import *
from fightingSystem import *
from heal import healing
from abilities import *
from artifactStats import *
from Equipment import *
from helpText import helps
client = discord.Client()
client = commands.Bot(command_prefix='-')
client.remove_command('help')
#commands
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="-help for information"))
@client.command()
async def petshop(ctx):
    await ctx.send(Inventory)
    await ctx.message.author
@client.command()
async def profile(ctx):
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
    \t-Swordsman, are more durable, slower than Archer, and it's the most durable class.\n
    🙤Archer
    \t-Archer, are more faster and are better against bosses.\n
    🙤Mage
    \t-Mage, Stronger than Swordsman, but not more durable,not stronger than archer, and it is the slowest class.\n
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
    \t-find(-location to see all locations)\n
    🙤Guilds only:
    \t-dungeon\n
    🙤Casino only:
    \t(on Progress)
    ''')
    await ctx.send(embed=embed)
@client.command()
async def coinflip(ctx, ammount=0, HorT=None):
    id = ctx.message.author.id
    if getDataValue(id, 'coin') >= 10 and  getDataValue(id, 'coin') >= ammount:
        if HorT != None:
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
async def guess(ctx, gNum=0, diff=0):
    id = ctx.message.author.id
    if getDataKey(id, 'class'):
        if gNum == None or diff == None:
            await ctx.send("Choose a number and 1 out of what(-guesser 10 10(min 10 no max), this an example, the user picked 10 and it is 1-100) o(≧▽≦)o")
        elif gNum > 0 and diff > 9:
            await ctx.send(guesser(gNum, diff, id))
        else:
            await ctx.send("Choose a number and 1 out of what(-guesser 10 10(min 10 no max), this an example, the user picked 10 and it is 1-100) ٩(｡•́‿•̀｡)۶")
    else:
        await ctx.send("Please choose a class first. (≧◡≦)")
@client.command()
async def guild(ctx):
    id = ctx.message.author.id
    if getDataKey(id, 'guild'):
        await ctx.send("You are already signed in")
    else:
        await ctx.send("Hello, do you want to buy the guild pass for 100 coins? y/n")
        try:
            msg = await client.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author and 
            message.channel == ctx.channel)
        except asyncio.TimeoutError:
            await ctx.message.delete()
        await ctx.send(guildSignup(id, msg))

@client.command()
async def find(ctx, location=None):
    id = ctx.message.author.id
    if location != None:
        text = locations(id, location)
    else:
        await ctx.send("You didn't pick a location, do -find (location) ex. forest")
    await ctx.send(text)
@client.command()
async def sell(ctx, item, ammount=1):
    id = ctx.message.author.id
    if item == None:
        ctx.send('Please write the item name after the command.')
    await ctx.send(sells(id, item, ammount))
@client.command()
async def inventory(ctx):
    id = ctx.message.author.id
    text = ''
    for key, value in inventorys(id).items():
        if value != 0:
            text += f"{key}: {value} \n"
    await ctx.send(text)

@client.command()
async def dungeon(ctx, floor=None):
    if floor == None:
        await ctx.send("enter floor number")
    id = ctx.message.author.id
    user = openNewDic(id, 'userStats')
    enemy = openNewDic(id, 'enemy')
    if getDataKey(id, 'guild'):
        enemys(id, floor)
        await ctx.send("entering dungeon")
        enemy = openNewDic(id, 'enemy')
        await ctx.send(f"Enemy Health: {enemy['hp']}")
        if floor == None:
            await ctx.send("enter floor number")
        else:
            while user['hp'] > 0:
                while enemy['hp'] > 0:
                    abilities = ability(id)
                    await ctx.send(f"Choose your ability, \n{abilities}")
                    try:
                        msg = await client.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author and 
                        message.channel == ctx.channel)
                    except asyncio.TimeoutError:
                        await ctx.send("You took to long")
                    await ctx.send(fight(id, msg))
                    user = openNewDic(id, 'userStats')
                    enemy = openNewDic(id, 'enemy')
                    if enemy['hp'] <= 0:
                        rarity, artifact = lootGain(id, floor)
                        coin = coinGain(id, floor)
                        exp = xpGain(id, floor)
                        insertToArtifactInv(id, rarity, artifact)

                        text = f"{artifact}: \n"
                        for key, value in openArtifactsInv(id, artifact).items():
                            text += f"{key}: {value} \n"
                        await ctx.send(f"You killed enemy, earned {coin} coin, earned {exp} xp")
                        await ctx.send(f"Artifact stats are... \n{text}")
                        await ctx.send(f"Do you want to equip the artifact/weapon? y/n, else it will be sold")
                        try:
                            msg = await client.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author and 
                            message.channel == ctx.channel)
                        except asyncio.TimeoutError:
                            await ctx.send("You took to long, item will be sold")
                        if msg.content.lower() == 'y' or msg.content.lower() == 'yes':
                            equip(id, artifact)
                            await ctx.send("equiped")
                        else:
                            await ctx.send(sellArtifact(id, rarity))
                        while levelUp(id, getDataValue(id, 'level'), getDataValue(id, 'exp')):
                            await ctx.send("LevelUp")
                            levelUp(id, getDataValue(id, 'level'), getDataValue(id, 'exp'))
                    elif user['hp'] <= 0:
                        await ctx.send("You died")
                        break
                user = openNewDic(id, 'userStats')
                enemy = openNewDic(id, 'enemy')

                if user['hp'] <= 0:
                    break
                else:
                    break
            else:
                await ctx.send("You need to heal")

@client.command()
async def heal(ctx):
    id = ctx.message.author.id
    await ctx.send("Do you want to heal? y/n")
    try:
        msg = await client.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author and 
        message.channel == ctx.channel)
    except asyncio.TimeoutError:
        await ctx.send("You took to long")
    if msg.content.lower() == 'y' or msg.content.lower() == 'yes':
        await ctx.send(healing(id))
    else:
        return "maybe next time then..."

@client.command()
async def location(ctx):
    embed = discord.Embed(title="Locations", description='''
    🙤Forest
    🙤River
    🙤Cave
    🙤Lake
    ''')
    await ctx.send(embed=embed)

@client.command()
async def shop(ctx, item=None):
    id = ctx.message.author.id
    text = shopList()
    embed = discord.Embed(title="Shop Items", description=text)
    if item != None:
        await ctx.send(buy(id, item))

    else:
        await ctx.send(embed=embed)

@client.command()
async def artifacts(ctx):
    id = ctx.message.author.id
    text = userArtifacts(id)
    embed = discord.Embed(title="Profile Artifacts", description=text)
    await ctx.send(embed=embed)

@client.command()
async def upgrade(ctx, artifact):
    id = ctx.message.author.id
    if artifact != None:
        await ctx.send(upgrades(id, artifact))
    else:
        await ctx.send("-upgrade (artifact you want to upgrade) ex. -upgrade weapon")

@client.command()
async def help(ctx):
    text = helps()
    embed = discord.Embed(title="Tutorial for Yuki's DiscordBot", description=text)
    embed.set_footer(text="This is yuki's beta version of the game, there are a lot missed future, it took 3 weeks, I think, I forgot... well have fun ig")
    await ctx.send(embed=embed)
#hiddenCode
def hiddenCode():
    client.run('Discord Token')
hiddenCode()    
