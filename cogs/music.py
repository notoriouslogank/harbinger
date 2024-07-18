import asyncio

import discord
import yt_dlp
from discord.ext import commands
from rich import print as pprint

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()
bot = Harbinger.bot
players = {}


ytdl_format_options = {
    "format": "bestaudio/best",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logstostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
}

ffmpeg_options = {"options": "-vn"}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    """Class to configure FFMpeg and yt-dlp to interact with commands.

    Args:
        discord (obj): discord.PCMVolumeTransformer
    """

    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        """Download or stream data from provided URL.

        Args:
            url (str): URL to be downloaded
            loop (optional): Defaults to None.
            stream (bool, optional): Whether to download or stream the data. Defaults to False.

        Returns:
            cls: An FFmpeg object?
        """
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=not stream)
        )

        if "entries" in data:
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    """A class of commands for streaming music via the bot in the voice channel."""

    music_queue = []

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Join the bot to the contextual voice channel."""
        cmd = "!join"
        cmd_msg = f"Added bot to voice channel."
        channel = ctx.message.author.voice.channel
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        """Leave the voice channel."""
        cmd = "!leave"
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            cmd_msg = f"Removed bot from voice channel."
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await voice_client.disconnect()
        else:
            cmd_msg = f"Failed to remove bot from channel (not in channel)."
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await ctx.send("Bot is not currently in a channel...")

    @commands.command()
    async def pause(self, ctx):
        """Pause the currently-playing song/video."""
        cmd = "!resume"
        cmd_msg = "Paused playback."
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            voice_client.pause()
            await ctx.send("Paused playback.")
        else:
            await ctx.send("Nothing playing.")

    @commands.command()
    async def resume(self, ctx) -> None:
        """Resume playback of a previously-paused video/song."""
        cmd = "!play"
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            cmd_msg = "Resumed playback."
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await ctx.send("Resuming playback.")
            voice_client.resume()
        else:
            cmd_msg = "Tried to resume playback; nothing playing."
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await ctx.send("Bot not paused...")

    @commands.command()
    async def stop(self, ctx: commands.Cog) -> None:
        """Stops playback."""
        cmd = "!stop"
        cmd_msg = f"{ctx.message.author} stopped playback."
        voice_client = ctx.message.guild.voice_client
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
        if voice_client.is_playing():
            voice_client.stop()
            await ctx.send("Stopping...")

    @commands.command()
    async def nq(self, ctx, *, search_term):
        """Enqueues track.

        Args:
            search_term (str): _description_
        """
        cmd = f"!nq {search_term}"
        cmd_msg = f"{search_term} added to queue."
        self.music_queue.append(search_term)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    def make_queue_dict(
        self,
    ):  # This is probably a retarded way of doing things but I couldn't find a better way
        """Creates a tracklist dictionary.

        Returns:
            queue_dict: Dictionary containing tracks in the queue
        """
        queue_dict = {}
        counter = 0
        queue = self.music_queue[:]
        for item in queue:
            queue_dict[f"{counter+1}"] = item
            counter += 1
        return queue_dict

    def make_queue_list(self):
        """Cast the queue dict to a more easily-printable string

        Returns:
            queue_list (list): List version of track queue
        """
        queue = self.make_queue_dict()
        queue_list = []
        for i in queue:
            track = f"{i}: {queue[i]}"
            queue_list.append(track)
        return queue_list

    @commands.command()
    async def queue(self, ctx):
        """Display the music queue."""
        cmd = f"!queue"
        cmd_msg = f"Printed music queue."
        queue = self.make_queue_list()
        if queue == None:
            queue_embed = discord.Embed(
                color=CUSTOM_COLOR,
                title=f"Queue Empty",
                description=queue,
            )
        else:
            queue_embed = discord.Embed(
                color=CUSTOM_COLOR,
                title=f"Songs in Queue",
                description=queue,
            )
        await ctx.send(embed=queue_embed)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def play(self, ctx, *, url: str = None) -> None:
        """Begin streaming audio from the given url.

        Args:
            url (str): YouTube search term from which to stream audio.
        """
        cmd = f"!play {url}"

        self.music_queue.append(url)
        async with ctx.typing():
            while self.music_queue != None:
                try:
                    player = await YTDLSource.from_url(
                        self.music_queue.pop(0), loop=self.bot.loop, stream=True
                    )
                    cmd_msg = f"Started playing queue"
                    ctx.voice_client.play(
                        player,
                        after=lambda e: asyncio.run_coroutine_threadsafe(
                            ctx.voice_client.play(player), bot.loop
                        ),
                    )

                except IndexError:
                    await ctx.send(f"Nothing in the queue. Or something got fucked.")
                Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @play.before_invoke
    async def ensure_voice(self, ctx) -> None:
        """Ensure that the ctx.message.author is actively in a voice channel.

        Raises:
            commands.CommandError: Raises when the command is invoked by someone not in a voice channel.
        """
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You must be connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Music(bot))
