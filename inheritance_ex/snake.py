from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "If I can touch it, I can smell it"


smart_snake = Snake()

print(f"This function is called from parent class - {smart_snake.hunt()}")
print(f"This function is called from the current class - {smart_snake.use_tongue_to_smell()}")
print(f"This function is called from the grandparent class - {smart_snake.breathe()}")

# use oop_pillars.md file to add this code to your documentation

