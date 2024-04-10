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

    @commands.command()
    async def mc(self, ctx: commands.Context, command: str) -> None:
        """Send an arbitrary command to the Minecraft server.

        Args:
            command (str): Command to send to the server.
        """
        cmd = f"!mccmd({command})"
        cmd_msg = f"Sent following command to server: {command}"
        mccommand = subprocess.run(
            ["tmux", "send", "-t", "Harbinger.1", f"{command}", "C-m"],
            stdout=subprocess.PIPE,
            text=True,
        )
        print(mccommand.stdout)
        # await ctx.send(f"Sending command: {command} to server...")
        # await ctx.send(f"{mccommand.stdout}")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


"""     def create_embed(version):
        Create an embed with the Minecraft server information.

        Args:
            version (str): The Minecraft version of the current server instance.

        Returns:
            embed: An embed object containing the Minecraft server version and IP address.

        minecraft_embed = discord.Embed(title="Minecraft", description=f"{version}")
        minecraft_embed.add_field(name="Server Address", value=f"{SERVER_PUBLIC_IP}")
        return minecraft_embed

    @commands.command()
    async def switch(self, ctx: commands.Context, state="on"):
        Toggle the state of the Minecraft server.

        Args:
            state (str, optional): Whether to turn the server on or off. Defaults to "on".

        cmd = f"!switch({state})"
        cmd_msg = f"Switched Minecraft server {state}."
        embed = Minecraft.create_embed("v1.20.1")
        if state == "on":
            subprocess.run(
                [
                    "tmux",
                    "send",
                    "-t",
                    "harbinger:0",
                    f"zsh {SERVER_STARTUP_SCRIPT}",
                    "C-m",
                ]
            )
            await ctx.send("Server is starting...")
            await ctx.send(embed=embed)
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        elif state == "off":
            subprocess.run(["tmux", "send", "-t", "harbinger:1", "/stop", "C-m"])
            await ctx.send("Stopping server...")
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        else:
            await ctx.send("Invalid argument.")


 """


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(Minecraft(bot))
