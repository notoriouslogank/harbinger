from discord.ext import commands
from helpers import timestamp

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def clear(self, ctx: commands.Context, amount=2) -> None:
        amount = amount + 1
        if amount > 101:
            await ctx.send("Cannot delete more than 100 messages.")
        else:
            await ctx.channel.purge(limit=amount)
            print(f'{ctx.message.author} deleted {amount} messages.')
            timestamp()
            
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Moderation(bot))