import subprocess
from os import listdir

from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

DELETION_TIME = configs.delete_time()
MODERATOR_ROLE_ID = configs.moderator_id()


class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(MODERATOR_ROLE_ID)
    async def reload_all(self, ctx):
        """Reloads all cogs in the cogs directory."""
        cmd = "!reload_all"
        cmd_msg = "Reloaded all cogs."
        message = await ctx.send("Reloading cogs...")
        await ctx.message.delete()
        try:
            for cog in listdir("./cogs"):
                if cog.endswith(".py") == True:
                    await self.bot.reload_extension(f"cogs.{cog[:-3]}")
        except Exception as exc:
            await message.edit(
                content=f"An error has occured: {exc}", delete_after=DELETION_TIME
            )
        else:
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await message.edit(
                content="All cogs have been reloaded.", delete_after=DELETION_TIME
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
    @commands.has_role(MODERATOR_ROLE_ID)
    async def load_cog(self, ctx, *, cog: str) -> None:
        """Load a given (unloaded) cog.

        Args:
            cog (str): The name of the cog to be loaded
        """
        cmd = "!load_cog"
        cmd_msg = f"Loaded cog: {cog}"
        message = await ctx.send("Loading...")
        await ctx.message.delete()
        try:
            await self.bot.load_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(
                content=f"An erroor has occured: {exc}", delete_after=DELETION_TIME
            )
        else:
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await message.edit(
                content=f"{self.check_cog(cog)} has been loaded.",
                delete_after=DELETION_TIME,
            )

    @commands.command()
    @commands.has_role(MODERATOR_ROLE_ID)
    async def unload_cog(self, ctx, *, cog: str) -> None:
        """Unload a given cog.

        Args:
            cog (str): The cog to be unloaded
        """
        cmd = "!unload_cog"
        cmd_msg = f"Unloaded cog: {cog}"
        message = await ctx.send("Unloading...")
        await ctx.message.delete()
        try:
            await self.bot.unload_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(
                content=f"An error has occured: {exc}", delete_after=DELETION_TIME
            )
        else:
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await message.edit(
                content=f"{self.check_cog(cog)} has been unloaded.",
                delete_after=DELETION_TIME,
            )

    @commands.command()
    @commands.has_role(MODERATOR_ROLE_ID)
    async def reload_cog(self, ctx, *, cog: str) -> None:
        """Reload a given cog.

        Args:
        cog (str): The cog to be reloaded
        """
        cmd = "!reload_cog"
        cmd_msg = f"Reloaded cog: {cog}"
        message = await ctx.send("Reloading...")
        await ctx.message.delete()
        try:
            await self.bot.reload_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(
                content=f"An error has occured: {exc}", delete_after=DELETION_TIME
            )
        else:
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await message.edit(
                content=f"{self.check_cog(cog)} has been reloaded.",
                delete_after=DELETION_TIME,
            )

    @commands.command()
    @commands.has_role(MODERATOR_ROLE_ID)
    async def update(self, ctx):
        cmd = "!update"
        cmd_msg = "Pulled from GitHub."
        message = await ctx.send("Checking GitHub for updates...")
        await ctx.message.delete()
        subprocess.run(["git", "pull"])
        await message.edit(
            content=f"Bot is now on version {Harbinger.get_ver()}",
            delete_after=DELETION_TIME,
        )

    @reload_all.error
    async def reload_all_error(self, ctx, error) -> None:
        """Send message when !reload_all command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: ReloadAllError"
        cmd_msg = f"User is not bot owner."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=DELETION_TIME)

    @reload_cog.error
    async def reload_cog_error(self, ctx, error):
        """Send message when !reload_cog command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: ReloadCogError"
        cmd_msg = f"User is not bot owner."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=DELETION_TIME)

    @unload_cog.error
    async def unload_cog_error(self, ctx, error):
        """Send message when !unload_cog command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: UnloadCogError"
        cmd_msg = f"User is not bot owner."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=DELETION_TIME)

    @load_cog.error
    async def load_cog_error(self, ctx, error):
        """Send message when !load_cog command fails due to MissingRole.

        Args
            error (MissingRole): The exception raised
        """
        cmd = f"ERROR: LoadCogError"
        cmd_msg = f"User is not bot owner."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=DELETION_TIME)


async def setup(bot):
    """Load the cog into the bot."""
    await bot.add_cog(Dev(bot))
