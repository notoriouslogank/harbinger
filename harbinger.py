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
        print(f"++++\n{current_time}\nUSR| {user}\nCMD| {cmd}\nMSG| {cmd_msg}\n++++")

    def start() -> None:
        """Start the bot."""
        bot.run(TOKEN)

    def is_admin(self, ctx: commands.Context, member: discord.Member) -> bool:
        roles = member.roles
        admin = discord.Guild.get_role(ctx.guild, MODERATOR)
        if admin in roles:
            return True
        else:
            return False

    def is_dev(self, ctx: commands.Context, member: discord.Member) -> bool:
        roles = member.roles
        dev = discord.Guild.get_role(ctx.guild, DEVELOPER)
        if dev in roles:
            return True
        else:
            return False

    async def send_dm(ctx, member: discord.Member, *, content) -> None:
        """Create a Direct Message channel with a given member."""
        channel = await member.create_dm()
        await channel.send(content)


bot = Harbinger.bot


def main():
    Harbinger.start()


if __name__ == "__main__":
    main()
