from OOP_part_5_GettersNSetters_item import Item

class Phone(Item):  # "inheriting" the methods inside the parent class to child class,

    # class Phone: "child class"
    # class Item: "parent class"
    def __init__(self,
                 name: str,
                 price: float,
                 quantity=0,
                 broken_phones=0):  # this occurs automatically during instantiation/ constructor

        # call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )  # this helps to inherit all the Item class attributes

        # Run validations to the received arguments/ "conditionals for arguments"

        assert broken_phones >= 0, f"Broken Phones {quantity} is not greater than zero!"

        # Assign to self object/ instantiation attribute
        self.broken_phones = broken_phones


    pass
