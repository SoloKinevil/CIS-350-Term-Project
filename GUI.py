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

class GUI(tk.Frame):
    # Constructor for user GUI and format
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        notebook = ttk.Notebook(self, height = 300, width = 300)
        notebook.pack(expand = True, fill = 'both')
        dice_roll_tab = Dice_roll_tab(notebook)
        notes = Notes_tab(notebook)
        notebook.add(dice_roll_tab, text='Dice Roll')
        notebook.add(notes, text='Character',)


# This Class initialized the Notes tab
class Notes_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # ENTRY WIDGET
        # Read in saved_contents to updated user notes
        f = open('saved_contents.txt', 'r')
        self.saved_contents = f.read()
        f.close()

        self.label2 = tk.Label(self, text="Notes")
        self.label2.pack()

        # Initialize Entry values for NOTES
        self.notes = tk.Entry(self ,width = 100)  # Starts tk entry field

        self.contents = tk.StringVar()
        self.contents.set(self.saved_contents)  # Sets the entry field to previous notes
        self.notes.pack()

        # Widget follows changes
        self.notes["textvariable"] = self.contents

        # Saves new user changes to text document when return it pressed
        self.notes.bind('<Key-Return>', self.save_contents)

    # This function saves the users stored information
    def save_contents(self, *args):
        self.saved_contents = self.contents.get()
        f = open('saved_contents.txt', 'w')
        f.write(self.saved_contents)
        f.close()



class Dice_roll_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.dice_roller = dice_rolling.DiceRoll()
        self.dice_roller.set_dice(1)
        self.dice_roller.set_sides(20)
        
        self.label2 = tk.Label(self, text="Roll: 0")
        self.label2.pack()

        self.button4 = tk.Button(self, text='Roll', command=self.roll_dice)
        self.button4.pack()

    def roll_dice(self):
        result = self.dice_roller.dice_roll(self.dice_roller.dice, self.dice_roller.sides)
        self.label2.config(text=f"Roll: {result}")



# class export()

# class import()

root = tk.Tk()
root.title("D&D Companion App")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

myapp = GUI(root)
myapp.mainloop()