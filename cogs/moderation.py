from os import path

import discord
from discord.ext import commands

from utils.helpers import Helpers


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
        cmd = f'!clear({amount})'
        cmd_msg = f'Deleted {amount} messages.'
        amount = amount + 1
        if amount > 100:
            await ctx.send("Cannot delete more than 100 messages.")
        else:
            await ctx.channel.purge(limit=amount)
            print(f'{Helpers.timestamp(ctx.message.author, cmd, cmd_msg)}')
            
    @commands.command()
    async def joined(self, ctx: commands.Context, member: discord.Member):
        """Get user's join datetime."""
        joined = f"{member.name} joined on {discord.utils.format_dt(member.joined_at)}."
        print(f"{joined}")
        await ctx.send(f"{joined}")
        Helpers.timestamp()

    @commands.command()
    async def say(self, ctx: commands.Context, message: str):
        """Say message as bot."""
        print(f"{ctx.message.author} made McSwitch say:")
        print(f"{message}")
        Helpers.timestamp()
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{message}")

    @commands.command()
    async def playing(
        self, ctx: commands.Context, game="Minecraft", field="Server Address", value=""
    ):
        """Create game info embed."""
        embedPlaying = discord.Embed(title=game, color=Helpers.color1)
        if path.exists("ip.txt"):
            with open("ip.txt", "r") as f:
                ip = f.readline()
            embedPlaying.add_field(name=f"Server IP", value=f"{ip}")
            embedPlaying.add_field(name=f"Version", value="1.20.1")
            print(f"Printed Minecraft server info.")
        else:
            embedPlaying.add_field(name=f"{field}", value=f"{value}", inline=True)
            print(f"{ctx.message.author} is playing {game}: {field}, {value}")
            Helpers.timestamp()
        await ctx.send(embed=embedPlaying)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Moderation(bot))