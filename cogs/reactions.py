from random import randint
from discord.ext import commands
from harbinger import Harbinger

lol = [
    "https://64.media.tumblr.com/80ce2d4f77c4ddc5d9e395a43e37c532/tumblr_o5r3vkiaGo1qh9nffo3_250.gifv",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2c4azRvZmpodDYzOTN5aGl0N2xqdGNnM3NzN2QwbWNybHgyYmQ3diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12PIT4DOj6Tgek/giphy.gif",
    "https://media2.giphy.com/media/I8nepxWwlEuqI/200w.webp?cid=ecf05e47q00zdqc42u14cy528d4rcj89xaiu9gx3bz4xy3yr&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXkzdGdzbHZra2JneXNhMnZ5cDkxcTRjdjlvZnhyZnFxYjBuaDF6eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QgixZj4y3TwnS/giphy.gif",
]
wtf = [
    "https://media0.giphy.com/media/bzOwkffoJcEXcP2OxW/200w.webp?cid=ecf05e47rdl7ds16ptpy4ackpa1zfy6dzk25jbbqk47vc3yd&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/AAsj7jdrHjtp6/giphy.webp?cid=ecf05e47rdl7ds16ptpy4ackpa1zfy6dzk25jbbqk47vc3yd&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media2.giphy.com/media/Ni4cpi0uUkd6U/giphy.webp?cid=ecf05e47rdl7ds16ptpy4ackpa1zfy6dzk25jbbqk47vc3yd&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media0.giphy.com/media/9Vkm7LGgrPTcA345Sb/200w.webp?cid=ecf05e479du76ov5ukjutsv1xdc2zcir1nvhitbh48i9ych9&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/3vc4sSq0l8AbS/200.webp?cid=ecf05e47nc9ii1oscf4lzwcja5klijy76704u1gzoniop9ur&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media1.giphy.com/media/yoJC2qedZeZRggbqtG/200w.webp?cid=ecf05e47bl1q90hm1btm2wck93xp9ujh3w4hoq0qbevuw43f&ep=v1_gifs_search&rid=200w.webp&ct=g",
]
no = [
    "https://media1.giphy.com/media/3o6ZsZKbgw4QVWEbzq/200w.webp?cid=ecf05e47ly5eknhrmfatioojd45qrh2f8jejh7vguuagfy2h&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzh1OTlwM3p1b203czA2MHkxcnd5aHdjbXQzNXRnb2Rzb3I3M3E4aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ui4VjMUBGXhwgdwUnK/giphy.gif",
    "https://media0.giphy.com/media/Yycc82XEuWDaLLi2GV/200.webp?cid=ecf05e47ly5eknhrmfatioojd45qrh2f8jejh7vguuagfy2h&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media4.giphy.com/media/LRKET0Syb0rDO/200w.webp?cid=ecf05e47z3vdnygvzfyu7sh09896lkyx0qq8ohra4e5wma28&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/nXUCkgH6BmigU/200.webp?cid=ecf05e47b7l93krgopaxiabpimb21ieflunrz6z8gj2qzsac&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media3.giphy.com/media/1gdie7opvzRZv1yy9n/200w.webp?cid=ecf05e47nc9ii1oscf4lzwcja5klijy76704u1gzoniop9ur&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media2.giphy.com/media/l0IydskeKoJrzg69G/200w.webp?cid=ecf05e47j2nmvchn44vzgl9zdn4etase4chp1vwu8p926umy&ep=v1_gifs_search&rid=200w.webp&ct=g",
]
yes = [
    "https://media4.giphy.com/media/MNmyTin5qt5LSXirxd/200.webp?cid=ecf05e477c2k5wyck03d41c7i6cv5ubpcwri1oyanwbudb6k&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/WQr2txk5iEYUS6Kv3d/200.webp?cid=ecf05e477c2k5wyck03d41c7i6cv5ubpcwri1oyanwbudb6k&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/kEvVbCJunMEfqc7zjT/200w.webp?cid=ecf05e47mkwgp3wjzcqoipqc59gxkye0c3vfpzm0jepzh7w6&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/kwCLw42hH2cxvIywIi/200w.webp?cid=ecf05e47ptfnjng1zzw0gk4ophtvu32pmxg36wj2v7ftckyl&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/oGO1MPNUVbbk4/200.webp?cid=ecf05e47ptfnjng1zzw0gk4ophtvu32pmxg36wj2v7ftckyl&ep=v1_gifs_search&rid=200.webp&ct=g",
]
fu = [
    "https://media2.giphy.com/media/wgts1jTI7vmy9M0XlP/200w.webp?cid=ecf05e47miltp8fnqr8oph03op32r4ng7lciaeyqoez7ygr7&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media4.giphy.com/media/duf84Bx74ujSXvJs0I/200w.webp?cid=ecf05e47miltp8fnqr8oph03op32r4ng7lciaeyqoez7ygr7&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media4.giphy.com/media/I7p8K5EY9w9dC/200.webp?cid=ecf05e47miltp8fnqr8oph03op32r4ng7lciaeyqoez7ygr7&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/XHr6LfW6SmFa0/200.webp?cid=ecf05e47miltp8fnqr8oph03op32r4ng7lciaeyqoez7ygr7&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/x1kS7NRIcIigU/giphy.webp?cid=ecf05e47miltp8fnqr8oph03op32r4ng7lciaeyqoez7ygr7&ep=v1_gifs_search&rid=giphy.webp&ct=g",
]
sorry = [
    "https://media1.giphy.com/media/xjlC6nomocZhVXuZgM/200w.webp?cid=ecf05e47b7l93krgopaxiabpimb21ieflunrz6z8gj2qzsac&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/3ohA2ZD9EkeK2AyfdK/200w.webp?cid=ecf05e47ry78qi8v7tifuw8pn43ul4mir6bfeqycgahi1cmy&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/RWUqVYucDBD4A/giphy.webp?cid=ecf05e47ry78qi8v7tifuw8pn43ul4mir6bfeqycgahi1cmy&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media0.giphy.com/media/RFDXes97gboYg/giphy.webp?cid=ecf05e47ry78qi8v7tifuw8pn43ul4mir6bfeqycgahi1cmy&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media1.giphy.com/media/Lhu0BJTZVB6zSLMfbB/200.webp?cid=ecf05e47qk5q031o1hih6qay0fux3o7bd4vdob3uyaand4hg&ep=v1_gifs_search&rid=200.webp&ct=g",
]
hi = [
    "https://media3.giphy.com/media/Na2i9xObnOz3W/giphy.webp?cid=ecf05e47nc9ii1oscf4lzwcja5klijy76704u1gzoniop9ur&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media0.giphy.com/media/Vbtc9VG51NtzT1Qnv1/200.webp?cid=ecf05e47yfu9kmgrnq17l1a9r8n9j179i5wbsk0odgb3hyen&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/ASd0Ukj0y3qMM/200.webp?cid=ecf05e47yfu9kmgrnq17l1a9r8n9j179i5wbsk0odgb3hyen&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/QYkX9IMHthYn0Y3pcG/giphy.webp?cid=ecf05e47ffv5q0nyvp2tnftvlxu6rhpque5u2z7xxijuw5yy&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media4.giphy.com/media/qQh0DBncuFJwQ/200.webp?cid=ecf05e47ffv5q0nyvp2tnftvlxu6rhpque5u2z7xxijuw5yy&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media3.giphy.com/media/jOmQmJkjcvB3Bc8CRb/200.webp?cid=ecf05e47sy9z5shrlhl37rvb4le7slzwa0w6kevwz069wk38&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media4.giphy.com/media/L13NsH0Aij4Sf2Gdjt/200.webp?cid=ecf05e47sy9z5shrlhl37rvb4le7slzwa0w6kevwz069wk38&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media3.giphy.com/media/YTDZakyAorkLDYqN0q/200.webp?cid=ecf05e47sy9z5shrlhl37rvb4le7slzwa0w6kevwz069wk38&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media2.giphy.com/media/h0m6DAVQ1zBfi/200w.webp?cid=ecf05e47sy9z5shrlhl37rvb4le7slzwa0w6kevwz069wk38&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media4.giphy.com/media/ZCNjymWszyazkph0z2/200.webp?cid=ecf05e47sy9z5shrlhl37rvb4le7slzwa0w6kevwz069wk38&ep=v1_gifs_search&rid=200.webp&ct=g",
]
bye = [
    "https://media2.giphy.com/media/UIKUeFj40vTP2/200w.webp?cid=ecf05e47nc9ii1oscf4lzwcja5klijy76704u1gzoniop9ur&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/pGfeUvh4hnoKnJ9JkW/200w.webp?cid=ecf05e47nc9ii1oscf4lzwcja5klijy76704u1gzoniop9ur&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media2.giphy.com/media/KctrWMQ7u9D2du0YmD/200w.webp?cid=ecf05e47c9zdc8kxepk82p61yjtm0il18blpr72bmi7f41lm&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/3ohs7KViF6rA4aan5u/200.webp?cid=ecf05e47c9zdc8kxepk82p61yjtm0il18blpr72bmi7f41lm&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media2.giphy.com/media/l49FqlUguNsGDNCGk/200w.webp?cid=ecf05e47qtujkc2ys2a2emzwwmhlqy8pjqlwib04xou5rh1n&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/2WxWfiavndgcM/200w.webp?cid=ecf05e47z464xqlwr5nzsgxsto0ajxxd5xk5kpytkyg86kxn&ep=v1_gifs_search&rid=200w.webp&ct=g",
]
bored = [
    "https://media1.giphy.com/media/KFiQXtO3rWxlzpjnrV/200.webp?cid=ecf05e47e5mpjxaeupuvpnx0itpfxbvekxqokd163u5kf3fk&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media4.giphy.com/media/rq6c5xD7leHW8/200w.webp?cid=ecf05e47e5mpjxaeupuvpnx0itpfxbvekxqokd163u5kf3fk&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/iW8tsoJWcfPc4/giphy.webp?cid=ecf05e47e5mpjxaeupuvpnx0itpfxbvekxqokd163u5kf3fk&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media1.giphy.com/media/eg9UMthX68nJgZ99lk/200w.webp?cid=ecf05e4749sc08uj4nolkxvkluctlriimd1nx0c5x8854wju&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media2.giphy.com/media/9VarJN4ZBDZFC/200w.webp?cid=ecf05e4749sc08uj4nolkxvkluctlriimd1nx0c5x8854wju&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/57IQRWq3eidi0/200w.webp?cid=ecf05e47oexp882gg0yt1dk3owi0o7xgunhhfcxu2g2ad6a4&ep=v1_gifs_search&rid=200w.webp&ct=g",
]
shook = [
    "https://media3.giphy.com/media/l3q2K5jinAlChoCLS/200w.webp?cid=ecf05e47m1dqhedhejneba3i8hy7ryhwzfxw52v8enpr14np&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/ZUkausLsSMJpu/giphy.webp?cid=ecf05e47m1dqhedhejneba3i8hy7ryhwzfxw52v8enpr14np&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media4.giphy.com/media/xT0GqDD0xyeG2k4q52/200w.webp?cid=ecf05e47m1dqhedhejneba3i8hy7ryhwzfxw52v8enpr14np&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/vLq5FWMjfN47S/200.webp?cid=ecf05e47m1dqhedhejneba3i8hy7ryhwzfxw52v8enpr14np&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media3.giphy.com/media/l0IypeKl9NJhPFMrK/200w.webp?cid=ecf05e4780er9ukqyzlgt27rnzhtqjoki3trgvos0dsgslus&ep=v1_gifs_search&rid=200w.webp&ct=g",
]
angry = [
    "https://media0.giphy.com/media/aNFT7eG2rIKK715uLk/200w.webp?cid=ecf05e475skjt638cddsrgswygx6lebpkckvu8m1g67t0m8t&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/lqpfdJr57GAOQHSuLr/200w.webp?cid=ecf05e475skjt638cddsrgswygx6lebpkckvu8m1g67t0m8t&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/p8Uw3hzdAE2dO/200.webp?cid=ecf05e475skjt638cddsrgswygx6lebpkckvu8m1g67t0m8t&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media4.giphy.com/media/l0MYrqggEwtDscVP2/200w.webp?cid=ecf05e47vmuhx0h0p3iyr4iyuxtwokc3njejgccoeca856yt&ep=v1_gifs_search&rid=200w.webp&ct=g",
]
sad = [
    "https://media4.giphy.com/media/dJYoOVAWf2QkU/200w.webp?cid=ecf05e47z464xqlwr5nzsgxsto0ajxxd5xk5kpytkyg86kxn&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/Ty9Sg8oHghPWg/giphy.webp?cid=ecf05e473tqr287a0ua8z2zfeceqzsvmwrw1sxrv4ln2j9dx&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media1.giphy.com/media/TU76e2JHkPchG/200w.webp?cid=ecf05e473tqr287a0ua8z2zfeceqzsvmwrw1sxrv4ln2j9dx&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/3o6wrebnKWmvx4ZBio/200w.webp?cid=ecf05e473tqr287a0ua8z2zfeceqzsvmwrw1sxrv4ln2j9dx&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/OPU6wzx8JrHna/200.webp?cid=ecf05e473tqr287a0ua8z2zfeceqzsvmwrw1sxrv4ln2j9dx&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media1.giphy.com/media/7SF5scGB2AFrgsXP63/200w.webp?cid=ecf05e473tqr287a0ua8z2zfeceqzsvmwrw1sxrv4ln2j9dx&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media4.giphy.com/media/Ase7L4MjavtBb0L3cx/200w.webp?cid=ecf05e47x8o0sxcavnd4jgsbsu97y90fbwy6gtyhfbsgsu8u&ep=v1_gifs_search&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/a9xhxAxaqOfQs/200w.webp?cid=ecf05e47x8o0sxcavnd4jgsbsu97y90fbwy6gtyhfbsgsu8u&ep=v1_gifs_search&rid=200w.webp&ct=g",
]


class React(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

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
