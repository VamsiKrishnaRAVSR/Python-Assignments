# Create animal base class with attribute and related methods then create sub concrete subclass using animal
#  eg of subclass: cow, horse, dog


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(F"{self.name} says -> {self.sound}")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Mooo!")
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow!")
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof!")


cat = Cat("Nemu")  #cat name 
dog=Dog("June")  #dog name
cow=Cow("Cow")  #can't think of a name for this

cat.make_sound()
dog.make_sound()
cow.make_sound()



# ------------------------------------------------------------------------ 

# Create a Bank Account in class which includes customer balance, day wise transactions, 
# can transfer money to different person account, interest given to him with a specific percentage

class Account:
    interest_rate_per_year=8
    def __init__(self, name, balance):
        self.name = name
        self.balance= balance
        self.transactions = 0

    # transfer amount
    def transfer(self, account, amount):
        if(self.balance < amount):
            print("Insufficient funds")
        else:
            self.transactions+=1
            account.transactions+=1
            account.balance += amount
            self.balance -=amount
            print(F'Amount{amount} transferrend from {self.name} to {account.name}')

# No logic, only solved question. Else only on deposits we will calculate interest. 
    def calculate_interest(self):
        interest_earned = self.balance * self.interest_rate_per_year / 100
        self.balance += interest_earned
        self.transactions += 1  # Add a transaction for interest earned
        print(f"Interest earned: {interest_earned}")


    # EXTRA - TO SEE classmethods work in this way Interests are given only on deposit amounts. 
    @classmethod
    def deopsit_enquiry(cls, amount):
        returns = amount * cls.interest_rate_per_year / 100
        print(F"Interest rate is {cls.interest_rate_per_year}")
        print(F"After 1 year, your total returns will be {returns}")

    
acc1 = Account("Vamsi", 1000)
acc2 = Account("Rishabh", 10000)
print(acc1.balance)  #ideally it should be a method named getBalance but time constraints
print(acc2.balance)
acc1.transfer(acc2, 1000)
print(acc1.balance)
print(acc2.balance)
