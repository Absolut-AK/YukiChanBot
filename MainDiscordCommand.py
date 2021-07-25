import discord, random, os
from database import ids, profile
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

async def p(ctx):
    username = await ctx.message.author.id
    if ids(username):
        await ctx.send(profile(username))
        
client.run(os.getenv('TOKEN'))