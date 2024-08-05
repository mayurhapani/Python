rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

list = [rock, paper, scissors]

playerMove = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

# rock > scissors , scissors > paper, paper > rock
# 0 > 2, 2 > 1, 1 > 0

if playerMove >= 3 or playerMove < 0:
    print("You typed an invalid number, you lose!")
else:
    computerMove = random.randint(0, 2)

    print("The computer move is :")
    print(list[computerMove])

    print("The your move is :")
    print(list[playerMove])

    if playerMove == computerMove:
        print("It's a draw")
    else:
        if playerMove == 0 and computerMove == 1:
            print("You lose!")
        elif playerMove == 0 and computerMove == 2:
            print("You win!")

        if playerMove == 1 and computerMove == 0:
            print("You win!")
        elif playerMove == 1 and computerMove == 2:
            print("You lose!")

        if playerMove == 2 and computerMove == 0:
            print("You lose!")
        elif playerMove == 2 and computerMove == 1:
            print("You win!")
