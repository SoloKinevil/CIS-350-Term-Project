'''
CIS 350 - Dungeons and Dragons Companion App
Shayan, Phoenix and Ian

This file contains the constructors for the GUI. The GUI will allow user input to export and input character
data as well as specific inventories and notes.
'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import dice_rolling
from tkinter import filedialog
import os
import unittest

class GUI(tk.Frame):
    # Constructor for user GUI and format
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # Create notebook and format
        notebook = ttk.Notebook(self, height = 450, width = 500)
        notebook.pack(expand = True, fill = 'both')

        #Add notebook tab with roll function
        dice_roll_tab = Dice_roll_tab(notebook)
        notebook.add(dice_roll_tab, text='Dice Roll')

        # Add notebook tab with Notes functionality
        notes = Notes_tab(notebook)
        notebook.add(notes, text='Character Creator', )






# This Class initializes the Notes tab where the fields are saved
class Notes_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure grid columns for better spacing
        for i in range(1, 7):
            self.columnconfigure(i, weight=1, pad=10)

        # Configure grid rows for spacing
        for i in range(1, 8):
            self.rowconfigure(i, pad=10)

            # Label for Name
            self.label = ttk.Label(self, text="Character Name")
            self.label.grid(row=1, column=1, sticky="w")
            # Initialize Entry values for Name
            self.name = tk.Entry(self, width=25)
            self.name_contents = tk.StringVar()
            self.name.grid(row=2, column=1, sticky="w")

            # Label for Race
            self.label2 = tk.Label(self, text="Race")
            self.label2.grid(row=1, column=2, sticky="w")
            # Initialize Entry values for Race
            self.race_options = [
                "Dragonborn", "Dwarf", "Eladrin", "Elf", "Gnome", "Half-elf",
                "Half-orc", "Halfling", "Human", "Tiefling"
            ]
            self.race_contents = StringVar()
            race_drop = ttk.OptionMenu(self, self.race_contents, *self.race_options)
            race_drop.grid(row=2, column=2, sticky="w")

            # Label for Class
            self.label3 = tk.Label(self, text="Class")
            self.label3.grid(row=1, column=3, sticky="w")
            # Initialize Entry values for class
            self.class_options = [
                "Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter",
                "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock",
                "Wizard", "Mystic"
            ]
            self.class_contents = StringVar()
            class_drop = ttk.OptionMenu(self, self.class_contents, *self.class_options)
            class_drop.grid(row=2, column=3, sticky="w")

            # Label for Dex Modifier
            self.Dex = ttk.Label(self, text="Dexterity")
            self.Dex.grid(row=3, column=1, sticky="w")
            # Initialize Entry values for Dex
            self.dex = tk.Entry(self, width=10)
            self.dex_contents = tk.StringVar()
            self.dex.grid(row=4, column=1, sticky="w")

            # Label for Str Modifier
            self.Str = ttk.Label(self, text="Strength")
            self.Str.grid(row=3, column=2, sticky="w")
            # Initialize Entry values for Dex
            self.str = tk.Entry(self, width=10)
            self.str_contents = tk.StringVar()
            self.str.grid(row=4, column=2, sticky="w")

            # Label for Int Modifier
            self.Int = ttk.Label(self, text="Intelligence")
            self.Int.grid(row=3, column=3, sticky="w")
            # Initialize Entry values for Dex
            self.int = tk.Entry(self, width=10)
            self.int_contents = tk.StringVar()
            self.int.grid(row=4, column=3, sticky="w")

            # Label for Notes
            self.label4 = tk.Label(self, text="Notes")
            self.label4.grid(row=5, column=1, sticky="nw")
            # Initialize Entry values for NOTES
            self.notes = tk.Entry(self, width=100)
            self.note_contents = tk.StringVar()
            self.notes.grid(row=6, column=1, columnspan=3, sticky="w")

            # Bind text variables to entries
            self.notes["textvariable"] = self.note_contents
            self.dex["textvariable"] = self.dex_contents
            self.str["textvariable"] = self.str_contents
            self.int["textvariable"] = self.int_contents
            self.name["textvariable"] = self.name_contents

            # Import button
            open_button = tk.Button(self, text="Import Data", command=self.open_file)
            open_button.grid(row=8, column=1, sticky="w")

            # Save button
            save_button = tk.Button(self, text="Save Data", command=self.save_contents)
            save_button.grid(row=8, column=3, sticky="w")

        # Set fields to previously saved values
        if os.path.exists('saved_contents.txt'):
            with open('saved_contents.txt', 'r') as incoming:
                lines = incoming.readlines()

            if len(lines) >= 7:
                self.name_contents.set(lines[0].strip())
                self.race_contents.set(lines[1].strip())
                self.class_contents.set(lines[2].strip())
                self.dex_contents.set(lines[3].strip())
                self.str_contents.set(lines[4].strip())
                self.int_contents.set(lines[5].strip())
                self.note_contents.set(lines[6].strip())

    # This function saves the users stored information to a file of their choice "Export"
    def save_contents(self, *args):
        filepath = filedialog.asksaveasfilename()
        with open(filepath, 'w') as f:
            f.write(self.name_contents.get() + "\n")
            f.write(self.race_contents.get() + "\n")
            f.write(self.class_contents.get() + "\n")
            f.write(self.dex_contents.get() + "\n")
            f.write(self.str_contents.get() + "\n")
            f.write(self.int_contents.get() + "\n")
            f.write(self.note_contents.get() + "\n")
        with open('saved_contents.txt', 'w') as f:
            f.write(self.name_contents.get() + "\n")
            f.write(self.race_contents.get() + "\n")
            f.write(self.class_contents.get() + "\n")
            f.write(self.dex_contents.get() + "\n")
            f.write(self.str_contents.get() + "\n")
            f.write(self.int_contents.get() + "\n")
            f.write(self.note_contents.get() + "\n")

    # Allows user to upload text document to input into application
    def open_file(self):
        # Ask user for filepath through file explorer
        filepath = filedialog.askopenfilename()
        while filepath:
            # Ensure file is .txt
            if filepath.endswith('.txt'):
                print("Opening Text File: " + filepath)
                with open(filepath, 'r') as incoming:
                    lines = incoming.readlines()

                # Assign values from the file if they exist
                if len(lines) >= 5:
                    self.name_contents.set(lines[0].strip())
                    self.race_contents.set(lines[1].strip())
                    self.class_contents.set(lines[2].strip())
                    self.dex_contents.set(lines[3].strip())
                    self.str_contents.set(lines[4].strip())
                    self.int_contents.set(lines[5].strip())
                    self.note_contents.set(lines[6].strip())
                else:
                    print("Error: File does not contain enough data.")
                return
            return




class Dice_roll_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.updated_sides = 20

        self.dice_roller = dice_rolling.DiceRoll()
        self.dice_roller.set_dice(1)
        self.dice_roller.set_sides(20)
        
        self.label2 = tk.Label(self, text="Roll: 0")
        self.label2.pack()

        self.button4 = tk.Button(self, text='Roll', command=self.roll_dice)
        self.button4.pack()

        self.confirm_button = tk.Button(self, text = 'Confirm', command = self.set_sides)
        self.confirm_button.pack()

        self.sides1 = tk.Entry(self, width = 10)
        self.sides1.pack()

    def roll_dice(self):
        result = self.dice_roller.dice_roll(self.dice_roller.dice, self.dice_roller.sides)
        self.label2.config(text=f"Roll: {result}")

    def set_sides(self):
        string_sides = self.sides1.get()
        self.dice_roller.set_sides(int(string_sides))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("D&D Companion App")
    myapp = GUI(root)
    myapp.mainloop()