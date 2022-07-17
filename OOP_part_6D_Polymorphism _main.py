from OOP_part_6D_Polymorphism_Keyboard import Keyboard

item1 = Keyboard("dong's Keyboard", 1000, 3)

item1.apply_discount()
# with inheritance, diff objects can use functions of a single parent class --> polymorphism concept


print(item1.price)