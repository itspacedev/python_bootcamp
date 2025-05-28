from menu import MENU

COIN_QUARTER_VALUE = 0.25
COIN_DIME_VALUE = 0.1
COIN_NICKEL_VALUE = 0.05
COIN_PENNY_VALUE = 0.01

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "balance": 0.0
}


def print_report():
    """
    Prints information about hte coffee machine's resources
    """
    print("Coffee Machine Resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Balance: ${resources['balance']}")


def is_resources_sufficient(coffee_type):
    """
    Checks if the coffee machine has enough resources to make a coffee
    """
    ingredients = MENU[coffee_type]['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient} for a {coffee_type}")
            return False
    return True


def process_coins(coffee_type):
    """
    Asks a customer to insert coins and gives a change if a customer inserts more coins than needed
    """
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_amount_inserted = quarters * COIN_QUARTER_VALUE + dimes * COIN_DIME_VALUE + nickles * COIN_NICKEL_VALUE + pennies * COIN_PENNY_VALUE
    coffee_price = MENU[coffee_type]['cost']
    if total_amount_inserted >= coffee_price:
        change_amount = round(total_amount_inserted - coffee_price, 2)
        if change_amount > 0:
            print(f"Here is ${change_amount} in change.")
        return True

    print("Sorry, that's not enough money. Money refunded.")
    return False


def update_coffee_machine_resources(coffee_type):
    """
    Updates the coffee machine resources including water, milk, coffee, and the balance
    """
    global resources
    ingredients = MENU[coffee_type]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    resources['balance'] += MENU[coffee_type]['cost']


def make_a_coffee(coffee_type):
    """
    Checks the resources of a machine, processes coins and finally makes a coffee
    """
    if not is_resources_sufficient(coffee_type):
        return
    if not process_coins(coffee_type):
        return
    update_coffee_machine_resources(coffee_type)
    print(f"Here is your {coffee_type} ☕. Enjoy!")


stop_coffe_machine = False
while not stop_coffe_machine:
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if action == "off":
        stop_coffe_machine = True
    elif action == "report":
        print_report()
    elif action in ['espresso', 'latte', 'cappuccino']:
        make_a_coffee(action)
    else:
        print("You pressed the wrong button. Please try again.")

print("Coffee machine is under maintenance. Please come back later.")
