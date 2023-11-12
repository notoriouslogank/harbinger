import discord
from discord.ext import commands

from mcswitch import Mcswitch

bot = Mcswitch.bot
color = Mcswitch.custom_color


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


async def setup(bot):
    await bot.add_cog(MineServ(bot))


############ Here's the original code:
# @commands.command()
# async def switch(self, ctx: commands.Context, state="on"):
#     """Bot command to start the remote Minecraft server.

#     Args:
#         state (str, optional): Switch the server 'on' or 'off'. Defaults to "on".
#     """
#     cmd = f"!switch{state}"
#     if state == "on":
#         cmd_msg = "attempting to start server"
#         Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
#         await ctx.channel.send("Attempting to start the server...")
#         try:
#             ServerAgent.start_server()
#             await ctx.channel.send("Sucessfully started server...")
#         except:
#             await ctx.channel.send("ERROR: 666")
#     elif state == "off":
#         cmd_msg = "attempting to stop server"
#         Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
#         try:
#             ServerAgent.stop_server()
#             await ctx.channel.send("Server is stopping...")
#         except:
#             await ctx.channel.send("ERROR: 667")
#     else:
#         cmd_message = "ERROR: Invalid choice"
#         Helpers.timestamp(ctx.message.author, cmd, cmd_msg)
#         await ctx.channel.send("Invalid Syntax!")
#         await ctx.channel.send("!switch <on|off>")
