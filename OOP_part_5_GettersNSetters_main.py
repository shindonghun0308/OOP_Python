# use main file to just instantiate instances

from OOP_part_5_GettersNSetters_item import Item

item1 = Item("MyItem", 750)
# item1.name = "OtherItem"
#now that name is read-only attribute, it cannot be editted like above

# item1.__name --> clean read-only
# --> is not accessible outside the class due to help of __
# which is like a private key in java and c#

item1.name = "OtherItem"
print(item1.name)
# can be overwritten even though it is read-only,
# due to name.setter in the Item class
