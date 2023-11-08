import discord
from discord.ext import commands

from helpers import bot, getVer, purple # might be able to remove bot import

VERSION = getVer()
PURPLE = purple


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help command is online.")

    @commands.command()
    async def help(self, ctx):
        """Return help embed with command descriptions."""
        help_embed = discord.Embed(
            title="Command Help",
            description=f"Commands for bot v{VERSION}",
            color=PURPLE,
        )
        # MODERATION
        help_embed.add_field(
            name="!clear", value="Delete a number of messages.", inline=False
        )
        help_embed.add_field(
            name="!joined", value="Get datetime user joined.", inline=False
        )
        help_embed.add_field(name="!say", value="Send message as bot.", inline=False)
        help_embed.add_field(
            name="!playing", value="Embed and send game info to channel.", inline=False
        )
        # STATUS
        help_embed.add_field(
            name="!status", value="Confirm bot online and reachable.", inline=False
        )
        help_embed.add_field(
            name="!info", value="Get details about this bot.", inline=False
        )
        help_embed.add_field(name="!ping", value="Get network latency.", inline=False)
        help_embed.add_field(name="!uptime", value="Get bot uptime.", inline=False)
        help_embed.add_field(
            name="!shutdown", value="Gracefully shutdown the bot.", inline=False
        )
        # TOOLS
        help_embed.add_field(
            name="!lmgtfy", value="Let me Google that for you...", inline=False
        )
        help_embed.add_field(name="!add", value="Add two numbers.", inline=False)
        help_embed.add_field(name="!roll", value="Roll NdN dice.", inline=False)
        help_embed.add_field(
            name="!rps",
            value="Play rock, paper, scissors against the bot.",
            inline=False,
        )
        # OTHER
        help_embed.add_field(
            name="Need Help?",
            value="[Join the Bot-Dev Server](https://discord.gg/9zAW8DfV)",
            inline=False,
        )
        help_embed.set_footer(
            text=f"Requested by {ctx.author}>.", icon_url=ctx.author.avatar
        )

        await ctx.send(embed=help_embed)


async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
