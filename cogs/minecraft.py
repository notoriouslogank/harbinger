import os
import subprocess
from datetime import date
from time import sleep

import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()
SERVER_PUBLIC_IP = configs.server_public_ip()
SERVER_STARTUP_SCRIPT = configs.startup_script()
SERVER_DIR = configs.server_dir()
LOG_NAME = r"logs/latest.log"
fname = os.path.join(SERVER_DIR, LOG_NAME)
bot = Harbinger.bot


class Minecraft(commands.Cog):
    """Class of commands for the Minecraft server."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def get_cmd_stdout(self):
        """Parse and return final line of latest.log (simulating STDOUT).

        Returns:
            str: Final line of log file
        """
        with open(fname) as f:
            for line in f:
                pass
            last_line = line
            return last_line

    def get_mc_version(self) -> str:
        """Retrieve Minecraft client version from log file.

        Returns:
            str: Minecraft client version
        """
        with open(fname) as f:
            line = f.readlines()
            version = line[3]
            return version[-7:-1]

    @commands.command()
    async def startmc(self, ctx: commands.Context):
        """Start the Minecraft server."""
        cmd = f"!startmc"
        cmd_msg = f"Started Minecraft server."
        subprocess.run(
            [
                "tmux",
                "send",
                "-t",
                "Harbinger.1",
                f"zsh {SERVER_STARTUP_SCRIPT}",
                "ENTER",
            ]
        )
        await ctx.send(f"Starting Minecraft server...")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def backupmc(self, ctx: commands.Context) -> None:
        cmd = f"!backupmc"
        cmd_msg = f"Backing up Minecraft server data."
        backup_30 = "Server will shutdown in 30 seconds to backup files.  Please disconnect or you will be kicked."
        backup_20 = "Server will shutdown in 20 seconds to backup files.  Please disconnect or you will be kicked."
        backup_10 = "Server will shutdown in 10 seconds to backup files.  Please disconnect or you will be kicked."
        await ctx.channel.purge(limit=1)
        await ctx.send(message=backup_30)
        sleep(10)
        await ctx.channel.purge(limit=1)
        await ctx.send(message=backup_20)
        sleep(10)
        await ctx.channel.purge(limit=1)
        await ctx.send(message=backup_10)
        sleep(10)
        await ctx.channel.purge(limit=1)
        await ctx.send(message=f"Minecraft server saving and shutting down...")
        subprocess.run(["tmux", "send", "-t", "Harbinger.1", f"stop", "ENTER"])
        filename = date.today()
        await ctx.channel.purge(limit=1)
        await ctx.channel.send("Creating server backup, please standby.")
        subprocess.run(
            [
                "tmux",
                "send",
                "-t",
                "Harbinger.1",
                f"tar -czvf ../{filename}.tar.gz {SERVER_DIR}",
            ]
        )
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(
            message=f"Successfully created server backup: ../{filename}.tar.gz"
        )
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    # tar -czvf backup_date.tar.gz /[path]/

    @commands.command()
    async def mc(self, ctx: commands.Context, command=None) -> None:
        """Send an arbitrary command to the Minecraft server.

        Args:
            command (str): Command to send to the server.
        """
        cmd = f"!mccmd({command})"
        cmd_msg = f"Sent following command to server: {command}"
        if command == None:
            mc_embed = discord.Embed(
                title="Minecraft Server",
                description="",
                color=CUSTOM_COLOR,
            )
            mc_embed.add_field(
                name="Client Version", value=f"``{self.get_mc_version()}``"
            )
            mc_embed.add_field(name="Server Address", value=f"``{SERVER_PUBLIC_IP}``")
            await ctx.send(embed=mc_embed)
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        else:
            subprocess.run(
                ["tmux", "send", "-t", "Harbinger.1", f"{command}", "C-m"],
            )
            await ctx.channel.purge(limit=1)
            await ctx.send(f"``> {command}``")
            stdout = self.get_cmd_stdout()
            await ctx.send(f"``{stdout}``")
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(Minecraft(bot))
