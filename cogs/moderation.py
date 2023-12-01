from os import path

import discord
from discord.ext import commands

from harbinger import Harbinger

mod = Harbinger.moderator_role_id
deletion_time = Harbinger.d_time


class Moderation(commands.Cog):
    """Server moderation commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    @commands.has_role(mod)
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
    @commands.has_role(mod)
    async def serverinfo(self, ctx: commands.Context):
        """Create embeds containing server details and member information and send them to the channel."""
        cmd = "!serverinfo"
        cmd_msg = "Get details about the server."
        owner = str(ctx.guild.owner)
        guild_id = str(ctx.guild.id)
        member_count = str(ctx.guild.member_count)
        # icon = str(ctx.guild.icon_url)
        desc = ctx.guild.description

        embed = discord.Embed(
            title=ctx.guild.name + "Server Information",
            description=desc,
            color=Harbinger.custom_color,
        )
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=guild_id, inline=True)
        embed.add_field(name="Member Count", value=member_count, inline=True)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(embed=embed)

        members = []
        async for member in ctx.guild.fetch_members(limit=150):
            members_embed = discord.Embed(
                title=f"{member.display_name}",
                description=f"Status: {member.status}",
                color=member.color,
            )
            members_embed.add_field(name="Member Since: ", value=f"{member.joined_at}")
            members_embed.set_thumbnail(url=member.display_avatar.url)
            await ctx.send(embed=members_embed)

    @commands.command()
    @commands.has_role(mod)
    async def whois(self, ctx: commands.Context, member: discord.Member) -> None:
        """Get detailed information about given member.

        Args:
            member (discord.Member): Member to get info for (must be exact)
        """
        cmd = "!whois"
        cmd_msg = f"Got whois info for {member}."
        whois_embed = discord.Embed(
            title=f"{member.display_name}",
            description=f"{member.status}",
            color=member.color,
        )
        whois_embed.add_field(name="Roles:", value=f"{member.roles}")
        whois_embed.add_field(name="Joined:", value=f"{member.joined_at}", inline=True)
        whois_embed.set_image(url=member.display_avatar.url)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(embed=whois_embed)

    @commands.command()
    @commands.has_role(mod)
    async def say(self, ctx: commands.Context, *message: str) -> None:
        """Say message as bot."""
        cmd = f"!say({message})"
        string_message = ""
        for word in message:
            string_message = string_message + str(word) + " "
        content = string_message.strip()
        await ctx.channel.purge(limit=1)
        cmd_msg = f"Harbinger says: {content}"
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)
        await ctx.send(f"{content}")

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

    # ERRORS
    @clear.error
    async def clear_error(self, ctx, error) -> None:
        """Error raised when !clear command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: clear_error"
        cmd_msg = f"User does not have mod role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a moderator to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @say.error
    async def say_error(self, ctx, error):
        """Error raised when !say command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: say_error"
        cmd_msg = f"User does not have mod role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a moderator to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @whois.error
    async def whois_error(self, ctx, error):
        """Error raised when !whois command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: whois_error"
        cmd_msg = f"User does not have mod role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a moderator to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
        """Error raised when !serverinfo command fails

        Args:
            error (MissingRole): Raised if user does not have developer role.
        """
        cmd = f"ERROR: serverinfo_error"
        cmd_msg = f"User does not have mod role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("You must be a moderator to do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Moderation(bot))
