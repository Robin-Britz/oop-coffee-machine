import menu
import coffee_maker
import money_machine

option = menu.Menu()
machine = coffee_maker.CoffeeMaker()
money = money_machine.MoneyMachine()


def restart():
    choice = input(f"What would you like? {option.get_items()}: ")

    if choice == "off":
        exit()

    # TODO print report
    elif choice == "report":
        machine.report()
        money.report()
        restart()

    else:
        drink = option.find_drink(choice)

        # TODO check resources sufficient?.
        sufficient_resources = machine.is_resource_sufficient(drink)
        if sufficient_resources:
            # TODO process coins
            payment = money.make_payment(drink.cost)

            # TODO check transaction successful?
            if payment:
                # TODO make coffee
                machine.make_coffee(drink)
                restart()


restart()
