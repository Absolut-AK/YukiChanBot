import discord
from database import ids, profile
from discord.ext import commands
from DiscordBlackJack import blackJack

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
async def bj(ctx):
    blackJack()
client.run('ODQ2NTg1MDMyMTg5NTQyNDEw.YKxpwA.zUSGN7_vFNV7xIVV69Ulss1AdoE')