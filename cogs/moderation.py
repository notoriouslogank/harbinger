import base64
import random
from pathlib import Path
import discord
from config.read_configs import ReadConfigs as configs
from discord.ext import commands
from harbinger import Harbinger


DELETION_TIME = configs.delete_time()
CUSTOM_COLOR = configs.custom_color()
BOT_CHANNEL = configs.bot_channel()

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Moderation(commands.Cog):
    """Server moderation commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def get_bot_channel(self):
        bot_channel = discord.Client.get_channel(self.bot, BOT_CHANNEL)
        return bot_channel

    def caeser_cipher(key: int, message: str) -> str:
        """Encipher the given message with a Caeser shift.

        Args:
            key (int): Amount to shift
            message (str): Message to encode

        Returns:
            str: Encoded message
        """
        message = message.upper()
        result = ""

        for letter in message:
            if letter in alpha:
                letter_index = (alpha.find(letter) + key) % len(alpha)
                result = result + alpha[letter_index]
            else:
                result = result + letter
        return result

    def caeser_decipher(key: int, message: str) -> str:
        """Decipher given Caser-shifted messge.

        Args:
            key (int): Amount to shift
            message (str): Message to decode

        Returns:
            str: Decoded message
        """
        message = message.upper()
        result = ""

        for letter in message:
            if letter in alpha:
                letter_index = (alpha.find(letter) - int(key)) % len(alpha)
                result = result + alpha[letter_index]
            else:
                result = result + letter
        return result

    @commands.command()
    async def decrypt(
        self, ctx: commands.Context, code: str, key: int, *, message: str
    ):
        """Decrypt the given message.

        Args
            code (str): Encoding schema to use for decoding
            key (int): Amount to shift (if Caeser cipher)
            message (str): _description_
        """
        cmd = f"!decrypt {code} {key} {message}"
        await ctx.channel.purge(limit=1)
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Decrypted {code}-encoded message."
            if code == "b64":
                bytes_object = base64.b64decode(message)
                decrypted_message = (
                    f"Decrypted message:\n**``{bytes_object.decode('utf-8')}``**"
                )
                await Harbinger.send_dm(
                    ctx=ctx, member=ctx.message.author, content=decrypted_message
                )
            elif code == "bin":
                decrypted_message = "".join(
                    chr(int(message[i * 8 : i * 8 + 8], 2))
                    for i in range(len(message) // 8)
                )
                decryption_message = f"Decrypted message:\n``{decrypted_message}``"
                await Harbinger.send_dm(
                    ctx=ctx, member=ctx.message.author, content=decryption_message
                )
            elif code == "csr":
                decrypted_message = f"Decrypted message:\n**``{Moderation.caeser_decipher(key, message)}``**"
                await Harbinger.send_dm(
                    ctx=ctx, member=ctx.message.author, content=decrypted_message
                )
            elif code == "hex":
                bytes_obj = bytes.fromhex(message)
                decrypted_message = (
                    f"Decrypted message:\n**``{bytes_obj.decode('utf-8')}``**"
                )
                await Harbinger.send_dm(
                    ctx=ctx, member=ctx.message.author, content=decrypted_message
                )
            else:
                await ctx.send("Not a valid encoding schema.")
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

        else:
            cmd_msg = "ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int = 1) -> None:
        """Delete given number of messages from channel.

        Args
            amount (int, optional): Number of messages to delete. Defaults to 1.
        """
        cmd = f"!clear {amount}"
        await ctx.message.delete()
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            if amount > 100:
                await ctx.send("You may not purge more than 99 messages.")
                cmd_msg = f"ERROR: Tried to delete too many messages."
            else:
                cmd_msg = f"Deleted {amount} messages."
                await ctx.channel.purge(limit=amount)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send(f"You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def whisper(self, ctx, member: discord.Member, *, message: str) -> None:
        """Send a DM to given user as Harbinger.

        Args:
            member (discord.Member): User to send DM to
            message (str): Message to send
        """
        cmd = f"!whisper({member})"
        await ctx.channel.purge(limit=1)
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Whispered: {message}"
            channel = await member.create_dm()
            await channel.send(message)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send(f"You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def code_whisper(
        self, ctx: commands.Context, code: str, member: discord.Member, *, message: str
    ) -> None:
        """Send encoded message in DM to given user as Harbinger.

        Args:
            code (str): Encoding schema to encrypt message (bin|b64|csr|hex)
            member (discord.Member): User to DM
            message (str): Message to encrypt and send
        """
        cmd = f"!code_whisper {code}{member}{message}"
        await ctx.channel.purge(limit=1)
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Whispered: {message}"
            recipient = await member.create_dm()
            sender = await ctx.message.author.create_dm()
            embed = discord.Embed(
                title="Ecrypted Transmission",
                description=f"from **{ctx.message.author}**",
                color=CUSTOM_COLOR,
            )
            if code == "bin":
                binary_message = "".join(
                    format(i, "08b") for i in bytearray(message, encoding="utf-8")
                )
                embed.add_field(name="Message", value=f"**``{binary_message}``**")
                await recipient.send(embed=embed)
            elif code == "csr":
                key = random.randint(1, 26)
                caeser_message = Moderation.caeser_cipher(key, message)
                caeser_key_embed = discord.Embed(
                    title="Caeser Cipher Key",
                    description="You will need to provide this key to your recipient for him/her to decode your message!",
                    color=CUSTOM_COLOR,
                )
                caeser_key_embed.add_field(
                    name="Recipient", value=f"**{member}**", inline=False
                )
                caeser_key_embed.add_field(
                    name="Message", value=f"**``{caeser_message}``**", inline=False
                )
                caeser_key_embed.add_field(name="Key", value=f"**``{key}``**")
                message_record = (
                    f"Ecrypted message:\n**``{caeser_message}``**\nKey:\n**``{key}``**"
                )
                embed.add_field(name="Message", value=f"**``{caeser_message}``**")
                await recipient.send(embed=embed)
                await sender.send(embed=caeser_key_embed)
            elif code == "hex":
                hex_message = message.encode("utf-8").hex()
                embed.add_field(name="Message", value=f"**``{hex_message}``**")
                await recipient.send(embed=embed)
            elif code == "b64":
                content_bytes = message.encode("ascii")
                base64_bytes = base64.b64encode(content_bytes)
                base64_message = str(base64_bytes, encoding="utf-8")
                embed.add_field(name="Message", value=f"**``{base64_message}``**")
                await recipient.send(embed=embed)
            else:
                await ctx.send(
                    "Please choose a valid encoding schema: binary [bin], hexadecimal [hex], or base64 [b64]."
                )
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def log(self, ctx: commands.Context, author: discord.Member = None):
        """Write channel history to log.txt file.

        Args:
            author (discord.Member, optional): User whose message history should be pulled. Defaults to None.
        """
        cmd = f"!log {author}"
        await ctx.channel.purge(limit=1)
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = "Wrote to log.txt"
            counter = 0
            filename = "log.txt"  # TODO: Make this part of the config.ini
            logfile = Path(filename)
            channel = await self.get_bot_channel()
            await ctx.channel.purge(limit=1)
            async with channel.typing():
                async for message in ctx.channel.history(limit=None):
                    if author != None:
                        if message.author == author:
                            entry = f"{counter + 1} - {message.created_at}: {message.content}\n"
                            author_log = Path(f"{author}.{logfile}")
                            with open(author_log, "a") as log:
                                log.write(entry)
                                counter += 1
                        else:
                            await channel.send(f"{author} not found in messages.")
                    elif author == None:
                        logfile = Path(filename)
                        entry = f"{counter+1} {message.created_at} - {message.author}: {message.content}\n"
                        with open(logfile, "a") as log:
                            log.write(entry)
                            counter += 1
                    else:
                        await ctx.send(
                            f"ERROR: If you've received this message, please file a bug report.\n!bug <exact message you attempted to send>."
                        )
            await channel.send("Wrote logs.")
        else:
            cmd_msg = "ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def history(self, ctx: commands.Context, amount: int):
        """Retrieve a number of messages from the channel history.

        Args:
            amount (int): Number of messages to retrieve
        """
        cmd = f"!history {amount}"
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Retrieved message history."
            counter = 0
            message_list = []
            channel = await self.get_bot_channel()
            async for message in ctx.channel.history(limit=amount):
                entry = f"{counter+1} {message.author}: {message.content}"
                message_list.append(entry)
                counter += 1
            await channel.send(message_list)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def serverinfo(self, ctx: commands.Context):
        """Create embeds containing server details and member information and send them to the channel."""
        cmd = "!serverinfo"
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = "Get details about the server."
            owner = str(ctx.guild.owner)
            guild_id = str(ctx.guild.id)
            member_count = str(ctx.guild.member_count)
            channel = await self.get_bot_channel()
            desc = ctx.guild.description

            embed = discord.Embed(
                title=ctx.guild.name + "Server Information",
                description=desc,
                color=CUSTOM_COLOR,
            )
            embed.set_thumbnail(ctx.guild.icon)
            embed.add_field(name="Owner", value=f"{owner}", inline=True)
            embed.add_field(name="Server ID", value=guild_id, inline=True)
            embed.add_field(name="Member Count", value=member_count, inline=True)
            await channel.send(embed=embed)
            members = []
            async for member in ctx.guild.fetch_members(limit=150):
                members_embed = discord.Embed(
                    title=f"{member.display_name}",
                    description=f"Status: {member.raw_status}",
                    color=int(member.color),
                )
                members_embed.add_field(
                    name="Member Since: ", value=f"{member.joined_at}"
                )
                members_embed.set_thumbnail(url=member.display_avatar.url)
                await channel.send(embed=members_embed)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def whois(self, ctx: commands.Context, member: discord.Member) -> None:
        """Get detailed information about given member.

        Args:
            member (discord.Member): Member to get info for (must be exact)
        """
        await ctx.channel.purge(limit=1)
        cmd = "!whois"
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Got whois info for {member}."
            whois_embed = discord.Embed(
                title=f"{member.display_name}",
                description=f"{member.desktop_status}",
                color=int(member.color),
            )
            whois_embed.add_field(name="Role:", value=f"{member.top_role}", inline=True)
            whois_embed.add_field(
                name="Joined:", value=f"{member.joined_at}", inline=True
            )
            whois_embed.set_image(url=member.display_avatar.url)
            await ctx.send(embed=whois_embed)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def code_say(self, ctx: commands.Context, code: str, *, message: str) -> None:
        """Send an encrypted message to the channel as Harbinger.

        Args:
            code (str): Encoding schema to use (bin|b64|csr|hex).
            message (str): Message to encrypt.
        """
        cmd = f"!code_say {code}"
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"{message}"
            await ctx.channel.purge(limit=1)
            if code == "bin":
                binary_message = "".join(
                    format(i, "08b") for i in bytearray(message, encoding="utf-8")
                )
                embed = discord.Embed(
                    title="Ecrypted Transmission",
                    description=f"**``{binary_message}``**",
                    color=CUSTOM_COLOR,
                )
                await ctx.send(embed=embed)
            elif code == "csr":
                sender = await ctx.author.create_dm()
                key = random.randint(1, 26)
                caeser_message = Moderation.caeser_cipher(key, message)
                caeser_key_embed = discord.Embed(
                    title="Caeser Cipher Key",
                    description="You will need to provide this key to your recipient for him/her to decode your message!",
                    color=CUSTOM_COLOR,
                )
                caeser_key_embed.add_field(
                    name="Recipient", value=f"**{ctx.channel}**", inline=False
                )
                caeser_key_embed.add_field(
                    name="Message", value=f"**``{caeser_message}``**", inline=False
                )
                caeser_key_embed.add_field(name="Key", value=f"**``{key}``**")
                embed = discord.Embed(
                    title="Ecrypted Transmission",
                    description=f"**``{caeser_message}``**",
                    color=CUSTOM_COLOR,
                )
                await ctx.send(embed=embed)
                await sender.send(embed=caeser_key_embed)
            elif code == "hex":
                hex_message = message.encode("utf-8").hex()
                embed = discord.Embed(
                    title="Ecrypted Transmission",
                    description=f"**``{hex_message}``**",
                    color=CUSTOM_COLOR,
                )
                await ctx.send(embed=embed)
            elif code == "b64":
                content_bytes = message.encode("ascii")
                base64_bytes = base64.b64encode(content_bytes)
                base64_message = str(base64_bytes, encoding="utf-8")
                embed = discord.Embed(
                    title="Ecrypted Transmission",
                    description=f"**``{base64_message}``**",
                    color=CUSTOM_COLOR,
                )
                await ctx.send(embed=embed)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def say(self, ctx: commands.Context, *message: str) -> None:
        """Send a message as Harbinger.

        Args:
            message (str): Message to send
        """
        cmd = f"!say({message})"
        await ctx.channel.purge(limit=1)
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Harbinger says: {message}"
            string_message = ""
            for word in message:
                string_message = string_message + str(word) + " "
            content = string_message.strip()
            await ctx.send(f"{content}")
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def embed(
        self,
        ctx: commands.Context,
        title: str = None,
        description: str = None,
        image: str = None,
        url: str = None,
    ):
        """Send an embed to the channel as Harbinger.

        Args:
            title (str, optional): Title of the embed. Defaults to None.
            description (str, optional): Description of embed. Defaults to None.
            image (str, optional): Image to embed (must be https url). Defaults to None.
            url (str, optional): url to link (must be https). Defaults to None.
        """
        await ctx.channel.purge(limit=1)
        cmd = f"!embed {title},{description},{image},{url}"
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Harbinger sent an embed."
            embed = discord.Embed(
                title=title, description=description, color=CUSTOM_COLOR, url=url
            )
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute that command.")
        Harbinger.timestamp(ctx.author, cmd, cmd_msg)

    @commands.command()
    async def playing(
        self,
        ctx: commands.Context,
        game: str,
        description: str = None,
        field=None,
        value=None,
    ) -> None:
        """Send an embed to the channel as Harbinger, intended to aid sharing server IPs, room codes, etc.

        Args:
            game (str): Name of game
            description (str, optional): Further info
            field (any, optional): Title of optional field. Defaults to None.
            value (any, optional): Value of optional field. Defaults to None.
        """
        cmd = f"!playing({game}, {field}, {value})"
        if Harbinger.is_admin(self, ctx, ctx.message.author) == True:
            cmd_msg = f"Created playing embed with these values: {game},{field},{value}"
            playing_embed = discord.Embed(title=f"{game}", description=f"{description}")
            playing_embed.add_field(name=f"{field}", value=f"{value}")
            await ctx.send(embed=playing_embed)
        else:
            cmd_msg = f"ERROR: Missing Admin role."
            await ctx.send("You must have Admin role to execute this command.")
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Moderation(bot))
