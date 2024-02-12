from datetime import datetime
from os import listdir

import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs

TOKEN = configs.discord_token()
OWNER = configs.owner_id()
MODERATOR = configs.moderator_id()
DEVELOPER = configs.developer_id()


class Harbinger:
    """Class for the main bot functions."""

    start_time = datetime.now()

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(
        command_prefix="!", owner_id=OWNER, intents=intents, help_command=None
    )

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def setup_hook() -> None:
        """Sequentially load cogs."""
        print(f"Loading cogs...")
        for cog in listdir("cogs"):
            if cog.endswith(".py") == True:
                try:
                    await bot.load_extension(f"cogs.{cog[:-3]}")
                    print(f"Loaded {cog}")
                except Exception as exc:
                    print(f"An error has occured: {exc}.")

    @bot.event
    async def on_member_join(member:discord.Member, ctx):
        channel = ctx.channel
        role = discord.utils.get(member.guild.roles, id=MODERATOR)
        if member.id == configs.owner_id():
            await member.add_roles(role)
        else:
            await channel.send(f"{member} joined the server.")

    def get_ver() -> str:
        """Check CHANGELOG.md for version info, return version string.

        Returns:
            str: Software version
        """
        with open("docs/CHANGELOG.md", "r") as f:
            changelog = f.readlines()
            version_line = changelog[6]
            version = version_line[4:9]
            return version

    def timestamp(user, cmd, cmd_msg) -> None:
        """Print timestamp and end-of-command separator."""
        current_time = datetime.now()
        print(f"++++\n{current_time}\nUSR| {user}\nCMD| {cmd}\nMSG| {cmd_msg}")

    def start() -> None:
        """Start the bot."""
        bot.run(TOKEN)

    def is_admin(self, ctx: commands.Context, member: discord.Member) -> bool:
        """Check whether user has admin role.

        Args:
            member (discord.Member): User to check

        Returns:
            bool: True if user has admin role; False if not
        """
        roles = member.roles
        admin = discord.Guild.get_role(ctx.guild, MODERATOR)
        if admin in roles:
            return True
        else:
            return False

    def is_dev(self, ctx: commands.Context, member: discord.Member) -> bool:
        """Check whether user has dev role.

        Args:
            member (discord.Member): User to check

        Returns:
            bool: True of user has dev role; False if not
        """
        roles = member.roles
        dev = discord.Guild.get_role(ctx.guild, DEVELOPER)
        if dev in roles:
            return True
        else:
            return False

    async def send_dm(ctx, member: discord.Member, *, content: str) -> None:
        """Send a DM to a given user.

        Args:
            member (discord.Member): User to send DM.
            content (str): Message to send.
        """
        channel = await member.create_dm()
        await channel.send(content)



if __name__ == "__main__":
    bot = Harbinger.bot
    Harbinger.start()
