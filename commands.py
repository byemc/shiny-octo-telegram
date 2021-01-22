import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='sot!')

@bot.command()
async def ping(ctx):
    tic = time.perf_counter()
    await ctx.send('Pong!')
    toc = time.perf_counter()
    tictoc = toc - tic
    await ctx.send('Time:', tictoc)

bot.run('[OMITTED]')
