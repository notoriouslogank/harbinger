import helpers

bot = helpers.bot
TOKEN = helpers.TOKEN
CHANNEL = helpers.CHANNEL
COGS = helpers.COGS

bot.remove_command('help')

@bot.event
async def setup_hook() -> None:
    """Loads cogs."""
    print(f"Loaded the following cogs: ")
    for cog in COGS:
        print(cog)
        await bot.load_extension(cog)


def main():
    """Start the bot."""
    bot.run(TOKEN)


main()
