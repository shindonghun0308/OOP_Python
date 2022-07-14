class Item:
    pay_rate = 0.8 #this is class attribute
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

    # def calculate_total_price(self, x, y):
    #     return x*y

    def calculate_total_price(self):
        return self.price * self.quantity #once the instances have been created, these attributes are made auto
    pass

    def apply_discount(self):
        self.price = self.price * Item.pay_rate ## syntax for using class level attribute




item1 = Item("Phone", 100, 3) #item1 is an instance of Item class
# item1.name = "Phone" #addingt attributes
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))


item2 = Item("Book", 40, 2) #item1 is an instance of Item class
# # item2.name = "Book" #addingt attributes
# item2.price = 40
# item2.quantity = 2

print(item1.calculate_total_price())

# print(type(item1)) # <class '__main__.Item'>, customised type/class
# print(type(item1.name)) # <class 'str'>

# random_str = "aaa"
# print(random_str.upper()) # this is how a pre-defined method/function in class is used, function inside class is called method

print(Item.pay_rate) #class attribute
print(item1.pay_rate) #it can access class level attribute

print(Item.__dict__) # Show all the attributes for class level
print(item1.__dict__) # All the contributes for instance level

item1.pay_rate = 0.7 # this is in instance level
Item.pay_rate # this is class level

print(Item.pay_rate - item1.pay_rate ) #these are two diff attributes one in class level, one is instance level


