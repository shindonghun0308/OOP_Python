import csv

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



    @classmethod
    def instantiate_from_csv(cls): #class method, cls, class is called behind this function
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader) #contains list of Dictionaries

        for item in items:
            # print(item) #print out each dictionary set
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )


    @staticmethod
    def is_integer(num):
        # WE will count out the floats that are point zero
        # for i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self): #authomatic method to show how instances will be "represented"
        ## old ver ## return f"Item({self.name}, {self.price}, {self.quantity})"
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
        # it is a way to access to name of the class from instance


class Phone(Item): # "inheriting" the methods inside the parent class to child class,
                    # class Phone: "child class"
                    # class Item: "parent class"
    def __init__(self,
                 name: str,
                 price: float,
                 quantity=0,
                 broken_phones=0):  # this occurs automatically during instantiation/ constructor

        #call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )   # this helps to inherit all the Item class attributes

        # Run validations to the received arguments/ "conditionals for arguments"

        assert broken_phones >= 0, f"Broken Phones {quantity} is not greater than zero!"

        # Assign to self object/ instantiation attribute
        self.broken_phones = broken_phones

    pass


# phone1 = Item("jscPhonev10", 500, 5)
# phone1.broken_phones = 1
# phone2 = Item("jscPhonev20", 700, 5)
# phone2.broken_phones = 1

# phone1 = Phone("jscPhonev10", 500, 5)   #top and this works without error
# phone1.broken_phones = 1 # but this attribute will only apply to the Phone class
# phone2 = Phone("jscPhonev20", 700, 5)
# phone2.broken_phones = 1

phone1 = Phone("jscPhonev10", 500, 5)

print(Item.all)
print(Phone.all) #it shows that the [Item(jscPhonev10, 500, 5)], due to repr inline 65.
# it works even though all is no longer in Phone class, due to inheritance