from random import randint

import aiohttp
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
        """Return an embedded definition and pronunciation guide for a given word.

        Args:
            word (str): Word to be defined
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            ) as resp:
                dict_entry = await resp.json()
                pronunciation = None
                phonetics = None
                await ctx.message.delete()
                try:
                    pronunciation = str(dict_entry[0]["phonetics"][0]["audio"])
                except Exception:
                    pass
                try:
                    phonetics = str(dict_entry[0]["phonetics"][0]["text"])
                except Exception:
                    pass
                definition = dict_entry[0]["meanings"][0]["definitions"][0][
                    "definition"
                ]
                if phonetics == None:
                    embed = discord.Embed(
                        title=f"{word}",
                        description=f"No phonetic guide available.",
                        color=CUSTOM_COLOR,
                    )
                elif pronunciation == None:
                    print(f"pronounce: {pronunciation}")
                    embed = discord.Embed(
                        title=f"{word}", description=f"{phonetics}", color=CUSTOM_COLOR
                    )
                else:
                    embed = discord.Embed(
                        title=f"{word}",
                        description=f"[{phonetics}]({pronunciation})",
                        color=CUSTOM_COLOR,
                    )
                embed.add_field(name=" ", value=f"{definition}")
                await ctx.send(embed=embed)
                await session.close()
                # print(word, pronunciation, phonetics, definition)

    @commands.command()
    async def insult(self, ctx: commands.Context, member: discord.Member) -> None:
        """Send a random insult to (and @mention) a given user.

        Args:
            member (discord.Member): Member to insult and @mention.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://evilinsult.com/generate_insult.php?lang=en&type=json"
            ) as resp:
                insult_json = await resp.json()
                await ctx.message.delete()
                insult = str(insult_json["insult"])
                await ctx.send(f"{member.mention}: {insult}")
                await session.close()

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
        embedRPS.add_field(name=ctx.author, value=f"{choice}", inline=True)
        embedRPS.add_field(name=self.bot.user, value=f"{botChoice}", inline=True)
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
