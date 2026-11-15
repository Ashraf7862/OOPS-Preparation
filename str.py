class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return f"Product Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

if __name__=="__main__":
    product=Product("Laptop",50000,2)
    print([product])
    print()
    print(repr(product))
    print()
    print(product.__repr__())
    print()
    print(product.__str__())
    print()
    print(str(product)[0])