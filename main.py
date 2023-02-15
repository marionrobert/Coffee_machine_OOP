from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_on = True

while machine_on:
    if coffee_maker.resources["water"] < 50 or coffee_maker.resources["coffee"] < 18:
        print("The coffee machine has not enough resources anymore, even for an espresso!")
        print("Machine turned off.")
        machine_on = False

    else:
        client_choice = input(f"What would you like? {menu.get_items()}: ").lower()

        if client_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif client_choice == "off":
            print("Machine turned off.")
            machine_on = False
        else:
            drink = menu.find_drink(client_choice)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    print(f"{drink.name} costs ${drink.cost}. ")
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
