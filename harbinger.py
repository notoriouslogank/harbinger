from configparser import ConfigParser
from datetime import datetime

import subprocess
import discord
from discord.ext import commands

config_path = "config.ini"
config = ConfigParser()
config.read(config_path)    

class harbinger:
    token = config["Bot"]["token"]
    channel = config["Bot"]["channel"]
    mc_host = config["Server"]['mc_host']
    custom_color = config["Bot"]["custom_color"]

    cogs = "cogs.moderation", "cogs.status", "cogs.help", "cogs.tools"
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
        print(f"Loading cogs")
        for cog in cogs:
            await bot.load_extension(cog)

    def get_token():
        token = config["Bot"]["token"]
        return token

    def get_mc_host():
        mc_host = config["Server"]["mc_host"]
        return mc_host

    def get_channel():
        channel = config["Bot"]["channel"]
        return channel

    def get_ver():
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
        bot.run(harbinger.get_token())

    async def send_dm(ctx, member: discord.Member, *, content):
        """Create a Direct Message channel with a given member."""
        channel = await member.create_dm()
        await channel.send(content)


bot = harbinger.bot
cogs = harbinger.cogs


def main():
    try:
        subprocess.run(['tmux', 'new', '-d', '-s', 'harbinger'])
        subprocess.run(['tmux', 'a', '-t', 'harbinger:0'])
    except Exception:
        print('oops')
        
    harbinger.start()
    # TODO: create a tmux session for the Minecraft server as well


if __name__ == "__main__":
    harbinger.start()
