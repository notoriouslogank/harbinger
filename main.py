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

def getVer():
    with open('CHANGELOG.md', 'r') as f:
        changes = f.readlines()
        vLine = changes[6]
        version = vLine[4:9]
        return version

TOKEN = os.getenv('TOKEN')
VERSION = getVer()
sTime = datetime.now()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logging.INFO(f'Bot logged in and listening as {bot.user}.')
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print(sTime)
    print('---------')

@bot.command()
async def online(ctx):
    logging.DEBUG(f'User: {ctx.message.author} Command: online Time: {datetime.now()}')
    await ctx.send(f'{bot.user} is online.')

@bot.command()
async def add(ctx, left: int, right: int):
    logging.DEBUG(f'User: {ctx.message.author} Command: add Time: {datetime.now()}')
    logging.DEBUG(f'Output: {left + right}')
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    logging.DEBUG(f'User: {ctx.message.author} Command: roll({dice}) Time: {datetime.now()}')
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        logging.WARN(f'Incorrect format: {dice}')
        await ctx.send('Format must be NdN!')
        return    
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    logging.INFO(f'User: {ctx.message.author}')
    logging.INFO(f'Result: {result}')
    await ctx.send(result)

@bot.command()
async def joined(ctx, member: discord.Member):
    logging.INFO(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def info(ctx):
    logging.DEBUG(f'User: {ctx.message.author} Command: info()')
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
    logging.DEBUG(f'User: {ctx.message.author} Command: ping()')
    logging.INFO('Ping: {0}'.format(round(bot.latency, 2)))
    await ctx.send('Current ping: {0}'.format(round(bot.latency, 2)))

@bot.command()
async def uptime(ctx):
    logging.DEBUG(f'User: {ctx.message.author} Command: uptime()')
    cTime = datetime.now()
    delta = cTime - sTime
    logging.INFO(f'Uptime: {delta}')
    await ctx.send(f'Uptime: {delta}')

@bot.command()
async def shutdown(ctx):
    logging.DEBUG(f'User: {ctx.message.author} Command: shutdown()')
    embedShutdown = discord.Embed(title='Shutdown', color=0xff0000, timestamp=datetime.now())
    embedShutdown.add_field(name='user', value=f'{ctx.message.author}', inline=True)
    logging.WARN(f'Shutting down!')
    await ctx.send(embed = embedShutdown)
    sys.exit()

@bot.command()
async def mcstart(ctx):
    await os.system('sh mc.sh')
    print('Starting the server, maybe.')
    await ctx.send('Starting MC Server.')

@bot.command()
async def rps(ctx, choice):
    logging.DEBUG(f'User: {ctx.message.author} Command: rps({choice})')
    choices = ['rock', 'paper', 'scissors']
    botChoice = choices[random.randint(0, 2)]
    embedRPS = discord.Embed(color=0x0000ff, title='rock, paper, scissors')
    embedRPS.add_field(name='You', value=f'{choice}', inline=True)
    embedRPS.add_field(name='Bot', value=f'{botChoice}', inline=True)
    if choice == botChoice:
        embedRPS.add_field(name='result', value='You tied!', inline=False)
        logging.DEBUG(f'Player: {choice} Bot: {botChoice} Result: Tied')
        await ctx.send(embed=embedRPS)
    elif botChoice == 'rock' and choice == 'paper':
        embedRPS.add_field(name='result', value='You win!', inline=False)
        logging.DEBUG(f'Player: {choice} Bot: {botChoice} Result: Win')
        await ctx.send(embed=embedRPS)
    elif botChoice == 'paper' and choice == 'scissors':
        embedRPS.add_field(name='result', value='You win!', inline=False)
        logging.DEBUG(f'Player: {choice} Bot: {botChoice} Result: Win')
        await ctx.send(embed=embedRPS)
    elif botChoice == 'scissors' and choice == 'rock':
        embedRPS.add_field(name='result', value='You win!', inline=False)
        logging.DEBUG(f'Player: {choice} Bot: {botChoice} Result: Win')
        await ctx.send(embed=embedRPS)
    else:
        embedRPS.add_field(name='result', value='You lose!', inline=False)
        logging.DEBUG(f'Player: {choice} Bot: {botChoice} Result: Lose')
        await ctx.send(embed=embedRPS)

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
