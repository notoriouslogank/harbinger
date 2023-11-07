from discord.ext import commands
import helpers
import discord
from random import randint

class Tools(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def lmgtfy(self, ctx: commands.Context, query: str):
        google = "https://google.com/search?q="
        search = google + query
        embed = discord.Embed(color=purple, title="LMGTFY")
        embed.description = (f'[Here]({search}), let me Google that for you!')
        print(f'LMGTFY: {search}')
        helpers.timestamp()
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
        await helpers.send_dm(ctx=ctx, member=ctx.message.author, content=query)
        
    @commands.command()
    async def add(self, ctx: commands.Context, left: int, right: int):
        total = left + right
        print(f'{left} + {right} = {total}')
        helpers.timestamp()
        await ctx.send(f'{total}')
        
    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.send("Format must be NdN!")
            return
        result = ", ".join(str(randint(1, limit)) for r in range(rolls))
        print(f'Roll: {result}')
        helpers.timestamp()
        await ctx.send(f'{result}')    
            
    @commands.command()
    async def rps(self, ctx: commands.Context, choice: str):
        choices = ["rock", "paper", "scissors"]
        botChoice = choices[randint(0, 2)]
        embedRPS = discord.Embed(color=purple, title="rock, paper, scissors")
        embedRPS.add_field(name="You", value=f'{choice}', inline=True)
        embedRPS.add_field(name="Bot", value=f'{botChoice}', inline=True)
        if choice == botChoice:
            embedRPS.add_field(name="result", value="You tied!", inline=False)
            await ctx.send(embed=embedRPS)
        elif botChoice == "rock" and choice == "paper":
            embedRPS.add_field(name="result", value="You win!", inline=False)
            await ctx.send(embed=embedRPS)
        elif botChoice == "paper" and choice == "scissors":
            embedRPS.add_field(name="result", value="You win!", inline=False)
            await ctx.send(embed=embedRPS)
        elif botChoice == "scissors" and choice == "rock":
            embedRPS.add_field(name="result", value="You win!", inline=False)
            await ctx.send(embed=embedRPS)
        elif choice not in choices:
            await ctx.send('Please choose rock, paper, or scissors.')
        else:
            embedRPS.add_field(name="result", value="You lose!", inline=False)
            await ctx.send(embed=embedRPS)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Tools(bot))