import discord
from discord.ext import commands

from utils.helpers import getVer, purple

VERSION = getVer()
PURPLE = purple


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog online.")
        

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
            name="!clear", value="Delete a number of messages.", inline=True
        )
        help_embed.add_field(
            name="!joined", value="Get datetime user joined.", inline=True
        )
        help_embed.add_field(name="!say", value="Send message as bot.", inline=True)
        help_embed.add_field(
            name="!playing", value="Embed and send game info to channel.", inline=True
        )
        # STATUS
        help_embed.add_field(
            name="!status", value="Confirm bot online and reachable.", inline=True
        )
        help_embed.add_field(
            name="!info", value="Get details about this bot.", inline=True
        )
        help_embed.add_field(name="!ping", value="Get network latency.", inline=True)
        help_embed.add_field(name="!uptime", value="Get bot uptime.", inline=True)
        help_embed.add_field(
            name="!shutdown", value="Gracefully shutdown the bot.", inline=True
        )
        # TOOLS
        help_embed.add_field(
            name="!define", value="Get the definition of a given word.", inline=True
        )
        help_embed.add_field(
            name="!lmgtfy", value="Let me Google that for you...", inline=True
        )
        help_embed.add_field(name="!add", value="Add two numbers.", inline=True)
        help_embed.add_field(name="!roll", value="Roll NdN dice.", inline=True)
        help_embed.add_field(
            name="!rps",
            value="Play rock, paper, scissors against the bot.",
            inline=True,
        )
        # OTHER
        help_embed.add_field(
            name="Need Help?",
            value="[Join the Bot-Dev Server](https://discord.gg/9zAW8DfV)",
            inline=True,
        )
        help_embed.add_field(
            name="Find a Problem?",
            value="[Submit a Bug Report](https://github.com/notoriouslogank/mcswitch/issues)",
            inline=True,
        )
        help_embed.set_footer(
            text=f"Requested by {ctx.author}>.", icon_url=ctx.author.avatar
        )

        await ctx.send(embed=help_embed)


async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
