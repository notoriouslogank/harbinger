import aiohttp
import discord
from discord.ext import commands
import json
from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger

CUSTOM_COLOR = configs.custom_color()


class Cards(commands.Cog):

    def sanitize_cards(hand):
            faces = "KING", "QUEEN", "JACK"
            int_cards = []
            
            for card in hand:
                if card == "ACE":
                    hand.insert(0, 11)
                    hand.remove("ACE")
                if card in faces:
                    hand.insert(0, 10)
                    hand.remove(card)
            
            for card in hand:
                card = int(card)
                int_cards.append(card)
                
            total = sum(int_cards)
            return total


    @commands.command()
    async def blackjack(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://deckofcardsapi.com/api/deck/new/draw/?count=4"
            ) as cards_json:
                await ctx.message.delete()
                message = await ctx.send("Dealing...")
                # Get cards
                cards = await cards_json.json()
                dealer_hand_codes = [cards["cards"][0]["code"], cards["cards"][1]["code"]]
                player_hand_codes = [cards["cards"][2]["code"], cards["cards"][3]["code"]]
                dealer_hand_values = [cards["cards"][0]["value"], cards["cards"][1]["value"]]
                player_hand_values = [cards["cards"][2]["value"], cards["cards"][3]["value"]]
                # Sanitize
                dealer_total = Cards.sanitize_cards(dealer_hand_values)
                player_total = Cards.sanitize_cards(player_hand_values)

                # Print Hand to player quietly
                await ctx.send(f"{ctx.message.author.mention}\nHand: {player_hand_codes[0]} {player_hand_codes[1]}\nTotal: {player_total}")
                # Print to bot loudly
                await ctx.send(f"{ctx.message.author.mention}\nHand:\n _____ \n|\ ~ /|\n|}}:{{|\n|}}:{{|\n|}}:{{|\n|/_~_\|\n {dealer_hand_codes[1]}\nTotal: {dealer_total}")
                
#      _____ 
#     |\ ~ /|
#     |}}:{{|
#     |}}:{{|
#     |}}:{{|
#     |/_~_\|
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
