from datetime import datetime
from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TOKEN")
CHANNEL = getenv("CHANNEL")
COGS = ("cogs.moderation", "cogs.tools", "cogs.status")
sTime = datetime.now()
purple = 0x884EA0  # Should move this to .env

help_command = commands.DefaultHelpCommand(show_parameter_description=False)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=help_command)
channel = bot.get_channel(CHANNEL)


def getVer():
    """Return bot software version.

    Returns:
        version (str): software version
    """
    with open("CHANGELOG.md", "r") as f:
        changes = f.readlines()
        vLine = changes[6]
        version = vLine[4:9]
        return version


def getLog():
    """Read CHANGELOG.md and return it as a string.

    Returns:
        changelog (str): a string containing CHANGELOG.md
    """
    with open("CHANGELOG.md", "r") as f:
        changelog = f.readlines()
        return changelog


def timestamp():
    """Print current timestamp of command and end-of-command signifier."""
    cTime = datetime.now()
    print(f"{cTime}")
    print(f"----------")


async def send_dm(ctx, member: discord.Member, *, content):
    """Create a Direct Message channel with a given member.

    Args:
        member (discord.Member): the member who invoked the command
        content (str): content of the DM
    """
    channel = await member.create_dm()
    await channel.send(content)
