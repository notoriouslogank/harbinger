from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass
    
    @commands.command()
    async def test(self, ctx: commands.Context) -> None:
        pass
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TestCog(bot))