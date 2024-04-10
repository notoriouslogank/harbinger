import subprocess

import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

SERVER_PUBLIC_IP = configs.server_public_ip()
SERVER_STARTUP_SCRIPT = configs.startup_script()

bot = Harbinger.bot


class Minecraft(commands.Cog):
    """Class of commands for the Minecraft server."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def mc(self, command):
        subprocess.run(["tmux", "send", "-t", "Harbinger.0", f"{command}", "ENTER"])


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(Minecraft(bot))
