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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough_resources(order_ingredients):
    for ing in order_ingredients:
        if order_ingredients[ing] > resources[ing]:
            print(f"Sorry there is not enough {ing}")
            return False
    return True


def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


is_on = True
while is_on:
    choice = input(
        "enter the choce fo the coffee latte or espresso or cuppuccin:->")
    if choice == "off":
        is_on = False
    elif choice == "Report":
        print("Milk ", resources['milk'])
        print("water ", resources['water'])
        print("Coffee ", resources['coffee'])
        print("profit ", profit)
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = process_coins()
            if payment >= drink["cost"]:
                result = payment - drink["cost"]
                print("Here is your change", result)
                for i in drink["ingredients"]:
                    resources[i] = resources[i] - drink["ingredients"][i]
                profit = profit + drink["cost"]
            else:
                print("sorry thats not enough money refunded")
