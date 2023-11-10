from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

from utils.helpers import timestamp

load_dotenv()
color1 = 0x884EA0

class Moderation(commands.Cog):
    """Server moderation commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Cog online.")

    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int = 2) -> None:
        """Delete a number of messages in channel."""
        amount = amount + 1
        if amount > 101:
            await ctx.send("Cannot delete more than 100 messages.")
        else:
            await ctx.channel.purge(limit=amount)
            print(f"{ctx.message.author} deleted {amount} messages.")

    @commands.command()
    async def joined(self, ctx: commands.Context, member: discord.Member):
        """Get user's join datetime."""
        joined = f"{member.name} joined on {discord.utils.format_dt(member.joined_at)}."
        print(f"{joined}")
        await ctx.send(f"{joined}")
        timestamp()

    @commands.command()
    async def say(self, ctx: commands.Context, message: str):
        """Say message as bot."""
        print(f"{ctx.message.author} made McSwitch say:")
        print(f"{message}")
        timestamp()
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{message}")

    @commands.command()
    async def playing(self, ctx: commands.Context, game: str, field: str, value: str):
        """Create game info embed."""
        embedPlaying = discord.Embed(title=game, color=color1)
        embedPlaying.add_field(name=f"{field}", value=f"{value}", inline=True)
        print(f"{ctx.message.author} is playing {game}: {field}, {value}")
        timestamp()
        await ctx.send(embed=embedPlaying)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Moderation(bot))
