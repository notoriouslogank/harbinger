import discord
from discord.ext import commands
from harbinger import Harbinger
from config.read_configs import ReadConfigs as configs

CUSTOM_COLOR = configs.custom_color()

# Major Keys

c = ["C", "Dm", "Em", "F", "G", "Am", "Bdim"]
db = ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"]
d = ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"]
eb = ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"]
e = ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"]
f = ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
gb = ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fdim"]
g = ["G", "Am", "Bm", "C", "D", "Em", "F#dim"]
ab = ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"]
a = ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"]
bb = ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"]
b = ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"]

major_keys = {
    "C": c,
    "Db": db,
    "D": d,
    "Eb": eb,
    "E": e,
    "F": f,
    "Gb": gb,
    "G": g,
    "Ab": ab,
    "A": a,
    "Bb": bb,
    "B": b,
}

# Minor Keys
cm = ["Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb"]
cshm = ["C#m", "D#dim", "E", "F#m", "G#m", "A", "B"]
dm = ["Dm", "Edim", "F", "Gm", "Am", "Bb", "C"]
ebm = ["Ebm", "Fbdim", "Gb", "Abm", "Bbm", "Cb", "Db"]
em = ["Em", "F#dim", "G", "Am", "Bm", "C", "D"]
fm = ["Fm", "Gdim", "Ab", "Bbm", "Cm", "Db", "Eb"]
fshm = ["F#m", "G#dim", "A", "Bm", "C#m", "D", "E"]
gm = ["Gm", "Adim", "Bb", "Cm", "Dm", "Eb", "F"]
gshm = ["G#m", "A#dim", "B", "C#m", "D#m", "E", "F#"]
am = ["Am", "Bdim", "C", "Dm", "Em", "F", "G"]
bbm = ["Bbm", "Cdim", "Db", "Ebm", "Fm", "Gb", "Ab"]
bm = ["Bm", "C#dim", "D", "Em", "F#m", "G", "A"]

minor_keys = {
    "Am": am,
    "Bbm": bbm,
    "Bm": bm,
    "Cm": cm,
    "C#m": cshm,
    "Dm": dm,
    "Ebm": ebm,
    "Em": em,
    "Fm": fm,
    "F#m": fshm,
    "Gm": gm,
    "G#m": gshm,
}


class MajorKeys:

    def __init__(self, key):
        self.i = key[0]
        self.ii = key[1]
        self.iii = key[2]
        self.iv = key[3]
        self.v = key[4]
        self.vi = key[5]
        self.vii = key[6]

    def chords(self):
        chords = f"{self.i} {self.ii} {self.iii} {self.iv} {self.v} {self.vi} {self.vii}"
        return chords

    def progressions(self):
        # I IV vi V
        progression1 = f"{self.i} {self.iv} {self.vi} {self.v}"
        print(f"Progression 1: I IV vi V\n{progression1}")
        # I IV I V
        progression2 = f"{self.i} {self.iv} {self.i} {self.v}"
        print(f"Progression 2: I IV I V\n{progression2}")
        # I V IV V
        progression3 = f"{self.i} {self.v} {self.iv} {self.v}"
        print(f"Progression 3: I V IV V\n{progression3}")
        # I vi IV V
        progression4 = f"{self.i} {self.vi} {self.iv} {self.v}"
        print(f"Progression 4: I vi IV V\n{progression4}")


class MinorKeys:

    def __init__(self, key):
        self.i = key[0]
        self.ii = key[1]
        self.iii = key[2]
        self.iv = key[3]
        self.v = key[4]
        self.vi = key[5]
        self.vii = key[6]

    def chords(self):
        chords = f"{self.i} {self.ii} {self.iii} {self.iv} {self.v} {self.vi} {self.vii}"
        return chords

    def progressions(self):
        # i iv v i
        progression1 = f"{self.i} {self.iv} {self.v} {self.i}"
        print(f"Progression 1: i iv v i\n{progression1}")
        # i ii v i
        progression2 = f"{self.i} {self.ii} {self.v} {self.i}"
        print(f"Progression 2: i ii v i\n{progression2}")
        # i bVI bIII bVII
        progression3 = f"{self.i} {self.vi} {self.iii} {self.vii}"
        print(f"Progression 3: i VI III VII\n{progression3}")
        # i bVII bVI bVII i
        progression4 = f"{self.i} {self.vii} {self.vi} {self.vii} {self.i}"
        print(f"Progression 4: i VII VI VII i\n{progression4}")


class Keyfinder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def keyfinder(self, ctx, key):
        key = key.capitalize()
        if key in major_keys.keys():
            maj = MajorKeys(major_keys.pop(key))
            embed_title = f"Key of {key}"
            embed_descrpition = maj.chords()
            embed = discord.Embed(title=embed_title, description=embed_descrpition, color=CUSTOM_COLOR)
            embed.add_field(name="I IV vi V", value=f"{maj.i} {maj.iv} {maj.vi} {maj.v}", inline=False)
            embed.add_field(name="I IV I V", value=f"{maj.i} {maj.iv} {maj.i} {maj.v}", inline=False)
            embed.add_field(name="I V IV V", value=f"{maj.i} {maj.v} {maj.iv} {maj.v}", inline=False)
            embed.add_field(name="I vi IV V", value=f"{maj.i} {maj.vi} {maj.iv} {maj.v}", inline=False)
            await ctx.send(embed=embed)
        if key in minor_keys.keys():
            min = MinorKeys(minor_keys.pop(key))
            embed_title = f"Key of {key}"
            embed_description = min.chords()
            embed = discord.Embed(title=embed_title, description=embed_description, color=CUSTOM_COLOR)
            embed.add_field(name="i iv v i", value=f"```{min.i} {min.iv} {min.v} {min.i}```", inline=False)
            embed.add_field(name="i ii v i", value=f"```{min.i} {min.ii} {min.v} {min.i}```", inline=False)
            embed.add_field(name="i VI III VII", value=f"```{min.i} {min.vi} {min.iii} {min.vii}```", inline=False)
            embed.add_field(name="i VII VI VII i", value=f"```{min.i} {min.vii} {min.vi} {min.vii} {min.i}```")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Please choose a valid key.")

async def setup(bot):
    await bot.add_cog(Keyfinder(bot))