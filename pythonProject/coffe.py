from main import MENU, resources

user_choice = input("what would you like? (espresso/latte/cappuccino): ").lower()

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 2.5


def resources_check():
    if water < MENU["latte"]["ingredients"]["water"]:
        return "Sorry there is not enough water"
    # if coffee < user_choice1:
    #     return "Sorry there is not enough water"
    # if milk < user_choice1:
    #     return "Sorry there is not enough water"


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g ")
    print(f"Money: ${money}")


def coffee_machine(user_choice):
    if user_choice == "latte":
        return MENU["latte"]["cost"]
    elif user_choice == "espresso":
        return MENU["espresso"]["cost"]
    elif user_choice == "cappuccino":
        return MENU["cappuccino"]["cost"]
    elif user_choice == "report":
        return report()


def process_money():
    print("Please insert a coins. ")
    coins_quarters = int(input("How many quarters?: "))
    coins_dimes = int(input("How many dimes?: "))
    coins_nickles = int(input("How many nickles?: "))
    coins_pennies = int(input("How many pennies?: "))
    m_quartes = coins_quarters * 0.25
    m_dimes = coins_dimes * 0.10
    m_nickles = coins_nickles * 0.05
    m_pennies = coins_pennies * 0.01
    total_money = m_quartes + m_dimes + m_nickles + m_pennies
    return total_money


# def resources_check():
#     user_choice1 = coffee_machine(user_choice=user_choice)
#     if water > MENU["latte"]["water"]:
#         return "Sorry there is not enough water"
#     if coffee < user_choice1:
#         return "Sorry there is not enough water"
#     if milk < user_choice1:
#         return "Sorry there is not enough water"


coffee_machine(user_choice=user_choice)

resources_check()
# print(process_money())










