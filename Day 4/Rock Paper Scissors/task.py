import random
from random import choice

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, "
                        "or 2 for Scissors.\n"))
cpu_choice = random.randint(0,2)
result = ["It's a Draw", "You Win!", "You Lose."]
choice_variables = [rock, paper, scissors]

print("You chose:", choice_variables[user_choice])
print("Computer chose:", choice_variables[cpu_choice])

if user_choice == 0:
    if cpu_choice == 0:
        print(result[0])
    elif cpu_choice == 1:
        print(result[2])
    elif cpu_choice == 2:
        print(result[1])
elif user_choice == 1:
    if cpu_choice == 0:
        print(result[1])
    elif cpu_choice == 1:
        print(result[0])
    elif cpu_choice == 2:
        print(result[2])
elif user_choice == 2:
    if cpu_choice == 0:
        print(result[2])
    elif cpu_choice == 1:
        print(result[1])
    elif cpu_choice == 2:
        print(result[0])
else:
    print("Something went wrong!")
