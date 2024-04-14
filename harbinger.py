import argparse
import subprocess
import sys
from datetime import datetime
from os import listdir

import discord
from discord.ext import commands

from config.configure import Configure
from config.read_configs import ReadConfigs as configs


def get_version():
    """Get Harbinger version."""
    with open("docs/CHANGELOG.md", "r") as f:
        changelog = f.readlines()
        version_line = changelog[6]
        version = version_line[4:9]
        print(f"Harbinger v{version}")


parser = argparse.ArgumentParser(prog="Harbinger", description="Harbinger Discord bot.")

parser.add_argument(
    "-c",
    "--configure",
    help="create configuration file(s) for Harbinger",
    action="store_true",
)

parser.add_argument(
    "-C",
    "--Configure",
    help="create configuration file(s) for Harbinger and launch Harbinger using new configuration",
    action="store_true",
)

parser.add_argument(
    "-s",
    "--show",
    help="show decrypted contents of configfile",
    action="store_true",
)

parser.add_argument(
    "-u",
    "--update",
    help="perform a git pull from the Harbinger repo (main branch)",
    action="store_true",
)

parser.add_argument(
    "-v",
    "--version",
    help="show version info",
    action="store_true",
)

args = parser.parse_args()

if args.update == True:
    subprocess.run(["git", "switch", "main"])
    subprocess.run(["git", "pull"])
    sys.exit()

if args.version == True:
    get_version()
    sys.exit()

if args.configure == True:
    Configure.check_config(
        keyfile="config/key.key", python_config_file="config/config.ini"
    )
    sys.exit()

if args.Configure == True:
    Configure.check_config(
        keyfile="config/key.key", python_config_file="config/config.ini"
    )


if args.show == True:
    print(
        f"Email Address: {configs.email_address()}\nEmail Password: {configs.email_password()}\nDiscord Token: {configs.discord_token()}\nDelete After: {configs.delete_time()}\nOwner ID: {configs.owner_id()}\nCustom Color: {configs.custom_color()}\nServer Directory: {configs.server_dir()}\nStartup Script: {configs.startup_script()}\nLocal IP: {configs.server_local_ip()}\nPublic IP: {configs.server_public_ip()}\nModerator Role ID: {configs.moderator_id()}\nDeveloper ID: {configs.developer_id()}"
    )
    sys.exit()

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
    async def on_member_join(member: discord.Member):
        """Elevate bot owner to dev and mod roles on join."""
        if member.id == configs.owner_id():
            mod = discord.utils.get(member.guild.roles, id=MODERATOR)
            dev = discord.utils.get(member.guild.roles, id=DEVELOPER)
            await member.add_roles(mod)
            await member.add_roles(dev)

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
