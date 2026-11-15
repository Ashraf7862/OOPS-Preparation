from shop1 import Product

class shoppingCart:
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        self.products.append(product)

    def remove_prod(self,id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print(f"product {id} removed successfully")
                break
        else:
            print("No product found to be removed")
    def price(self,product):
        print(product.price)

    def display(self,name):
        print(f"{name}'s Cart:\n")
        for obj in self.products:
            print(f"Name: {obj.name}\nPrice: {obj.price}\nid: {obj.id}\n")

class Customer:
    def __init__(self,name):
        self.name=name
        self.cart=shoppingCart()

object1=Product("Bottle",200,12)
object2=Product("pillow",300,15)
customer1 = Customer("Rahul")
customer2 = Customer("Arun")
customer1.cart.add_product(object1)
customer1.cart.add_product(object2)
customer1.cart.display(customer1.name)
customer1.cart.remove_prod(13)
customer1.cart.remove_prod(15)
customer1.cart.display(customer1.name)

object3=Product("pencil",15,13)
object4=Product("pen",50,14)
customer2.cart.add_product(object3)
customer2.cart.add_product(object4)
customer2.cart.display(customer2.name)
customer2.cart.remove_prod(13)
customer2.cart.remove_prod(15)
customer2.cart.display(customer2.name)
