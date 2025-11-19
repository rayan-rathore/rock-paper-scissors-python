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
your_win=0
computer_win=0
drawl=0

players= [rock, paper, scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_input < 0 or user_input > 2:
    print("invalid choice, you lose!")
    exit()
else:
    user_choice = players[user_input]
    print("you choose: ",players[user_input])

computer = random.randint(0,2)
print("computer choose: ")
print(players[computer])
#rules
""""Rock beats Scissors.
    Scissors beat Paper.
    Paper beats Rock."""
if user_input == computer:
    print("it's drawl")
elif  (user_input == 0 and computer == 2) or \
      (user_input == 2 and computer == 1) or \
      (user_input == 1 and computer == 0):
    print("your win")
else:
    print("you lose!")

if user_input == computer:
    drawl+=1
elif user_input>computer:
    your_win +=1
else:
    computer_win+=1

print(f"score:\n you win:{your_win}, computer win:{computer_win}, drawl:{drawl}")