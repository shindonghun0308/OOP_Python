from OOP_part_6A_Encapsulation_Prac_item import Item


class Keyboard(Item):  # "inheriting" the methods inside the parent class to child class,

    pay_rate = 0.4 #overriding in child class of parent class attribute is legal

    def __init__(self,
                 name: str,
                 price: float,
                 quantity=0):

        super().__init__(
            name, price, quantity
        )  # this helps to inherit all the Item class attributes
        pass
