from __future__ import annotations
from abc import ABC, abstractmethod
import random

class State(ABC):
  @abstractmethod
  def insertQuarter(self) -> None:
    pass

  @abstractmethod
  def ejectQuarter(self) -> None:
    pass

  @abstractmethod
  def turnCrank(self) -> None:
    pass

  @abstractmethod
  def dispense(self) -> None:
    pass

class SoldOutState(State):
    def __init__(self, gumballMachine: GumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def __str__(self):
        return "sold out"

class SoldState(State):
    def __init__(self, gumballMachine : GumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def refill(self):
        pass

    def __str__(self):
        return "dispensing a gumball"

class WinnerState(State):
    def __init__(self, gumballMachine : GumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a Gumball")

    def ejectQuarter(self):
        print("Please wait, we're already giving you a Gumball")

    def turnCrank(self):
        print("Turning again doesn't get you another gumball!")

    def dispense(self):
        print("YOU'RE A WINNER! You get two gumballs for your quarter")
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("Oops, out of gumballs!")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def refill(self):
        pass

    def __str__(self):
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"
    
class NoQuarterState(State):
    def __init__(self, gumballMachine : GumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")

    def refill(self):
        pass

    def __str__(self):
        return "waiting for quarter"

class HasQuarterState(State):
    def __init__(self, gumballMachine : GumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert another quarter")

    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("You turned...")
        winner = random.randint(0, 9)
        if (winner == 0) and (self.gumballMachine.getCount() > 1):
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        pass

    def __str__(self):
        return "waiting for turn of crank"

class GumballMachine:

  soldOutState = None
  noQuarterState = None
  hasQuarterState = None
  soldState = None
  winnerState = None

  state = soldOutState
  count = 0

  def __init__(self, numberGumballs):
    self.soldOutState =  SoldOutState(self)
    self.noQuarterState = NoQuarterState(self)
    self.hasQuarterState = HasQuarterState(self)
    self.soldState = SoldState(self)
    self.winnerState = WinnerState(self)

    self.count = numberGumballs
    if numberGumballs > 0:
      self.state = self.noQuarterState

  def insertQuarter(self):
    self.state.insertQuarter()

  def ejectQuarter(self):
    self.state.ejectQuarter()

  def turnCrank(self):
    self.state.turnCrank()
    self.state.dispense()

  def setState(self, state) :
    self.state = state

  def releaseBall(self):
    print("A gumball comes rolling out the slot...")
    if self.count > 0:
      self.count -= 1

  def getCount(self):
    return self.count

  def refill(self, count):
    self.count += count
    print("The gumball machine was just refilled; it's new count is: " + str(self.count))
    self.state.refill()

  def getState(self):
    return self.state

  def getSoldOutState(self):
    return self.soldOutState

  def getNoQuarterState(self):
    return self.noQuarterState

  def getHasQuarterState(self):
    return self.hasQuarterState

  def getSoldState(self):
    return self.soldState

  def getWinnerState(self):
    return self.winnerState

  def __str__(self):
    result = "\nMighty Gumball, Inc."
    result += "\nPython-enabled Standing Gumball Model #2023"
    result += "\nInventory: " + str(self.count) + " gumball"
    if self.count != 1:
      result += "s"
    result += "\n"
    result += "Machine is " + str(self.state) + "\n"
    return result

gumballMachine = GumballMachine(10)

print(gumballMachine)

gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()

print(gumballMachine)
print('Check ---> Correct number of gumball should be 8 \n')

gumballMachine.ejectQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.ejectQuarter()

print(gumballMachine)
print('Check ---> Correct number should be 8 \n')

gumballMachine.insertQuarter()
gumballMachine.ejectQuarter()
gumballMachine.turnCrank()

print(gumballMachine)
print('Check ---> Correct number should be 8 \n')

