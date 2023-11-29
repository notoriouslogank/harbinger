import random

from discord.ext import commands

from harbinger import Harbinger

answers = [
    "Have you tried turning it off and back on again?",
    "The butler did it. Duh.",
    "Look for the Bugbear to find the answer.",
    "Your dilemma would be solved by not fighting a DRAGON.",
    "That sounds like a question for a crystal ball.",
    "Do I look like a wizard to you?",
    "I'll see what I can do.",
    "If it doesn't work then you really fucked up.",
    "The Magic Fluid Needs Replacement.",
    "I am a bot, not a globe or map, I don't know where you are",
    "You know I'm not actually magic right? Heck, these answers are prewritten!",
    "Whether I tell you yes or no, all I truly reveal is which one you were hoping for",
    "Long rest, and try again.",
    "Goodbye.",
    "The Glass is Half Full.",
    "The Glass is Half Empty.",
    "Anyway, here's Wonderwall.",
    "Your Funeral.",
    "Whoa! Why do I have to answer this?",
    "I have failed you, Anakin! I have failed you.",
    "Your Mom.",
    "I know my job, Jeff!",
    "Search your Feelings. You know it to be true.",
    "Turn around.",
    "Just don't bother.",
    "In the loosest sense, yes.",
    "In the loosest sense, no.",
    "Theoretically, it could work. I would not recommend it, though.",
    "Could you please think before you ask me something?",
    "Dodge left!",
    "Don't ask me!",
    "The stars shall give you the answer.",
    "I'm not nearly omnipotent enough for this.",
    "Sure, if you want a tragedy on your hands.",
    "No, but the failure will be entertaining!",
    "Survey says: Bzzzt!",
    "Diviners are currently busy. Please try again later.",
    "Oh, a good omen!",
    "When the Nine Hells freeze over.",
    "Yes, now leave me alone.",
    "Yes! I mean no! Wait...",
    "Your intellect score must be in the negatives, because the answer is NO!",
    "It won't work, but it will be very funny",
    "Technically yes, but you'll hate it",
    "I might be magic but how would I ever know that?",
    "Ask later, I'm writing a novel and I feel very inspired right now.",
    "You don't want to know, trust me.",
    "Even the worm turns",
    "An ominous wind blows",
    "Try a direct approach",
    "There is no answer",
    "Is no fun, is no blinsky",
    "Plan for success.",
    "Prepare for failure.",
    "You'll know when you know.",
    "Alone you will fail.",
    "Best have a backup plan.",
    "Circumstances make your question irrelevant.",
    "Soon",
    "The future is bloody.",
    "The future is unclear.",
    "You will fail.",
    "You will succeed.",
    "Only with a god's intervention.",
    "No, but I know you're going to try anyway, you fool.",
    "Help will come from an unexpected source... like, REALLY unexpected.",
    "Don't trust the human.",
    "Despite your fumbling efforts, you will meet with success!",
    "No, you're all going to die.",
    "Yes, but pack an extra healing potion just in case. Trust me on this one.",
    "Your question will be answered... eventually.",
    "Sorry. No one is here right now to take your call. Leave a message after the tone <<BEEP>>",
    "Nice try, you already know the answer.",
    "No way, buddy!",
    "Hey, leave me out of this!",
    "Yes, immediately.",
    "Highly unlikely.",
    "Let's just say anything is possible through the liberal application of fire.",
    "What? Sorry, I wasn't listening.",
    "Ask me again, and this time try not to sound like such a moron.",
    "No, and if I were you I'd be more discrete asking such questions.",
    "SEEK NOT THE ANSWER, YOU KNOW NOT THE COST",
    "42",
    "Heaven brings forth innumerable things to nurture man.",
    "Man has nothing good with which to recompense Heaven.",
    "Kill. Kill. Kill. Kill. Kill. Kill. Kill.",
    "Do you really wish to know?",
    "Perhaps, with great power of will.",
    "The answer you seek involves multitudes of spiders.",
    "Seriously?! this is the question you decided to ask?!",
    "I'm not even going to answer this one.",
    "Sure, but with caution.",
    "...What kind of question is that? Absloutely not!",
    "Sure, it'll be fun.",
    "Honestly even with all my magic, i don't think i can answer such a question.",
    "Maybe, maybe not.",
    "Get yourself together and ask again.",
    "I will let this one speak for itself.",
    "This was not in the job description!",
    "I don't know! You should ask yourself!",
    "What am I, a divination spell?",
    "Leylines shifting, ask again later.",
    "Future looks grim. Expect trouble",
    "Try asking it of a corpse",
    "No, she's way out of your charisma attribute.",
]


class Eightball(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def ask(self, ctx: commands.Context, question: str):
        cmd = "!ask"
        if question.endswith("?"):
            cmd_msg = f"{ctx.message.author} asked {question}."
            response = answers[random.randint(0, (len(answers) - 1))]
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await ctx.send(f"{response}")
        else:
            cmd_msg = f"{ctx.message.author} did not ask a valid question: {question}."
            Harbinger.timestamp(ctx.message.author, cmd, cmd_msg)
            await ctx.send(
                f"Not a valid question.  (Questions end with a question mark.)"
            )


async def setup(bot):
    """Load cogs into bot."""
    await bot.add_cog(Eightball(bot))
