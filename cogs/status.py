import sys
from datetime import datetime

import discord
from discord.ext import commands

from harbinger import harbinger

bot = harbinger.bot
currentVersion = harbinger.get_ver()


class Status(commands.Cog):
    """Commands to find out status of bot services."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Confirm bot is logged in."""
        harbinger.timestamp("BOT", "INITIALIZE", "BOT IS ONLINE")

    @commands.command()
    async def status(self, ctx: commands.Context):
        """Confirm bot is online and reachable."""
        cmd = "!status"
        cmd_msg = "Status: online."
        status_msg = f"{bot.user} is online."
        harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{status_msg}")

    @commands.command()
    async def info(self, ctx: commands.Context):
        """Get information about this bot."""
        cmd = "!info"
        cmd_msg = f"Sent info embed to channel {ctx.channel.id}"
        cTime = datetime.now()
        delta = cTime - harbinger.sTime
        embedInfo = discord.Embed(title="harbinger", color=0x884EA0)
        embedInfo.add_field(name="version", value=f"v{currentVersion}", inline=True)
        embedInfo.add_field(name="uptime", value=f"{delta}", inline=True)
        embedInfo.add_field(name="author", value="notoriouslogank", inline=True)
        embedInfo.add_field(
            name="source code",
            value="https://github.com/notoriouslogank/harbinger",
            inline=False,
        )
        harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(embed=embedInfo)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Check network latency."""
        ping = (round(self.bot.latency, 2)) * 1000
        cmd = f"!ping"
        cmd_msg = "Pong!"
        harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"Pong! ({ping} ms)")

    @commands.command()
    async def uptime(self, ctx: commands.Context):
        """Get bot uptime."""
        cmd = "!uptime"
        cTime = datetime.now()
        delta = cTime - harbinger.sTime
        up_msg = f"uptime: {delta}"
        cmd_msg = f"{up_msg}"
        harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{up_msg}")

    @commands.command()
    async def changelog(self, ctx: commands.Context):  # TODO: Fix this (again)
        """Get changelog."""
        cmd = "!changelog"
        cmd_msg = f"Uploaded CHANGELOG.md to channel."
        file = discord.File(fp="docs/CHANGELOG.md", filename="CHANGELOG.md")
        harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(file=file)

    @commands.command()
    async def shutdown(self, ctx: commands.Context):
        """Gracefully shutdown the bot."""
        cmd = "!shutdown"
        cmd_msg = f"Shutting down..."
        embedShutdown = discord.Embed(
            title="shutdown", color=0xFF0000, timestamp=datetime.now()
        )
        embedShutdown.add_field(name="user", value=f"{ctx.message.author}", inline=True)
        await ctx.send(embed=embedShutdown)
        harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        sys.exit()


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Status(bot))
