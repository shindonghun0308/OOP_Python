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
        self.name = name # take note of __ for read only
        self.__price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self) #Item is the "class", self here is the "instance"

    def __connect(self, smpt_server): # __ only allows it to be called within the class
        pass
    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, Donghun
        """
    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()


    def __repr__(self): #authomatic method to show how instances will be "represented"
        ## old ver ## return f"Item({self.name}, {self.price}, {self.quantity})"
        return f"{self.__class__.__name__}({self.name}, {self.__price}, {self.quantity})"
        # it is a way to access to name of the class from instance

