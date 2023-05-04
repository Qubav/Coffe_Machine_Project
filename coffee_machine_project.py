from os import system as sys
import time
from art import logo

# global variable

coffee_flavors = [
    {
        "name": "Espresso",
        "price": 1.5,  # $
        "water": 50,    # ml
        "milk": 0,      # ml
        "coffee": 18,    # g
    },
    {
        "name": "Latte",
        "price": 2.5,
        "water": 200,
        "milk": 150,
        "coffee": 24,
    },
    {
        "name": "Cappuccino",
        "price": 3.0,
        "water": 250,
        "milk": 100,
        "coffee": 24,
    }
]

coins = {
    "Penny": 0.01,  # $
    "Nickel": 0.05,
    "Dime": 0.1,
    "Quarter": 0.25, 
}

# functions 

def paying_money():
    """Function ask user how many coins of each type he puts into machine and returns list with amount of each thrown in type of coin. List order [Penny, Nickel, Dime, Quarter]."""

    print("Pleas insert coins")
    q_amount = int(input("How many quarters?"))
    d_amount = int(input("How many dimes?"))
    n_amount = int(input("How many nickles?"))
    p_amount = int(input("How many pennies?"))

    return [p_amount, n_amount, d_amount, q_amount]

def calculate_value(c_amount: list):
    """Function returns total value of all coins paid by user based on their amount is list."""

    # multiplying amount of each coin by its value and adding up to total value
    return c_amount[0] * coins["Penny"] + c_amount[1] * coins["Nickel"] + c_amount[2] * coins["Dime"] + c_amount[3] * coins["Quarter"]

def report(resources: dict):
    """Function prints out resources."""

    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n")

def check_if_resources_are_sufficient(coffee: dict, resources: dict):
    """Function checks if resources are sufficient to make given coffee flavor cup. Function returns True if resources are sufficient or False if they are not sufficient."""
    
    # checking if value of any resources is not sufficient to make cup of chosen flavor of coffee, if so giving feedback and returning False
    if coffee["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")

        return False
    
    elif coffee["water"] > resources["water"]:
        print("Sorry there is not enough water.")
    
        return False
    
    elif coffee["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")

        return False
    
    # in any of previous conditions weren't met it means resources are sufficient to make cup of chosen flavor coffee so True is returned
    else:
        
        return True

def update_resources(bought_flavor: dict, resources: dict,  refill: bool = False):
    """Function updates resources based on bought flavor of coffee. If refill is True function treat bought_flavor as positive value and increase resources values but money is set to $0."""

    # based on using resources or refilling it new dictionary is created with upgraded values
    if refill is False:
        update = {
            "water": resources["water"] - bought_flavor["water"] ,
            "milk": resources["milk"] - bought_flavor["milk"],
            "coffee": resources["coffee"] - bought_flavor["coffee"],
        }
        
    else:
        update = {
            "water": resources["water"] + bought_flavor["water"] ,
            "milk": resources["milk"] + bought_flavor["milk"],
            "coffee": resources["coffee"] + bought_flavor["coffee"],
        }
    
    # returning dictionary with upgraded values
    return update

def compare_payment(cost: float, paid_money: float):
    """Function compares coffee cost and amount of money user paid and returns True/False based on condition if paid money is greater of even to cost."""
    
    # checking for possible conditions. based on condition met setting enough value to True or False and givin feedback
    if paid_money == cost:
        enough = True
        print("The fee is correct.")

    elif paid_money > cost:
        enough = True
        print(f"Your change is {round(paid_money - cost, 2)}. Collect the money.")
    
    else:
        enough = False
        print(f"You paid to little. Chosen coffee cost {cost}, and You paid {round(paid_money, 2)}.")
    
    return enough

def coffee_ordering(c_resources: dict, money: float):
    """Function performs tasks connected with ordering coffee and returns resources with updated values based on selling coffee."""

    # taking order from user
    flavor = input("Choose a flavor. Type:\n\"Espresso\" - $1.50\n\"Latte\" - $2.50\n\"Cappuccino\" - $3.00\n")

    # setting flv_num value based on chosen by user coffee flavor
    if flavor == "Espresso":
        flv_num = 0
    elif flavor == "Latte":
        flv_num = 1
    else:
        flv_num = 2

    # checking if resources are sufficient to make cup of chosen flavor coffee
    resources_sufficient = check_if_resources_are_sufficient(coffee_flavors[flv_num], c_resources)

    # based on sufficiency of resources continuing ordering or ending
    if resources_sufficient is True:

        # taking input from user of amount of each type of coin put into machine, calculating its total value and setting cost value to price of chosen flavor coffee 
        coins_list = paying_money()
        paid_money = calculate_value(coins_list)
        cost = coffee_flavors[flv_num]["price"]

        # setting enough value based on if paid by user money is enough to pay for cup of chosen flavored coffee
        enough = compare_payment(cost, paid_money)

        # if user paid enough continuing ordering
        if enough is True:
            
            # updating resources after making coffee
            new_resources = update_resources(coffee_flavors[flv_num], c_resources)
            money += cost

            # communication
            print(f"Here is Your {coffee_flavors[flv_num]['name']}. Enjoy!\n")

            # time for user to see feedback given
            time.sleep(5)

            return new_resources, money

        # if user didn't pay enough feedback and back to main menu
        else:
            
            # time for user to see feedback given
            time.sleep(5)

            return c_resources, money
    
    # if resources aren't sufficient feedback and back to main menu
    else:

        # time for user to see feedback given
        time.sleep(5)

        return c_resources, money


def coffee_machine():

    # variables
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    }

    machine_on = True
    money = 0

    # main loop
    while machine_on:
        sys("cls")
        print(logo)

        # asking user for decision which action to perform
        decision = input("What would u like? Type:\n\"order\" -  to order coffee\n\"report\" - to show current resources values\n\"refill\" - to refill resources\n")
        
        # money and off are not shown for user because only maintenance should use it
        if decision == "off":

            # changing value of variable responsible for loop repeating
            machine_on = False

        elif decision == "money":

            # printing value of money collected
            print(f"Value of money collected in machine is: ${round(money, 2)}")
            time.sleep(5)

        elif decision == "order":

            # using function to perform ordering operations
           resources, money = coffee_ordering(resources, money)
        
        elif decision == "refill":
            
            # asking user for amount of single resource refilled
            water_val = int(input("Water ml added: "))
            milk_val = int(input("Milk ml added: "))
            coffee_val = int(input("Coffee g added: "))

            # creating dictionary with given resources that will be added to resources
            refill_vals = {
               "water": water_val,
                "milk": milk_val,
                "coffee": coffee_val,
            }

            # updated resources
            resources  = update_resources(refill_vals, resources, True)

            # while refilling money is withdrawn from machine
            money = 0

        else:

            # using function to show resources values
            report(resources)
            time.sleep(5)

if __name__ == "__main__":
    sys("cls")
    coffee_machine()