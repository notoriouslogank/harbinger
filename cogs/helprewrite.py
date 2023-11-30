import discord
from discord.ext import commands

from harbinger import Harbinger


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, command=None) -> None:
        custom_color = Harbinger.custom_color

        # HELP
        if command == None:
            help_embed = discord.Embed(
                title="Help",
                description=f"Harbinger v{Harbinger.get_ver()}",
                color=custom_color,
            )
            help_embed.add_field(
                name="Usage", value="!help <category|command>", inline=False
            )
            help_embed.add_field(
                name="Help Categories",
                value="minecraft, moderation, music, status, tools",
                inline=True,
            )
            help_embed.add_field(
                name="Help Commands",
                value="mccmd, switch, clear, serverinfo, whois, join, leave, pause, play, stream, bug, info, ping, shutdown, up, uptime, add, ask, cnote, define, lmgtfy, note, notes, playing, roll, rps, say",
                inline=True,
            )
            await ctx.send(embed=help_embed)
        # CATEGORIES
        elif command == "minecraft":
            minecraft_embed = discord.Embed(
                title="Minecraft Commands",
                description="Commands to control the Minecraft server instance.",
                color=custom_color,
            )
            minecraft_embed.add_field(
                name="!mccmd",
                value="Send an arbitrary command to the Minecraft server.",
                inline=True,
            )
            minecraft_embed.add_field(
                name="!switch",
                value="Toggle the Minecraft server on or off.",
                inline=True,
            )
            await ctx.send(embed=minecraft_embed)
        elif command == "moderation":
            moderation_embed = discord.Embed(
                title="Moderation Commands",
                description="Commands for moderating the Discord server.",
                color=custom_color,
            )
            moderation_embed.add_field(
                name="!clear",
                value="Delete an arbitrary number of messages.",
                inline=True,
            )
            moderation_embed.add_field(
                name="!serverinfo", value="Get details about this server.", inline=True
            )
            moderation_embed.add_field(
                name="!whois",
                value="Get detailed information about a server member.",
                inline=True,
            )
            #            moderation_embed.add_field()
            #            moderation_embed.add_field()
            await ctx.send(embed=moderation_embed)
        elif command == "music":
            music_embed = discord.Embed(
                title="Music Commands",
                description="Commands to control the music player.",
                color=custom_color,
            )
            music_embed.add_field(
                name="!join",
                value="Join bot to your current voice channel.",
                inline=True,
            )
            music_embed.add_field(
                name="!leave",
                value="Remove the bot from the current voice channel,",
                inline=True,
            )
            music_embed.add_field(
                name="!pause", value="Pause the currently playing track.", inline=True
            )
            music_embed.add_field(
                name="!play", value="Resume playback of a paused track.", inline=True
            )
            music_embed.add_field(
                name="!stream",
                value="Start audio stream in current voice channel.",
                inline=True,
            )
            await ctx.send(embed=music_embed)
        elif command == "status":
            status_embed = discord.Embed(
                title="Status Commands",
                description="Commands to get various status information.",
                color=custom_color,
            )
            status_embed.add_field(
                name="!bug",
                value="Email a bug report to the bot developer(s).",
                inline=True,
            )
            status_embed.add_field(
                name="!info", value="Get details about this bot.", inline=True
            )
            status_embed.add_field(
                name="!ping", value="Get network latency.", inline=True
            )
            status_embed.add_field(
                name="!shutdown", value="Gracefully shut down the bot.", inline=True
            )
            status_embed.add_field(
                name="!up", value="Check whether bot is online.", inline=True
            )
            status_embed.add_field(
                name="!uptime", value="Get uptime of the bot.", inline=True
            )
            await ctx.send(embed=status_embed)
        elif command == "tools":
            tools_embed = discord.Embed(
                title="Tools",
                description="Various tools or interesting gadgets.",
                color=custom_color,
            )
            tools_embed.add_field(
                name="!add",
                value="Get the sum of an arbitrary list of numbers.",
                inline=True,
            )
            tools_embed.add_field(
                name="!ask",
                value="Ask the bot a question and get some advice.",
                inline=True,
            )
            tools_embed.add_field(
                name="!cnote", value="Clear all of your notes.", inline=True
            )
            tools_embed.add_field(
                name="!define",
                value="Get the definition of a given word from Meriam-Webster.",
                inline=True,
            )
            tools_embed.add_field(
                name="!lmgtfy", value="Let me Google that for you.", inline=True
            )
            tools_embed.add_field(
                name="!note", value="Add a note to your user notes file.", inline=True
            )
            tools_embed.add_field(
                name="!notes", value="Print all your current notes.", inline=True
            )
            tools_embed.add_field(
                name="!playing",
                value="Create an embed with arbitrary game information.",
                inline=True,
            )
            tools_embed.add_field(name="!roll", value="Roll some dice.", inline=True)
            tools_embed.add_field(
                name="!rps",
                value="Play rock, paper, scissors against the bot.",
                inline=True,
            )
            tools_embed.add_field(
                name="!say", value="Send a message as the bot.", inline=True
            )
            await ctx.send(embed=tools_embed)
        # COMMANDS
        elif command == "":
            embed = discord.Embed(
                title="add", description="Add some numbers.", color=custom_color
            )
            embed.add_field(name="Usage", value="!add <*numbers>", inline=True)
            embed.add_field(
                name="<*numbers: int>",
                value="An arbitrary amount of integers to be added.",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="ask",
                description="Ask Harbinger for some advice",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!ask <*question>", inline=True)
            embed.add_field(
                name="<*question: str>", value="Question to ask the bot.", inline=True
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="bug",
                description="Send a bug report to bot developers.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!bug <*report>", inline=True)
            embed.add_field(
                name="<*report: str>",
                value="The content of the bug report to send.",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="clear",
                description="Remove an arbitrary number of messages from the current channel.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!clear <num>", inline=True)
            embed.add_field(
                name="<num: int>",
                value="Number of messages to be deleted.",
                inline=True,
            )
            embed.set_footer(text="Note: Number of messages must be under 100.")
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="cnote",
                description="Clear all of your user notes.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!cnote", inline=True)
            embed.set_footer(text="Note: This action cannot be undone.")
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="define",
                description="Get the Meriam-Webster definition of a given word.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!define <word>", inline=True)
            embed.add_field(
                name="<word: str>", value="A word to be defined.", inline=True
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="info",
                description="Get detailed information about this bot.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!info", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="join",
                description="Move the bot into current voice channel to prepare to play music.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!join", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="leave",
                description="Remove the bot from the current voice channel.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!leave", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="lmgtfy",
                description="Let me Google that for you.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!lmgtfy <*query>", inline=True)
            embed.add_field(
                name="<*query: str>",
                value="String to be searched on Google.",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="mccmd",
                description="Send an arbitrary command to the Minecraft server.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!mccmd <command>", inline=True)
            embed.add_field(
                name="<command: str>",
                value="Command string to send to the Minecraft server.",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="note",
                description="Add a note to your user notes file.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!note <*message>", inline=True)
            embed.add_field(
                name="<*message: str>",
                value="Arbitrary string to be saved to user's note file.",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="notes",
                description="Retreive all of your user notes.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!notes", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="pause",
                description="Pause the currently playing track.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!pause", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="ping", description="Get network latency.", color=custom_color
            )
            embed.add_field(name="Usage", value="!ping", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="play",
                description="Resume playback of paused music track.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!play", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="playing",
                description="Create an embed with arbitrary game information.",
                color=custom_color,
            )
            embed.add_field(
                name="Usage",
                value="!playing <game> <description> <field> <value>",
                inline=True,
            )
            embed.add_field(
                name="<game: str>", value="Game the embed is about.", inline=True
            )
            embed.add_field(
                name="<description: str>",
                value="Arbitrary further info about the game.",
                inline=True,
            )
            embed.add_field(
                name="<field: str>",
                value="Arbitrary additional field (eg Server Address, Room Code)",
                inline=True,
            )
            embed.add_field(
                name="<value: str>",
                value="Value for the <field> (eg 10.0.0.1, ABCD)",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="roll", description=f"Roll some dice.", color=custom_color
            )
            embed.add_field(name="Usage", value=f"!roll *x*d*y*", inline=True)
            embed.add_field(
                name="<x: int>", value="Number of dice to roll.", inline=True
            )
            embed.add_field(
                name="<y: int>", value="*y*-sided die to be rolled.", inline=True
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="rps",
                description="Play rock, paper, scissors against the bot.",
                color=custom_color,
            )
            embed.add_field(
                name="Usage", value="!rps <rock|paper|scissors>", inline=True
            )
            embed.add_field(
                name="<rock|paper|scissors: str>",
                value="Which move to play.",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="say",
                description="Send message to current channel as bot.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!say <*message>", inline=True)
            embed.add_field(
                name="<*message: str>",
                value="Arbitrary message to be sent.",
                inline=True,
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="serverinfo",
                description="Get detailed server information.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!serverinfo", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="shutdown",
                description="Gracefully shut down the bot.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!shutdown", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="stream",
                description="Start streaming audio in the current voice channel.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!stream <URL>", inline=True)
            embed.add_field(
                name="<URL: str>", value="URL of the audio to be streamed.", inline=True
            )
            embed.set_footer(
                text="Note: while other websites *may* work, only YouTube URLs are *officially* supported."
            )
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="up",
                description="Check whether bot is online.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!up", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="uptime",
                description="Get current uptime of the bot.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!uptime", inline=True)
            await ctx.send(embed=embed)
        elif command == "":
            embed = discord.Embed(
                title="whois",
                description="Get detailed information about a given server member.",
                color=custom_color,
            )
            embed.add_field(name="Usage", value="!whois <member>", inline=True)
            embed.add_field(
                name="<member: discord.Member>",
                value="The member whose info will be retreived.",
                inline=True,
            )
            await ctx.send(embed=embed)


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(HelpCommand(bot))
