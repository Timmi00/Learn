from random import randint


class Dice:

    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


dice = Dice(6)
dice.roll_die()
