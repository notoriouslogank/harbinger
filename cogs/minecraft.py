import discord
from discord.ext import commands
from harbinger import Harbinger
import subprocess

bot = Harbinger.bot
custom_color = Harbinger.custom_color


class Minecraft(commands.Cog):
    """Class of commands for the Minecraft server."""
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def switch(self, ctx: commands.Context, state="on"):
        """Toggle the state of the Minecraft server.

        Args:
            state (str, optional): Whether to turn the server on or off. Defaults to "on".
        """
        cmd = f'!switch({state})'
        cmd_msg = f'Switched Minecraft server {state}.'
        startup_script = Harbinger.startup_script
        if state == "on":
            subprocess.run(
                ["tmux", "send", "-t", "harbinger:0", f"zsh {startup_script}", "C-m"]
            )
            await ctx.send("Server is starting...")
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        elif state == "off":
            subprocess.run(["tmux", "send", "-t", "harbinger:0", "stop", "C-m"])
            await ctx.send("Stopping server...")
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        else:
            await ctx.send("Invalid argument.")
            

    @commands.command()
    async def mccmd(self, ctx: commands.Context, command: str) -> None:
        """Send an arbitrary command to the Minecraft server.

        Args:
            command (str): Command to send to the server.
        """
        cmd = f'!mccmd({command})'
        cmd_msg = f'Sent following command to server: {command}'
        subprocess.run(["tmux", "send", "-t", "harbinger:0", f"{command}", "C-m"])
        await ctx.send(f"Sending command: {command} to server...")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(Minecraft(bot))
