import discord
from discord.ext import commands
from harbinger import Harbinger
import subprocess

bot = Harbinger.bot
color = Harbinger.custom_color


class Minecraft(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def switch(self, ctx: commands.Context, state="on"):
        if state == "on":
            subprocess.run("zsh ~/SERVER/run.sh")
            await ctx.send("Server is starting...")
        elif state == "off":
            subprocess.run('tmux -t harbinger:0 "stop" C-m')
            await ctx.send("Stopping server...")
        else:
            await ctx.send("Invalid argument.")
