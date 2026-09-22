from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

machine_on = True

menu = Menu()
coffee_machine = CoffeeMaker()
cashier = MoneyMachine()
table_coffee = PrettyTable()
table_coffee.add_column("Coffee", ["Espresso", "Latte", "Cappuccino"])
table_coffee.add_column("Price", ["$" + str(menu.menu[0].cost), "$" + str(menu.menu[1].cost), "$" + str(menu.menu[2].cost)])

while machine_on:
    print(table_coffee)
    user_order = input("What would you like?: ").lower()
    print("\n")

    if user_order == 'report':
        coffee_machine.report()
        cashier.report()
        print("\n")
        continue

    elif user_order == 'off':
        machine_on = False
        continue

    choice = menu.find_drink(user_order)

    for item in range(len(menu.menu)):
        if menu.menu[item].name == choice.name:
            choice_index = item

    if choice == None:
        print("\n")
        continue

    else:
        if coffee_machine.is_resource_sufficient(choice):
            cashier.make_payment(menu.menu[choice_index].cost)
            coffee_machine.make_coffee(choice)

    print("\n")