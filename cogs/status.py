import sys
from datetime import datetime

import discord
from discord.ext import commands

from utils.helpers import Helpers

bot = Helpers.bot
currentVersion = Helpers.getVer()


class Status(commands.Cog):
    """Commands to find out status of bot services."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Confirm bot is logged in."""
        print("Status Cog online.")

    @commands.command()
    async def status(self, ctx: commands.Context):
        """Confirm bot is online and reachable."""
        status_msg = f"{bot.user} is online."
        print(f"{status_msg}")
        Helpers.timestamp()
        await ctx.send(f"{status_msg}")

    @commands.command()
    async def info(self, ctx: commands.Context):
        """Get information about this bot."""
        cTime = datetime.now()
        delta = cTime - Helpers.sTime
        embedInfo = discord.Embed(title="mcswitch", color=0x884EA0)
        embedInfo.add_field(name="version", value=f"v{currentVersion}", inline=True)
        embedInfo.add_field(name="uptime", value=f"{delta}", inline=True)
        embedInfo.add_field(name="author", value="notoriouslogank", inline=True)
        embedInfo.add_field(
            name="source code",
            value="https://github.com/notoriouslogank/mcswitch",
            inline=False,
        )
        print(f"info dumped")
        Helpers.timestamp()
        await ctx.send(embed=embedInfo)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Check network latency."""
        ping_msg = "Current ping: {0}".format(round(bot.latency, 2))
        print(f"{ping_msg}")
        Helpers.timestamp()
        await ctx.send(f"{ping_msg}")

    @commands.command()
    async def uptime(self, ctx: commands.Context):
        """Get bot uptime."""
        cTime = datetime.now()
        delta = cTime - Helpers.sTime
        up_msg = f"uptime: {delta}"
        print(f"{up_msg}")
        Helpers.timestamp()
        await ctx.send(f"{up_msg}")

    @commands.command()
    async def changelog(self, ctx: commands.Context):  # TODO: Fix this (again)
        """Get changelog."""
        file = discord.File(fp="docs/CHANGELOG.md", filename="CHANGELOG.md")
        await ctx.send(file=file)

    @commands.command()
    async def shutdown(self, ctx: commands.Context):
        """Gracefully shutdown the bot."""
        embedShutdown = discord.Embed(
            title="shutdown", color=0xFF0000, timestamp=datetime.now()
        )
        embedShutdown.add_field(name="user", value=f"{ctx.message.author}", inline=True)
        print(f"{ctx.message.author} initiated shutdown.")
        Helpers.timestamp()
        await ctx.send(embed=embedShutdown)
        sys.exit()


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Status(bot))
