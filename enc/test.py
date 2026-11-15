# _name -> Single underscore(Protected) is just a convetion to tell "please dont access it directly from outside"
# __name -> Double unserscore(Private) drigger something called name mangling (Direct access from outside cause AttributeError)

class BankAccount:
    def __init__(self,holder,branch,balance):
        self.holder=holder
        self._branch=branch
        self.__balance=balance

    def set_balance(self,balance):
        if balance<0:
            print("invalid balance")
        else:
            self.__balance=balance
    def get_balance(self):
        return self.__balance
    def display(self):
        return f"{self.holder}\n{self._branch}\n{self.__balance}"

object=BankAccount("Rahul","XYZ",20000)
object._branch="ABC"  # Shouldn't do this
object.__balance=40000   # Create new Attribut with this name on the object
print(object.__balance)
object._BankAccount__balance=30000   # Shouldn't do this
print(object.display())
print()
object.set_balance(90000)
print(object.get_balance())