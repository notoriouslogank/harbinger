from curses import keyname
import json
from pstats import SortKey
import aiohttp
from random import randint

import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()

bot = Harbinger.bot


class Tools(commands.Cog):
    """Commands containing various tools/utilites."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def lmgtfy(self, ctx: commands.Context, *query: str) -> None:
        """Let Me Google That For You"""
        cmd = f"!lmgtfy({query})"
        google = "https://google.com/search?q="
        string_query = ""
        for word in query:
            string_query = string_query + str(word) + " "
        sanitized_query = string_query.replace(" ", "+")
        search = google + sanitized_query
        cmd_msg = f"URL: {search}"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.channel.purge(limit=1)
        await ctx.send("Here, let me just Google that for you:")
        await ctx.send(search)
        await Harbinger.send_dm(ctx=ctx, member=ctx.message.author, content=search)

    @commands.command()
    async def define(self, ctx: commands.Context, word: str) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}') as resp:
                dict_entry = await resp.json()
                try:
                    pronunciation = dict_entry[0]["phonetics"][0]["audio"]
                except Exception:
                    pronunciation = ""
                try:
                    definition = dict_entry[0]["meanings"][0]["definitions"][0]["definition"]
                except:
                    await ctx.send(f"Error: Could not find definition for {word}.\nPlease check the spelling and try again.")
                try:
                    definition2 = dict_entry[0]["meanings"][1]["definitions"][0]["definition"]
                except Exception:
                    definition2 = None
                await ctx.message.delete()
                try:
                    phonetics = dict_entry[0]["phonetics"][0]["text"]
                except:
                    phonetics = None
                if pronunciation != "":
                    if phonetics != None:
                        embed = discord.Embed(title=f"**{word}**", description=f"[{phonetics}]({pronunciation})", color=CUSTOM_COLOR)
                    elif phonetics == None:
                        embed = discord.Embed(title=f"**{word}**", description=f"[Pronunciation]({pronunciation})")
                elif pronunciation == "":
                    if phonetics != None:
                        embed = discord.Embed(title=f"**{word}**", description=f"{phonetics}", color=CUSTOM_COLOR)
                    elif phonetics == None:
                        embed = discord.Embed(title=f"**{word}**", description=f"No phonetic information available", color=CUSTOM_COLOR)
                embed.add_field(name="1", value=f"*{definition}*", inline=False)
                if definition2 != None:
                    embed.add_field(name="2", value=f"*{definition2}*", inline=False)
                else:
                    pass
                await ctx.send(embed=embed)

    @commands.command()
    async def add(self, ctx: commands.Context, *num: int) -> None:
        """Adds two integers and returns result as message."""
        cmd = f"!add({num})"
        total = 0
        for i in num:
            total = total + i
        cmd_msg = f"total: {total}"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{total}")

    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str) -> None:
        """Roll NdN dice and get results."""
        cmd = f"!roll({dice})"
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.send("Format must be NdN!")
            return
        result = ", ".join(str(randint(1, limit)) for r in range(rolls))
        cmd_msg = f"rolled {dice}; result: {result}"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{result}")

    @commands.command()
    async def rps(self, ctx: commands.Context, choice: str) -> None:
        """Play rock, paper, scissors against the bot."""
        cmd = f"!rps(choice)"
        cmd_msg = f"choice: {choice}"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        choices = ["rock", "paper", "scissors"]
        botChoice = choices[randint(0, 2)]
        embedRPS = discord.Embed(color=CUSTOM_COLOR, title="rock, paper, scissors")
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
