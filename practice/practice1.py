from inheritance_ex.snake import Snake


# 1.
# correct syntax for defining a function
def function():
    pass


# 2.
list_items = [1, 2, 3, 4, 5]

for i in list_items:
    print(i)

print("\nmiddle\n")

limit = 0
while limit < 5:
    print(list_items[limit])
    limit += 1

# 3.

# Correct syntax for boolean operators:
# "and", "or", "not"
# no: &&, ||, &, |

# 4.

# dictionary declaration syntax
dictionary = {
    "name": "Angel",
    "last_name": "Gelemerov",
    "age": 21,
    "DOB": "08/11/2000",
    "test": True
}

# list syntax
listings = [1, 2, 3, 4, 5]

# tuple syntax
tuples = (1, 2, 3, 4, 5)

# indexing always starts at 0 for any data structure in python

# print 3rd and 5th item from list
for i in range(5):
    if i == 2:
        print(i)
    elif i == 4:
        print(i)

# print 3rd and 5th item from tuple
for i in range(5):
    if i == 2:
        print(i)
    elif i == 4:
        print(i)

# print 3rd and 5th item from dictionary
counter = 0
for x, y in dictionary.items():
    counter += 1
    if counter == 3:
        print(x, y)
    elif counter == 5:
        print(x, y)


# lists and dictionaries are mutable (changeable), tuples are not
# lists or dicts within a tuple are immutable


# create a class and instances
class Testing(Snake):
    def __init__(self):
        super().__init__()
        self.new_var = "test new_var"


test1 = Testing()
print(test1.new_var)

# adding item to list, tuple and dict

listings.append(8)
# we cannot ammend tuples, no addition method
dictionary.update({"Testing": 9})

print(listings)
print(dictionary.items())

# shopping items

shopping_items = {
    "eggs": 1.85,
    "bread": 1.50,
    "peppers": 0.90
}


def food_bill():
    total_bill = 0
    print(shopping_items.values())
    for item in shopping_items.values():
        total_bill += item

    print(total_bill)
    for item, cost in shopping_items.items():
        print(item, cost)

    return total_bill


print(food_bill())
