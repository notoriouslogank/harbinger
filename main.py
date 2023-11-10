import logging

from utils.helpers import Helpers

sTime = Helpers.sTime
bot = Helpers.bot
cogs = Helpers.cogs
bot.remove_command("help")


@bot.event
async def setup_hook() -> None:
    """Load cogs."""
    print(f"Loading cogs...")
    for cog in cogs:
        await bot.load_extension(cog)


def main():
    """Start the bot."""
    bot.run(Helpers.get_token())


main()
