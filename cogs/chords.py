import discord
from discord.ext import commands
from harbinger import Harbinger
from config.read_configs import ReadConfigs as configs

CUSTOM_COLOR = configs.custom_color()

## Triads
# C
c_triad = ["C", "E", "G"]
cm_triad = ["C", "Eb", "G"]
csh_triad = ["C#", "E#", "G#"]
cshm_triad = ["C#", "E", "G#"]
# D
d_triad = ["D", "F#", "A"]
dm_triad = ["D", "F", "A"]
dsh_triad = ["D#", "F", "A#"]
dshm_triad = ["D#", "F#", "A#"]
# E
e_triad = ["E", "G#", "B"]
em_triad = ["E", "G", "B"]
# F
f_triad = ["F", "A", "C"]
fm_triad = ["F", "Ab", "C"]
fsh_triad = ["F#", "A#", "C#"]
fshm_triad = ["F#", "A", "C#"]
# G
g_triad = ["G", "B", "D"]
gm_triad = ["G", "Bb", "D"]
gsh_triad = ["G#", "B#", "D#"]
gshm_triad = ["G#", "B", "D#"]
# A
a_triad = ["A", "C#", "E"]
am_triad = ["A", "C", "E"]
ash_triad = ["A#", "C#", "E#"]
ashm_triad = ["A#", "C", "E#"]
# B
b_triad = ["B", "D#", "F#"]
bm_triad = ["B", "D", "F#"]

## Notation
# Unplayed String
x = "--"
# Open String
o = "-0"
# Space
space = "-"

## Power Chords
# major
a5 = {"e": x, "B": x, "G": x, "D": "-7", "A": "-7", "E": "-5", "triad": a_triad}
b5 = {"e": x, "B": x, "G": x, "D": "-9", "A": "-9", "E": "-7", "triad": b_triad}
c5 = {"e": x, "B": x, "G": x, "D": "10", "A": "10", "E": "-8", "triad": c_triad}
d5 = {"e": x, "B": x, "G": x, "D": "12", "A": "12", "E": "10", "triad": d_triad}
e5 = {"e": x, "B": x, "G": "-9", "D": "-9", "A": "-7", "E": x, "triad": e_triad}
f5 = {"e": x, "B": x, "G": x, "D": "-3", "A": "-3", "E": "-1", "triad": f_triad}
g5 = {"e": x, "B": x, "G": x, "D": "-5", "A": "-5", "E": "-3", "triad": g_triad}
# minor
a5m = {"e": x, "B": x, "G": x, "D": "-7", "A": "-6", "E": "-5", "triad": am_triad}
b5m = {"e": x, "B": x, "G": x, "D": "-9", "A": "-8", "E": "-7", "triad": bm_triad}
c5m = {"e": x, "B": x, "G": x, "D": "10", "A": "-9", "E": "-8", "triad": cm_triad}
d5m = {"e": x, "B": x, "G": x, "D": "12", "A": "11", "E": "10", "triad": dm_triad}
e5m = {"e": x, "B": x, "G": "-9", "D": "-8", "A": "-7", "E": x, "triad": em_triad}
f5m = {"e": x, "B": x, "G": x, "D": "-3", "A": "-2", "E": "-1", "triad": fm_triad}
g5m = {"e": x, "B": x, "G": x, "D": "-5", "A": "-4", "E": "-3", "triad": gm_triad}
# sharp major
ash5 = {"e": x, "B": x, "G": x, "D": "-8", "A": "-8", "E": "-6", "triad": ash_triad}
csh5 = {"e": x, "B": x, "G": x, "D": "11", "A": "11", "E": "-9", "triad": csh_triad}
dsh5 = {"e": x, "B": x, "G": x, "D": "13", "A": "13", "E": "11", "triad": dsh_triad}
fsh5 = {"e": x, "B": x, "G": x, "D": "-4", "A": "-4", "E": "-2", "triad": fsh_triad}
gsh5 = {"e": x, "B": x, "G": x, "D": "-6", "A": "-6", "E": "-4", "triad": gsh_triad}
# sharp minor
ash5m = {"e": x, "B": x, "G": x, "D": "-8", "A": "-7", "E": "-6", "triad": ashm_triad}
csh5m = {"e": x, "B": x, "G": x, "D": "11", "A": "10", "E": "-9", "triad": cshm_triad}
dsh5m = {"e": x, "B": x, "G": x, "D": "13", "A": "12", "E": "11", "triad": dshm_triad}
fsh5m = {"e": x, "B": x, "G": x, "D": "-4", "A": "-3", "E": "-2", "triad": fshm_triad}
gsh5m = {"e": x, "B": x, "G": x, "D": "-6", "A": "-5", "E": "-4", "triad": gshm_triad}

power_chords = {
    "A": a5,
    "A#": ash5,
    "Am": a5m,
    "A#m": ash5m,
    "B": b5,
    "Bm": b5m,
    "C": c5,
    "C#": csh5,
    "Cm": c5m,
    "C#m": c5m,
    "D": d5,
    "D#": dsh5,
    "Dm": d5m,
    "D#m": dsh5m,
    "E": e5,
    "Em": e5m,
    "F": f5,
    "F#": fsh5,
    "Fm": f5m,
    "F#m": fsh5m,
    "G": g5,
    "G#": gsh5,
    "Gm": g5m,
    "G#m": gsh5m,
}
## Open Chords
# major
a = {"e": o, "B": "-2", "G": "-2", "D": "-2", "A": o, "E": x, "triad": a_triad}
b = {"e": "-2", "B": "-4", "G": "-4", "D": "-4", "A": "-2", "E": x, "triad": b_triad}
c = {"e": o, "B": "-1", "G": o, "D": "-2", "A": "-3", "E": x, "triad": c_triad}
d = {"e": "-2", "B": "-3", "G": "-2", "D": o, "A": x, "E": x, "triad": d_triad}
e = {"e": o, "B": o, "G": "-1", "D": "-2", "A": "-2", "E": o, "triad": e_triad}
f = {"e": "-1", "B": "-1", "G": "-2", "D": "-3", "A": x, "E": x, "triad": f_triad}
g = {"e": "-3", "B": o, "G": o, "D": o, "A": "-2", "E": "-3", "triad": g_triad}
# minor
am = {"e": o, "B": "-1", "G": "-2", "D": "-2", "A": o, "E": x, "triad": am_triad}
bm = {"e": "-2", "B": "-3", "G": "-4", "D": "-4", "A": "-2", "E": x, "triad": bm_triad}
cm = {"e": o, "B": "-1", "G": o, "D": "-1", "A": "-3", "E": x, "triad": cm_triad}
dm = {"e": "-1", "B": "-3", "G": "-2", "D": o, "A": x, "E": x, "triad": dm_triad}
em = {"e": o, "B": o, "G": o, "D": "-2", "A": "-2", "E": o, "triad": em_triad}
fm = {
    "e": "-1",
    "B": "-1",
    "G": "-1",
    "D": "-3",
    "A": "-3",
    "E": "-1",
    "triad": fm_triad,
}
gm = {"e": "-3", "B": "-3", "G": o, "D": o, "A": "-1", "E": "-3", "triad": gm_triad}
# sharp major
ash = {"e": "-1", "B": "-3", "G": "-3", "D": "-3", "A": x, "E": x, "triad": ash_triad}
csh = {"e": "-1", "B": "-2", "G": "-1", "D": "-3", "A": x, "E": x, "triad": csh_triad}
dsh = {"e": x, "B": "-8", "G": "-8", "D": "-8", "A": "-6", "E": x, "triad": dsh_triad}
fsh = {
    "e": "-2",
    "B": "-2",
    "G": "-3",
    "D": "-4",
    "A": "-4",
    "E": "-2",
    "triad": fsh_triad,
}
gsh = {
    "e": "-4",
    "B": "-4",
    "G": "-5",
    "D": "-6",
    "A": "-6",
    "E": "-4",
    "triad": gsh_triad,
}
# sharp minor
ashm = {
    "e": "-1",
    "B": "-2",
    "G": "-3",
    "D": "-3",
    "A": "-1",
    "E": x,
    "triad": ashm_triad,
}
cshm = {
    "e": "-4",
    "B": "-5",
    "G": "-6",
    "D": "-6",
    "A": "-4",
    "E": x,
    "triad": cshm_triad,
}
dshm = {"e": "-2", "B": "-4", "G": "-3", "D": "-1", "A": x, "E": x, "triad": dshm_triad}
fshm = {"e": "-2", "B": "-2", "G": "-2", "D": "-4", "A": x, "E": x, "triad": fshm_triad}
gshm = {
    "e": "-4",
    "B": "-4",
    "G": "-4",
    "D": "-6",
    "A": "-6",
    "E": "-4",
    "triad": gshm_triad,
}

open_chords = {
    "A": a,
    "A#": ash,
    "Am": am,
    "A#m": ashm,
    "B": b,
    "Bm": bm,
    "C": c,
    "C#": csh,
    "Cm": cm,
    "C#m": cshm,
    "D": d,
    "D#": dsh,
    "Dm": dm,
    "D#m": dshm,
    "E": e,
    "Em": em,
    "F": f,
    "F#": fsh,
    "Fm": fm,
    "F#m": fshm,
    "G": g,
    "G#": gsh,
    "Gm": gm,
    "G#m": gshm,
}


# Triads


class Triad:

    def __init__(self, triad):
        self.first = triad


class OpenChord:

    def __init__(self, chord):
        self.e = "".join(["e", space, chord.get("e"), space, "|"])
        self.B = "".join(["B", space, chord.get("B"), space, "|"])
        self.G = "".join(["G", space, chord.get("G"), space, "|"])
        self.D = "".join(["D", space, chord.get("D"), space, "|"])
        self.A = "".join(["A", space, chord.get("A"), space, "|"])
        self.E = "".join(["E", space, chord.get("E"), space, "|"])
        self.triad = chord.get("triad")

    def show_all():
        for chord in open_chords.keys():
            open_chord = OpenChord(chord)
            print(
                f"\n{open_chord.e}\n{open_chord.B}\n{open_chord.G}\n{open_chord.D}\n{open_chord.A}\n{open_chord.E}\n"
            )

    def get_diagram(chord):
        open_chord = OpenChord(chord)
        result = f"\n{open_chord.e}\n{open_chord.B}\n{open_chord.G}\n{open_chord.D}\n{open_chord.A}\n{open_chord.E}\n"
        return result

    def usr_choice():
        chord = input("Chord: ")
        chord = chord.capitalize()
        open_chord = open_chords.get(chord)
        return open_chord


class PowerChord:

    def __init__(self, chord):
        self.e = "".join(["e", space, chord.get("e"), space, "|"])
        self.B = "".join(["B", space, chord.get("B"), space, "|"])
        self.G = "".join(["G", space, chord.get("G"), space, "|"])
        self.D = "".join(["D", space, chord.get("D"), space, "|"])
        self.A = "".join(["A", space, chord.get("A"), space, "|"])
        self.E = "".join(["E", space, chord.get("E"), space, "|"])
        self.triad = chord.get("triad")

    def show_all():
        for chord in power_chords.keys():
            power_chord = PowerChord(chord)
            print(
                f"{power_chord.e}\n{power_chord.B}\n{power_chord.G}\n{power_chord.D}\n{power_chord.A}\n{power_chord.E}\n"
            )

    def get_diagram(chord):
        power_chord = PowerChord(chord)
        result = (
            f"\n{power_chord.e}\n{power_chord.B}\n{power_chord.G}\n{power_chord.D}\n{power_chord.A}\n{power_chord.E}\n"
        )
        return result

class Chords(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def chords(self, ctx, chord):
        chord = chord.capitalize()
        if chord in open_chords.keys() | power_chords.keys():
            get_chord = open_chords.keys(chord)
            get_triad = OpenChord(get_chord)
            triad = get_triad.triad
            chord_embed = discord.Embed(title=f"{chord}", description=f"{triad}", color=CUSTOM_COLOR)
        if chord in open_chords.keys():
            oc = open_chords.get(chord)
            diagram = OpenChord.get_diagram(oc)
            get_triad = OpenChord(oc)
            triad = get_triad.triad
            chord_embed.add_field(name="Open Chord", value=f"```{diagram}```")
            #await ctx.send(f"``{diagram}``")
        if chord in power_chords.keys():
            pc = power_chords.get(chord)
            diagram = PowerChord.get_diagram(pc)
            chord_embed.add_field(name="Power Chord", value=f"```{diagram}```")
            #await ctx.send(f"``{diagram}``")
        await ctx.send(embed=chord_embed)

    def chord_list():
        chords = []
        for chord in open_chords.keys():
            chords.append(chord)
        for chord in power_chords.keys():
            chords.append(chord)
        result = list(set(chords))
        result.sort()
        return result

    @commands.command()
    async def chordlist(self, ctx, scope="all"):
            if scope == "all":
                chordlist = Chords.chord_list()
                chordlist_embed = discord.Embed(title=f"All Chords", description=chordlist, color=CUSTOM_COLOR)
                chordlist_embed.add_field(name="All", value=chordlist)
                await ctx.send(embed=chordlist_embed)
            if scope == "p":
                pclist = []
                for chord in get_chords:
                    pclist.append(chord)
                get_chords = power_chords.keys()
                chordlist_embed = discord.Embed(title=f"Power Chords", description=pclist, color=CUSTOM_COLOR)
                await ctx.send(embed=chordlist_embed)
            if scope == "o":
                oclist = []
                for chord in open_chords.keys():
                    oclist.append(chord)
                chordlist_embed = discord.Embed(title=f"Open Chords", description=oclist, color=CUSTOM_COLOR)
                await ctx.send(embed=chordlist_embed)

async def setup(bot):
    await bot.add_cog(Chords(bot))
