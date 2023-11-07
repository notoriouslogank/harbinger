import helpers

bot = helpers.bot
TOKEN = helpers.TOKEN
CHANNEL = helpers.CHANNEL
COGS = helpers.COGS

@bot.event
async def setup_hook() -> None:
    for cog in COGS:
        print(cog)
        await bot.load_extension(cog)
    
def main():
    bot.run(TOKEN)
    
main()
