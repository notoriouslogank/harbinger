from discord.ext import commands

from os import listdir
from harbinger import Harbinger

deletion_time = Harbinger.d_time


class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload_all(self, ctx):
        """Reloads all cogs in the cogs directory."""
        message = await ctx.send("Reloading cogs...")
        await ctx.message.delete()
        try:
            for cog in listdir("./cogs"):
                if cog.endswith(".py") == True:
                    await self.bot.reload_extension(f"cogs.{cog[:-3]}")
        except Exception as exc:
            await message.edit(
                content=f"An error has occured: {exc}", delete_after=deletion_time
            )
        else:
            await message.edit(
                content="All cogs have been reloaded.", delete_after=deletion_time
            )

    def check_cog(self, cog) -> str:
        """Correctly formats the cog name.

        Args:
            cog (str): The cog name to be formatted

        Returns:
            str: Correctly formatted cog name
        """
        if (cog.lower()).startswith("cogs.") == True:
            return cog.lower()
        return f"cogs.{cog.lower()}"

    @commands.command()
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str) -> None:
        """Load a given (unloaded) cog.

        Args:
            cog (str): The name of the cog to be loaded
        """
        message = await ctx.send("Loading...")
        await ctx.message.delete()
        try:
            await self.bot.load_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(
                content=f"An erroor has occured: {exc}", delete_after=deletion_time
            )
        else:
            await message.edit(
                content=f"{self.check_cog(cog)} has been loaded.",
                delete_after=deletion_time,
            )

    @commands.command()
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str) -> None:
        """Unload a given cog.

        Args:
            cog (str): The cog to be unloaded
        """
        message = await ctx.send("Unloading...")
        await ctx.message.delete()
        try:
            await self.bot.unload_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(
                content=f"An error has occured: {exc}", delete_after=deletion_time
            )
        else:
            await message.edit(
                content=f"{self.check_cog(cog)} has been unloaded.",
                delete_after=deletion_time,
            )

    @commands.command()
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str) -> None:
        """Reload a given cog.

        Args:
        cog (str): The cog to be reloaded
        """
        message = await ctx.send("Reloading...")
        await ctx.message.delete()
        try:
            await self.bot.reload_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(
                content=f"An error has occured: {exc}", delete_after=deletion_time
            )
        else:
            await message.edit(
                content=f"{self.check_cog(cog)} has been reloaded.",
                delete_after=deletion_time,
            )

    @reload_all.error
    async def reload_all_error(self, ctx, error) -> None:
        """Send message when !reload_all command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @reload_cog.error
    async def reload_cog_error(self, ctx, error):
        """Send message when !reload_cog command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @unload_cog.error
    async def unload_cog_error(self, ctx, error):
        """Send message when !unload_cog command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)

    @load_cog.error
    async def load_cog_error(self, ctx, error):
        """Send message when !load_cog command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=deletion_time)


async def setup(bot):
    await bot.add_cog(Dev(bot))
