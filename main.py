import discord
import os
import logging
import random
import sys
import sched
import time
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
load_dotenv()

purple = '0x884ea0'



def getVer():
    with open("CHANGELOG.md", "r") as f:
        changes = f.readlines()
        vLine = changes[6]
        version = vLine[4:9]
        return version
    
def getLog():
    with open('CHANGELOG.md', 'r') as f:
        changelog = f.readlines()
        return changelog
    
TOKEN = os.getenv("TOKEN")
VERSION = getVer()
sTime = datetime.now()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(sTime)
    print("---------")

#@bot.command()
#async def remindme(ctx, message: str, time: str):
#    await ctx.send(f'I will remind you about {message} in {time}.')
#    scheduler = sched.scheduler(time.time, time.sleep)
#    scheduler.enter({time}, 1, {message})
#    scheduler.run


@bot.command()
async def changelog(ctx):
    changelog = getLog()
    print('Getting changelog...')
    print(f'{changelog}')
    print(f'{sTime}')
    print('---------')
    await ctx.send(f'{changelog}')
    

@bot.command()
async def status(ctx):
    print(f'{bot.user} is online.')
    print(f'{sTime}')
    print('---------')
    await ctx.send(f"{bot.user} is online.")


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def say(ctx, message: str):
    print('BOT SAYS:')
    await ctx.send(message)

@bot.command()
async def roll(ctx, dice: str):
    print('Rolling dice...')
    print(f'{sTime}')
    print('---------')
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        logging.warn(f"Bad format: {dice}")
        await ctx.send("Format must be NdN!")
        return
    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def joined(ctx, member: discord.Member):
    print('Joined....')
    print(f'{sTime}')
    print('---------')
    await ctx.send(f"{member.name} joined {discord.utils.format_dt(member.joined_at)}")


@bot.command()
async def info(ctx):
    cTime = datetime.now()
    delta = cTime - sTime
    embedVar = discord.Embed(title="mcswitch", color=purple)
    embedVar.add_field(name="version", value=f"v{VERSION}", inline=True)
    embedVar.add_field(name="uptime", value=f"{delta}", inline=True)
    embedVar.add_field(name="author", value="notoriouslogank", inline=True)
    embedVar.add_field(
        name="source code", value="https://github.com/notoriouslogank/mcswitch"
    )
    await ctx.send(embed=embedVar)


@bot.command()
async def ping(ctx):
    await ctx.send("Current ping: {0}".format(round(bot.latency, 2)))


@bot.command()
async def uptime(ctx):
    cTime = datetime.now()
    delta = cTime - sTime
    await ctx.send(f"Uptime: {delta}")


@bot.command()
async def shutdown(ctx):
    embedShutdown = discord.Embed(
        title="Shutdown", color=0xFF0000, timestamp=datetime.now()
    )
    embedShutdown.add_field(name="user", value=f"{ctx.message.author}", inline=True)
    logging.warn(f"Shutting down!")
    await ctx.send(embed=embedShutdown)
    sys.exit()


@bot.command()
async def mcstart(ctx):
    await os.system("sh mc.sh")
    print("Starting the server, maybe.")
    await ctx.send("Starting MC Server.")


@bot.command()
async def rps(ctx, choice):
    choices = ["rock", "paper", "scissors"]
    botChoice = choices[random.randint(0, 2)]
    embedRPS = discord.Embed(color=0x0000FF, title="rock, paper, scissors")
    embedRPS.add_field(name="You", value=f"{choice}", inline=True)
    embedRPS.add_field(name="Bot", value=f"{botChoice}", inline=True)
    if choice == botChoice:
        embedRPS.add_field(name="result", value="You tied!", inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == "rock" and choice == "paper":
        embedRPS.add_field(name="result", value="You win!", inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == "paper" and choice == "scissors":
        embedRPS.add_field(name="result", value="You win!", inline=False)
        await ctx.send(embed=embedRPS)
    elif botChoice == "scissors" and choice == "rock":
        embedRPS.add_field(name="result", value="You win!", inline=False)
        await ctx.send(embed=embedRPS)
    else:
        embedRPS.add_field(name="result", value="You lose!", inline=False)
        await ctx.send(embed=embedRPS)

@bot.command()
async def lmgtfy(ctx, query: str):
    google = 'https://google.com/search?q='
    search = google + query
    embed = discord.Embed()
    embed.description = f"[Here]({search}), let me Google that for you!"
    print(search)
    await ctx.send(embed=embed)

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
