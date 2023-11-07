import discord
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
            
    @commands.command()
    async def joined(self, ctx: commands.Context, member: discord.Member):
        joined = (f'{member.name} joined on {discord.utils.format_dt(member.joined_at)}.')
        print(f'{joined}')
        await ctx.send(f'{joined}')
        timestamp()
        
    @commands.command
    async def say(self, ctx: commands.Context, message: str):
        print(f"{ctx.message.author} made McSwitch say:")
        print(f'{message}')
        timestamp()
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{message}')
        
    @commands.command
    async def playing(self, ctx: commands.Context, game: str, field: str, value: any):
        embedPlaying = discord.Embed(title=game, color=purple)
        embedPlaying.add_field(name=f'{field}', value=f'{value}', inline=True)
        print(f'{ctx.message.author} is playing {game}: {field}, {value}')
        timestamp()
        await ctx.send(embed=embedPlaying)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Moderation(bot))