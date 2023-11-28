import os
from configparser import ConfigParser
from datetime import datetime

import discord
from discord.ext import commands

from config.configure import Configure


class Harbinger:
    """Class for the main bot functions."""

    config_path = "config/config.ini"
    config = ConfigParser()
    config.read(config_path)
    server_dir = config["Server"]["server_dir"]
    startup_script = config["Server"]["startup_script"]
    server_public_ip = config["Server"]["server_public_ip"]
    rgb = config["Custom Color"]["rgb"]
    r, g, b = map(int, rgb.split())
    custom_color = discord.Color.from_rgb(int(r), int(g), int(b))

    cogs = "cogs.moderation", "cogs.status", "cogs.help", "cogs.tools", "cogs.minecraft"
    start_time = datetime.now()

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    bot.remove_command("help")

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def setup_hook() -> None:
        """Sequentially load cogs."""
        for cog in cogs:
            print(f"Loading {cog}...")
            await bot.load_extension(cog)
            print(f"Loaded {cog}.")

    def get_ver() -> str:
        """Check CHANGELOG.md for version info, return version string.

        Returns:
            str: Software version
        """
        with open("docs/CHANGELOG.md", "r") as f:
            changelog = f.readlines()
            version_line = changelog[6]
            version = version_line[4:9]
            return version

    def timestamp(user, cmd, cmd_msg) -> None:
        """Print timestamp and end-of-command separator."""
        current_time = datetime.now()
        print(f"++++\n{current_time}\nUSR| {user}\nCMD| {cmd}\nMSG| {cmd_msg}")

    def start() -> None:
        """Start the bot."""
        config = ConfigParser()
        config.read(Harbinger.config_path)
        token = config["Bot"]["token"]
        bot.run(token)

    async def send_dm(ctx, member: discord.Member, *, content) -> None:
        """Create a Direct Message channel with a given member."""
        channel = await member.create_dm()
        await channel.send(content)


bot = Harbinger.bot
cogs = Harbinger.cogs


def check_config():
    if os.path.exists("config/config.ini"):
        print("Config file found.")
    else:
        print("No config file found.")
#        if os.path.exists("config/start.conf"):
#            pass
#        else:
#            Configure.write_sh_config(Configure.python_config_file)
#    else:
#        Configure.write_py_config()
#        Configure.write_sh_config(Configure.python_config_file)


def main():
    check_config()
    #Harbinger.start()


if __name__ == "__main__":
    main()
    #check_config()
    #Harbinger.start()
=======
from configparser import ConfigParser
from datetime import datetime

import discord
from discord.ext import commands

config_path = "config/config.ini"
config = ConfigParser()
config.read(config_path)
    
class Harbinger:
    """Class for the main bot functions."""
    token = config["Bot"]["token"]
    server_dir = config["Paths"]["server_dir"]
    startup_script = config["Paths"]["startup_script"]
    r = config["Custom Color"]['r']
    g = config['Custom Color']['g']
    b = config['Custom Color']['b']
    
    custom_color = discord.Color.from_rgb(int(r), int(g), int(b))
    
    cogs = "cogs.moderation", "cogs.status", "cogs.help", "cogs.tools", "cogs.minecraft"
    sTime = datetime.now()

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    bot.remove_command("help")

    def __init__(self, bot):
        self.bot = bot
        sTime = datetime.now()

    @bot.event
    async def setup_hook() -> None:
        """Sequentially load cogs."""
        print(f"Loading cogs")
        for cog in cogs:
            await bot.load_extension(cog)


    def get_ver() -> str:
        """Check CHANGELOG.md for version info, return version string.

        Returns:
            str: Software version
        """
        with open("docs/CHANGELOG.md", "r") as f:
            changes = f.readlines()
            vLine = changes[6]
            version = vLine[4:9]
            return version

    def timestamp(user, cmd, cmd_msg):
        """Print timestamp and end-of-command separator."""
        nl = "\n"
        cTime = datetime.now()
        print(f"++++")
        print(f"{cTime}")
        print(f"USR| {user}")
        print(f"CMD| {cmd}")
        print(f"MSG| {cmd_msg}")

    def start():
        """Start the bot."""
        bot.run(Harbinger.token)

    async def send_dm(ctx, member: discord.Member, *, content):
        """Create a Direct Message channel with a given member."""
        channel = await member.create_dm()
        await channel.send(content)


bot = Harbinger.bot
cogs = Harbinger.cogs


def main():
    Harbinger.start()


if __name__ == "__main__":
    Harbinger.start()
