#Rock,Paper,Scissors Game using Python

import random
print ("\n welcome to rock ,paper , sessisor game")
print("\n")

user_input = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ("rock", "paper", "scissors")
computer_input = random.choice(possible_actions)
print("\n You choose")
    