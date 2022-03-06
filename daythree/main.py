# print("Welcome to the rollercoaster!")
# height = int(input("What is your age in cm? "))
# age = int(input("How old are you?"))
# if height >= 120:
#     print("You can ride")
#     if age < 12:
#         print("Please pay 5")
#     elif age <= 18:
#         print("You must pay 7 dollars")
#     else:
#         print("You must paid 12 dollar")
#
# else:
#     print("You can not ride")
#  even odd number

# print("Welcome  to the odd even number")
# numberChoice = int(input("Please enter  a number: "))
#
# if numberChoice % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd  number.")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

whereTogo = input("Where do you want to go, Left or Right?  ").lower()


if whereTogo == "left":
    swim_or_wait = input("Do you want to swim or wait? ").lower()
    if swim_or_wait == "wait":
        door_option = input("Which door do you want to, Red, Blue, Yellow ").lower()
        if door_option == "yellow":
            print("You win")
        else:
            print("Game over, You the mean sister drown you")
    else:
        print("GameOver, swim is not fun")
else:
    print("GameOver, its never a good idea")
