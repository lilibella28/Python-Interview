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
choice_list = [rock, paper, scissors]
list_lent = len(choice_list)
computer_choice = random.randint(0, list_lent - 1)
# compuers = choice_list[computer_choice]
# print(rock)
user_choice = int(input(" what do you choose  type 0 for Rock, 1 for paper, or two for scissors"))

if user_choice == 0:
    user_choice = rock
if computer_choice == 0:
    computer_choice = rock
if user_choice == 1:
    user_choice = paper
if computer_choice == 1:
    computer_choice = paper
if user_choice == 2:
    user_choice = scissors
if computer_choice == 2:
    computer_choice = scissors

print(user_choice)
print(computer_choice)
if user_choice == computer_choice:
    print("its a tied")
elif user_choice == rock and computer_choice == scissors:
    print("Congratulation you have won")

elif user_choice == scissors and computer_choice == paper:
    print("Congratulation you have won")

elif user_choice == paper and computer_choice == rock:
    print("Congratulation you have won")
elif user_choice > list_lent or computer_choice > list_lent:
    print("Please enter correct number: 0 for rock, 1 for paper and 2 for scissor")

else:
    print("The computer won")

# determinate the winner