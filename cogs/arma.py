from discord.ext import commands
from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()
ServerIp = "24.254.180.161"
ServerPort = "2302"
ServerPassword = "Ktsx+G%ItPqCZWkZ"

bot = Harbinger.bot


class Arma(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def arma(self, ctx: commands.Context, command=None) -> None:
        cmd = f"!arma"
        cmd_msg = f"Sent Arma III server information."
        await ctx.channel.purge(limit=1)
        message_contents = f"Arma III Server IP: ``{ServerIp}`` \n Port: ``{ServerPort}``\nServer Password: ``{ServerPassword}``"
        await Harbinger.send_dm(
            ctx=ctx, member=ctx.message.author, content=message_contents
        )
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    await bot.add_cog(Arma(bot))
