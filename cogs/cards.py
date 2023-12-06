import aiohttp
import discord
from discord.ext import commands
import json
from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()

class Cards(commands.Cog):
    
    @commands.command()
    async def blackjack(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://deckofcardsapi.com/api/deck/new/draw/?count=2') as cards_json:
                await ctx.message.delete()
                message = await ctx.send("Dealing...")
                cards = await cards_json.json()
                card1 = cards["cards"][0]["image"]
                card2 = cards["cards"][1]["image"]
                await ctx.send(f'{card1}\n{card2}')