from discord.ext import commands

from harbinger import Harbinger

bot = Harbinger.bot
color = Harbinger.custom_color


class MineServ(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def switch(self, ctx: commands.Context, state="on") -> None:
        if state == "on":
            pass
        elif state == "off":
            pass
        else:
            pass

    @commands.command()
    async def mc_command(self, ctx: commands.Context, command: str) -> None:
        pass

    @commands.command()
    async def mc_status(self, ctx: commands.Context) -> None:
        pass

    @commands.command()
    async def mc_backup(self, ctx: commands.Context) -> None:
        pass
