# create class called Animal - file name starts with lower case, class name starts with upper case
# add common attributes and behaviour or functions
# syntax: class Name: - class Animal:
class Animal:  # follow correct naming convention and best practices
    # we need to initialise the class with built-in method called __init__(self)
    # self refers to current class
    def __init__(self):  # any attributes attached to the class should be part of init method
        # self.var = True
        self.alive = True
        self.spine = True
        self.eyes = True

    # let's create some methods to add common behaviours
    def breathe(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "time to eat!..."


# create an object of this class
cat = Animal()  # this will create an object of our Animal class

# print(cat.breathe())  # calling method using object of Animal class
# print(cat.eat())
