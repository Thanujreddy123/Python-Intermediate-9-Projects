from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
choice = input("Enter the output")
CoffeeMakerobj = CoffeeMaker()
MoneyMachineobj=MoneyMachine()
Menuobj=Menu()
while is_on:
    if choice == "report":
        print(CoffeeMakerobj.report())
        print(MoneyMachineobj.profit)
        is_on = False
    elif choice == "off":
      is_on = False
    else:
      drink=Menuobj.find_drink(choice)
      if CoffeeMakerobj.is_resource_sufficient(drink):
        if MoneyMachineobj.make_payment(drink.cost):
          CoffeeMakerobj.make_coffee(drink)
      is_on=False
