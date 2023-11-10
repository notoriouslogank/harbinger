from utils.helpers import Helpers


sTime = Helpers.sTime
bot = Helpers.bot
bot.remove_command("help")
cogs = Helpers.cogs


@bot.event
async def setup_hook() -> None:
    """Loads cogs."""
    print(f"Loading cogs...")
    for cog in cogs:
        await bot.load_extension(cog)


def main():
    """Start the bot."""
    token = Helpers.get_token()
    print(token)
    bot.run(token)


main()
