import random


rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

random_choice=random.randint(1,3)
print('''
1-)Rock
2-)Paper
3-)Scissors
''')

user_input=int(input("What is your choice: "))

if user_input == random_choice:
    print(f"Both players selected {user_input}. It's a tie!")

elif (user_input == 1) or (user_input == "rock"):
    print(f"\nYou:\n{rock}\n")
    if random_choice == 3:
        print(f"Computer:\n{scissors}")
        print("Rock smashes scissors! You win!")
    else:
        print(f"Computer:\n{paper}")
        print("Paper covers rock! You lose.")

elif (user_input == 2) or (user_input == "paper"):
    print(f"You:\n{paper}\n")
    if random_choice == 1:
        print(f"Computer:\n{rock}")
        print("Paper covers rock! You win!")
    else:
        print(f"Computer:\n{scissors}")
        print("Scissors cuts paper! You lose.")


elif (user_input == 3) or (user_input == "scissors"):
    print(f"You:\n{scissors}\n")
    if random_choice == 2:
        print(f"Computer:\n{paper}")
        print("Scissors cuts paper! You win!")
    else:
        print(f"Computer:\n{rock}")
        print("Rock smashes scissors! You lose.")
else:
    print("Invalid choose! You lose.")