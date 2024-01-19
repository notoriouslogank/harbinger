from datetime import datetime

from discord.ext import commands
from harbinger import Harbinger


class Notes(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def note(self, ctx: commands.Context, *content) -> None:
        """_summary_

        Args:
            *content (str): The content of the user note.
        """
        cmd = "!note"
        cmd_msg = f"{ctx.message.author.display_name} wrote a new note."
        note_author = str(ctx.message.author.display_name)
        note_content = ""
        timestamp = datetime.now()
        for word in content:
            note_content = note_content + word + " "
        with open(f"user_notes/{note_author}.txt", "a") as n:
            n.writelines(f"{timestamp}\n\n{note_content}\n--------------------\n")
            n.close()
        await ctx.send("Noted!")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def notes(self, ctx: commands.Context) -> None:
        """Print user's notes to the channel."""
        cmd = "!notes"
        cmd_msg = f"{ctx.message.author} checked their notes."
        note_file = f"user_notes/{ctx.message.author.display_name}.txt"
        with open(note_file, "r") as n:
            all_notes = n.read()
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send(f"```{all_notes}```")

    @commands.command()
    async def cnote(self, ctx: commands.Context) -> None:
        """Clear user's notes."""
        cmd = "!cnote"
        cmd_msg = f"{ctx.message.author} deleted their notes."
        clear_message = " "
        with open(f"user_notes/{ctx.message.author.display_name}.txt", "w") as n:
            n.write(clear_message)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await ctx.send("Cleared your notes!")


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(Notes(bot))
