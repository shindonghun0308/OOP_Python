class Item:
    pay_rate = 0.8 #this is class attribute

    all = []
    def __init__(self, name: str, price: float, quantity=0): #this occurs automatically during instantiation/ constructor
                                                                # name only accepts str,
                                                                #quantity: only accepts int cuz default value is int

        # Run validations to the received arguments/ "conditionals for arguments"
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign to self object/ instantiation attribute
        self.name = name # assigning an attribute to each instance that is created
        self.price = price #assigning an attribute like this doesnt mean that they cannot be added for specific instances
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self) #Item is the "class", self here is the "instance"

    # def calculate_total_price(self, x, y):
    #     return x*y

    def calculate_total_price(self):
        return self.price * self.quantity #once the instances have been created, these attributes are made auto
    pass

    def apply_discount(self):
        self.price = self.price * self.pay_rate ## syntax for using class level attribute

    def __repr__(self): #authomatic method to show how instances will be "represented"
        return f"Item({self.name}, {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)

print(Item.all)
# when no repr, [<__main__.Item object at 0x0000013B73051FD0>, <__main__.Item object at 0x0000013B73051F10>,
# which is not v friendly --> use __repr__ method in the class
# with repr, printed: [Item(Phone, 100, 1), Item(Laptop, 1000, 3), Item(Cable, 10, 5), Item(Mouse, 50, 5), Item(Keyboard, 75, 5)]