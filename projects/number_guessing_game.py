# Number Guessing Game
# Write a program to have the computer randomly select a number between 1 and
# 100, and then prompt the player to guess the number. The program should give
# hints if the guess is too high or too low.


from random import randint

num = randint(1, 100) # the guess number
max_attempts = 10

# guess = 0
guesses = 0


while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        guesses += 1

        if(guess > num):
            print(f"Too high! remaining attempts {max_attempts - guesses}")
            # guesses += 1

        elif(guess < num):
            print(f"Too low! remaining attempts {max_attempts - guesses}")
            # guesses += 1
        else: 
            print(f"Contratulations! You guessed the number in {guesses} attemps")
            break
             

    except ValueError:
        print("Please enter a valid number")

    if(guesses == max_attempts):
                    print(f"😢 Runs out of attempts! Numner of guesses {guesses} The correct number was {num}.")
                    break  # Stop the game after max attempts

    

