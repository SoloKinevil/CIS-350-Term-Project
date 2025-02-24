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

class GUI(tk.Frame):
    # Constructor for user GUI and format
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # Create notebook and format
        notebook = ttk.Notebook(self, height = 450, width = 300)
        notebook.pack(expand = True, fill = 'both')

        #Add notebook tab with roll function
        dice_roll_tab = Dice_roll_tab(notebook)
        notebook.add(dice_roll_tab, text='Dice Roll')

        # Add notebook tab with Notes functionality
        notes = Notes_tab(notebook)
        notebook.add(notes, text='Active Character', )




# This Class initializes the Notes tab where the fields are saved
class Notes_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Read in saved_contents to updated user notes
        f = open('saved_contents.txt', 'r')
        self.saved_contents = f.read()
        f.close()

        # Label for Name
        self.label = ttk.Label(self, text = "Character Name")
        self.label.pack()
        # Initialize Entry values for Name
        self.name = tk.Entry(self, width=25)  # Starts tk entry field
        self.name_contents = tk.StringVar()
        self.name_contents.set(self.saved_contents)  # Sets the entry field to previous name
        self.name.pack()

        # Label for Race
        self.label2 = ttk.Label(self, text="Race")
        self.label2.pack()
        # Initialize Entry values for Race
        self.race = tk.Entry(self, width=25)  # Starts tk entry field
        self.race_contents = tk.StringVar()
        self.race_contents.set(self.saved_contents)  # Sets the entry field to previous race
        self.race.pack()

        # Label for Class
        self.label3 = ttk.Label(self, text="Class")
        self.label3.pack()
        # Initialize Entry values for class
        self.Class = tk.Entry(self, width=25)  # Starts tk entry field
        self.Class_contents = tk.StringVar()
        self.Class_contents.set(self.saved_contents)  # Sets the entry field to previous class
        self.Class.pack()

        # Label for Dex Modifier ##### USED FOR DICE ROLL
        self.Dex = ttk.Label(self, text="Class")
        self.Dex.pack()
        # Initialize Entry values for Dex
        self.dex = tk.Entry(self, width=25)  # Starts tk entry field
        self.dex_contents = tk.StringVar()
        self.dex_contents.set(self.saved_contents)  # Sets the entry field to previous Dex
        self.dex.pack()

        # Label for Notes
        self.label4 = tk.Label(self, text="Notes")
        self.label4.pack()
        # Initialize Entry values for NOTES
        self.notes = tk.Entry(self ,width = 100)  # Starts tk entry field
        self.note_contents = tk.StringVar()
        self.note_contents.set(self.saved_contents)  # Sets the entry field to previous notes
        self.notes.pack()

        # Follows text changes within notebook
        self.notes["textvariable"] = self.note_contents
        self.dex["textvariable"] = self.dex_contents
        self.Class["textvariable"] = self.Class_contents
        self.race["textvariable"] = self.race_contents
        self.name["textvariable"] = self.name_contents

        # Creates import button
        open_button = tk.Button(self, text="Import Data", command=self.open_file)
        open_button.pack(pady=20)

        # Saves new user changes to text document when clicked
        save_button = tk.Button(self, text="Save Data", command=self.save_contents)
        save_button.pack(pady=20)

    # This function saves the users stored information "Export"
    def save_contents(self, *args):
        f = open('saved_contents.txt', 'w')
        f.write(self.name_contents.get())
        f.write("/n")
        f.write(self.race_contents.get())
        f.write("/n")
        f.write(self.Class_contents.get())
        f.write("/n")
        f.write(self.dex_contents.get())
        f.write("/n")
        f.write(self.note_contents.get())
        f.close()

    # Allows user to upload text document to input into application
    def open_file(self):
        # Ask user for filepath through file explorer
        filepath = filedialog.askopenfilename()
        while filepath:
            # Ensure file is .txt
            if filepath.endswith('.txt'):
                print("Opening Text File: " + filepath)
                with open(filepath, 'r') as incoming, open('saved_contents.txt', 'w') as Characterdata:
                    for line in incoming:
                        Characterdata.write(line)
                f = open('saved_contents.txt', 'r')
                self.saved_contents = f.read()
                f.close()
                return
        return





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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("D&D Companion App")
    myapp = GUI(root)
    myapp.mainloop()