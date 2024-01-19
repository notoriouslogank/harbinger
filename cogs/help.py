from re import M
import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()

moderation_commands = {
    "clear": "Delete a given number of messages.",
    "history": "Retrieve a given number of messages in this channel.",
    "serverinfo": "Get server information (owner, members list).",
    "whois": "Get detailed information about a given user.",
    "whisper": "Send a DM to a given user as Harbinger.",
    "code_whisper": "Send a an *encrypted* DM to a given user as Harbinger.",
    "log": "Write log.txt file (all messages or by author).",
    "code_say": "Send an *encrypted* message to the channel as Harbinger.",
    "say": "Send a message to the channel as Harbinger.",
}

bot_commands = {
    "reload_all": "Reload all cogs.",
    "load_cog": "Load a given cog.",
    "unload_cog": "Unload a given cog.",
    "reload_cog": "Reload a given cog.",
    "update": "Perform a ``git pull`` on the Harbinger host machine.",
    "up": "Confirm Harbinger is online.",
    "info": "Get Harbinger build info.",
    "ping": "Get the server latency.",
    "uptime": "Get the current uptime of Harbinger.",
    "changelog": "Get the CHANGELOG.md from the Harbinger repository.",
    "bug": "Send a bug report to Harbinger's maintainer.",
    "shutdown": "Gracefully shut down Harbinger.",
}

music_commands = {
    "join": "Join Harbinger to the currently-connected voice channel.",
    "leave": "Remove Harbinger from the currently-connected voice channel.",
    "pause": "Pause the currently-playing stream.",
    "play": "Play from url.",
    "stop": "Stop the currently-playing stream.",
    "stream": "Start playing from url.",
}

misc_commands = {
    "ask": "Ask Harbinger a yes/no question and get an answer.",
    "embed": "Send an embed to the channel as Harbinger.",
    "playing": "Create an embed with info about a current game.",
    "switch": "Turn the Minecraft server on or off.",
    "mccmd": "Send the given command to the Minecraft server.",
    "note": "Add the given message to the user's notes file.",
    "notes": "Get your notes.",
    "cnote": "Clear your notes.",
    "lmgtfy": "Let me Google that for you.",
    "define": "Get the Meriam-Webster definition for a given word.",
    "insult": "Insult a given user as Harbinger.",
    "add": "Add some numbers.",
    "roll": "Roll x amount of y-sided dice.",
    "rps": "Play rock, paper, scissors with Harbinger.",
}


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def command_list():
        master_commands_list = []
        for cmd in moderation_commands:
            master_commands_list.append(cmd)
        for cmd in bot_commands:
            master_commands_list.append(cmd)
        for cmd in music_commands:
            master_commands_list.append(cmd)
        for cmd in misc_commands:
            master_commands_list.append(cmd)
        master_commands_list.sort()
        return master_commands_list

    def categories_list():
        categories = ["moderation", "bot", "misc", "music"]
        categories.sort()
        return categories

    @commands.command()
    async def help(self, ctx, *, command=None) -> None:
        """Get help information about a given command or cog.

        Args:
            command (str, optional): Command or category (cog) to get help for. Defaults to None.
        """
        cmd = f"!help {command}"
        cmd_msg = f"Requested help with {command}."
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)
        HelpCommand.sort_commands()
        counter = 0
        # USAGE
        u_ask = {
            "__Usage__": "``!ask <question>``",
            "__Args__": "**question (str)**: Question to ask Harbinger [must end in ``?``].",
        }
        u_embed = {
            "__Usage__": "``!embed <title> <description> <image> <url>``",
            "__Args__": "**title (str)**: Title of embed.[Optional]\n**description (str)**: Description of embed. [Optional]\n**image (url)**: Image to upload.\n**url (url)**: url to embed (must he *https*)",
        }
        u_playing = {
            "__Usage__": "``!playing <game> <description> <field> <value>``",
            "__Args__": "**game (str)**: Name of game (title of embed).\n**description (str)**: Further info\n**field (str)**: Additional info field. [Optional]\n**value (str)**: Value for *field*.[Optional]",
        }
        u_switch = {
            "__Usage__": "``!switch <state>``",
            "__Args__": "**state (on|off)**: Default value is ``on``; pass ``'off'`` to turn server off.",
        }
        u_mccmd = {
            "__Usage__": "``!mccmd <command>``",
            "__Args__": "**command <str>**: Command to send to the Minecraft server.",
        }
        u_note = {
            "__Usage__": "``!note <message>``",
            "__Args__": "**message (str)**: Message to add to user's notes file.",
        }
        u_notes = {"__Usage__": "``!notes``", "__Args__": "[None]"}
        u_cnote = {"__Usage__": "``!cnote``", "__Args__": "[None]"}
        u_lmgtfy = {
            "__Usage__": "``!lmgtfy <query>``",
            "__Args__": "**query (str)**: Search query.",
        }
        u_define = {
            "__Usage__": "``!define <word>``",
            "__Args__": "**word (str)**: Word to define.",
        }
        u_insult = {
            "__Usage__": "``!insult <user>``",
            "__Args__": "**user (discord.Member)**: Discord member to insutl (creates ``@mention``)",
        }
        u_add = {
            "__Usage__": "``!add <number(s)>``",
            "__Args__": "**number(s) (int)**: The value(s) to be summed; may be any number of integers.",
        }
        u_roll = {
            "__Usage__": "``!roll <x>d<y>``",
            "__Args__": "**x (int)**: Quantity of dice to roll\n**y (int)**: The die to roll (eg d6, d20)",
        }
        u_rps = {
            "__Usage__": "``!rps <choice>``",
            "__Args__": "**choice (rock|paper|scissors)**: What to play against Harbinger.",
        }
        u_join = {"__Usage__": "``!join``", "__Args__": "[None]"}
        u_leave = {"__Usage__": "``!leave``", "__Args__": "[None]"}
        u_pause = {"__Usage__": "``!pause``", "__Args__": "[None]"}
        u_play = {
            "__Usage__": "``!play <url>``",
            "__Args__": "**url**: url to stream from (must be ``https``)",
        }
        u_stop = {"__Usage__": "``!stop``", "__Args__": "[None]"}
        u_stream = {
            "__Usage__": "``!stream <url>``",
            "__Args__": "**url**: url to stream from (must be ``https``)",
        }
        u_reload_all = {"__Usage__": "``!reload_all``", "__Args__": "[None]"}

        u_load_cog = {
            "__Usage__": "``!load_cog <cog>``",
            "__Args__": "**cog (str)**: Name of cog to load.",
        }
        u_unload_cog = {
            "__Usage__": "``!unload_cog <cog>``",
            "__Args__": "**cog (str)**: Name of cog to unload.",
        }
        u_reload_cog = {
            "__Usage__": "``!reload_cog <cog>``",
            "__Args__": "**cog (str)**: Name of cog to reload.",
        }
        u_update = {"__Usage__": "``!update``", "__Args__": "[None]"}
        u_up = {"__Usage__": "``!up``", "__Args__": "[None]"}
        u_info = {"__Usage__": "``!info``", "__Args__": "[None]"}
        u_ping = {"__Usage__": "``!ping``", "__Args__": "[None]"}
        u_uptime = {"__Usage__": "``!uptime``", "__Args__": "[None]"}
        u_changelog = {"__Usage__": "``!changelog``", "__Args__": "[None]"}
        u_bug = {
            "__Usage__": "``!bug <message>``",
            "__Args__": "**message (str)**: Content of the bug report.",
        }
        u_shutdown = {"__Usage__": "``!shutdown``", "__Args__": "[None]"}
        u_clear = {
            "__Usage__": "``!clear <amount>``",
            "__Args__": "**amount (int)**: Number of messages to delete.",
        }
        u_history = {
            "__Usage__": "``!history <amount>``",
            "__Args__": "**amount (int)**: Number of messages to show.",
        }
        u_serverinfo = {
            "__Usage__": "``!serverinfo``",
            "__Args__": "[None]",
        }
        u_whois = {
            "__Usage__": "``!whois <user>``",
            "__Args__": "**user (discord.Member)**: User name to get information about.",
        }
        u_whisper = {
            "__Usage__": "``!whisper <user> <message>``",
            "__Args__": "**user (discord.Member)**: User to send DM to.\n**message (str): Message to send.",
        }
        u_code_whisper = {
            "__Usage__": "``!code_whisper <encoding> <user> <message>``",
            "__Args__": "**encoding (bin|csr|hex|b64)**: Encoding schema to use.\n**user (discord.Member)**: User to DM.\n**message (str)**: Message to send.",
        }
        u_log = {
            "__Usage__": "``!log <author>``",
            "__Args__": "**author (discord.Member)**: User name to fetch messages for; leave blank to retrieve *all* messages.",
        }
        u_code_say = {
            "__Usage__": "``!code_say <encoding> <message>``",
            "__Args__": "**encoding (bin|csr|hex|b64)**: Encoding schema to use for message (binary, Caeser cipher, hex, base64).\n**message (str)**: Message to encode.",
        }
        u_say = {
            "__Usage__": "``!say <message>``",
            "__Args__": "**message (str)**: Message to send.",
        }
        # GENERAL
        if command == None:
            embed = discord.Embed(
                title="__HELP!__",
                description="Further information about supported bot commands.",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__COMMAND CATEGORIES__",
                value=f"{' '.join(HelpCommand.categories_list())}",
                inline=False,
            )
            embed.add_field(
                name="__ALL COMMANDS__",
                value=f"{' '.join(HelpCommand.command_list())}",
                inline=False,
            )
            await ctx.send(embed=embed)
        # CATEGORIES
        if command == "moderation":
            embed = discord.Embed(
                title="MODERATION COMMANDS",
                description="Commands for server moderation.",
                color=CUSTOM_COLOR,
            )
            for cmd in moderation_commands:
                key, value = list(moderation_commands.items())[counter]
                embed.add_field(
                    name=f"{str(key)}",
                    value=f"{str(value)}",
                    inline=True,
                )
                counter += 1
                embed.set_footer(
                    text="*You must have Admin role or above to excecute these commands*"
                )
            await ctx.send(embed=embed)
        if command == "bot":
            embed = discord.Embed(
                title="BOT COMMANDS",
                description="Commands for maintaining the Harbinger instance.",
                color=CUSTOM_COLOR,
            )
            for cmd in bot_commands:
                key, value = list(bot_commands.items())[counter]
                embed.add_field(
                    name=f"{str(key)}",
                    value=f"{str(value)}",
                    inline=True,
                )
                counter += 1
                embed.set_footer(
                    text="*You must have developer role or above to execute these commands.*"
                )
            await ctx.send(embed=embed)
        if command == "music":
            embed = discord.Embed(
                title="MUSIC COMMANDS",
                description="Commands to control Harbinger's music playing capability.",
                color=CUSTOM_COLOR,
            )
            for cmd in music_commands:
                key, value = list(music_commands.items())[counter]
                embed.add_field(
                    name=f"{str(key)}",
                    value=f"{str(value)}",
                    inline=True,
                )
                counter += 1
                embed.set_footer(
                    text="*You must be in a voice channel to join the bot.*"
                )
            await ctx.send(embed=embed)
        if command == "misc":
            embed = discord.Embed(
                title="MISC COMMANDS",
                description="General purpose commands.",
                color=CUSTOM_COLOR,
            )
            for cmd in misc_commands:
                key, value = list(misc_commands.items())[counter]
                embed.add_field(
                    name=f"{str(key)}",
                    value=f"{str(value)}",
                    inline=True,
                )
                counter += 1
                embed.set_footer(
                    text="*These commands may be executed by anyone, regardless of role."
                )
            await ctx.send(embed=embed)
        # MODERATION
        if command == "history":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands['history']}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_history['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_history['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "clear":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands['clear']}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_clear['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_clear["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "serverinfo":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_serverinfo['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_serverinfo["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "whois":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_whois['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_whois["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "whisper":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_whisper['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_whisper["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "code_whisper":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_code_whisper['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_code_whisper["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "log":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_log['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_log["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "code_say":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_code_say['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_code_say["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "say":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_say['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_say["__Args__"]}')
            await ctx.send(embed=embed)
        # BOT
        if command == "reload_all":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_reload_all['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_reload_all["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "load_cog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_load_cog['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_load_cog["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "unload_cog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_unload_cog['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_unload_cog["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "reload_cog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_reload_cog['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_reload_cog["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "update":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_update['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_update["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "up":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_up['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_up["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "info":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_info['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_info["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "ping":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_ping['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_ping["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "uptime":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_uptime['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_uptime["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "changelog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_changelog['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_changelog["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "bug":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_bug['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_bug["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "shutdown":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_shutdown['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_shutdown["__Args__"]}')
            await ctx.send(embed=embed)
        # MUSIC
        if command == "join":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_join['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_join["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "leave":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_leave['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_leave["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "pause":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_pause['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_pause["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "play":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_play['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_play["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "stop":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_stop['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_stop["__Args__"]}')
            await ctx.send(embed=embed)
        if command == "stream":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_stream['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f'{u_stream["__Args__"]}')
            await ctx.send(embed=embed)
        # MISC
        if command == "add":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_add['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f"{u_add['__Args__']}", inline=False)
            await ctx.send(embed=embed)
        if command == "ask":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_ask['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f"{u_ask['__Args__']}", inline=False)
            await ctx.send(embed=embed)
        if command == "embed":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_embed['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_embed['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "playing":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_playing['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_playing['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "switch":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_switch['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_switch['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "mccmd":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_mccmd['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_mccmd['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "note":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_note['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_note['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "notes":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_notes['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_notes['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "cnote":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_cnote['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_cnote['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "lmgtfy":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_lmgtfy['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_lmgtfy['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "define":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_define['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_define['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "insult":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_insult['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_insult['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "roll":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_roll['__Usage__']}", inline=False
            )
            embed.add_field(
                name="__Args__", value=f"{u_roll['__Args__']}", inline=False
            )
            await ctx.send(embed=embed)
        if command == "rps":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="__Usage__", value=f"{u_rps['__Usage__']}", inline=False
            )
            embed.add_field(name="__Args__", value=f"{u_rps['__Args__']}", inline=False)
            await ctx.send(embed=embed)


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(HelpCommand(bot))
