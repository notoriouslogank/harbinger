from random import randint

from discord.ext import commands

from assets import urls
from harbinger import Harbinger

lol = urls.LOL
wtf = urls.WTF
no = urls.NO
yes = urls.YES
fu = urls.FU
sorry = urls.SORRY
hi = urls.HI
bye = urls.BYE
bored = urls.BORED
shook = urls.SHOOK
angry = urls.ANGRY
sad = urls.SAD
trump = urls.TRUMP
biden = urls.BIDEN

BINGO = [
    "Trump stalks Biden like prey",
    "Biden offers to fight",
    "Biden loses his train of thought",
    "'Bigly'",
    "Fly lands on someone's head",
    "Both candidates get muted",
    "Biden gets muted",
    "Trump gets muted",
    "Biden freezes",
    "Biden wanders off",
    "'Malarkey'",
    "'Not a joke'",
    "'Gina'",
    "'Will you shut up man?'",
    "'Sleepy Joe'",
    "'Creepy Joe'",
    "Burisma",
    "Cocaine",
    "'Come on, man!'",
    "'The sould of democracy'",
    "'Build the wall'",
    "Russia",
    "'No tax off tips'",
    "Student loans",
    "Mentally unfit",
    "'Rigged'",
    "January 6",
    "'Insurrection'",
    "'MAGA Republicans'",
    "'Convicted felon'",
    "'Hilary'",
    "Laptop from Hell",
    "'Look, folks...'",
    "Candidate told time is up",
    "'COVID'",
    "Biden refers to a dead person",
    "TikTok",
    "Hamas",
    "'Fine people' hoax",
    "'Let's go Brandon'",
    "'FJB'",
    "Fani Willis",
    "Obama",
    "'Crooked'",
    "'Mar-a-lago'",
    "Drug test",
]


class React(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def bingo_card(self, ctx: commands.Context):
        cmd = "!bingo_card"
        cmd_msg = "Make bingo card."
        await ctx.channel.purge(limit=1)
        row = [
            BINGO[randint(0, 6)],
            BINGO[randint(0, 6)],
            BINGO[randint(0, 6)],
            BINGO[randint(0, 6)],
            BINGO[randint(0, 6)],
        ]
        # counter = 5
        # row.append(BINGO[randint(0, len(BINGO) - 1)])
        # card.append(row)
        await ctx.channel.send(row)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def biden(self, ctx: commands.Context):
        cmd = "!biden"
        cmd_msg = "FJB"
        await ctx.channel.purge(limit=1)
        reaction = biden[randint(0, len(biden) - 1)]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def trump(self, ctx: commands.Context):
        cmd = "!trump"
        cmd_msg = "Trump 2024"
        await ctx.channel.purge(limit=1)
        reaction = trump[randint(0, len(trump) - 1)]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def bored(self, ctx: commands.Context):
        cmd = "!bored"
        cmd_msg = "Bored"
        await ctx.channel.purge(limit=1)
        reaction = bored[randint(0, (len(bored) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def shook(self, ctx: commands.Context):
        cmd = "!shook"
        cmd_msg = "Shook"
        await ctx.channel.purge(limit=1)
        reaction = shook[randint(0, (len(shook) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def angry(self, ctx: commands.Context):
        cmd = "!angry"
        cmd_msg = "Angry"
        await ctx.channel.purge(limit=1)
        reaction = angry[randint(0, (len(angry) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def sad(self, ctx: commands.Context):
        cmd = "!sad"
        cmd_msg = "Sad"
        await ctx.channel.purge(limit=1)
        reaction = sad[randint(0, (len(sad) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def yes(self, ctx: commands.Context):
        cmd = "!yes"
        cmd_msg = "Yes"
        await ctx.channel.purge(limit=1)
        reaction = yes[randint(0, (len(yes) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def no(self, ctx: commands.Context):
        cmd = "!no"
        cmd_msg = "No"
        await ctx.channel.purge(limit=1)
        reaction = no[randint(0, (len(no) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def lol(self, ctx: commands.Context):
        cmd = "!lol"
        cmd_msg = "LOL"
        await ctx.channel.purge(limit=1)
        reaction = lol[randint(0, (len(lol) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def wtf(self, ctx: commands.Context):
        cmd = "!wtf"
        cmd_msg = "WTF?"
        await ctx.channel.purge(limit=1)
        reaction = wtf[randint(0, (len(wtf) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def sorry(self, ctx: commands.Context):
        cmd = "!sorry"
        cmd_msg = "Sorry"
        await ctx.channel.purge(limit=1)
        reaction = sorry[randint(0, (len(sorry) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def fu(self, ctx: commands.Context):
        cmd = "!fu"
        cmd_msg = "Fuck you"
        await ctx.channel.purge(limit=1)
        reaction = fu[randint(0, (len(fu) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def hi(self, ctx: commands.Context):
        cmd = "!hi"
        cmd_msg = "Hi!"
        await ctx.channel.purge(limit=1)
        reaction = hi[randint(0, (len(hi) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)

    @commands.command()
    async def bye(self, ctx: commands.Context):
        cmd = "!bye"
        cmd_msg = "Goodbye!"
        await ctx.channel.purge(limit=1)
        reaction = bye[randint(0, (len(bye) - 1))]
        await ctx.send(reaction)
        Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)


async def setup(bot):
    await bot.add_cog(React(bot))
