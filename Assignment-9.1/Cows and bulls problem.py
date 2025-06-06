"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number(Digits should not be repeated). For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1250
  1 cow, 1 bull
  ...
Until the user guesses the number.
"""

import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def count_cows_and_bulls(secret, guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return cows, bulls

def play_cows_and_bulls():
    secret_number = generate_secret_number()
    guesses = 0

    print("Welcome to the Cows and Bulls Game!")
    print("Guess a 4-digit number. Digits should not be repeated.")

    while True:
        guess = input(">>> ")
        guesses += 1

        if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
            print("Please enter a valid 4-digit number with no repeating digits.")
            continue

        cows, bulls = count_cows_and_bulls(secret_number, guess)

        if cows == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {guesses} guesses.")
            break
        else:
            print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    play_cows_and_bulls()
