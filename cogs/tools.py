from random import randint

import discord
from discord.ext import commands

from utils.helpers import Helpers
from utils.serverAgent import *

bot = Helpers.bot
color1 = Helpers.color1


class Tools(commands.Cog):
    """Commands containing various tools/utilites."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def switch(self, ctx: commands.Context, state="on"):
        """Bot command to start the remote Minecraft server.

        Args:
            state (str, optional): Switch the server 'on' or 'off'. Defaults to "on".
        """
        cmd = f"!switch({state})"
        if state == "on":
            cmd_msg = "attempting to start server"
            Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
            await ctx.channel.send("Attempting to start the server...")
            try:
                ServerAgent.start_server()
                ip = Helpers.get_public_ip()
                await ctx.channel.send("Server is online.")
                await Helpers.embed_server(ctx=ctx, ip=ip)
                Helpers.cleanup()
            except:
                await ctx.channel.send("ERROR: 666")
        elif state == "off":
            cmd_msg = "stopping server"
            Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
            try:
                ServerAgent.stop_server()
                await ctx.channel.send("Server is stopping...")
            except:
                await ctx.channel.send("ERROR: 667")
        else:
            cmd_msg = "ERROR: Invalid choice"
            Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
            await ctx.channel.send("Invalid Syntax!")
            await ctx.channel.send("!switch <on|off>")

    @commands.command()
    async def commandMc(self, ctx: commands.Context, command: str):
        """Send an arbitrary Minecraft server command to the server.

        Args:
            command (str): Command to send to the server
        """
        cmd = f"!commandMc({command})"
        cmd_msg = f"sent command {command} to server"
        ServerAgent.command_server()
        Helpers.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def lmgtfy(self, ctx: commands.Context, query: str):
        """Let Me Google That For You"""
        cmd = f"!lmgtfy({query})"
        google = "https://google.com/search?q="
        search = google + query
#        embed = discord.Embed(color=color1, title="Let Me Google That for You")
#        embed.description = f"{search}"
        cmd_msg = f"url: {search}"
        Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.channel.purge(limit=1)
#        await ctx.send(embed=embed)
        await ctx.channel.send('Here, let me Google that for you!', mention_author=True)
        await ctx.channel.send(f'{search}', mention_author=True)
        await Helpers.send_dm(ctx=ctx, member=ctx.message.author, content={search})

    @commands.command()
    async def define(self, ctx: commands.Context, word: str):
        """Get the Meriam-Webster definition of a word.

        Args:
            word (str): the word to be defined
        """
        cmd = f"!define({word})"
        dictionary = "https://www.merriam-webster.com/dictionary/"
        define_url = dictionary + word
        cmd_msg = f"url: {define_url}"
        Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f'{define_url}')
        await Helpers.send_dm(ctx=ctx, member=ctx.message.author, content=define_url)

    @commands.command()
    async def add(self, ctx: commands.Context, left: int, right: int):
        """Adds two integers and returns result as message."""
        cmd = f"!add({left} {right})"
        total = left + right
        cmd_msg = f"total: {total}"
        Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{total}")

    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):
        """Roll NdN dice and get results."""
        cmd = f"!roll({dice})"
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.send("Format must be NdN!")
            return
        result = ", ".join(str(randint(1, limit)) for r in range(rolls))
        cmd_msg = f"rolled {dice}; result: {result}"
        Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{result}")

    @commands.command()
    async def rps(self, ctx: commands.Context, choice: str):
        """Play rock, paper, scissors against the bot."""
        cmd = f"!rps(choice)"
        cmd_msg = f"choice: {choice}"
        Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
        choices = ["rock", "paper", "scissors"]
        botChoice = choices[randint(0, 2)]
        embedRPS = discord.Embed(color=color1, title="rock, paper, scissors")
        embedRPS.add_field(name="You", value=f"{choice}", inline=True)
        embedRPS.add_field(name="Bot", value=f"{botChoice}", inline=True)
        if choice == botChoice:
            embedRPS.add_field(name="result", value="You tied!", inline=False)
            await ctx.send(embed=embedRPS)
        elif botChoice == "rock" and choice == "paper":
            embedRPS.add_field(name="result", value="You win!", inline=False)
            await ctx.send(embed=embedRPS)
        elif botChoice == "paper" and choice == "scissors":
            embedRPS.add_field(name="result", value="You win!", inline=False)
            await ctx.send(embed=embedRPS)
        elif botChoice == "scissors" and choice == "rock":
            embedRPS.add_field(name="result", value="You win!", inline=False)
            await ctx.send(embed=embedRPS)
        elif choice not in choices:
            await ctx.send("Please choose rock, paper, or scissors.")
        else:
            embedRPS.add_field(name="result", value="You lose!", inline=False)
            await ctx.send(embed=embedRPS)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Tools(bot))
