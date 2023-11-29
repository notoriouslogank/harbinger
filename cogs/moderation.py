from os import path

import discord
from discord.ext import commands

from harbinger import Harbinger


class Moderation(commands.Cog):
    """Server moderation commands."""

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
    async def serverinfo(self, ctx: commands.Context):
        cmd = "!serverinfo"
        cmd_msg = "Get details about the server."
        owner = str(ctx.guild.owner)
        #        region = str(ctx.guild.region)
        guild_id = str(ctx.guild.id)
        member_count = str(ctx.guild.member_count)
        # icon = str(ctx.guild.icon_url)
        desc = ctx.guild.description

        embed = discord.Embed(
            title=ctx.guild.name + "Server Information",
            description=desc,
            color=Harbinger.custom_color,
        )
        # embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=guild_id, inline=True)
        #        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=member_count, inline=True)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(embed=embed)

        members = []
        async for member in ctx.guild.fetch_members(limit=150):
            members_embed = discord.Embed(
                title=f"{member.display_name}",
                description=f"Status: {member.status}",
                color=member.accent_color,
            )
            members_embed.add_field(name="Member Since: ", value=f"{member.joined_at}")
            members_embed.set_thumbnail(member.avatar)
            await ctx.send(embed=members_embed)
            # await ctx.send(
            #    "Name : {}\t Status : {}\n Joined at {}".format(
            #        member.display_name, str(member.status), str(member.joined_at)
            #    )
            # )

    @commands.command()
    async def joined(self, ctx: commands.Context, member: discord.Member) -> None:
        """Get user's join datetime."""
        cmd = f"!joined({member})"
        cmd_msg = f"Got join data for: {member}."
        joined = f"{member.name} joined on {discord.utils.format_dt(member.joined_at)}."
        await ctx.send(f"{joined}")
        Harbinger.timestamp(ctx.author.message, cmd, cmd_msg)

    @commands.command()
    async def say(self, ctx: commands.Context, message: str) -> None:
        """Say message as bot."""
        cmd = f"!say({message})"
        cmd_msg = f"Harbinger says: {message}"
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{message}")

    @commands.command()
    async def playing(
        self, ctx: commands.Context, game, description, field, value
    ) -> None:
        """Create game info embed."""
        cmd = f"!playing({game}, {field}, {value})"
        cmd_msg = f"Created playing embed with these values: {game},{field},{value}"
        custom_color = Harbinger.custom_color
        playing_embed = discord.Embed(title=f"{game}", description=f"{description}")
        playing_embed.add_field(name=f"{field}", value=f"{value}")
        await ctx.send(embed=playing_embed)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Moderation(bot))
