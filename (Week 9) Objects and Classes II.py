import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class DiceSet:
    def __init__(self, num_dice=2, sides=6):
        self.dice = [Die(sides) for _ in range(num_dice)]

    def roll_all(self):
        return [die.roll() for die in self.dice]

class DiceRollerApp:
    def __init__(self, sides, num_dice, num_rolls):
        self.dice_set = DiceSet(num_dice, sides)
        self.num_rolls = num_rolls

    def run(self):
        print(f" Rolling {len(self.dice_set.dice)} dice with {self.dice_set.dice[0].sides} sides, {self.num_rolls} times...\n")
        for i in range(1, self.num_rolls + 1):
            result = self.dice_set.roll_all()
            print(f"Roll {i}: {result} → Total: {sum(result)}")

if __name__ == "__main__":
    sides = int(input("How many sides per die? "))
    num_dice = int(input("How many dice to roll? "))
    num_rolls = int(input("How many times to roll the dice? "))

    app = DiceRollerApp(sides, num_dice, num_rolls)
    app.run()
