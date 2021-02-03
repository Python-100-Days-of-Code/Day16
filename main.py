import os
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_object = Menu()
coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()

os.system("clear")
not_turn_off = True


while not_turn_off:
    # TODO: 1. Ask user
    option = input(f"What would you like? {menu_object.get_items()}: ")
    if option == "off":
        not_turn_off = False
    elif option == "report":
        coffee_maker_object.report()
        money_machine_object.report()
    else:
        drink = menu_object.find_drink(option)
        if coffee_maker_object.is_resource_sufficient(drink):
            if money_machine_object.make_payment(drink.cost):
                coffee_maker_object.make_coffee(drink)

    # Space between runs
    print("\n")
