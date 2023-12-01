import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage
from random import randint

import discord
from discord.ext import commands

from harbinger import Harbinger

dev = Harbinger.developer_role_id
deletion_time = Harbinger.d_time

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
    "dead",
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
    @commands.has_role(dev)
    async def up(self, ctx: commands.Context) -> None:
        """Confirm bot is online and reachable."""
        cmd = "!up"
        cmd_msg = "Status: online."
        up_msg = f"{self.bot.user} is online."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send(f"{up_msg}")
        await ctx.message.delete()
        await message.edit(delete_after=deletion_time)

    @commands.command()
    @commands.has_role(dev)
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
    @commands.has_role(dev)
    async def ping(self, ctx: commands.Context) -> None:
        """Check network latency."""
        ping = (round(self.bot.latency, 2)) * 1000
        cmd = f"!ping"
        cmd_msg = "Pong!"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send(f"Pong! ({ping} ms)")
        await ctx.message.delete()
        await message.edit(delete_after=deletion_time)

    @commands.command()
    @commands.has_role(dev)
    async def uptime(self, ctx: commands.Context) -> None:
        """Get bot uptime."""
        cmd = "!uptime"
        current_time = datetime.now()
        delta = current_time - Harbinger.start_time
        up_msg = f"uptime: {delta}"
        cmd_msg = f"{up_msg}"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send(f"{up_msg}")
        await ctx.message.delete()
        await message.edit(delete_after=deletion_time)

    @commands.command()
    @commands.has_role(dev)
    async def changelog(self, ctx: commands.Context) -> None:  # TODO: Fix this (again)
        """Get changelog."""
        cmd = "!changelog"
        cmd_msg = f"Uploaded CHANGELOG.md to channel."
        file = discord.File(fp="docs/CHANGELOG.md", filename="CHANGELOG.md")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send(file=file)
        await ctx.message.delete()
        await message.edit(delete_after=deletion_time)

    @commands.command()
    async def bug(self, ctx: commands.Context, *raw_message: str) -> None:
        """Generate and email a bug report to the bot maintainer."""
        cmd = f"!bug {raw_message}"
        cmd_msg = f"Sent bug report."
        message = ""
        for word in raw_message:
            message = message + str(word) + " "
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
    @commands.has_role(dev)
    async def shutdown(self, ctx: commands.Context) -> None:
        """Gracefully shutdown the bot."""
        cmd = "!shutdown"
        cmd_msg = f"Shutting down..."
        embedShutdown = discord.Embed(
            title="shutdown", color=0xFF0000, timestamp=datetime.now()
        )
        embedShutdown.add_field(name="user", value=f"{ctx.message.author}", inline=True)
        message = await ctx.send(embed=embedShutdown)
        await ctx.message.delete()
        await message.edit(f"Goodbye!", delete_after=deletion_time)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        sys.exit()

    # ERRORS
    @up.error
    async def up_error(self, ctx, error):
        """Error raised when !up command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: UpError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a developer to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @info.error
    async def info_error(self, ctx, error):
        """Error raised when !info command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: InfoError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a developer to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @ping.error
    async def ping_error(self, ctx, error):
        """Error raised when !ping command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: PingError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a developer to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @uptime.error
    async def uptime_error(self, ctx, error):
        """Error raised when !uptime command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a developer to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @shutdown.error
    async def shutdown_error(self, ctx, error):
        """Error raised when !shutdown command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a developer to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Status(bot))
