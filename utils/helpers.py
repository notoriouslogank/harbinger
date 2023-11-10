from datetime import datetime
from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv


class Helpers:
    """Class to help integrate modules together.

    Methods
    -------
    get_token():
        Return the API token as a string.

    get_channel():
        Return the 'main' channel ID.

    get_mc_host():
        Returns Minecraft server hostname ({user@host})

    get_ver():
        Return the current version number from CHANGELOG.md.

    get_log():
        Return the changelog as a string.

    timestamp():
        Return a timestamp and end-of-message horizontal line.

    send_dm(ctx, member, *, content):
        Send a DM to a given user.
    """

    cogs = "cogs.moderation", "cogs.status", "cogs.help", "cogs.tools"
    color1 = 0x884EA0
    sTime = datetime.now()

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    def __init__(self, bot):
        """Gather parameters for bot."""
        self.bot = bot
        sTime = datetime.now()

    def get_token():
        """Get Discord API token from file.

        Returns:
            token (str): string containing the Discord API token
        """
        load_dotenv()
        token = str(getenv("TOKEN"))
        return token

    def get_channel():
        """Get channel ID number from file.

        Returns:
            channel (int): Discord channel ID number
        """
        channel = getenv("CHANNEL")
        return channel

    def get_mc_host():
        """Get Minecraft server hostname information from file.

        Returns:
            mc_host (str): the Minecraft server host information {user@hostname}
        """
        mc_host = str(getenv("MC_HOST"))
        return mc_host

    def get_ver():
        """Return bot software version.

        Returns:
            version (str): the current version information from CHANGELOG.md
        """
        with open("docs/CHANGELOG.md", "r") as f:
            changes = f.readlines()
            vLine = changes[6]
            version = vLine[4:9]
            print(f"Current version: {version}")
            return version

    def get_log():  # TODO: Replace this with embed function
        """Read CHANGELOG.md and return it as a string.

        Returns:
            changelog (str): the entire changelog as a string
        """
        with open("docs/CHANGELOG.md", "r") as f:
            changelog = f.readlines()
            return changelog

    def timestamp(user, cmd, cmd_msg):
        """Print timestamp and end-of-command separator."""
        nl = '\n'
        cTime = datetime.now()
        print(f'{cTime}:')
        print(f'USR: {user} CMD: {cmd}')
        print(f'CMD_MSG: {cmd_msg}')
            
    
    async def send_dm(ctx, member: discord.Member, *, content):
        """Create a Direct Message channel with a given member."""
        channel = await member.create_dm()
        await channel.send(content)
