from OOP_part_6B_Abstraction_Prac_item import Item

item1 = Item("MyItem", 750)

item1.send_email() ## autocompletion happens
# item1.connect() ## does not happen due to abstraction,
# connect is private for class level due to __