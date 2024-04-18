from datetime import date

import discord
from discord.ext import commands
from assets import urls

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()
source_code = urls.SOURCE_CODE
issues = urls.ISSUES
footer = urls.FOOTER


class Release(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.version = Harbinger.get_ver()

    def release_embed(self, text):
        embed = discord.Embed(
            title="Harbinger: Release Notes",
            description=f"v{self.version}",
            color=CUSTOM_COLOR,
        )
        embed.add_field(name="Released", value=f"{date.today()}")
        embed.add_field(
            name="What's New",
            value=f"{text}\nTo view the full changelog for this release, run ``!changelog``",
            inline=False,
        )
        embed.add_field(name="Source Code", value=f"{source_code}", inline=False)
        embed.add_field(name="Report a Bug", value=f"{issues}", inline=False)
        embed.set_footer(text=f"{footer}")
        return embed

    @commands.command()
    async def release(self, ctx: commands.Context, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=self.release_embed(text))


async def setup(bot):
    await bot.add_cog(Release(bot))
