import discord
from discord.ext import commands
from datetime import datetime
from harbinger import Harbinger


class Notes(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def note(self, ctx: commands.Context, *content):
        note_author = str(ctx.message.author.display_name)
        note_content = ""
        timestamp = datetime.now()
        for word in content:
            note_content = note_content + word + " "
        with open(f"user_notes/{note_author}.txt", "a") as n:
            n.writelines(f"{timestamp}\n\n{note_content}\n--------------------\n")
            n.close()

    @commands.command()
    async def notes(self, ctx: commands.Context):
        note_file = f"user_notes/{ctx.message.author.display_name}.txt"
        with open(note_file, "r") as n:
            all_notes = n.read()
        await ctx.send(f"```{all_notes}```")

    @commands.command()
    async def cnote(self, ctx: commands.Context):
        clear_message = " "
        with open(f"user_notes/{ctx.message.author.display_name}.txt", "w") as n:
            n.write(clear_message)


async def setup(bot):
    await bot.add_cog(Notes(bot))
