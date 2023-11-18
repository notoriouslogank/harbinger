from os import path

import discord
from discord.ext import commands

from harbinger import Harbinger
from configparser import ConfigParser


class Moderation(commands.Cog):
    """Server moderation commands."""

    config_path = "config.ini"
    config = ConfigParser()
    config.read(config_path)

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int = 2) -> None:
        """Delete a number of messages in channel."""
        cmd = f"!clear({amount})"
        cmd_msg = f"Deleted {amount} messages."
        amount = amount + 1
        if amount > 100:
            await ctx.send("Cannot delete more than 100 messages.")
        else:
            await ctx.channel.purge(limit=amount)
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def joined(self, ctx: commands.Context, member: discord.Member):
        """Get user's join datetime."""
        cmd = f"!joined({member})"
        cmd_msg = f"Got join data for: {member}."
        joined = f"{member.name} joined on {discord.utils.format_dt(member.joined_at)}."
        await ctx.send(f"{joined}")
        Harbinger.timestamp(ctx.author.message, cmd, cmd_msg)

    @commands.command()
    async def say(self, ctx: commands.Context, message: str):
        """Say message as bot."""
        cmd = f"!say({message})"
        cmd_msg = f"Harbinger says: {message}"
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{message}")

    @commands.command()  # Should probably break the automated message system out into its own functionality
    async def playing(
        self, ctx: commands.Context, game="Minecraft", field="Server Address", value=""
    ):
        """Create game info embed."""
        cmd = f"!playing({game}, {field}, {value})"
        cmd_msg = f"Created playing embed with these values: {game},{field},{value}"
        embedPlaying = discord.Embed(title=game, color=Harbinger.custom_color)
        if path.exists("ip.txt"):
            with open("ip.txt", "r") as f:
                ip = f.readline()
            embedPlaying.add_field(name=f"Server IP", value=f"{ip}")
            embedPlaying.add_field(name=f"Version", value="1.20.1")
        else:
            embedPlaying.add_field(name=f"{field}", value=f"{value}", inline=True)
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(embed=embedPlaying)

    @commands.command()
    async def server_info(self, ctx, ip):
        """Generate information about the Minecraft server."""
        embed_server_info = discord.Embed(
            title="Minecraft", color=Moderation.config["Bot"]["custom_color"]
        )
        embed_server_info.add_field(name="Server Address", value="127.0.0.1")
        embed_server_info.add_field(name="Version", value="1.20.2 I think")


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Moderation(bot))
