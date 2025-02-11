"""
CIS 350 - Dungeons and Dragons Companion App
Shayan, Phoenix and Ian

This file contains a Dice Rolling Class which will be used to roll dice for the game. 
This code does so by utilizing the random module's randint method in Python.
"""
from random import randint


class DiceRoll():
    # Constructor for the Class
    def __init__(self):
        self.dice = 0 # The number of dice to be rolled
        self.sides = 0 # The number of sides of the dice
        self.modifier = 0 # The modifier to be added to the dice
    
    # This function sets the number of dice to be rolled
    def set_dice(self, dice:int):
        if type(dice) != int:
            raise TypeError("Dice must be an integer") # Return a TypeError if the input is not an integer
        elif dice < 1:
            raise ValueError("Dice must be greater than 0") # Return a ValueError if the input is less than 1
        self.dice = dice
    
    # This function sets the number of sides on the dice
    def set_sides(self, sides: int):
        if type(sides) != int:
            raise TypeError("Sides must be an integer") # Return a TypeError if the input is not an integer
        elif sides < 1:
            raise ValueError("Sides must be greater than 0") # Return a ValueError if the input is less than 1
        self.sides = sides
    
    # This function sets the modifier to be added to the roll
    def set_modifier(self, modifier: int):
        if type(modifier) != int:
            raise TypeError("Modifier must be an integer") # Return a TypeError if the input is not an integer
        elif modifier < 0:
            raise ValueError("Modifier must be greater than or equal to 0") # Return a ValueError if the input is less than 0
        self.modifier = modifier
    
    # This function rolls the dice and returns the result
    def dice_roll(self, dice, sides):
        total = 0 # Set the total to 0
        # Create a for loop to iterate through the number of dice to be used.
        for i in range(dice):
            # Add the result of the dice roll to the total
            total += randint(1, sides)
        return total # Return the total of the dice rolls.

# Test code to see if the class works as expected.    
if __name__ == "__main__":
    dice = DiceRoll()
    dice.set_dice(1)
    dice.set_sides(20)
    dice.set_modifier(0)
    print(dice.dice_roll(dice.dice, dice.sides)) # Print the result of the dice roll