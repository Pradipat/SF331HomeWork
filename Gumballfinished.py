from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_quarter(self):
        pass
    
    @abstractmethod
    def eject_quarter(self):
        pass
    
    @abstractmethod
    def turn_crank(self):
        pass
    
    @abstractmethod
    def dispense(self):
        pass
    

class SoldState(State):
    def insert_quarter(self,gumball_machine):
        print("Please wait, we're already giving you a gumball")
    
    def eject_quarter(self,gumball_machine):
        print("Sorry, you already turned the crank")
    
    def turn_crank(self,gumball_machine):
        print("Turning twice doesn't get you another gumball")
    
    def dispense(self,gumball_machine):
        gumball_machine.release_ball()
        if gumball_machine.get_count() > 0:
            gumball_machine.set_state(gumball_machine.no_quarter_state)
        else:
            print("Oops, out of gumballs!")
            gumball_machine.set_state(gumball_machine.sold_out_state)

class NoQuarterState(State):
    def insert_quarter(self , gumball_machine):
        print("You inserted a quarter")
        gumball_machine.set_state(gumball_machine.has_quarter_state)
    
    def eject_quarter(self,gumball_machine):
        print("You haven't inserted a quarter")
    
    def turn_crank(self,gumball_machine):
        print("You turned, but there's no quarter")
    
    def dispense(self,gumball_machine):
        print("You need to pay first")

class SoldOutState(State):
    def insert_quarter(self,gumball_machine):
        print("You can't insert another quarter, the machine is sold out")
    
    def eject_quarter(self,gumball_machine):
        print("you can't eject, You haven't inserted a quarter yet")
    
    def turn_crank(self,gumball_machine):
        print("You turned but there are no gumballs")
    
    def dispense(self,gumball_machine):
        print("No gumball dispensed")

class HasQuarterState(State):
    def insert_quarter(self,gumball_machine):
        print("You can't insert another quarter, the machine is sold out")
    
    def eject_quarter(self,gumball_machine):
        print("Quarter returned")
        gumball_machine.set_state(gumball_machine.no_quarter_state)
    
    def turn_crank(self,gumball_machine):
        print("You turned...")
        gumball_machine.set_state(gumball_machine.sold_state)
    
    def dispense(self,gumball_machine):
        print("No gumball dispensed")

class GumballMachine:
    def __init__(self,numberGumballs):
        self.sold_out_state = SoldOutState()
        self.no_quarter_state = NoQuarterState()
        self.has_quarter_state = HasQuarterState()
        self.sold_state = SoldState()
        
        
        self.count = numberGumballs
        if self.count > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self,gumball_machine):
        self.state.insert_quarter(gumball_machine)

    def eject_quarter(self,gumball_machine):
        self.state.eject_quarter(gumball_machine)

    def turn_crank(self,gumball_machine):
        self.state.turn_crank(gumball_machine)
        self.state.dispense(gumball_machine)

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        if self.count != 0:
            print("A gumball comes rolling out the slot...")
            self.count -= 1
    
    def get_count(self):
        return self.count


gumball_machine = GumballMachine(0)
print("Initial State:", gumball_machine.state)

gumball_machine.insert_quarter(gumball_machine)
print("After Insert Quarter:", gumball_machine.state)

gumball_machine.turn_crank(gumball_machine)
print("After Turn Crank:", gumball_machine.state)

gumball_machine.insert_quarter(gumball_machine)
print("After Insert Quarter:", gumball_machine.state)

gumball_machine.turn_crank(gumball_machine)
print("After Turn Crank:", gumball_machine.state)
