# PROJECT 2 – THE PERFECT GUESS
# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.
import random

START = 1
END = 100
n = random.randint(START, END)
guess = 0
guesses = 1
while(guess != n):
    guess = int(input(f"Guess the the number between {START} and {END}: "))
    if guess > n :
        print("Lower number Please!")
        guesses += 1

    elif guess < n :
        print("Higher number Please!")
        guesses += 1

    

print(f"You have guessed the number {n} correctly in {guesses} attempts")