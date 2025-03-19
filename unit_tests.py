"""
CIS 350 - Dungeons & Dragons Companion App
Shayan, Phoenix, Ian

This file contains the unit tests for the DiceRoll class along with other classes utilizied in the project.
"""
import unittest
from dice_rolling import DiceRoll
from initiative_tracker import InitiativeTracker

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

class TestInitiativeTracker(unittest.TestCase):
    # Test the add_combatant function
    def test_add_combatant(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        self.assertEqual(initiative.combatants["Goblin"], 15) # Check if the combatant was added to the combatants dictionary

    # Test the remove_combatant function
    def test_remove_combatant(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.remove_combatant("Goblin") # Remove the combatant from the Initiative Tracker
        self.assertNotIn("Goblin", initiative.combatants) # Check if the combatant was removed from the combatants dictionary
    
    # Test the remove_combatant function with a combatant that is not in the combatants dictionary
    def test_remove_combatant_not_in_combatants(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.remove_combatant("Orc") # Try to remove a combatant that is not in the combatants dictionary
        self.assertEqual(initiative.combatants["Goblin"], 15) # Check if the combatant is still in the combatants dictionary

    # Test the update_turn_order function
    def test_update_turn_order(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.add_combatant("Orc", 10) # Add another combatant to the Initiative Tracker
        initiative.update_turn_order() # Update the turn order
        self.assertEqual(initiative.turn_order, ["Goblin", "Orc"]) # Check if the turn order is updated correctly

    # Test the next_turn function
    def test_next_turn(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.add_combatant("Orc", 10) # Add another combatant to the Initiative Tracker
        initiative.update_turn_order() # Update the turn order
        initiative.next_turn() # Advance to the next turn
        self.assertEqual(initiative.current_turn, 1) # Check if the current turn is updated correctly

    # Test the previous_turn function
    def test_previous_turn(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.add_combatant("Orc", 10) # Add another combatant to the Initiative Tracker
        initiative.update_turn_order() # Update the turn order
        initiative.next_turn() # Advance to the next turn
        initiative.previous_turn() # Go back to the previous turn
        self.assertEqual(initiative.current_turn, 0) # Check if the current turn is updated correctly
    
    # Test the reset_turns function
    def test_reset_turns(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.add_combatant("Orc", 10) # Add another combatant to the Initiative Tracker
        initiative.update_turn_order() # Update the turn order
        initiative.next_turn() # Advance to the next turn
        initiative.reset_turns() # Reset the turn order
        self.assertEqual(initiative.current_turn, 0) # Check if the current turn is reset to 0
    
    # Test the display_initiative_order function
    def test_display_initiative_order(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.add_combatant("Orc", 10) # Add another combatant to the Initiative Tracker
        initiative.update_turn_order()
        initiative.display_initiative_order()

    # Test the rest_session function
    def test_reset_session(self):
        # Initialize the InitiativeTracker class
        initiative = InitiativeTracker()
        initiative.add_combatant("Goblin", 15) # Add a combatant to the Initiative Tracker
        initiative.add_combatant("Orc", 10) # Add another combatant to the Initiative Tracker
        initiative.update_turn_order()
        initiative.reset_session() # Reset the Initiative Session
        self.assertEqual(initiative.combatants, {}) # Check if the combatants dictionary is empty
        self.assertEqual(initiative.turn_order, []) # Check if the turn order is empty
        self.assertEqual(initiative.current_turn, 0) # Check if the current turn is reset to 0
