# Rock, Paper, Scissors Game
# Write a program to simulate a game of Rock, Paper, Scissors.
# The game will prompt the player to choose rock, paper, or scissors by typing 'r',
# 'p', or 's'. The computer will randomly select its choice. The game will then display
# both choices using emojis and determine the winner based on the rules

# rock     0      rock beats scissors
# paper    1      paper beats rock.
# scissors 2      scissors beat paper

# import random


# DICT = {"r": 0, "p": 1, "s": 2}
# reversedDICT = {0: "🪨", 1: "📃", 2: "✂️"}

# # reversedDICT = {0: "Rock", 1: "Paper", 2: "Scissors"}

# def get_user_choice():
#     while True:
#         player1Move = input("Rocks, paper, or scissors? (r/p/s): ").strip().lower()
#         if player1Move in DICT:
#             return player1Move
#         else:
#             print("Invalid choice. Please enter (r/p/s).")
#             continue

# def display_choices(player1, computer):
#      print(f"You chose {reversedDICT[player1]}\nComputer chose {reversedDICT[computer]}")

# def determine_winner(player1, computer):
#     if player1 == computer:
#         print("It's a draw")
#     else:
#       if player1 == 0 and computer == 1:   # -1
#            print("You lose!")
#       elif player1 == 0 and computer == 2: # -2
#            print("You win!")
#       elif player1 == 1 and computer == 0: # 1
#            print("You win!")
#       elif player1 == 1 and computer == 2: # -1
#            print("You lose!")
#       elif player1 == 2 and computer == 0: #  2
#            print("You lose!")
#       elif player1 == 2 and computer == 1: #  1
#            print("You win!")

# def play_game():
#      while True:
#         player1Move = get_user_choice()

#         player1 = DICT[player1Move]

#         computer = random.choice([0, 1, 2])

#         print(computer)

#         display_choices(player1, computer)

#         determine_winner(player1, computer)

#         play_again = input('Continue? (y/n): ').lower()
#         if play_again == 'n':
#          break

# play_game()
    


import random

DICT = {"r": 0, "p": 1, "s": 2}
reversedDICT = {0: "🪨", 1: "📃", 2: "✂️"}
# reversedDICT = {0: "Rock", 1: "Paper", 2: "Scissors"}

class RockPaperScissors:
    def __init__(self):
        pass
    def get_user_choice(self):
     while True:
          player1Move = input("Rocks, paper, or scissors? (r/p/s): ").strip().lower()
          if player1Move in DICT:
               return DICT[player1Move]
          else:
               print("Invalid choice. Please enter (r/p/s).")

    def display_choices(self, player1, computer):
          print(f"You chose {reversedDICT[player1]}\nComputer chose {reversedDICT[computer]}")

    def determine_winner(self, player1, computer):
     if player1 == computer:
          print("It's a draw")
     else:
          if player1 == 0 and computer == 1:   # -1
               print("You lose!")
          elif player1 == 0 and computer == 2: # -2
               print("You win!")
          elif player1 == 1 and computer == 0: # 1
               print("You win!")
          elif player1 == 1 and computer == 2: # -1
               print("You lose!")
          elif player1 == 2 and computer == 0: #  2
               print("You lose!")
          elif player1 == 2 and computer == 1: #  1
               print("You win!")

    def play_game(self):
          while True:
               computer = random.choice([0, 1, 2])
               print(computer)
               player1 = self.get_user_choice()
               self.display_choices(player1, computer)
               self.determine_winner(player1, computer)
               play_again = input('Continue? (y/n): ').lower()
               if play_again == 'n':
                break

if __name__ == "__main__":
    game =  RockPaperScissors()
    game.play_game()





    
