"""
CIS 350 - Dungeons & Dragons Companion App
Shayan, Phoenix, Ian

This file contains the unit tests for the DiceRoll class along with other classes utilizied in the project.
"""
import unittest
from dice_rolling import DiceRoll

class TestDiceRoll(unittest.TestCase):
    # Test the set_dice function
    def test_set_dice(self):
        #Initialize the DiceRoll class
        dice = DiceRoll()

        # Set the number of Dice to 1
        dice.set_dice(1)
        
        # Check if the number of dice is set to 1
        self.assertEqual(dice.dice, 1)

        with self.assertRaises(TypeError):
            dice.set_dice("1") # Raises an Error if the input is not an integer
        with self.assertRaises(ValueError):
            dice.set_dice(0) # Raises an error if the input is less than 1

    # Test the set_sides function
    def test_set_sides(self):
        # Initialize the DiceRoll class
        dice = DiceRoll()
        
        # Set the sides of the dice to 20
        dice.set_sides(20)

        # Check if the sides are set to 20
        self.assertEqual(dice.sides, 20)

        with self.assertRaises(TypeError):
            dice.set_sides("20") # Return a TypeError if the input is not an integer
        with self.assertRaises(ValueError):
            dice.set_sides(0) # Return a ValueError if the input is less than 1

    # Test the set_modifier function
    def test_set_modifier(self):
        # Initialize the DiceRoll class
        dice = DiceRoll()

        # Set the current modifier to 1
        dice.set_modifier(1)

        # Check if the modifier was successfully set to 1
        self.assertEqual(dice.modifier, 1)
        
        with self.assertRaises(TypeError):
            dice.set_modifier("1") # Return a TypeError if the input is not an integer
        with self.assertRaises(ValueError):
            dice.set_modifier(-1) # Return a ValueError if the input is less than 0

    # Test the roll_dice function
    def test_roll_dice(self):
        # Initialize the DiceRoll class
        dice = DiceRoll()
        dice.set_dice(1) # Set the number of dice to 1
        dice.set_sides(20) # Set the sides of the dice to 20
        self.assertTrue(dice.dice_roll(dice.dice, dice.sides) in range(1, 21)) # Check if the roll is between 1 and 20

    def test_get_dice(self):
        # Initialize the DiceRoll class
        dice = DiceRoll()
        dice.set_dice(1) # Set the number of dice to 1
        self.assertEqual(dice.get_dice(), 1) # Check if the number of dice is 1

    def test_get_sides(self):
        #Initialize the DiceRoll class
        dice = DiceRoll()
        dice.set_sides(20) # Set the sides of the dice to 20
        self.assertEqual(dice.get_sides(), 20) # Check if the sides are 20
    
    def test_get_modifier(self):
        # Initialize the DiceRoll class
        dice = DiceRoll()
        dice.set_modifier(1) # Set the modifier to be added to the dice roll to 1
        self.assertEqual(dice.get_modifier(), 1) # Check if the modifier is 1
    

if __name__ == '__main__':
    unittest.main() # Run the tests