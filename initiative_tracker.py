'''
CIS 350 - Dungeons and Dragons Companion App
Shayan, Phoenix and Ian

This file contains the code for the Initative Tracker to be used in the GUI. This allows someone to add and remove combatants,
cycle through the list of combatants, and roll for initiative for each combatant should they choose to do so.
'''

class InitiativeTracker:
    def __init__(self):
        self.combatants = {} # Stores combatants and their initiative, {name: initiative}
        self.turn_order = [] # Ordered list of names. The order of this list is the order of combatants in the round
        self.current_turn = 0 # Index of the current turn in the turn_order list
    
    def add_combatant(self, name, initiative):
        # Add a combatant to the combatants dictionary and update the turn order.
        self.combatants[name] = initiative
        self.update_turn_order()
    
    def remove_combatant(self,name):
        # If the name is in the Combatants Dictionary, remove it and update the turn order.
        if name in self.combatants:
            del self.combatants[name]
            self.update_turn_order()
        else:
            print(f"{name} is not in the combatants list.")

    def update_turn_order(self):
        # Updates the initiative order based on the stored values.
        self.turn_order = sorted(self.combatants.keys(), key=lambda x: self.combatants[x], reverse=True)
    
    def next_turn(self):
        # Advance to the next turn in the Initiative.
        self.current_turn = (self.current_turn + 1) % len(self.turn_order)
        
    def previous_turn(self):
        # Go back to the previous turn in the Initiative.
        self.current_turn = (self.current_turn - 1) % len(self.turn_order)
        
    def reset_turns(self):
        # Reset the turn order to the beginning.
        self.current_turn = 0
    
    def reset_session(self):
        # Reset the Initiative Session to its default state.
        self.combatants = {}
        self.turn_order = []
        self.current_turn = 0
        
    def display_initiative_order(self):
        # Displays the current Initiative Order with the current turn highlighted.
        for i, name in enumerate(self.turn_order):
            marker = "-->" if i ==self.current_turn else ""
            print(f"{marker} {name}: {self.combatants[name]}")
