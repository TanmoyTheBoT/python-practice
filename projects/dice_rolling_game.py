# Dice Rolling Game
# Write a program that simulates rolling a pair of dice. Each time the program runs, it
# should randomly generate two numbers between 1 and 6 (inclusive), representing
# the result of each die. The program should then display the results and ask if the
# user would like to roll again.


# from random import randint


# while True:
#     dice1 = randint(1, 6)
#     dice2 = randint(1, 6)
#     userinput = input("Roll the dice? (y/n): ").lower()

#     if(userinput == "y" ):
#         print(f'({dice1}, {dice2})')

#     elif userinput == "n":
#         print("Thanks for playing!")
#         break

#     else:
#         print("Invalid choice!")


import random

def roll_dice():
     return random.randint(1, 6), random.randint(1, 6)

def get_user_choice():
    while True:
        user_input = input("Roll the dice? (y/n): ").strip().lower()
        if user_input in ('y', 'n'):
            return user_input
        else:
            print("Invalid choice! Please enter 'y' or 'n'.")

def display_result(dice1, dice2):
        print(f'You rolled: ({dice1}, {dice2})')

def play():
    while True:
        user_input = get_user_choice()
        if user_input == "y":
            dice1, dice2 = roll_dice()
            display_result(dice1, dice2)
        else:
            print("Thanks for playing!")
            break

def main():
    play()

if __name__ == "__main__":
    main()



