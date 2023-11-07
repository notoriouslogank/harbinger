import os
import random
import sys
from datetime import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv

from helpers import getLog, getVer, mcswitch, timestamp

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")
VERSION = getVer()
COGS = ("cogs.test",)
sTime = datetime.now()  # Application launch time; used to calc delta()
purple = 0x884EA0


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
channel = bot.get_channel(CHANNEL)

@bot.event
async def setup_hook() -> None:
    for cog in COGS:
        print(cog)
        await bot.load_extension(cog)
    
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)


@bot.event
async def on_ready():
    """Print username and ID on successful login."""
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    timestamp()


@bot.command()
async def clear(ctx, amount=2):
    """Delete multiple messages at once.

    Args:
        amount (int, optional): The number of messages to clear; defaults to 1.
    """
    amount = amount + 1  # So that we don't just delete the same message over and over
    if amount > 101:
        await ctx.send("Cannot delete more than 100 messages.")
    else:
        await ctx.channel.purge(limit=amount)
        print(f"{ctx.message.author} cleared {amount} messages.")


@bot.command()
async def changelog(ctx):
    """View the changelog."""
    changelog = getLog()
    print("Getting changelog...")
    print(f"{changelog}")
    timestamp()
    await ctx.send(f"{changelog}")


@bot.command()
async def status(ctx):
    """Confirm connection status."""
    print(f"{bot.user} is online.")
    timestamp()
    await ctx.send(f"{bot.user} is online.")


@bot.command()
async def add(ctx, left: int, right: int):
    """Add two integers and return total.

    Args:
        left (int): first addend
        right (int): second addend
    """
    total = left + right
    print(f"Adding {left} and {right}.")
    print(f"Total = {total}")
    timestamp()
    await ctx.send(total)


@bot.command()
async def say(ctx, message: str):
    """Repeat the message received as an argument.

    Args:
        message (str): Text of the message to be said by the bot
    """
    print("BOT SAYS:")
    print(f"{message}")
    await ctx.channel.purge(limit=1)
    await ctx.send(message)


@bot.command()
async def roll(ctx, dice: str):
    """Roll NdN dice and return result(s).

    Args:
        dice (str): amount of n-sided dice to roll (NdN)
    """
    print("Rolling dice...")
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        await ctx.send("Format must be NdN!")
        return
    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    print(result)
    timestamp()
    await ctx.send(result)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Return datetime a member joined.

    Args:
        member (discord.Member): The name of the member to be looked up.
    """
    print(f"Join on {member.name}")
    timestamp()
    await ctx.send(f"{member.name} joined {discord.utils.format_dt(member.joined_at)}")


@bot.command()
async def info(ctx):
    """Returns detailed information about current bot version."""
    cTime = datetime.now()
    delta = cTime - sTime
    embedVar = discord.Embed(title="mcswitch", color=purple)
    embedVar.add_field(name="version", value=f"v{VERSION}", inline=True)
    embedVar.add_field(name="uptime", value=f"{delta}", inline=True)
    embedVar.add_field(name="author", value="notoriouslogank", inline=True)
    embedVar.add_field(
        name="source code", value="https://github.com/notoriouslogank/mcswitch"
    )
    print(f"info dumped")
    timestamp()
    await ctx.send(embed=embedVar)

@bot.command()
async def playing(ctx, game, field, value):
    """Create an embed with specific game information.

    Args:
        game (str): game you're playing
        field (str): name of data field you want to share (e.g.: IP, room code, etc.). Multiple words must be quoted.
        value (str): value of data field. Multiple words must be quoted.
    """
    embedGame = discord.Embed(title=game, color=purple)
    embedGame.add_field(name=f'{field}', value=f'{value}', inline=True)
    print(f'Playing {game}: {field}, {value}')
    timestamp()
    await ctx.send(embed=embedGame)


@bot.command()
async def ping(ctx):
    """Returns current network latency."""
    print(f"pinged")
    timestamp()
    await ctx.send("Current ping: {0}".format(round(bot.latency, 2)))


@bot.command()
async def uptime(ctx):
    """Returns the uptime of the current bot instance."""
    cTime = datetime.now()
    delta = cTime - sTime
    print(f"uptime: {delta}")
    timestamp()
    await ctx.send(f"Uptime: {delta}")


@bot.command()
async def shutdown(ctx):
    """Safely shutdown the bot instance."""
    embedShutdown = discord.Embed(
        title="Shutdown", color=0xFF0000, timestamp=datetime.now()
    )
    embedShutdown.add_field(name="user", value=f"{ctx.message.author}", inline=True)
    logging.warn(f"Shutting down!")
    print("Shutdown command received!")
    timestamp()
    await ctx.send(embed=embedShutdown)
    sys.exit()


@bot.command()
async def rps(ctx, choice: str):
    """Play a game of rock, paper, scissors.

    Args:
        choice (str): rock, paper, or scissors
    """
    print(f"played rps")
    timestamp()
    choices = ["rock", "paper", "scissors"]
    botChoice = choices[random.randint(0, 2)]
    embedRPS = discord.Embed(color=purple, title="rock, paper, scissors")
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
    """Passive-aggressively Google something.

    Args:
        query (str): string to be Googled
    """
    google = "https://google.com/search?q="
    search = google + query
    embed = discord.Embed(color=purple, title="LMGTFY")
    embed.description = f"[Here]({search}), let me Google that for you!"
    print(f"LMGTFY: {search}")
    timestamp()
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
    await send_dm(ctx=ctx, member=ctx.message.author, content=query)

def main():
    bot.run(TOKEN)
    
main()
