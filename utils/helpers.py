from datetime import datetime
from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

sTime = datetime.now()
load_dotenv()
token = getenv("TOKEN")
channel = getenv("CHANNEL")
cogs = getenv("COGS")
color1 = getenv("COLOR1")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# def startServer():
#    """Start the Minecraft server.
#    """
#    ssh = Connection('logank@mimir')
#    tmuxStart = ssh.run('tmux new -d -s server')
#    tmuxCd = ssh.run('tmux send -t server:0 "cd /home/logank/paper-test" C-m')
#    tmuxPaper = ssh.run('tmux send -t server:0 "./java.sh" C-m')


def getVer():
    """Return bot software version.

    Returns:
        version (str): software version
    """
    with open("docs/CHANGELOG.md", "r") as f:
        changes = f.readlines()
        vLine = changes[6]
        version = vLine[4:9]
        return version


def getLog():  # TODO: Replace this with embed function
    """Read CHANGELOG.md and return it as a string.

    Returns:
        changelog (str): a string containing CHANGELOG.md
    """
    with open("docs/CHANGELOG.md", "r") as f:
        changelog = f.readlines()
        return changelog


def timestamp():
    """Print timestamp and end-of-command separator."""
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
