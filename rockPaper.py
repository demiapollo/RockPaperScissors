import random
print("Welcome to the Rock, Paper, Scissors Game")
print("-----------------------------------------")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Scissor
'''

user_choice = input("What do you choose? Type 'R' for Rock, 'P' for Paper or 'S' for Scissors.\n")
options = ["R", "P", "S"]
computer_choice = random.choice(options)

if user_choice.upper() == "R":
    print(f"You chose \n{rock}")
    if computer_choice == "R":
        print(f"Computer chose \n{rock}")
        print(f"It's a tie. Try again.")
    elif computer_choice == "P":
        print(f"Computer chose \n{paper}")
        print(f"You lost.")
    elif computer_choice == "S":
        print(f"Computer chose \n{scissors}")
        print(f"You won.")
elif user_choice.upper() == "P":
    print(f"You chose \n{paper}")
    if computer_choice == "P":
        print(f"Computer chose \n{paper}")
        print(f"It's a tie. Try again.")
    elif computer_choice == "R":
        print(f"Computer chose \n{rock}")
        print(f"You won.")
    elif computer_choice == "S":
        print(f"Computer chose \n{scissors}")
        print(f"You lost.")
elif user_choice.upper() == "S":
    print(f"You chose \n{scissors}")
    if computer_choice == "S":
        print(f"Computer chose \n{scissors}")
        print(f"It's a tie. Try again.")
    elif computer_choice == "R":
        print(f"Computer chose \n{rock}")
        print(f"You lose.")
    elif computer_choice == "P":
        print(f"Computer chose \n{paper}")
        print(f"You won.")
else:
    print(f"Please type R, P, or S")


