#Rock,Paper,Scissors Game using Python

import random
print ("\n welcome to rock ,paper , sessisor game")
print("\n")

userinput = input("Enter a choice (rock, paper, scissor): ")
possible_actions = ("rock", "paper", "scissor")
computerinput = random.choice(possible_actions)
print(f"\nYou chose {userinput}, computer chose {computerinput}.\n")

if userinput == computerinput:
    print(f"Both players selected {userinput}. It's a tie!")
elif userinput == "rock":
    if computerinput == "scissor":
        print("Rock beats scissor! You win!")
    else:
        print("Paper beats rock! You lose.")
elif userinput == "paper":
    if computerinput == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif userinput == "scissor":
    if computerinput == "paper":
        print("Scissor beats paper! You win!")
    else:
        print("Rock beats scissor! You lose.")
