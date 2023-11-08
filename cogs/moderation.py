import discord
from discord.ext import commands

from helpers import purple, timestamp


class Moderation(commands.Cog):
    """Commands to aid in server moderation.
    """
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int=2) -> None:
        """Delete a number of messages in channel.
        """
        amount = amount + 1
        if amount > 101:
            await ctx.send("Cannot delete more than 100 messages.")
        else:
            await ctx.channel.purge(limit=amount)
            print(f"{ctx.message.author} deleted {amount} messages.")

    @commands.command()
    async def joined(self, ctx: commands.Context, member: discord.Member):
        """Return join date for given user.iption_
        """
        joined = f"{member.name} joined on {discord.utils.format_dt(member.joined_at)}."
        print(f"{joined}")
        await ctx.send(f"{joined}")
        timestamp()

    @commands.command()
    async def say(self, ctx: commands.Context, message: str):
        """Send a str as the bot instance.
        """
        print(f"{ctx.message.author} made McSwitch say:")
        print(f"{message}")
        timestamp()
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{message}")

    @commands.command()
    async def playing(self, ctx: commands.Context, game: str, field: str, value: str):
        """Send embed to channel with game info.
        """
        embedPlaying = discord.Embed(title=game, color=purple)
        embedPlaying.add_field(name=f"{field}", value=f"{value}", inline=True)
        print(f"{ctx.message.author} is playing {game}: {field}, {value}")
        timestamp()
        await ctx.send(embed=embedPlaying)


async def setup(bot: commands.Bot) -> None:
    """Load cogs into bot proper.
    """
    await bot.add_cog(Moderation(bot))
