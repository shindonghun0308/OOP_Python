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
        self.__name = name # take note of __ for read only
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self) #Item is the "class", self here is the "instance"

    @property # helps to "get" the read-only attribut, name
    # Property Decorator = Read-Only Attribute (unedittable)
    def name(self):
        # can write function like
        # print("you are trying to GET"
        return self.__name # take note of __

    @name.setter #still want to set even though it is read only
    def name(self, value):
        # can write function like
        # print("you are trying to SET")
        # or
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

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