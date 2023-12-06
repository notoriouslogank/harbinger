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
                if card1_value == "ACE":
                    card1_value = 11
                if card1_value == "JACK":
                    card1_value = 10
                if card1_value == "QUEEN":
                    card1_value = 10
                if card1_value == "KING":
                    card1_value = 10
                card2 = cards["cards"][1]["image"]
                card2_value = cards["cards"][1]["value"]
                if card2_value == "ACE":
                    card2_value = 11
                if card2_value == "JACK":
                    card2_value = 10
                if card2_value == "QUEEN":
                    card2_value = 10
                if card2_value == "KING":
                    card2_value = 10
                card3 = cards["cards"][2]["image"]
                card3_value = cards["cards"][2]["value"]
                if card3_value == "ACE":
                    card3_value = 11
                if card3_value == "JACK":
                    card3_value = 10
                if card3_value == "QUEEN":
                    card3_value = 10
                if card3_value == "KING":
                    card3_value = 10
                card4 = cards["cards"][3]["image"]
                card4_value = cards["cards"][3]["value"]
                if card4_value == "ACE":
                    card4_value = 11
                if card4_value == "JACK":
                    card4_value = 10
                if card4_value == "QUEEN":
                    card4_value = 10
                if card4_value == "KING":
                    card4_value = 10
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