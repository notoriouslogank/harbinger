import random

from discord.ext import commands

from cogs.dev import DELETION_TIME
from harbinger import Harbinger
from assets import strings

answers = strings.ANSWERS

class Eightball(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def ask(self, ctx: commands.Context, *question: str) -> None:
        """Send an answer to the user's question from answers list.

        Args:
            question (str): The question to be answered
        """
        cmd = "!ask"
        string_question = ""
        for word in question:
            string_question = string_question + " " + word
        if string_question.endswith("?"):
            cmd_msg = f"{ctx.message.author} asked: {string_question}."
            response = answers[random.randint(0, (len(answers) - 1))]
            await ctx.send(f"{response}")
        else:
            cmd_msg = (
                f"{ctx.message.author} did not ask a valid question: {string_question}."
            )
            await ctx.send(
                f"Not a valid question.  (Questions end with a question mark.)",
                delete_after=DELETION_TIME,
            )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Eightball(bot))
