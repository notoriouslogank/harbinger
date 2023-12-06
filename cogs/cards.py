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
            async with session.get(f'https://deckofcardsapi.com/api/deck/new/draw/?count=4') as cards_json:
                await ctx.message.delete()
                message = await ctx.send("Dealing...")
                cards = await cards_json.json()
                dealer_one_image = cards["cards"][0]["image"]
                dealer_one_value = int(cards["cards"][0]["value"])
                dealer_two_image = cards["cards"][1]["image"]
                dealer_two_value = int(cards["cards"][1]["value"])
                dealer_total = dealer_one_value-dealer_two_value
                print(dealer_one_value, dealer_two_value, dealer_total)
                # card1_value = int(cards["cards"][0]["value"])
                

async def setup(bot):
    await bot.add_cog(Cards(bot))