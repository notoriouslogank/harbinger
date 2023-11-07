from discord.ext import commands
from datetime import datetime
import subprocess
from datetime import datetime
import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv("TOKEN")
CHANNEL = getenv("CHANNEL")
COGS = ("cogs.moderation", "cogs.tools", "cogs.status")
sTime = datetime.now()
purple = 0x884EA0 # Should move this to .env

intents = discord.Intents.default()
intents.members = True
intents.message_content = True    
bot = commands.Bot(command_prefix="!", intents=intents)
channel = bot.get_channel(CHANNEL)

def mcswitch():
    result = subprocess.run(["sh", "./mc.sh"], shell=True, capture_output=True, text=True)
    print(result.stdout)

def getVer():
    with open('CHANGELOG.md', 'r') as f:
        changes = f.readlines()
        vLine = changes[6]
        version = vLine[4:9]
        return version

def getLog():
    with open('CHANGELOG.md', 'r') as f:
        changelog = f.readlines()
        return changelog
    
def timestamp():
    cTime = datetime.now()
    print(f'{cTime}')
    print(f'----------')

async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)
