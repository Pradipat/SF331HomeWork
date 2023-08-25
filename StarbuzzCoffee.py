class Beverage:
    def cost(self):
        pass

    def description(self):
        pass

class Espresso(Beverage):
    def cost(self):
        return 1.99
    
    def description(self):
        return "Espresso"

class HouseBlend(Beverage):
    def cost(self):
        return 0.89
    
    def description(self):
        return "HouseBlend"
    
class DarkRoast(Beverage):
    def cost(self):
        return 0.99
    
    def description(self):
        return "DarkRoast"
    
class Decaf(Beverage):
    def cost(self):
        return 1.05
    
    def description(self):
        return "Decaf"


class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        pass

    def description(self):
        pass

class Milk(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.1

    def description(self):
        return self.beverage.description() + ", Milk"

class Mocha(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.2

    def description(self):
        return self.beverage.description() + ", Mocha"
    
class Soy(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.15

    def description(self):
        return self.beverage.description() + ", Soy"
    
class Whip(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.1

    def description(self):
        return self.beverage.description() + ", Whip"


beverage = HouseBlend()
print(beverage.description(), "$", beverage.cost())

beverage2 = Espresso()
beverage2 = Milk(beverage2)
beverage2 = Mocha(beverage2)
print(beverage2.description(), "$", beverage2.cost())

beverage3 = DarkRoast()
beverage3 = Mocha(beverage3)
beverage3 = Mocha(beverage3)
beverage3 = Whip(beverage3)
print(beverage3.description(), "$", beverage3.cost())

beverage4 = Decaf()
beverage4 = Soy(beverage4)
beverage4 = Mocha(beverage4)
beverage4 = Whip(beverage4)
print(beverage4.description(), "$", beverage4.cost())
