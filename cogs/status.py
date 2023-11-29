import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage

import discord
from discord.ext import commands

from config.configure import Configure
from harbinger import Harbinger
from random import randint

playing = [
    "with myself",
    "the synth",
    "bass",
    "with fire",
    "with my food",
    "games with my heart",
    "God",
    "Half Life 3",
    "Notepad",
    "grab ass with your mom",
    "knifey-stabby",
    "Find the Open Network Port",
]
listening = [
    "the screams of my enemies",
    "your phonecalls",
    "the voices",
    "complaints",
    "the national anthem",
    "some guy bloody ramble",
    "that new Olivia Rodrigo jam",
]
watching = [
    "you sleep",
    "my mouth",
    "the world burn",
    "you",
    "Star Trek probably",
    "the horror unfold",
    "you",
    "it all come crashing down",
    "from within the walls of your home",
    "in abject terror",
    "from the shadows",
    "your Internet traffic",
]

Watching = discord.Activity(
    type=discord.ActivityType.watching,
    name=f"{watching[randint(0, (len(watching)-1))]}",
)
Playing = discord.Game(playing[randint(0, (len(playing) - 1))])
Listening = discord.Activity(
    type=discord.ActivityType.listening,
    name=f"{listening[randint(0, (len(listening)-1))]}",
)

presences = [Watching, Playing, Listening]


def get_presence():
    """Randomly select a bot presence from the lists.

    Returns:
        obj: An activity object to set bot activity status.
    """
    presence = presences[randint(0, (len(presences) - 1))]
    return presence


status = presences[randint(0, (len(presences) - 1))]


class Status(commands.Cog):
    """Commands to find out status of bot services."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Confirm bot is logged in."""
        await self.bot.change_presence(activity=get_presence())
        Harbinger.timestamp("BOT", "INITIALIZE", "BOT IS ONLINE")

    @commands.command()
    async def status(self, ctx: commands.Context) -> None:
        """Confirm bot is online and reachable."""
        cmd = "!status"
        cmd_msg = "Status: online."
        status_msg = f"{self.bot.user} is online."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{status_msg}")

    @commands.command()
    async def info(self, ctx: commands.Context) -> None:
        """Get information about this bot."""
        cmd = "!info"
        cmd_msg = f"Sent info embed to channel {ctx.channel.id}"
        current_version = Harbinger.get_ver()
        current_time = datetime.now()
        delta = current_time - Harbinger.start_time
        embedInfo = discord.Embed(title="Harbinger", color=Harbinger.custom_color)
        embedInfo.add_field(name="version", value=f"v{current_version}", inline=True)
        embedInfo.add_field(name="uptime", value=f"{delta}", inline=True)
        embedInfo.add_field(name="author", value="notoriouslogank", inline=True)
        embedInfo.add_field(
            name="source code",
            value="https://github.com/notoriouslogank/Harbinger",
            inline=False,
        )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(embed=embedInfo)

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """Check network latency."""
        ping = (round(self.bot.latency, 2)) * 1000
        cmd = f"!ping"
        cmd_msg = "Pong!"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"Pong! ({ping} ms)")

    @commands.command()
    async def uptime(self, ctx: commands.Context) -> None:
        """Get bot uptime."""
        cmd = "!uptime"
        current_time = datetime.now()
        delta = current_time - Harbinger.start_time
        up_msg = f"uptime: {delta}"
        cmd_msg = f"{up_msg}"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{up_msg}")

    @commands.command()
    async def changelog(self, ctx: commands.Context) -> None:  # TODO: Fix this (again)
        """Get changelog."""
        cmd = "!changelog"
        cmd_msg = f"Uploaded CHANGELOG.md to channel."
        file = discord.File(fp="docs/CHANGELOG.md", filename="CHANGELOG.md")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(file=file)

    @commands.command()
    async def bug(self, ctx: commands.Context, message) -> None:
        cmd = "!bug"
        cmd_msg = f"Sent bug report."
        email_address = Harbinger.email_address
        password = Harbinger.email_pass
        email = EmailMessage()
        email["From"] = "Harbinger"
        email["To"] = email_address
        email["Subject"] = f"BUG REPORT - {ctx.message.author}"
        email.set_content(message)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email_address, password)
            smtp.send_message(email)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(
            "Thank you for submitting a bug report.\nIf you'd like to keep abreast of updates/bugfixes, please check out https://github.com/notoriouslogank/harbinger"
        )

    @commands.command()
    async def bug(self, ctx: commands.Context, message) -> None:
        cmd = "!bug"
        cmd_msg = f"Sent bug report."
        email_address = Harbinger.email_address
        password = Harbinger.email_pass
        email = EmailMessage()
        email["From"] = "Harbinger"
        email["To"] = email_address
        email["Subject"] = f"BUG REPORT - {ctx.message.author}"
        email.set_content(message)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email_address, password)
            smtp.send_message(email)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(
            "Thank you for submitting a bug report.\nIf you'd like to keep abreast of updates/bugfixes, please check out https://github.com/notoriouslogank/harbinger"
        )

    @commands.command()
    async def shutdown(self, ctx: commands.Context) -> None:
        """Gracefully shutdown the bot."""
        cmd = "!shutdown"
        cmd_msg = f"Shutting down..."
        embedShutdown = discord.Embed(
            title="shutdown", color=0xFF0000, timestamp=datetime.now()
        )
        embedShutdown.add_field(name="user", value=f"{ctx.message.author}", inline=True)
        await ctx.send(embed=embedShutdown)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        sys.exit()


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Status(bot))
