class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if amount<=0:
            print("Insufficient amount")
        else:
            self.balance+=amount

    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient Balance")
        elif amount<=0:
            print("Insufficient amount")
        else:
            self.balance-=amount

    def check_balance(self):
        print(f"Name: {self.name}\nBalance: {self.balance}")

object=BankAccount("rahul",5000)
object.withdraw(6000)
object.withdraw(2000)
object.check_balance()
object.deposit(3000)
object.check_balance()
print()
object1=BankAccount("shankar",10000)
object1.withdraw(6000)
object1.withdraw(2000)
object1.check_balance()
object1.deposit(3000)
object1.check_balance()
