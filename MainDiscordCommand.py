import discord, random, os
from database import ids
from discord.ext import commands
from helpText import help

client = discord.Client()
client = commands.bot(command_prefix='-')

#commands
@client.command()
async def profile(ctx, arg):
    await ctx.send(arg)

async def leaderboard(ctx):
    print(leaderboard)

async def help(ctx):
    print(help)

async def accountCreation(user):
    ids(user)
        

client.run(os.getenv('TOKEN'))