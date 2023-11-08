import discord
from discord.ext import commands

from helpers import bot, getVer, purple

VERSION = getVer()
PURPLE = purple

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help command is online.')
        
    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(title='Help Desk', description=f"All commands for mcswitch v{VERSION}", color=PURPLE)
        # MODERATION
        help_embed.add_field(name="!clear <amount: int>", value="Delete <amount> of messages.", inline=False)
        help_embed.add_field(name="!joined <member: discord.Member>", value="Return <datetime> <member: discord.Member> joined.", inline=False)
        help_embed.add_field(name="!say <message: str>", value="Send <message: str> to channel as mcswitch.", inline=False)
        help_embed.add_field(name="!playing <game: str> <field1: str> <value1: str>", value="Create and send embed with <game: str> <field1: str> <field2: str>", inline=False)
        # STATUS
        help_embed.add_field(name="!status", value="Return confirmation if the bot is online and reachable.", inline=False)
        help_embed.add_field(name="!info", value="Return an embed with details about this bot.", inline=False)
        help_embed.add_field(name="!ping", value="Return network latency in ms.", inline=False)
        help_embed.add_field(name="!uptime", value="Return <time.delta> since bot instance was started.", inline=False)
        help_embed.add_field(name="!shutdown", value="Shutdown the bot and return an embed with information about <user> who invoked the command.", inline=False)
        # TOOLS
        help_embed.add_field(name="!lmgtfy <'*arg+*arg+*arg...'>", value="Let Me Google That For You", inline=False)
        help_embed.add_field(name="!add <num1> <num2>", value="Adds two integers and returns result as message.", inline=False)
        help_embed.add_field(name="!roll <NdN>", value="Roll <NdN> dice and return result(s) as message.", inline=False)
        help_embed.add_field(name="!rps <rock|paper|scissors>", value="Play rock, paper, scissors against the bot.", inline=False)        
        # OTHER
        help_embed.add_field(name="Need Help?", value="[Join the Bot-Dev Server](https://discord.gg/9zAW8DfV)", inline=False)
        help_embed.set_footer(text=f'Requested by {ctx.author}>.', icon_url=ctx.author.avatar)
        
        await ctx.send(embed=help_embed)
        
async def setup(bot):
    await bot.add_cog(HelpCommand(bot))