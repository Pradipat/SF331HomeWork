class Beverage:
    def cost(self):
        pass

    def description(self):
        pass

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

beverage = HouseBlend()
print(beverage.description(), "$", beverage.cost())

beverage2 = DarkRoast()
beverage2 = Milk(beverage2)
beverage2 = Mocha(beverage2)
print(beverage2.description(), "$", beverage2.cost())

beverage3 = DarkRoast()
beverage3 = Mocha(beverage3)
beverage3 = Mocha(beverage3)
print(beverage3.description(), "$", beverage3.cost())
