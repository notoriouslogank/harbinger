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
                dealer_hand = [cards["cards"][0]["value"], cards["cards"][1]["value"]]
                player_hand = [cards["cards"][2]["value"], cards["cards"][3]["value"]]
                hands = dealer_hand, player_hand
                faces = "KING", "QUEEN", "JACK"
                print(f"Starting hand: {dealer_hand}")
                print(f"Player hand: {player_hand}")
                
                for hand in hands:
                    for card in hand:
                        if card == "ACE":
                            hand.insert(0, 11)
                            hand.remove("ACE")
                #for hand in hands:
                #    for card in hand:
                        if card in faces:
                            hand.insert(0, 10)
                            hand.remove(card)
                        else:
                            hand.insert(0, int(card))
                            hand.remove(card)
                                
                print(f"dealer: {dealer_hand}")
                
                print(f"player: {player_hand}")

                
                
                #for card in dealer_hand:
                #    print(card)
                    #if card in face_cards:
                    #    print(f'Face card: {card}')
                    #elif card == "ACE":
                    #    print(f'ACE')
                    #else:
                    #    print(int(card))
                        
                #dealer_hand.append((cards["cards"][0]["image"]))
                #dealer_hand.append((int(cards["cards"][0]["value"])))
                #dealer_hand.append(cards["cards"][1]["image"])
                #dealer_hand.append(int(cards["cards"][1]["value"]))
                
                #for card in dealer_hand:
                ##    if card in face_cards:
                 #       print(f"Face card: {card}")
                 #   elif card == "ACE":
                 #       print(f'Ace')
                 #   else:
                 #       print("ok?")
                
                
                #dealer_total = dealer_hand[1] + dealer_hand[3]
                        
                    
                #dealer_hand = []
                #print(f"{dealer_hand}\nTotal: {dealer_total}")

                # card1_value = int(cards["cards"][0]["value"])


async def setup(bot):
    
    await bot.add_cog(Cards(bot))
