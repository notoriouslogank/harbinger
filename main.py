import discord
import os
import logging
import random
import sys
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
load_dotenv()

TOKEN = os.getenv('TOKEN')
VERSION = '0.7.8'
sTime = datetime.now()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print(sTime)
    print('---------')

@bot.command()
async def online(ctx):
    await ctx.send(f'{bot.user} is online.')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format must be NdN!')
        return    
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def info(ctx):
    cTime = datetime.now()
    delta = cTime - sTime
    embedVar = discord.Embed(title='mcswitch', color=0x00ff00)
    embedVar.add_field(name='version', value=f'v{VERSION}', inline=True)
    embedVar.add_field(name='uptime', value=f'{delta}', inline=True)
    embedVar.add_field(name='author', value='notoriouslogank', inline=True)
    embedVar.add_field(name='source code', value='https://github.com/notoriouslogank/mcswitch')
    await ctx.send(embed=embedVar)

@bot.command()
async def ping(ctx):
    await ctx.send('Current ping: {0}'.format(round(bot.latency, 2)))

@bot.command()
async def uptime(ctx):
    cTime = datetime.now()
    delta = cTime - sTime
    await ctx.send(f'Uptime: {delta}')

@bot.command()
async def shutdown(ctx):
    shutdownTime = str(datetime.now())
    embedShutdown = discord.Embed(title='Shutdown', color=0xff0000, timestamp=datetime.now())
    embedShutdown.add_field(name='user', value=f'{ctx.message.author}', inline=True)
    await ctx.send(embed = embedShutdown)
    sys.exit()

@bot.command()
async def mcstart(ctx):
    await os.system('sh mc.sh')
    print('Starting the server, maybe.')
    await ctx.send('Starting MC Server.')

@bot.command()
async def rps(ctx, choice):
    choices = ['rock', 'paper', 'scissors']
    botChoice = choices[random.randint(0, 2)]
    embedRPS = discord.Embed(color=0x0000ff, title='rock, paper, scissors')
    embedRPS.add_field(name='You', value=f'{choice}', inline=True)
    embedRPS.add_field(name='Bot', value=f'{botChoice}', inline=True)
    if choice == botChoice:
        embedRPS.add_field(name='result', value='You tied!', inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == 'rock' and choice == 'paper':
        embedRPS.add_field(name='result', value='You win!', inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == 'paper' and choice == 'scissors':
        embedRPS.add_field(name='result', value='You win!', inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == 'scissors' and choice == 'rock':
        embedRPS.add_field(name='result', value='You win!', inline=False)
        await ctx.send(embed=embedRPS)
    else:
        embedRPS.add_field(name='result', value='You lose!', inline=False)
        await ctx.send(embed=embedRPS)

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
