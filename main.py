from os import getenv

from dotenv import load_dotenv

from utils import helpers, serverAgent


load_dotenv()
token = getenv("TOKEN")
channel = getenv("CHANNEL")
cogs = "cogs.help", "cogs.moderation", "cogs.status", "cogs.tools"
COLOR1 = getenv("COLOR1")
mc_host = getenv("MC_HOST")

bot = helpers.bot

bot.remove_command("help")

@bot.event
async def setup_hook() -> None:
    """Loads cogs."""
    print(f"Loading cogs...")
    for cog in cogs:
        await bot.load_extension(cog)


def main():
    """Start the bot."""
    bot.run(token)


main()
