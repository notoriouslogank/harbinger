import configparser
from datetime import datetime

import discord
from discord.ext import commands

config_path = "config.ini"
config = configparser.ConfigParser()
config.read(config_path)

token = config["Bot"]["token"]
print(token)


class harbinger:
    cogs = "cogs.moderation", "cogs.status", "cogs.help", "cogs.tools"
    custom_color = 0x884EA0
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
        token = config['Bot']['token']
        return token

    def get_mc_host():
        mc_host = config['Server']['mc_host']
        return mc_host

    def get_channel():
        channel = config['Bot']['channel']
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
    harbinger.start()
    # TODO: create a tmux session for the Minecraft server as well


if __name__ == "__main__":
    harbinger.start()
