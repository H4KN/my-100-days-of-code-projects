import random 


you = int(input("Choose your option, rock: 0, paper: 1, scissor: 2"))

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


options = [rock, paper, scissor]

computer_rand = random.randint(0, 2)

computer = options[computer_rand]


print(f"you:{options[you]}")

print(f"computer:{options[computer_rand]}")


if you == 0:
    if you == 0 and computer_rand == 1:    
        print("you lost.")
    elif you == 0 and computer_rand == 2:
        print("you won.")
    else:
        print("Draw")

if you == 1:
    if you == 1 and computer_rand == 0:    
        print("you won.")
    elif you == 1 and computer_rand == 2:
        print("you lost.")
    else:
        print("Draw")

if you == 2:
    if you == 2 and computer_rand == 1:    
        print("you won.")
    elif you == 2 and computer_rand == 0:
        print("you lost.")
    else:
        print("Draw")


