import datetime
import os
import subprocess
import tarfile
from time import sleep
from shutil import make_archive

import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()
SERVER_PUBLIC_IP = configs.server_public_ip()
SERVER_STARTUP_SCRIPT = configs.startup_script()
SERVER_DIR = configs.server_dir()
# BACKUP_DIR = configs.backup_dir()
LOG_NAME = r"logs/latest.log"
fname = os.path.join(SERVER_DIR, LOG_NAME)
bot = Harbinger.bot


class Minecraft(commands.Cog):
    """Class of commands for the Minecraft server."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def get_cmd_stdout(self):
        """Print final line of latest.log (simulating STDOUT).

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

    def start_server(self):
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

    def save_all(self):
        subprocess.run(["tmux", "send", "-t", "Harbinger.1", "save-all", "ENTER"])

    def stop_server(self):
        subprocess.run(["tmux", "send", "-t", "Harbinger.1", "stop", "ENTER"])

    @commands.command()
    async def backmc(self, ctx: commands.Context):
        filename = datetime.datetime.strftime(datetime.datetime.now(), f"%d%m%Y-%H%M")
        await ctx.channel.purge(limit=1)
        self.save_all()
        message = await ctx.channel.send(
            "The Minecraft server will be shutting down in 30s for server backup.  Please save and disconnect to avoid and lost progress..."
        )
        sleep(30)
        # stop the server
        message.edit("Minecraft server shutting down NOW!")
        # await ctx.send("Shutting down Minecraft server NOW!")
        sleep(0.5)
        self.stop_server()
        sleep(10)
        # backup
        message.edit("Backing up server, please standby...", delete_after=30)
        # await ctx.send("Making server backup, please wait...")
        if os.path.exists(f"backups"):
            os.chdir("backups")
            make_archive(filename, "gztar", root_dir=SERVER_DIR)
            message.edit("Backup complete!")
        else:
            os.mkdir("backups")
            os.chdir("backups")
            make_archive(filename, "gztar", root_dir=SERVER_DIR)
            message.edit("Backup complete!")

        os.chdir("..")

        # start server
        startup_message = await ctx.send(f"Minecraft server starting up...")
        self.start_server()
        startup_message.edit("Minecraft server online.")

    @commands.command()
    async def startmc(self, ctx: commands.Context):
        """Start the Minecraft server."""
        cmd = f"!startmc"
        cmd_msg = f"Started Minecraft server."
        self.start_server()
        await ctx.send(f"Starting Minecraft server...")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

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
