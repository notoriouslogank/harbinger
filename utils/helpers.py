from datetime import datetime
from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

class Helpers:
    sTime = datetime.now()

    cogs = "cogs.moderation", "cogs.status", "cogs.help", "cogs.tools"
    color1 = 0x884EA0
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    def __init__(self, bot):
        self.bot = bot
        sTime = datetime.now()
        load_dotenv()
        
    def get_token():
        token = getenv("TOKEN")
        return token
    
    def get_channel():
        channel = getenv("CHANNEL")
        return channel
    
    def get_mc_host():
        mc_host = getenv("MC_HOST")
        return mc_host
    
    def getVer():
        """Return bot software version.

        Returns:
            version (str): software version
        """
        with open("docs/CHANGELOG.md", "r") as f:
            changes = f.readlines()
            vLine = changes[6]
            version = vLine[4:9]
            print(f"Current version: {version}")
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
