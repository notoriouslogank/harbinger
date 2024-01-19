import subprocess
from os import listdir
from discord import Client

from discord.ext import commands


from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

DELETION_TIME = configs.delete_time()

channel = 1183811931920932984

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload_all(self, ctx):
        """Reloads all cogs in the cogs directory."""
        await ctx.channel.purge(limit=1)
        cmd = "!reload_all"
        if Harbinger.is_dev(self, ctx, ctx.message.author) == True:
            cmd_msg = "Reloaded all cogs."
            message = await ctx.send("Reloading cogs...")
            try:
                for cog in listdir("./cogs"):
                    if cog.endswith(".py") == True:
                        await self.bot.reload_extension(f"cogs.{cog[:-3]}")
            except Exception as exc:
                cmd_msg = f"ERROR: Unable to reload cogs."
                await message.edit(
                    content=f"An error has occured: {exc}", delete_after=DELETION_TIME
                )
            else:
                await message.edit(
                    content="All cogs have been reloaded.", delete_after=DELETION_TIME
                )
        else:
            cmd_msg = "ERROR: Missing dev role."
            await ctx.send(
                "You must have dev role to execute this command.",
                delete_after=DELETION_TIME,
            )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    async def get_bot_channel(self):
        bot_channel = Client.get_channel(self.bot, channel)
        return bot_channel
        
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
    async def load_cog(self, ctx, *, cog: str) -> None:
        """Load a given (unloaded) cog.

        Args:
            cog (str): The name of the cog to be loaded
        """
        await ctx.channel.purge(limit=1)
        cmd = "!load_cog"
        if Harbinger.is_dev(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Loaded cog: {cog}"
            message = await ctx.send("Loading...")
            try:
                await self.bot.load_extension(self.check_cog(cog))
            except Exception as exc:
                cmd_msg = f"ERROR: Unable to load cog {cog}"
                await message.edit(
                    content=f"An error has occured: {exc}", delete_after=DELETION_TIME
                )
            else:
                await message.edit(
                    content=f"{self.check_cog(cog)} has been loaded.",
                    delete_after=DELETION_TIME,
                )
        else:
            cmd_msg = "ERROR: Missing dev role."
            await ctx.send(
                "You must have dev role to execute this command.",
                delete_after=DELETION_TIME,
            )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def unload_cog(self, ctx, *, cog: str) -> None:
        """Unload a given cog.

        Args:
            cog (str): The cog to be unloaded
        """
        cmd = "!unload_cog"
        await ctx.channel.purge(limi=1)
        if Harbinger.is_dev(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Unloaded cog: {cog}"
            message = await ctx.send("Unloading...")
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
        else:
            cmd_msg = "ERROR: Missing dev role."
            await ctx.send(
                "You must have dev role to execute this command.",
                delete_after=DELETION_TIME,
            )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def reload_cog(self, ctx, *, cog: str) -> None:
        """Reload a given cog.

        Args:
        cog (str): The cog to be reloaded
        """
        cmd = "!reload_cog"
        await ctx.channel.purge(limit=1)
        if Harbinger.is_dev(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Reloaded cog: {cog}"
            message = await ctx.send("Reloading...")
            try:
                await self.bot.reload_extension(self.check_cog(cog))
            except Exception as exc:
                await message.edit(
                    content=f"An error has occured: {exc}", delete_after=DELETION_TIME
                )
            else:
                await message.edit(
                    content=f"{self.check_cog(cog)} has been reloaded.",
                    delete_after=DELETION_TIME,
                )
        else:
            cmd_msg = "ERROR: Missing dev role."
        await ctx.send(
            "You must have dev role to execute this command.",
            delete_after=DELETION_TIME,
        )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def update(self, ctx):
        """Performs a git pull against the Harbinger repository."""
        cmd = "!update"
        await ctx.channel.purge(limit=1)
        if Harbinger.is_dev(self, ctx, ctx.message.author) == True:
            cmd_msg = "Pulled from GitHub."
            channel = await self.get_bot_channel()
            message = await channel.send("Checking GitHub for updates...")
            subprocess.run(["git", "pull"])
            await message.edit(
                content=f"Bot is now on version {Harbinger.get_ver()}",
                delete_after=DELETION_TIME,
            )
        else:
            cmd_msg = "ERROR: Missing dev role."
            await ctx.send(
                "You must have dev role to execute this command.",
                delete_after=DELETION_TIME,
            )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load the cog into the bot."""
    await bot.add_cog(Dev(bot))
