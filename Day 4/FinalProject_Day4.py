import random

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if human_choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif human_choice == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif human_choice == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
print("Computer chose:")
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif computer_choice == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if(computer_choice == human_choice):
    print("It's a tie")
elif((human_choice == 0 and computer_choice == 1) or (human_choice == 1 and computer_choice == 2) or (human_choice == 2 and computer_choice == 0)):
    print("You lose")
elif((human_choice == 0 and computer_choice == 2) or (human_choice == 1 and computer_choice == 0) or (human_choice == 2 and computer_choice == 1)):
    print("You win")