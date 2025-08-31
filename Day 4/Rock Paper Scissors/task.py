import random
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

list_chooses = [rock, paper, scissors]
choose_computer = random.choice(list_chooses)

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choose == 0:
    print(rock)
    if choose_computer == rock:
        print("Computer chose:\n")
        print(rock)
        print("is a draw")
    elif choose_computer == paper:
        print("Computer chose:\n")
        print(paper)
        print("you lose")
    elif choose_computer == scissors:
        print("Computer chose:\n")
        print(scissors)
        print("Your win")
    else:
        print("You typed an invalid number, you lose!")
elif user_choose == 1:
    print(paper)
    if choose_computer == rock:
        print("Computer chose:\n")
        print(rock)
        print("Your win")

    elif choose_computer == paper:
        print("Computer chose:\n")
        print(paper)
        print("is a draw")

    elif choose_computer == scissors:
        print("Computer chose:\n")
        print(scissors)
        print("you lose")
    else:
        print("You typed an invalid number, you lose!")

elif user_choose == 2:
    print(scissors)
    if choose_computer == rock:
        print("Computer chose:\n")
        print(rock)
        print("you lose")

    elif choose_computer == paper:
        print("Computer chose:\n")
        print(paper)
        print("Your win")

    elif choose_computer == scissors:
        print("Computer chose:\n")
        print(scissors)
        print("is a draw")
    else:
        print("You typed an invalid number, you lose!")