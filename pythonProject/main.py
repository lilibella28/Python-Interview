# This is a sample Python script.
# TODO 1 print report
# TODO 2 check resources sufficient
# TODO 3 be able to only process coin
# TODO 4 check if the was good
# TODO 5 make a good coffee
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_payments(money_recieved, drinks_cost):
    """check is the user have enter enough money to process the drink
    it also return the change"""
    if money_recieved >= drinks_cost:
        change = round(money_recieved - drinks_cost, 2)
        print(f"Here is {change} in change")
        global money
        money += drinks_cost
        return True
    else:
        print("Sorry that is not enough money. Money refund")
        return False


def process_money():
    """process the user money, multiply it for the money value and the add it to their total"""
    print("Please insert a coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def resources_sufficients(user_orders):
    """ Check if the user have sufficient resources to process the order"""
    for item in user_orders:
        if user_orders[item] >= resources[item]:
           print(f"Sorry, there is not enough {item}")
           return False
    return True


def good_coffee(drink_choice, ingredients_choice):
    for item in ingredients_choice:
        resources[item] -= ingredients_choice[item]
    print(f"Here is your {drink_choice} Enjoy")


machine_on = True
while machine_on:

    user_choice = input("what would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
         print(f"Water: {resources['water']}ml")
         print(f"Milk: {resources['milk']}ml")
         print(f"Coffee: {resources['coffee']}g")
         print(f"Money: ${money}")
    else:
        drink = MENU[user_choice]
        if resources_sufficients(drink["ingredients"]):
            payment = process_money()
            if check_payments(payment, drink["cost"]):
                good_coffee(user_choice, drink["ingredients"])
