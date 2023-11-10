from random import randint

import discord
from discord.ext import commands

from utils import serverAgent
from utils.helpers import Helpers

bot = Helpers.bot
color1 = Helpers.color1

class Tools(commands.Cog):
    """Commands containing various tools/utilites."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Tools Cog online.")

    @commands.command()
    async def switch(self, ctx: commands.Context, state="on"):
        """Bot command to start the remote Minecraft server.

        Args:
            state (str, optional): Switch the server 'on' or 'off'. Defaults to "on".
        """
        if state == "on":
            print("Attempting to start the server.")
            await ctx.channel.send("Attempting to start the server...")
            try:
                serverAgent.startServer()
                await ctx.channel.send("Server is running...")
            except:
                await ctx.channel.send("Some kind of error.")
        elif state == "off":
            print("Attempting to stop the server...")
            try:
                serverAgent.stopServer()
                await ctx.channel.send("Server is stopping...")
            except:
                await ctx.channel.send("Some kind of error.")
        else:
            await ctx.channel.send("Invalid Syntax!")
            await ctx.channel.send("!switch <on|off>")

    @commands.command()
    async def commandMc(self, ctx: commands.Context, command: str):
        """Send an arbitrary Minecraft server command to the server.

        Args:
            command (str): Command to send to the server
        """
        serverAgent.commandServer(command)
        print(f"{ctx.author} sent {command} to the minecraft server.")

    @commands.command()
    async def lmgtfy(self, ctx: commands.Context, query: str):
        """Let Me Google That For You"""
        google = "https://google.com/search?q="
        search = google + query
        embed = discord.Embed(color=Helpers.get_color(), title="LMGTFY")
        embed.description = f"[Here]({search}), let me Google that for you!"
        print(f"LMGTFY: {search}")
        Helpers.timestamp()
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
        await Helpers.send_dm(ctx=ctx, member=ctx.message.author, content=query)

    @commands.command()
    async def define(self, ctx: commands.Context, word: str):
        """Get the Meriam-Webster definition of a word.

        Args:
            word (str): the word to be defined
        """
        dictionary = "https://www.merriam-webster.com/dictionary/"
        define_url = dictionary + word
        embed = discord.Embed(color=color1, title=f"Define: {word}")
        embed.description = f"[{word}]({define_url})"
        print(f"Define: {word}: {define_url}")
        Helpers.timestamp()
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
        await Helpers.send_dm(ctx=ctx, member=ctx.message.author, content=define_url)

    @commands.command()
    async def add(self, ctx: commands.Context, left: int, right: int):
        """Adds two integers and returns result as message."""
        total = left + right
        print(f"{left} + {right} = {total}")
        Helpers.timestamp()
        await ctx.send(f"{total}")

    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):
        """Roll NdN dice and get results."""
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.send("Format must be NdN!")
            return
        result = ", ".join(str(randint(1, limit)) for r in range(rolls))
        print(f"Roll: {result}")
        Helpers.timestamp()
        await ctx.send(f"{result}")

    @commands.command()
    async def rps(self, ctx: commands.Context, choice: str):
        """Play rock, paper, scissors against the bot."""
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
