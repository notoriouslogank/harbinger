import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command()
    async def test(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            ctx.send(f'Hello, {member.name}!')
        else:
            ctx.send(f'Hello, {member.name}. This feels familiar...')
        self._last_member = member
        
def setup(bot):
    bot.add_cog(Test(bot))