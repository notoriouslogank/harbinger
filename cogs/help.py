import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, command=None) -> None:
        """Get help information about a given command or cog.

        Args:
            command (str, optional): Command or category (cog) to get help for. Defaults to None.
        """

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
        mod_cmds = moderation_commands.keys()

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
        bot_cmds = bot_commands.keys()

        music_commands = {
            "join": "Join Harbinger to the currently-connected voice channel.",
            "leave": "Remove Harbinger from the currently-connected voice channel.",
            "pause": "Pause the currently-playing stream.",
            "play": "Play from url.",
            "stop": "Stop the currently-playing stream.",
            "stream": "Start playing from url.",
        }
        music_cmds = music_commands.keys()

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
        misc_cmds = misc_commands.keys()

        categories = ["moderation", "bot", "music", "misc"]
        categories = categories.sort()

        master_commands_list = [f"{mod_cmds},{bot_cmds},{music_cmds},{misc_cmds}"]
        # USAGE
        u_ask = {
            "Usage": "!ask **<question>**",
            "Args": "**question (str)**: Question to ask Harbinger [must end in ``?``].",
        }
        u_embed = {
            "Usage": "!embed **<title> <description> <image> <url>**",
            "Args": "**title (str)**: Title of embed.[Optional]\n**description (str)**: Description of embed. [Optional]\n**image (url)**: Image to upload.\n**url (url)**: url to embed (must he *https*)",
        }
        u_playing = {
            "Usage": "!playing **<game> <description> <field> <value>**",
            "Args": "**game (str)**: Name of game (title of embed).\n**description (str)**: Further info\n**field (str)**: Additional info field. [Optional]\n**value (str)**: Value for *field*.[Optional]",
        }
        u_switch = {
            "Usage": "!switch **<state>**",
            "Args": "**state (on|off)**: Default value is ``on``; pass ``'off'`` to turn server off.",
        }
        u_mccmd = {
            "Usage": "!mccmd **<command>**",
            "Args": "**command <str>**: Command to send to the Minecraft server.",
        }
        u_note = {
            "Usage": "!note **<message>**",
            "Args": "**message (str)**: Message to add to user's notes file.",
        }
        u_notes = {"Usage": "!notes", "Args": "[None]"}
        u_cnote = {"Usage": "!cnote", "Args": "[None]"}
        u_lmgtfy = {
            "Usage": "!lmgtfy **<query>**",
            "Args": "**query (str)**: Search query.",
        }
        u_define = {
            "Usage": "!define **<word>**",
            "Args": "**word (str)**: Word to define.",
        }
        u_insult = {
            "Usage": "!insult **<user>**",
            "Args": "**user (discord.Member)**: Discord member to insutl (creates ``@mention``)",
        }
        u_add = {
            "Usage": "!add **<number> <number>**",
            "Args": "**number (int)**: The value(s) to be summed; may be any number of integers.",
        }
        u_roll = {
            "Usage": "!roll **<x>**d**<y>**",
            "Args": "**x (int)**: Quantity of dice to roll\n**y (int)**: The die to roll (eg d6, d20)",
        }
        u_rps = {
            "Usage": "!rps **<choice>**",
            "Args": "**choice (rock|paper|scissors)**: What to play against Harbinger.",
        }
        u_join = {"Usage": "!join", "Args": "[None]"}
        u_leave = {"Usage": "!leave", "Args": "[None]"}
        u_pause = {"Usage": "!pause", "Args": "[None]"}
        u_play = {
            "Usage": "!play **<url>**",
            "Args": "**url**: url to stream from (must be ``https``)",
        }
        u_stop = {"Usage": "!stop", "Args": "[None]"}
        u_stream = {
            "Usage": "!stream **<url>**",
            "Args": "**url**: url to stream from (must be ``https``)",
        }
        u_reload_all = {"Usage": "!reload_all", "Args": "[None]"}
        u_load_cog = {
            "Usage": "!load_cog **<cog>**",
            "Args": "**cog (str)**: Name of cog to load.",
        }
        u_unload_cog = {
            "Usage": "!unload_cog **<cog>**",
            "Args": "**cog (str)**: Name of cog to unload.",
        }
        u_reload_cog = {
            "Usage": "!reload_cog **<cog>**",
            "Args": "**cog (str)**: Name of cog to reload.",
        }
        u_update = {"Usage": "!update", "Args": "[None]"}
        u_up = {"Usage": "!up", "Args": "[None]"}
        u_info = {"Usage": "!info", "Args": "[None]"}
        u_ping = {"Usage": "!ping", "Args": "[None]"}
        u_uptime = {"Usage": "!uptime", "Args": "[None]"}
        u_changelog = {"Usage": "!changelog", "Args": "[None]"}
        u_bug = {
            "Usage": "!bug **<message>**",
            "Args": "**message (str)**: Content of the bug report.",
        }
        u_shutdown = {"Usage": "!shutdown", "Args": "[None]"}
        u_clear = {
            "Usage": "!clear **<amount>**",
            "Args": "**amount (int)**: Number of messages to delete.",
        }
        u_history = {"Usage": "!history **<amount>**", "Args": ""}
        u_serverinfo = {
            "Usage": "",
            "Args": "**amount (int)**: Number of messages to show.",
        }
        u_whois = {
            "Usage": "!whois **<user>**",
            "Args": "**user (discord.Member)**: User name to get information about.",
        }
        u_whisper = {
            "Usage": "!whisper **<user> <message>**",
            "Args": "**user (discord.Member)**: User to send DM to.\n**message (str): Message to send.",
        }
        u_code_whisper = {
            "Usage": "!code_whisper **<encoding> <user> <message>**",
            "Args": "**encoding (bin|csr|hex|b64)**: Encoding schema to use.\n**user (discord.Member)**: User to DM.\n**message (str)**: Message to send.",
        }
        u_log = {
            "Usage": "!log **<author>**",
            "Args": "**author (discord.Member)**: User name to fetch messages for; leave blank to retrieve *all* messages.",
        }
        u_code_say = {
            "Usage": "!code_say **<encoding> <message>**",
            "Args": "**encoding (bin|csr|hex|b64)**: Encoding schema to use for message (binary, Caeser cipher, hex, base64).\n**message (str)**: Message to encode.",
        }
        u_say = {
            "Usage": "!say **<message>**",
            "Args": "**message (str)**: Message to send.",
        }
        # GENERAL
        if command == None:
            embed = discord.Embed(
                title="HELP!",
                description="Further information about supported bot commands.",
                color=CUSTOM_COLOR,
            )
            embed.add_field(
                name="COMMAND CATEGORIES", value=f"{categories}", inline=False
            )
            embed.add_field(name="ALL COMMANDS", value=f"{master_commands_list}")
            await ctx.send(embed=embed)
        # CATEGORIES
        if command == "moderation":
            embed = discord.Embed(
                title="MODERATION COMMANDS",
                description="Commands for server moderation.",
                color=CUSTOM_COLOR,
            )
            for cmd in moderation_commands:
                embed.add_field(
                    name={moderation_commands[cmd]},
                    value={moderation_commands.get(cmd)},
                    inline=False,
                )
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
                embed.add_field(
                    name={bot_commands[cmd]},
                    value={bot_commands.get(cmd)},
                    inline=False,
                )
                embed.set_footer(
                    text="*You must have developer role or above to execute these commands.*"
                )
            await ctx.send(embed=embed)
        if command == "music":
            embed = discord.Embed(
                title="MUSIC COMMANDS",
                description="Commands to control Harbinger's music playing capability.",
                inline=False,
            )
            for cmd in music_commands:
                embed.add_field(
                    name={music_commands[cmd]},
                    value={music_commands.get(cmd)},
                    inline=False,
                )
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
                embed.add_field(
                    name={misc_commands[cmd]},
                    value={misc_commands.get(cmd)},
                    inline=False,
                )
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
            embed.add_field(name="Usage", value=f"{u_history['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_history['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "clear":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands['clear']}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_clear['Usage']}")
            embed.add_field(name="Args", value=f'{u_clear["Args"]}')
            await ctx.send(embed=embed)
        if command == "serverinfo":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_serverinfo['Usage']}")
            embed.add_field(name="Args", value=f'{u_serverinfo["Args"]}')
            await ctx.send(embed=embed)
        if command == "whois":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_whois['Usage']}")
            embed.add_field(name="Args", value=f'{u_whois["Args"]}')
            await ctx.send(embed=embed)
        if command == "whisper":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_whisper['Usage']}")
            embed.add_field(name="Args", value=f'{u_whisper["Args"]}')
            await ctx.send(embed=embed)
        if command == "code_whisper":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_code_whisper['Usage']}")
            embed.add_field(name="Args", value=f'{u_code_whisper["Args"]}')
            await ctx.send(embed=embed)
        if command == "log":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_log['Usage']}")
            embed.add_field(name="Args", value=f'{u_log["Args"]}')
            await ctx.send(embed=embed)
        if command == "code_say":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_code_say['Usage']}")
            embed.add_field(name="Args", value=f'{u_code_say["Args"]}')
            await ctx.send(embed=embed)
        if command == "say":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{moderation_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_say['Usage']}")
            embed.add_field(name="Args", value=f'{u_say["Args"]}')
            await ctx.send(embed=embed)
        # BOT
        if command == "reload_all":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_reload_all['Usage']}")
            embed.add_field(name="Args", value=f'{u_reload_all["Args"]}')
            await ctx.send(embed=embed)
        if command == "load_cog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_load_cog['Usage']}")
            embed.add_field(name="Args", value=f'{u_load_cog["Args"]}')
            await ctx.send(embed=embed)
        if command == "unload_cog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_unload_cog['Usage']}")
            embed.add_field(name="Args", value=f'{u_unload_cog["Args"]}')
            await ctx.send(embed=embed)
        if command == "reload_cog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_reload_cog['Usage']}")
            embed.add_field(name="Args", value=f'{u_reload_cog["Args"]}')
            await ctx.send(embed=embed)
        if command == "update":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_update['Usage']}")
            embed.add_field(name="Args", value=f'{u_update["Args"]}')
            await ctx.send(embed=embed)
        if command == "up":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_up['Usage']}")
            embed.add_field(name="Args", value=f'{u_up["Args"]}')
            await ctx.send(embed=embed)
        if command == "info":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_info['Usage']}")
            embed.add_field(name="Args", value=f'{u_info["Args"]}')
            await ctx.send(embed=embed)
        if command == "ping":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_ping['Usage']}")
            embed.add_field(name="Args", value=f'{u_ping["Args"]}')
            await ctx.send(embed=embed)
        if command == "uptime":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_uptime['Usage']}")
            embed.add_field(name="Args", value=f'{u_uptime["Args"]}')
            await ctx.send(embed=embed)
        if command == "changelog":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_changelog['Usage']}")
            embed.add_field(name="Args", value=f'{u_changelog["Args"]}')
            await ctx.send(embed=embed)
        if command == "bug":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_bug['Usage']}")
            embed.add_field(name="Args", value=f'{u_bug["Args"]}')
            await ctx.send(embed=embed)
        if command == "shutdown":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{bot_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_shutdown['Usage']}")
            embed.add_field(name="Args", value=f'{u_shutdown["Args"]}')
            await ctx.send(embed=embed)
        # MUSIC
        if command == "join":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_join['Usage']}")
            embed.add_field(name="Args", value=f'{u_join["Args"]}')
            await ctx.send(embed=embed)
        if command == "leave":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_leave['Usage']}")
            embed.add_field(name="Args", value=f'{u_leave["Args"]}')
            await ctx.send(embed=embed)
        if command == "pause":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_pause['Usage']}")
            embed.add_field(name="Args", value=f'{u_pause["Args"]}')
            await ctx.send(embed=embed)
        if command == "play":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_play['Usage']}")
            embed.add_field(name="Args", value=f'{u_play["Args"]}')
            await ctx.send(embed=embed)
        if command == "stop":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_stop['Usage']}")
            embed.add_field(name="Args", value=f'{u_stop["Args"]}')
            await ctx.send(embed=embed)
        if command == "stream":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{music_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_stream['Usage']}")
            embed.add_field(name="Args", value=f'{u_stream["Args"]}')
            await ctx.send(embed=embed)
        # MISC
        if command == "add":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_add['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_add['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "ask":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_ask['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_ask['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "embed":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_embed['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_embed['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "playing":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_playing['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_playing['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "switch":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_switch['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_switch['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "mccmd":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_mccmd['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_mccmd['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "note":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_note['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_note['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "notes":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_notes['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_notes['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "cnote":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_cnote['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_cnote['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "lmgtfy":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_lmgtfy['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_lmgtfy['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "define":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_define['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_define['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "insult":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_insult['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_insult['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "roll":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_roll['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_roll['Args']}", inline=False)
            await ctx.send(embed=embed)
        if command == "rps":
            embed = discord.Embed(
                title=f"{command}",
                description=f"{misc_commands[command]}",
                color=CUSTOM_COLOR,
            )
            embed.add_field(name="Usage", value=f"{u_rps['Usage']}", inline=False)
            embed.add_field(name="Args", value=f"{u_rps['Args']}", inline=False)
            await ctx.send(embed=embed)


async def setup(bot):
    """Load cog into bot."""
    await bot.add_cog(HelpCommand(bot))
