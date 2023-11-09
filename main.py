from utils.helpers import bot, TOKEN, CHANNEL, COGS

bot = bot
token = TOKEN
channel = CHANNEL
cogs = COGS

bot.remove_command("help")


@bot.event
async def setup_hook() -> None:
    """Loads cogs."""
    print(f"Loaded the following cogs: ")
    for cog in cogs:
        print(cog)
        await bot.load_extension(cog)


def main():
    """Start the bot."""
    bot.run(token)


main()
