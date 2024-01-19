import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage
from random import randint
from time import sleep

import discord
from config.read_configs import ReadConfigs as configs
from discord.ext import commands
from harbinger import Harbinger


DELETION_TIME = configs.delete_time()
EMAIL_ADDRESS = configs.email_address()
EMAIL_PASSWORD = configs.email_password()
CUSTOM_COLOR = configs.custom_color()
BOT_CHANNEL = configs.bot_channel()

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
        presence: An activity object to set bot activity status.
    """
    presence = presences[randint(0, (len(presences) - 1))]
    return presence


status = presences[randint(0, (len(presences) - 1))]


class Status(commands.Cog):
    """Commands to find out status of bot services."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def get_bot_channel(self):
        bot_channel = discord.Client.get_channel(self.bot, BOT_CHANNEL)
        return bot_channel

    async def get_bot_author(self):
        bot_author = discord.Client.get_user(self.bot, 1154559282801549384)
        return bot_author

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Confirm bot is logged in."""
        await self.bot.change_presence(activity=get_presence())
        Harbinger.timestamp("BOT", "INITIALIZE", "BOT IS ONLINE")

    @commands.Cog.listener()
    async def on_message(self, ctx: commands.Context) -> None:
        """Logs all messages to bot-subscribed channels to stdout."""
        if ctx.author == self.bot.user:
            return
        username = str(ctx.author)
        user_message = str(ctx.content)
        channel = str(ctx.channel)
        timestamp = datetime.now()
        print(f"++++\n{timestamp}\n{channel} || {username}: {user_message}")

    @commands.command()
    async def up(self, ctx: commands.Context) -> None:
        """Confirm bot is online and reachable."""
        cmd = "!up"
        await ctx.channel.purge(limit=1)
        cmd_msg = "Status: online."
        up_msg = f"{self.bot.user} is online."
        message = await ctx.send(f"{up_msg}")
        await message.edit(delete_after=DELETION_TIME)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def info(self, ctx: commands.Context) -> None:
        """Get information about this bot."""
        cmd = "!info"
        await ctx.channel.purge(limit=1)
        cmd_msg = f"Sent info embed to channel {ctx.channel.id}"
        author = await self.get_bot_author()
        current_version = Harbinger.get_ver()
        current_time = datetime.now()
        delta = current_time - Harbinger.start_time
        embedInfo = discord.Embed(
            title=f"Harbinger v{current_version}", color=CUSTOM_COLOR
        )
        embedInfo.add_field(name="uptime", value=f"``{delta}``", inline=True)
        embedInfo.add_field(name="author", value=f"{author}", inline=True)
        embedInfo.add_field(
            name="source code",
            value="https://github.com/notoriouslogank/Harbinger",
            inline=False,
        )
        await ctx.send(embed=embedInfo)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """Check network latency."""
        ping = (round(self.bot.latency, 2)) * 1000
        cmd = f"!ping"
        cmd_msg = "Pong!"
        channel = await self.get_bot_channel()
        message = await channel.send(f"Pong! ({ping} ms)")
        await message.edit(delete_after=DELETION_TIME)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def uptime(self, ctx: commands.Context) -> None:
        """Get bot uptime."""
        cmd = "!uptime"
        await ctx.channel.purge(limit=1)
        channel = await self.get_bot_channel()
        current_time = datetime.now()
        delta = current_time - Harbinger.start_time
        up_msg = f"uptime: {delta}"
        cmd_msg = f"{up_msg}"
        message = await channel.send(f"{up_msg}")
        await message.edit(delete_after=DELETION_TIME)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def changelog(self, ctx: commands.Context) -> None:
        """Send changelog to channel."""
        cmd = "!changelog"
        await ctx.channel.purge(limit=1)
        cmd_msg = f"Uploaded CHANGELOG.md to {ctx.channel}."
        file = discord.File(fp="docs/CHANGELOG.md", filename="CHANGELOG.md")
        await ctx.send(file=file)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def bug(self, ctx: commands.Context, *, message) -> None:
        """Generate and email a bug report to the bot maintainer."""
        cmd = f"!bug {message}"
        await ctx.channel.purge(limit=1)
        cmd_msg = f"Sent bug report."
        email = EmailMessage()
        email["From"] = "Harbinger"
        email["To"] = EMAIL_ADDRESS
        email["Subject"] = f"BUG REPORT - v{Harbinger.get_ver()} - {ctx.message.author}"
        email.set_content(message)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(email)
        await Harbinger.send_dm(
            ctx=ctx,
            member=ctx.message.author,
            content=f"Thanks for submitting a bug report!  Maybe it'll get fixed someday...",
        )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def shutdown(self, ctx: commands.Context) -> None:
        """Gracefully shutdown the bot."""
        cmd = "!shutdown"
        timestamp = datetime.now()
        await ctx.channel.purge(limit=1)
        if Harbinger.bot.is_owner(ctx.message.author):
            cmd_msg = f"Shutting down..."
            channel = await self.get_bot_channel()
            embedGooodbye = discord.Embed(
                title="Harbinger is offline!",
                description=f"Shutdown by {ctx.message.author} at {timestamp}.",
                color=CUSTOM_COLOR,
            )
            embedShutdown = discord.Embed(
                title="Shutdown!",
                description=f"Shutdown message recieved. Harbinger will shutdown in 5 seconds!",
                color=0xFF0000,
                timestamp=datetime.now(),
            )
            embedShutdown.add_field(
                name="user", value=f"{ctx.message.author}", inline=True
            )
            message = await channel.send(embed=embedShutdown)
            sleep(5)
            await message.edit(embed=embedGooodbye)
            sys.exit()
        else:
            cmd_msg = f"ERROR: Not bot owner."
            await ctx.send(
                "You must be the bot owner to execute that command.",
                delete_after=DELETION_TIME,
            )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Status(bot))
