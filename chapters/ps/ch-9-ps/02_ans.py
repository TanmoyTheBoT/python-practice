# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random
def game():
    print("Your Playing the game...")
    score = random.randint(1, 63)
    # feaching
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score: {score}")
    if(score>hiscore):

        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
