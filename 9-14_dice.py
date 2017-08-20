from random import randint

class Die():
    """Create a random number generator"""
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        x = (randint(1,self.sides))
        print(x)

ten_sided = Die(10)
for i in range(0,10):
    ten_sided.roll_die()

twenty_sided = Die(20)
for i in range(0,10):
    twenty_sided.roll_die()
