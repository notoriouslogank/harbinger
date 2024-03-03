import discord
from discord.ext import commands
from harbinger import Harbinger
from config.read_configs import ReadConfigs as configs
from datetime import date

CUSTOM_COLOR = configs.custom_color()
source_code = "https://github.com/notoriouslogank/harbinger/releases"
issues = "https://github.com/notoriouslogank/harbinger/issues"
footer = "For information about new commands, say !help <command>."

class Release(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.version = Harbinger.get_ver()

    @commands.command()
    async def release(self, ctx, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=self.release_embed(ctx, text))

    def release_embed(self, ctx, text):
        embed = discord.Embed(title="Harbinger: Release Notes", description=f"v{self.version}", color=CUSTOM_COLOR)
        embed.add_field(name="Released", value=f"{date.today()}")
        embed.add_field(name="What's New", value=f"{text}\nTo view the full changelog for this release, run ``!changelog``", inline=False)
        embed.add_field(name="Source Code", value=f"{source_code}", inline=False)
        embed.add_field(name="Report a Bug", value=f"{issues}", inline=False)
        embed.set_footer(text=f"{footer}")
        return embed

async def setup(bot):
    await bot.add_cog(Release(bot))