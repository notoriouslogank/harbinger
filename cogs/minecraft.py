import discord
from discord.ext import commands
from harbinger import Harbinger
import subprocess

bot = Harbinger.bot
custom_color = Harbinger.custom_color


class Minecraft(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def switch(self, ctx: commands.Context, state="on"):
        startup_script = Harbinger.startup_script
        if state == "on":
            subprocess.run(["tmux", "send", "-t", "harbinger:0", "zsh", f"{startup_script}", "C-m"])
            await ctx.send("Server is starting...")
        elif state == "off":
            subprocess.run(["tmux", "send", "-t", "harbinger:0", "stop", "C-m"])
            await ctx.send("Stopping server...")
        else:
            await ctx.send("Invalid argument.")

    @commands.command()
    async def mccmd(self, ctx: commands.Context, command):
        subprocess.run(["tmux", "send", "-t", "harbinger:0", f"{command}", "C-m"])
        await ctx.send(f"Sending command: {command} to server...")


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(Minecraft(bot))
