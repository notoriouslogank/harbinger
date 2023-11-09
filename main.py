from utils.helpers import CHANNEL, COGS, TOKEN, bot, timestamp

bot = bot
token = TOKEN
channel = CHANNEL
cogs = COGS

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
