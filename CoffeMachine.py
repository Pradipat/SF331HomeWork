from __future__ import annotations
from abc import ABC, abstractmethod

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
    
class SoyMilk(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.15

    def description(self):
        return self.beverage.description() + ", Soy"


class State(ABC):
    @abstractmethod
    def orderBeverage(self) -> None:
        pass

    @abstractmethod
    def orderDecorator(self) -> None:
        pass

    @abstractmethod
    def summaryOrder(self) -> None:
        pass

    @abstractmethod
    def insertMoney(self) -> None:
        pass

    @abstractmethod
    def cancelOrder(self) -> None:
        pass

    @abstractmethod
    def changeMoney(self) -> None:
        pass

    @abstractmethod
    def releaseOrder(self) -> None:
        pass
  
class InitialState(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine

    def orderBeverage(self ,beverage ):
        self.coffeeMachine.setBeverage(beverage)
        self.coffeeMachine.setState(self.coffeeMachine.orderedBeverage)

    def orderDecorator(self, decorator):
        print("You must select Beverage first.")

    def summaryOrder(self):
        print("please order Beverage first.")

    def insertMoney(self, money):
        print("please order Beverage first.")

    def cancelOrder(self):
        print("You not order Beverage yet.")

    def changeMoney(self):
        print("You dont have Beverage yet.")

    def releaseOrder(self):
        print("You dont have Beverage yet.")

class OrderedBeverage(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine

    def orderBeverage(self ,beverage ):
        print("you changed your beverage from ", self.coffeeMachine.beverage , " to " , beverage)
        self.coffeeMachine.setBeverage(beverage)
    
    def orderDecorator(self, decorator):
        self.coffeeMachine.setDecorator(decorator)

    def summaryOrder(self):
        print(self.coffeeMachine.beverage.description(), "$",self.coffeeMachine.beverage.cost())
        self.coffeeMachine.setState(self.coffeeMachine.notEnoughMoneyState)

    def insertMoney(self, money):
        print("you must confirm your order before.")

    def cancelOrder(self):
        print("you canceled your order")
        self.coffeeMachine.setState(self.coffeeMachine.initialState)

    def changeMoney(self):
        print("you don't insert money yet")

    def releaseOrder(self):
        print("you don't confirm money yet")

class HaveEnoughMoneyState(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine

    def orderBeverage(self ,beverage ):
        print("you confirmed you order, cancel you order if you want")
        
    def orderDecorator(self, decorator):
        print("you confirmed you order, cancel you order if you want")

    def summaryOrder(self):
        print(self.coffeeMachine.beverage.description(), "$",self.coffeeMachine.beverage.cost())

    def insertMoney(self, money):
        print("you inserted money : ",money)
        self.coffeeMachine.setMoney(money)

    def cancelOrder(self):
        print("you canceled your order")
        self.coffeeMachine.setState(self.coffeeMachine.initialState)

    def changeMoney(self):
        print("You will get your changeMoney after Oreder released.")

    def releaseOrder(self):
        print("Waiting... Your Drink is cooking")
        self.coffeeMachine.setState(self.coffeeMachine.soldState)

class NotEnoughMoneyState(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine

    def orderBeverage(self ,beverage ):
        print("you confirmed you order, cancel you order if you want")
        

    def orderDecorator(self, decorator):
        print("you confirmed you order, cancel you order if you want")

    def summaryOrder(self):
        print(self.coffeeMachine.beverage.description(), "$",self.coffeeMachine.beverage.cost())

    def insertMoney(self, money):
        print("you inserted money : ",money)
        self.coffeeMachine.setMoney(money)

    def cancelOrder(self):
        print("you canceled your order")
        self.coffeeMachine.setState(self.coffeeMachine.initialState)

    def changeMoney(self):
        print("You will get your changeMoney after Oreder released.")

    def releaseOrder(self):
        print("Waiting... Your Drink is cooking")

class SoldState(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine

    def orderBeverage(self ,beverage ):
        print("you confirmed you order, cancel you order if you want")
        

    def orderDecorator(self, decorator):
        print("you confirmed you order, cancel you order if you want")

    def summaryOrder(self):
        print(self.coffeeMachine.beverage.description(), "$",self.coffeeMachine.beverage.cost())

    def insertMoney(self, money):
        print("You paid.")

    def cancelOrder(self):
        print("Your Order is finished")

    def changeMoney(self):
        changeMoney = self.coffeeMachine.moneyCount - self.coffeeMachine.beverage.cost()
        print("ChangeMoney : $",changeMoney)
        self.coffeeMachine.moneyCount = 0

    def releaseOrder(self):
        print("Your Beverage is ready to drink")

class NoMaterialState(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine

    def orderBeverage(self ,beverage ):
        print("Out of material.")
        
    def orderDecorator(self, decorator):
        print("Out of material.")

    def summaryOrder(self):
        print("Out of material.")

    def insertMoney(self, money):
        print("Out of material.")

    def cancelOrder(self):
        print("Out of material.")

    def changeMoney(self):
        print("Out of material.")

    def releaseOrder(self):
        print("Out of material.")
    

class CoffeeMachine:

    initialState = None
    haveEnoughMoneyState = None
    notEnoughMoneyState = None
    soldState = None
    noMaterialState = None
    orderedBeverage = None

    state = soldState
    moneyCount = 0

    def __init__(self):
        self.initialState =  InitialState(self)
        self.haveEnoughMoneyState = HaveEnoughMoneyState(self)
        self.notEnoughMoneyState = NotEnoughMoneyState(self)
        self.soldState = SoldState(self)
        self.noMaterialState = NoMaterialState(self)
        self.orderedBeverage = OrderedBeverage(self)


        self.state = self.initialState

        self.beverage = None

        self.houseBlend = 1000
        self.darkRoast = 1000
        self.milk = 5000
        self.soyMilk = 5000
        self.mocha = 1000

    def checkOutOfMaterial(self):
        if self.houseBlend <= 20 and self.darkRoast <= 20 and self.milk <= 200 and self.soyMilk <= 200 and self.mocha <= 50:
            return True

    def orderBeverage(self , beverage):
        if beverage == HouseBlend and  self.houseBlend >= 20:
            self.state.orderBeverage(beverage)
            self.houseBlend -= 20
        elif beverage == DarkRoast and self.darkRoast >= 20:
            self.state.orderBeverage(beverage)
            self.darkRoast -= 20
        elif self.checkOutOfMaterial():
            print("all Beverage is SoldOut")
            self.state = NoMaterialState
        else:
            print("Unknown beverage type or out of that beverage")

    def setBeverage(self , beverage):
        self.beverage = beverage()
        print("You Beverage is ", self.beverage.description())

    def orderDecorator(self , decorator):
        if decorator == Milk and self.milk >= 200:
            self.state.orderDecorator(decorator)
            self.milk -= 200
        elif decorator == SoyMilk and self.soyMilk >= 200:
            self.state.orderDecorator(decorator)
            self.soyMilk -= 200
        elif decorator == Mocha and self.mocha >= 50:
            self.state.orderDecorator(decorator)
            self.mocha -= 50
        elif self.checkOutOfMaterial():
            print("all Decorator is SoldOut")
            self.state = NoMaterialState
        else:
            print("Unknown decorator type or out ot that decorator")

    def moneyCheck(self, money):
        if self.moneyCount >= money:
            self.setState(self.haveEnoughMoneyState)


    def setDecorator(self , decorator):
        self.beverage = decorator(self.beverage)
        print("you add ",self.beverage.__class__.__name__, " now your is " ,self.beverage.description())
    
    def summaryOrder(self):
        self.state.summaryOrder()

    def insertMoney(self , money):
        self.state.insertMoney(money)
        self.moneyCheck(money)

    def cancelOrder(self):
        self.state.cancelOrder()

    def changeMoney(self):
        self.state.changeMoney()

    def releaseOrder(self):
        self.state.releaseOrder()

    def setState(self , state):
        self.state = state

    def setMoney(self, money):
        self.moneyCount += money
    
coffeeMachine1 = CoffeeMachine()
coffeeMachine1.orderBeverage(DarkRoast)
coffeeMachine1.orderDecorator(Milk)
coffeeMachine1.orderDecorator(SoyMilk)
coffeeMachine1.summaryOrder()
coffeeMachine1.insertMoney(10)
print(coffeeMachine1.state)
coffeeMachine1.releaseOrder()
coffeeMachine1.releaseOrder()