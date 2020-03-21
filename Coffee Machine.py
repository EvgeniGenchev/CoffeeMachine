class Machine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def inventory(self):
        print("""The coffee machine has:
                {} of water
                {} of milk
                {} of coffee beans
                {} of disposable cups
                {} of money""".format(self.water, self.milk, self.beans, self.cups, self.money))

    def order(self, water, milk, beans, price, cups):
        array = [water, milk , beans,cups]
        str_array = ["water", "milk", "beans", "cups"]
        flag = self.check(water, self.water) and self.check(milk , self.milk) and self.check(beans, self.beans) and self.check(cups, self.cups)
        message = self.message(flag)

        for items in range(len(array)):
            if array[items] == item:
                print(message.format(str_array[items]))

        if flag:
            self.water = self.water - water
            self.milk = self.milk - milk
            self.beans = self.beans - beans
            self.cups = self.cups - cups
            self.money = self.money + price



    def message(self, flag):
        if flag:
            print("I have enough resources, making you coffee!\n")
            return "clear"
        else:
            return "Sorry, not enough {}"


    def check(self, product, initial):
        global item
        item = -123
        if initial - product < 0:
            item = product
            return False
        return True


    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0


machine = Machine(0, 540, 120, 9, 550)

flag = True

while flag:
    user_input = input("Write action (buy, fill, take, remaining, exit):")
    if user_input == 'buy':
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee == '1':
            machine.order(250, 0, 16, 4, 1)
        elif coffee == '2':
            machine.order(350, 75, 20, 7, 1)
        elif coffee == '3':
            machine.order(200, 100, 12, 6, 1)


    elif user_input == 'fill':

        machine.order(-int(input("Write how many ml of water do you want to add:")), 0, 0, 0, 0)
        machine.order(0, -int(input("Write how many ml of milk do you want to add:")), 0, 0, 0)
        machine.order(0, 0, -int(input("Write how many grams of coffee beans do you want to add:")), 0, 0)
        machine.order(0, 0, 0, 0, -int(input("Write how many disposable cups of coffee do you want to add:")))

    elif user_input == 'take':
        machine.take()

    elif user_input == 'remaining':
        print()
        machine.inventory()


    elif user_input == 'exit':
        flag = False
# 400 540 120 9 550



