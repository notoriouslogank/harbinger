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
                card1 = cards["cards"][0]["image"]
                card1_value = cards["cards"][0]["value"]
                card2 = cards["cards"][1]["image"]
                card2_value = cards["cards"][1]["value"]
                card3 = cards["cards"][2]["image"]
                card3_value = cards["cards"][2]["value"]
                card4 = cards["cards"][3]["image"]
                card4_value = cards["cards"][3]["value"]
                player_hand = f'{card3}\n{card4}'
                player_total = f'Total: {str(int(card3_value)) + int(card4_value)}'
                player_message = f'{player_hand}\n'
                dealer_total = f'Total: {str(int(card1_value)) + int(card2_value)}'
                await ctx.send(f'{card1}\n{card2}')
                await ctx.send(dealer_total)
                await Harbinger.send_dm(ctx=ctx, member=ctx.message.author, content=player_message)
                await Harbinger.send_dm(ctx=ctx, member=ctx.message.author, content=player_total)
async def setup(bot):
    await bot.add_cog(Cards(bot))