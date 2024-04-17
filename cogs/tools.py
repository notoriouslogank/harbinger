from random import randint

import aiohttp
import discord
from discord.ext import commands
from jokeapi import Jokes

from assets import strings
from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger
import wikipediaapi

CUSTOM_COLOR = configs.custom_color()
EMAIL_ADDRESS = configs.email_address()
bubble_wrap = strings.BUBBLE_WRAP
bot = Harbinger.bot


class Tools(commands.Cog):
    """Commands containing various tools/utilites."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx: commands.Context, query: str):
        wiki = wikipediaapi.Wikipedia(f"{EMAIL_ADDRESS}", "en")
        page = wiki.page(query)
        # exist_msg = "Page Exists: %s" % page.exists()
        summary = page.summary[0:1999]
        await ctx.send(summary)

    @commands.command()
    async def bw(self, ctx):
        cmd = f"!bw"
        cmd_msg = f"Unspooled some bubble wrap."
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f"{bubble_wrap}")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def joke(self, ctx, type="any"):
        cmd = f"!joke"
        cmd_msg = f"Told a joke."
        await ctx.channel.purge(limit=1)
        j = await Jokes()
        get_joke = await j.get_joke(
            category=[type],
            safe_mode=False,
            amount=1,
            response_format="txt",
        )
        await ctx.send(get_joke)
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def slang(self, ctx: commands.Context, *query: str) -> None:
        """Query Urban Dictionary for a term and send definition to channel.

        Args:
            query (str): Search parameter(s)
        """
        cmd = f"!slang {query}"
        await ctx.channel.purge(limit=1)
        urban_dictionary = "https://www.urbandictionary.com/define.php?term="
        string_query = ""
        for word in query:
            string_query = string_query + str(word) + " "
        sanitized_query = string_query.replace(" ", "+")
        search = urban_dictionary + sanitized_query
        cmd_msg = f"Search: {query}"
        await ctx.send("Let me see what I can find...")
        async with ctx.channel.typing():
            await ctx.send(search)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def lmgtfy(self, ctx: commands.Context, *query: str) -> None:
        """Let me Google that for you.

        Args:
            query (str): Search query.
        """
        cmd = f"!lmgtfy({query})"
        await ctx.channel.purge(limit=1)
        google = "https://google.com/search?q="
        string_query = ""
        for word in query:
            string_query = string_query + str(word) + " "
        sanitized_query = string_query.replace(" ", "+")
        search = google + sanitized_query
        cmd_msg = f"URL: {search}"
        await ctx.send("Here, let me just Google that for you...")
        async with ctx.channel.typing():
            await ctx.send(search)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def define(self, ctx: commands.Context, word: str) -> None:
        """Get definition and pronunciation (if available) for given word.

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
        cmd = f"!insult {member}"
        await ctx.channel.purge(limit=1)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://evilinsult.com/generate_insult.php?lang=en&type=json"
            ) as resp:
                insult_json = await resp.json()
                insult = str(insult_json["insult"])
                cmd_msg = f"{insult}"
                await ctx.send(f"{member.mention}: {insult}")
                await session.close()
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def add(self, ctx: commands.Context, *num: float) -> None:
        """Adds an arbitrary number of integers and returns sum.

        Args:
            num (int): Any number of integers to sum.
        """
        cmd = f"!add({num})"
        total = 0
        for i in num:
            total = total + i
        cmd_msg = f"total: {total}"
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"{total}")

    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str) -> None:
        """Roll an arbitrary amount of n-sided dice.

        Args:
            dice (str): A string representing the dice to roll; must be in format xdy,
                        where (x) is the amount of dice, (d) is a mandatory separator,
                        and (y) is the 'sidedness' of the dice to roll.
        """
        cmd = f"!roll({dice})"
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.send("Format must be NdN!")
            return
        result = ", ".join(str(randint(1, limit)) for r in range(rolls))
        cmd_msg = f"rolled {dice}; result: {result}"
        await ctx.send(f"{result}")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def rps(self, ctx: commands.Context, choice: str) -> None:
        """Play rock, paper, scissors against Harbinger.

        Args:
            choice (str): Which move to play (rock|paper|scissors)
        """
        cmd = f"!rps(choice)"
        cmd_msg = f"choice: {choice}"
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
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Tools(bot))
