from sqlite3 import Timestamp
from discord.ext import commands

from os import listdir
from harbinger import Harbinger


class Dev(commands.Cog):
    version = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload_all(self, ctx):
        message = await ctx.send("Reloading cogs...")
        await ctx.message.delete()
        try:
            for cog in listdir("./cogs"):
                if cog.endswith(".py") == True:
                    await self.bot.reload_extension(f"cogs.{cog[:-3]}")
        except Exception as exc:
            await message.edit(content=f"An error has occured: {exc}", delete_after=20)
        else:
            await message.edit(content="All cogs have been reloaded.", delete_after=20)

    def check_cog(self, cog):
        if (cog.lower()).startswith("cogs.") == True:
            return cog.lower()
        return f"cogs.{cog.lower()}"

    @commands.command()
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        message = await ctx.send("Loading...")
        await ctx.message.delete()
        try:
            await self.bot.load_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(content=f"An erroor has occured: {exc}", delete_after=20)
        else:
            await message.edit(
                content=f"{self.check_cog(cog)} has been loaded.", delete_after=20
            )

    @commands.command()
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        message = await ctx.send("Unloading...")
        await ctx.message.delete()
        try:
            await self.bot.unload_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(content=f"An error has occured: {exc}", delete_after=20)
        else:
            await message.edit(
                content=f"{self.check_cog(cog)} has been unloaded.", delete_after=20
            )

    @commands.command()
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        message = await ctx.send("Reloading...")
        await ctx.message.delete()
        try:
            await self.bot.reload_extension(self.check_cog(cog))
        except Exception as exc:
            await message.edit(content=f"An error has occured: {exc}", delete_after=20)
        else:
            await message.edit(
                content=f"{self.check_cog(cog)} has been reloaded.", delete_after=20
            )

    @reload_all.error
    async def reload_all_error(self, ctx, error):
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=20)

    @reload_cog.error
    async def reload_cog_error(self, ctx, error):
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=20)

    @unload_cog.error
    async def unload_cog_error(self, ctx, error):
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=20)

    @load_cog.error
    async def load_cog_error(self, ctx, error):
        cmd = f"ERROR: UptimeError"
        cmd_msg = f"User does not have DEV role."
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        message = await ctx.send("Only the bot owner can do that!")
        await ctx.message.delete()
        if isinstance(error, commands.MissingRole):
            await message.edit(delete_after=20)


async def setup(bot):
    await bot.add_cog(Dev(bot))
