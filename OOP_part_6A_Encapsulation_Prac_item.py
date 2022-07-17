
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
        self.__price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self) #Item is the "class", self here is the "instance"

    @property
    def price(self):
        return self.__price

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate ## syntax for using class level attribute



    def __repr__(self): #authomatic method to show how instances will be "represented"
        ## old ver ## return f"Item({self.name}, {self.price}, {self.quantity})"
        return f"{self.__class__.__name__}({self.name}, {self.__price}, {self.quantity})"
        # it is a way to access to name of the class from instance

