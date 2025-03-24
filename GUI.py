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
import unittest
from PIL import Image, ImageTk

class GUI(tk.Frame):
    # Constructor for user GUI and format
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Create a frame to hold everything
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Make container grid
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        # Create frame for the notebook
        self.notebook_frame = ttk.Frame(self.container)
        self.notebook_frame.grid(row=0, column=0, sticky="nsew")

        self.notebook = ttk.Notebook(self.notebook_frame, height=500, width=800)
        self.notebook.pack(fill="both", expand=True)

        # Create frame for settings
        self.settings_frame = Notes_tab(self.container)
        self.settings_frame.grid(row=0, column=0, sticky="nsew")


        # come back and fix later, dice roll should NOT be a tab
        self.dice_roll = Dice_roll_tab(self.notebook)
        #self.notebook.add(self.dice_roll, text = "Dice Roll")

        # Add tabs to the notebook
        self.main = Main_menu_tab(self.notebook, self.settings_frame, self.dice_roll)
        self.notebook.add(self.main, text="Main Menu")
        dice_roll_tab = Dice_roll_tab(self.notebook)
        #self.notebook.add(dice_roll_tab, text="Dice Roll")

        image_path = "settings_icon.png"

        try:
            # Open image file correctly
            image = Image.open(image_path).convert("RGBA")  # Convert to avoid transparency issues
            image = image.resize((20, 20), Image.Resampling.LANCZOS)  # Resize if needed
            self.image_tk = ImageTk.PhotoImage(image)  # Convert for Tkinter
        except Exception as e:
            print("Error loading image:", e)
            self.image_tk = None  # Prevent crash if file is missing

        # Display image in a label
        if self.image_tk:
            settings_button = tk.Button(self.notebook_frame, image=self.image_tk, command=self.show_settings)
            settings_button.pack(side="bottom", pady=5)

        # Create settings button

        # Create main menu button
        back_button = tk.Button(self.settings_frame, text="Back", command=self.show_main)
        back_button.pack(side="bottom", pady=10)

        # Show tabs by default
        self.show_main()

    def show_settings(self):
        self.settings_frame.tkraise()

    def show_main(self):
        new_name = self.settings_frame.name_contents.get()
        new_race = self.settings_frame.race_contents.get()
        new_class = self.settings_frame.Class_contents.get()
        self.main.left_frame.char_name.config(text=f"Name: {new_name}")
        self.main.left_frame.char_race.config(text=f"Race: {new_race}")
        self.main.left_frame.char_class.config(text=f"Class: {new_class}")
        self.notebook_frame.tkraise()




# This Class initializes the Notes tab where the fields are saved
class Notes_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Label for Name
        self.label = ttk.Label(self, text = "Character Name")
        self.label.pack()
        # Initialize Entry values for Name
        self.name = tk.Entry(self, width=25)  # Starts tk entry field
        self.name_contents = tk.StringVar()
        self.name.pack()

        # Label for Race
        self.label2 = ttk.Label(self, text="Race")
        self.label2.pack()
        # Initialize Entry values for Race
        self.race = tk.Entry(self, width=25)  # Starts tk entry field
        self.race_contents = tk.StringVar()
        self.race.pack()

        # Label for Class
        self.label3 = ttk.Label(self, text="Class")
        self.label3.pack()
        # Initialize Entry values for class
        self.Class = tk.Entry(self, width=25)  # Starts tk entry field
        self.Class_contents = tk.StringVar()
        self.Class.pack()

        # Label for Dex Modifier ##### USED FOR DICE ROLL
        self.Dex = ttk.Label(self, text="Dex")
        self.Dex.pack()
        # Initialize Entry values for Dex
        self.dex = tk.Entry(self, width=25)  # Starts tk entry field
        self.dex_contents = tk.StringVar()
        self.dex.pack()

        # Label for Notes
        self.label4 = tk.Label(self, text="Notes")
        self.label4.pack()
        # Initialize Entry values for NOTES
        self.notes = tk.Entry(self ,width = 100)  # Starts tk entry field
        self.note_contents = tk.StringVar()
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

        close_button = tk.Button(self, text = "Close", command = self.hide)
        close_button.pack()

        # Set fields to previously saved values
        with open('saved_contents.txt', 'r') as incoming:
            lines = incoming.readlines()

        if len(lines) >= 5:
            self.name_contents.set(lines[0].strip())
            self.race_contents.set(lines[1].strip())
            self.Class_contents.set(lines[2].strip())
            self.dex_contents.set(lines[3].strip())
            self.note_contents.set(lines[4].strip())

    # This function saves the users stored information to a file of their choice "Export"
    def save_contents(self, *args):
        filepath = filedialog.asksaveasfilename()
        with open(filepath, 'w') as f:
            f.write(self.name_contents.get() + "\n")
            f.write(self.race_contents.get() + "\n")
            f.write(self.Class_contents.get() + "\n")
            f.write(self.dex_contents.get() + "\n")
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
                    self.Class_contents.set(lines[2].strip())
                    self.dex_contents.set(lines[3].strip())
                    self.note_contents.set(lines[4].strip())
                else:
                    print("Error: File does not contain enough data.")
                return
            return

    def hide(self):
        self.master.main.tkraise()




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


class Main_menu_tab(ttk.Frame):
    def __init__(self, parent, notes_tab, dice_roll):
        super().__init__(parent)

        self.notes_tab = notes_tab
        self.dice_roll = dice_roll

        # Configure columns
        self.columnconfigure(0, weight=1)  # Left spacer
        self.columnconfigure(1, weight=1)  # Middle area
        self.columnconfigure(2, weight=4)  # Right spacer
        
        # Configure rows
        self.rowconfigure(0, weight=1)  # Top spacer 


        self.middle_frame = MainMiddleFrame(self, self.notes_tab, self.dice_roll)
        self.middle_frame.grid(row = 0, column = 1, padx = 5, pady = 0, sticky = "nsew")

        self.left_frame = MainLeftFrame(self, self.notes_tab)
        self.left_frame.grid(row = 0, column = 0, padx = 5, pady = 0, sticky = "nsew")

        self.right_frame = MainRightFrame(self)
        self.right_frame.grid(row = 0, column = 2, padx = 5, pady = 0, sticky = "nsew")


class MainMiddleFrame(tk.Frame):
    def __init__(self, parent, notes_tab, dice_roll):
        super().__init__(parent, bg = "black")

        self.notes_tab = notes_tab
        self.dice_roll = dice_roll

        # Set grid weight for middle_frame
        self.columnconfigure(0, weight=1)  # Ensures content expands within the frame
        self.rowconfigure(0, weight=1)  # Log title
        self.rowconfigure(1, weight=5)  # Log box
        self.rowconfigure(2, weight=50)  # Spacer to push log box up

        # Title label
        main_label = tk.Label(self, text="Game Log", font=("Georgia", 17), fg="white", bg="black")
        main_label.grid(row=0, column=0, pady=0, padx=5, sticky="n")

        # Log text box
        self.log_text = tk.Text(self, height=12, width=40, bg="#1E1A2E", fg="white")
        self.log_text.grid(row=1, column=0, pady=(0, 0), padx=5, sticky="nsew")  # `pady=(0, 20)` moves it up

        self.dice_roller = dice_rolling.DiceRoll()
        self.dice_roller.set_dice(1)
        self.dice_roller.set_sides(20)

        # Roll button
        roll_button = tk.Button(self, text = "Roll Dice", command = self.roll_dice, bg="black", highlightthickness=0, borderwidth=0)
        roll_button.grid(row = 2, column = 0)

    def roll_dice(self):
        result = self.dice_roller.dice_roll(self.dice_roller.dice, self.dice_roller.sides)
        self.log_text.insert("end", f"Rolling dice...\n")

        self.after(500, lambda: self.show_dice_result(result))

    def show_dice_result(self, result): 
        """Displays the dice roll result after a short delay."""
        self.log_text.insert("end", f"{self.notes_tab.name_contents.get()} rolled a: {result}\n")  # Append result to log
        self.log_text.see("end")  # Auto-scroll to latest entry

class MainLeftFrame(tk.Frame):
    def __init__(self, parent, notes_tab):
        super().__init__(parent, bg = "grey")

        self.notes_tab = notes_tab

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 5)
        self.rowconfigure(3, weight = 5)
        self.rowconfigure(4, weight = 5)
        self.rowconfigure(5, weight = 40)

        left_label = tk.Label(self, text="Character", font=("Georgia", 17), fg="white", bg = "grey")
        left_label.grid(row=0, column=0, pady=0, padx=5, sticky="n")

        image_path = "blank-pfp.jpg"

        try:
            # Open image file correctly
            image = Image.open(image_path).convert("RGB")  # Convert to avoid transparency issues
            image = image.resize((180, 180), Image.Resampling.LANCZOS)  # Resize if needed
            self.image_tk = ImageTk.PhotoImage(image)  # Convert for Tkinter
        except Exception as e:
            print("Error loading image:", e)
            self.image_tk = None  # Prevent crash if file is missing

        # Display image in a label
        if self.image_tk:
            image_label = tk.Label(self, image=self.image_tk, bg="black")
            image_label.grid(row=1, column=0, pady=0, sticky="n")

        self.char_name = tk.Label(self, text = f"Name: {self.notes_tab.name_contents.get()}", font = ("Georgia", 14))
        self.char_name.grid(row = 2, column = 0, pady = 0, sticky = "n")
        self.char_race = tk.Label(self, text = f"Race: {self.notes_tab.race_contents.get()}", font = ("Georgia", 14))
        self.char_race.grid(row = 3, column = 0, pady = 0, sticky = "n")
        self.char_class = tk.Label(self, text = f"Class: {self.notes_tab.Class_contents.get()}", font = ("Georgia", 14))
        self.char_class.grid(row = 4, column = 0, pady = 0, sticky = "n")


class MainRightFrame(tk.Frame):  # ✅ Change ttk.Frame → tk.Frame
    def __init__(self, parent):
        super().__init__(parent, bg="grey")  # ✅ Set background color here

        # ✅ Make sure this frame expands fully
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # ✅ Inventory label stays at the top
        right_label = tk.Label(self, text="Inventory", font=("Georgia", 17), fg="white", bg="grey")
        right_label.grid(row=0, column=0, pady=5, sticky="n")

        # ✅ Stretch the right frame
        self.rowconfigure(1, weight=1)







if __name__ == "__main__":
    root = tk.Tk()
    root.title("D&D Companion App")
    myapp = GUI(root)
    myapp.mainloop()