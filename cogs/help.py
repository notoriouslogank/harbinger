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
        help_embed = discord.Embed(title='Help Desk', description=f"All commands for mcswitch v{VERSION}", color={purple})
        help_embed.set_author(name="mcswitch", icon_url=self.bot.avatar)
        # MODERATION
        help_embed.add_field(name="clear", value="Deletes a specified amount of messages.", inline=False)
        help_embed.add_field(name="joined", value="Get datetime when member joined.", inline=False)
        help_embed.add_field(name="say", value="Send message to channel as mcswitch.", inline=False)
        help_embed.add_field(name="playing", value="Create and send embed with game info (eg, IP address, room code)", inline=False)
        # STATUS
        # TOOLS
        # OTHER
        help_embed.add_field(name="Need Help?", value="[Join the Bot-Dev Server](https://discord.gg/9zAW8DfV)", inline=False)
        help_embed.set_footer(text=f'Requested by <@{ctx.author}>.', icon_url=ctx.author.avatar)
        
        await ctx.send(embed=help_embed)
        
async def setup(bot):
    await bot.add_cog(HelpCommand(bot))