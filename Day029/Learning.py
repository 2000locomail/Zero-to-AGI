# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()

# Encapsulation
# Wrapping data and function int a single unit (Object).



# Let's Practice
# Create Account class with 2 attributes - balance & account no
# Create Methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount}, was debited.")
        print(f"Total Balance = {self.get_balance()}")

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount}, was credited.")
        print(f"Total Balance = {self.get_balance()}")
    
    def get_balance(self):
        return self.balance
    

acc1 = Account(10000, 123456)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(5000)
print(acc1.balance)
print(acc1.account_no)
        
