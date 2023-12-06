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
            async with session.get(
                f"https://deckofcardsapi.com/api/deck/new/draw/?count=4"
            ) as cards_json:
                await ctx.message.delete()
                message = await ctx.send("Dealing...")
                cards = await cards_json.json()
                dealer_hand = []
                (cards["cards"][0]["image"]).append[dealer_hand]
                (int(cards["cards"][0]["value"])).append[dealer_hand]
                cards["cards"][1]["image"].append[dealer_hand]
                int(cards["cards"][1]["value"]).append[dealer_hand]
                dealer_total = dealer_hand[1] + dealer_hand[3]
                print(f"{dealer_hand}\nTotal: {dealer_total}")

                # card1_value = int(cards["cards"][0]["value"])


async def setup(bot):
    await bot.add_cog(Cards(bot))
