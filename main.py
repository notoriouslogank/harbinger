import logging
from utils.helpers import Helpers

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)

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
