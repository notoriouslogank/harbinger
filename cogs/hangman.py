import random

import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs
from harbinger import Harbinger


class Hangman(commands.Cog):
    word_dictionary = ["syzygy", "beans", "memes", "dildo", "blarney"]
    random_word = random.choice(word_dictionary)

    @commands.command()
    async def print_hangman(self, ctx, wrong: int):
        if wrong == 0:
            ctx.message.send(f"\n+---+\n     |\n     |\n     |\n   ===\n+---+")
        elif wrong == 1:
            ctx.message.send(f"\n+---+\n O   |\n     |\n     |\n   ===\n+---+")
        elif wrong == 2:
            ctx.message.send(f"\n+---+\n O   |\n|    |\n     |\n   ===\n+---+")
        elif wrong == 3:
            ctx.message.send(f"\n+---+\n O   |\n/|   |\n     |\n   ===\n+---+")
        elif wrong == 4:
            ctx.message.send(f"\n+---+\n O   |\n/|\   |\n     |\n   ===\n+---+")
        elif wrong == 5:
            ctx.message.send(f"\n+---+\n O   |\n/|\   |\n/    |\n   ===\n+---+")
        elif wrong == 6:
            ctx.message.send(f"\n+---+\n O   |\n/|\   |\n/ \  |\n   ===\n+---+")

    @commands.command()
    async def print_word(self, ctx, guessed_letters):
        counter = 0
        correct_letters = 0
        for char in Hangman.random_word:
            if char in guessed_letters:
                ctx.message.send(Hangman.random_word[counter])
            correct_letters += 1
        else:
            ctx.message.send(" ")
        counter += 1
        return Hangman.correct_letters

    @commands.command()
    async def print_lines(self, ctx):
        ctx.send("\r")
        for char in Hangman.random_word:
            ctx.send("\u203E")

    @commands.command()
    async def hangman(self, ctx: commands.Context):
        message = await ctx.send(f"Welcome to Hangman\n---------------")
        for x in Hangman.random_word:
            ctx.message.edit("_")
        length_of_word_to_guess = len(Hangman.random_word)
        amount_of_wrong_guesses = 0
        current_guess_index = 0
        current_letters_guessed = []
        current_letters_correct = 0

        while (
            amount_of_wrong_guesses != 6
            and current_letters_correct != length_of_word_to_guess
        ):
            ctx.message.edit("\nLetters guessed so far: ")
        for letter in current_letters_guessed:
            ctx.message.edit(letter)
        ### Prompt for input
        letter_guessed = input("\nGuess a letter.")
        ### User is correct
        if Hangman.random_word[current_guess_index] == letter_guessed:
            Hangman.print_hangman(amount_of_wrong_guesses)
            ## Print word
            current_guess_index += 1
            current_letters_guessed.append(letter_guessed)
            current_letters_correct = Hangman.print_word(current_letters_guessed)
            Hangman.print_lines()
        ### User incorrect
        else:
            amount_of_wrong_guesses += 1
            current_letters_guessed.append(letter_guessed)
            ### Update drawing
            Hangman.print_hangman(amount_of_wrong_guesses)
            ### Print word
            current_letters_correct = Hangman.print_word(current_letters_guessed)
            Hangman.print_lines()

async def setup(bot):
    await bot.add_cog(Hangman(bot))