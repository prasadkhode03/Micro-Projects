import random
rock = """
     _______
----'   ____)
      (_____)
      (_____)
      (____)
----.__(___)

"""

paper = """
     _______
----'   ____)____
          _______)
          ________)
         _______)
----._________)

"""

scissors = """
     _______
----'   ____)_____
          ________)
       ____________)
      (____)
----.__(___)

"""

print("Welcome to Rock, Paper and Scissors Game.")
user = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors - "))
computer = random.randint(0, 2)

print("Your choice : \n")
if user == 0 and computer == 0:
    print(rock)
    print("\nComputer Choice : ")
    print(rock)
    print("Draw.")
elif user == 0 and computer == 1:
    print(rock)
    print("\nComputer Choice : ")
    print(paper)
    print("You lose.")
elif user == 0 and computer == 2:
    print(rock)
    print("\nComputer Choice : ")
    print(scissors)
    print("You win")
elif user == 1 and computer == 0:
    print(paper)
    print("\nComputer Choice : ")
    print(rock)
    print("You win.")
elif user == 1 and computer == 1:
    print(paper)
    print("\nComputer Choice : ")
    print(paper)
    print("Draw.")
elif user == 1 and computer == 2:
    print(paper)
    print("\nComputer Choice : ")
    print(scissors)
    print("You lose.")
elif user == 2 and computer == 0:
    print(scissors)
    print("\nComputer Choice : ")
    print(rock)
    print("You lose.")
elif user == 2 and computer == 1:
    print(scissors)
    print("\nComputer Choice : ")
    print(paper)
    print("You win")
elif user == 2 and computer == 2:
    print(scissors)
    print("\nComputer Choice : ")
    print(scissors)
    print("Draw")
else:
    print("Invalid Input!")
