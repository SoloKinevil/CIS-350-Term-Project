'''
CIS 350 - Dungeons and Dragons Companion App
Shayan, Phoenix and Ian

This file contains the constructors for the GUI. The GUI will allow user input to export and input character
data as well as specific inventories and notes.
'''

import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
import dice_rolling
from tkinter import filedialog
import os
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

        # Create dice roll instance to use roll dice function
        self.dice_roll = Dice_roll_tab(self.notebook)

        # Add tabs to the notebook
        self.main = Main_menu_tab(self.notebook, self.settings_frame, self.dice_roll)
        self.notebook.add(self.main, text="Main Menu")
        dice_roll_tab = Dice_roll_tab(self.notebook)

        # Set image path
        image_path = "settings_icon.png"

        try:
            # Open image file correctly
            image = Image.open(image_path).convert("RGBA")  # Convert to avoid transparency issues
            image = image.resize((20, 20), Image.Resampling.LANCZOS)  # Resize image
            self.image_tk = ImageTk.PhotoImage(image)
        except Exception:
            self.image_tk = None  # Prevent crash if file is missing

        # Create settings button
        if self.image_tk:
            settings_button = tk.Button(self.notebook_frame, image=self.image_tk, command=self.show_settings)
            settings_button.pack(side="bottom", pady=5)

        # Create main menu button
        back_button = tk.Button(self.settings_frame, text="Back", command=self.show_main)
        back_button.grid(row=0, column=3)

        # Show main menu by default
        self.show_main()

    def show_settings(self):
        """Method to show the settings frame."""
        self.settings_frame.tkraise()

    def show_main(self):
        """Method to close the settings and update the character information."""
        new_name = self.settings_frame.name_contents.get()
        new_race = self.settings_frame.race_contents.get()
        new_class = self.settings_frame.class_contents.get()
        self.main.left_frame.char_name.config(text=f"Name: {new_name}")
        self.main.left_frame.char_race.config(text=f"Race: {new_race}")
        self.main.left_frame.char_class.config(text=f"Class: {new_class}")
        self.notebook_frame.tkraise()


# This Class initializes the Notes tab where the fields are saved
class Notes_tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure grid columns for better spacing
        for i in range(1, 5):
            self.columnconfigure(i, weight=1, pad=10)

        # Configure grid rows for spacing
        for i in range(1, 14):
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
        self.race_contents = StringVar(value="Dragonborn")
        race_drop = tk.OptionMenu(self, self.race_contents, *self.race_options)
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
        self.class_contents = StringVar(value="Artificer")

        class_drop = tk.OptionMenu(self, self.class_contents, *self.class_options)
        class_drop.grid(row=2, column=3, sticky="w")

        # Label for Str Modifier
        self.Str = ttk.Label(self, text="Strength")
        self.Str.grid(row=3, column=1, sticky="nesw")
        # Initialize Entry values for Str
        self.str = tk.Entry(self, width=10)
        self.str_contents = tk.StringVar()
        self.str.grid(row=4, column=1, sticky="w")

        # Label for Dex Modifier
        self.Dex = ttk.Label(self, text="Dexterity")
        self.Dex.grid(row=3, column=2, sticky="w")
        # Initialize Entry values for Dex
        self.dex = tk.Entry(self, width=10)
        self.dex_contents = tk.StringVar()
        self.dex.grid(row=4, column=2, sticky="w")

        # Label for Con Modifier
        self.Con = ttk.Label(self, text="Constitution")
        self.Con.grid(row=3, column=3, sticky="w")
        # Initialize Entry values for Con
        self.con = tk.Entry(self, width=10)
        self.con_contents = tk.StringVar()
        self.con.grid(row=4, column=3, sticky="w")

        # Label for Int Modifier
        self.Int = ttk.Label(self, text="Intelligence")
        self.Int.grid(row=5, column=1, sticky="w")
        # Initialize Entry values for Int
        self.int = tk.Entry(self, width=10)
        self.int_contents = tk.StringVar()
        self.int.grid(row=6, column=1, sticky="w")

        # Label for Wis Modifier
        self.Wis = ttk.Label(self, text="Wisdom")
        self.Wis.grid(row=5, column=2, sticky="w")
        # Initialize Entry values for Wis
        self.wis = tk.Entry(self, width=10)
        self.wis_contents = tk.StringVar()
        self.wis.grid(row=6, column=2, sticky="w")

        # Label for Cha Modifier
        self.Cha = ttk.Label(self, text="Charisma")
        self.Cha.grid(row=5, column=3, sticky="w")
        # Initialize Entry values for Cha
        self.cha = tk.Entry(self, width=10)
        self.cha_contents = tk.StringVar()
        self.cha.grid(row=6, column=3, sticky="w")

        # Label for Inventory
        self.label4 = tk.Label(self, text="Inventory", underline=True)
        self.label4.grid(row=7, column=2, sticky="nw")
        # Add Underline
        f = font.Font(self.label4, self.label4.cget("font"))
        f.configure(underline=True)
        self.label4.configure(font=f)

        # Label for small potion
        self.Small = ttk.Label(self, text="Small Potions")
        self.Small.grid(row=8, column=1, sticky="w")
        # Initialize Entry values for large potion
        self.small = tk.Entry(self, width=10)
        self.small_contents = tk.StringVar()
        self.small.grid(row=9, column=1, sticky="w")

        # Label for large potion
        self.Large = ttk.Label(self, text="Large Potions")
        self.Large.grid(row=8, column=2, sticky="w")
        # Initialize Entry values for large potion
        self.large = tk.Entry(self, width=10)
        self.large_contents = tk.StringVar()
        self.large.grid(row=9, column=2, sticky="w")

        # Label for Equipped Weapon
        self.label6 = tk.Label(self, text="Equipped Weapon")
        self.label6.grid(row=8, column=3, sticky="w")
        # Initialize Entry values for Equipped Weapon
        self.weapon_options = {
            "Dagger": "1d4", "Handaxe": "1d6", "Mace": "1d6", "Quarterstaff": "1d6",
            "Spear": "1d6", "Battleaxe": "1d8", "Greataxe": "1d12", "Greatsword": "2d6",
            "Longsword": "1d8", "Rapier": "1d8", "Scimitar": "1d6", "Shortsword": "1d6",
            "Warhammer": "1d8", "Whip": "1d4", "Hand Crossbow": "1d6", "Heavy Crossbow": "1d10",
            "Longbow": "1d8", "Shortbow": "1d6"
        }
        self.weapon_contents = StringVar(value="Dagger")

        weapon_drop = tk.OptionMenu(self, self.weapon_contents, *self.weapon_options)
        weapon_drop.grid(row=9, column=3, sticky="w")


        # Label for Notes
        self.label5 = tk.Label(self, text="Notes")
        self.label5.grid(row=12, column=2, sticky="nw")
        # Initialize Entry values for NOTES
        self.notes = tk.Entry(self, width=100)
        self.note_contents = tk.StringVar()
        self.notes.grid(row=13, column=1, columnspan=3, sticky="w")
        # Underline
        f = font.Font(self.label5, self.label5.cget("font"))
        f.configure(underline=True)
        self.label5.configure(font=f)


        # Import button
        open_button = tk.Button(self, text="Import Data", command=self.open_file)
        open_button.grid(row=14, column=1, sticky="w")

        # Save button
        save_button = tk.Button(self, text="Save Data", command=self.save_contents)
        save_button.grid(row=14, column=3, sticky="w")

        # Bind text variables to entries
        self.notes["textvariable"] = self.note_contents
        self.dex["textvariable"] = self.dex_contents
        self.str["textvariable"] = self.str_contents
        self.int["textvariable"] = self.int_contents
        self.cha["textvariable"] = self.cha_contents
        self.con["textvariable"] = self.con_contents
        self.wis["textvariable"] = self.wis_contents
        self.small["textvariable"] = self.small_contents
        self.large["textvariable"] = self.large_contents
        self.name["textvariable"] = self.name_contents

        # Set fields to previously saved values
        if os.path.exists('saved_contents.txt'):
            with open('saved_contents.txt', 'r') as incoming:
                lines = incoming.readlines()

            if len(lines) >= 13:
                self.name_contents.set(lines[0].strip())
                self.race_contents.set(lines[1].strip())
                self.class_contents.set(lines[2].strip())
                self.str_contents.set(lines[3].strip())
                self.dex_contents.set(lines[4].strip())
                self.con_contents.set(lines[5].strip())
                self.int_contents.set(lines[6].strip())
                self.wis_contents.set(lines[7].strip())
                self.cha_contents.set(lines[8].strip())
                self.small_contents.set(lines[9].strip())
                self.large_contents.set(lines[10].strip())
                self.weapon_contents.set(lines[11].strip())
                self.note_contents.set(lines[12].strip())

    # This function saves the users stored information to a file of their choice "Export"
    def save_contents(self, *args):
        filepath = filedialog.asksaveasfilename()
        with open(filepath, 'w') as f:
            f.write(self.name_contents.get() + "\n")
            f.write(self.race_contents.get() + "\n")
            f.write(self.class_contents.get() + "\n")
            f.write(self.str_contents.get() + "\n")
            f.write(self.dex_contents.get() + "\n")
            f.write(self.con_contents.get() + "\n")
            f.write(self.int_contents.get() + "\n")
            f.write(self.wis_contents.get() + "\n")
            f.write(self.cha_contents.get() + "\n")
            f.write(self.small_contents.get() + "\n")
            f.write(self.large_contents.get() + "\n")
            f.write(self.weapon_contents.get() + "\n")
            f.write(self.note_contents.get() + "\n")
        with open('saved_contents.txt', 'w') as f:
            f.write(self.name_contents.get() + "\n")
            f.write(self.race_contents.get() + "\n")
            f.write(self.class_contents.get() + "\n")
            f.write(self.str_contents.get() + "\n")
            f.write(self.dex_contents.get() + "\n")
            f.write(self.con_contents.get() + "\n")
            f.write(self.int_contents.get() + "\n")
            f.write(self.wis_contents.get() + "\n")
            f.write(self.cha_contents.get() + "\n")
            f.write(self.small_contents.get() + "\n")
            f.write(self.large_contents.get() + "\n")
            f.write(self.weapon_contents.get() + "\n")
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
                if len(lines) >= 13:
                    self.name_contents.set(lines[0].strip())
                    self.race_contents.set(lines[1].strip())
                    self.class_contents.set(lines[2].strip())
                    self.str_contents.set(lines[3].strip())
                    self.dex_contents.set(lines[4].strip())
                    self.con_contents.set(lines[5].strip())
                    self.int_contents.set(lines[6].strip())
                    self.wis_contents.set(lines[7].strip())
                    self.cha_contents.set(lines[8].strip())
                    self.small_contents.set(lines[9].strip())
                    self.large_contents.set(lines[10].strip())
                    self.weapon_contents.set(lines[11].strip())
                    self.note_contents.set(lines[12].strip())
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

        self.confirm_button = tk.Button(self, text = 'Confirm', command=self.set_sides)
        self.confirm_button.pack()

        self.sides1 = tk.Entry(self, width=10)
        self.sides1.pack()

    def roll_dice(self):
        result = self.dice_roller.dice_roll(self.dice_roller.dice, self.dice_roller.sides)
        self.label2.config(text=f"Roll: {result}") # Is this needed anymore?

    def set_sides(self):
        string_sides=self.sides1.get()
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

        # Set up the game information frame of the main menu
        self.middle_frame = MainMiddleFrame(self, self.notes_tab, self.dice_roll)
        self.middle_frame.grid(row=0, column=1, padx=5, pady=0, sticky="nsew")

        # Set up the Character info frame of the main menu
        self.left_frame = MainLeftFrame(self, self.notes_tab)
        self.left_frame.grid(row=0, column=0, padx=5, pady=0, sticky="nsew")

        # Set up the Inventory frame of the main menu
        self.right_frame = MainRightFrame(self)
        self.right_frame.grid(row=0, column=2, padx=5, pady=0, sticky="nsew")


class MainMiddleFrame(tk.Frame):
    def __init__(self, parent, notes_tab, dice_roll):
        super().__init__(parent, bg = "black")

        self.notes_tab = notes_tab
        self.dice_roll = dice_roll

        # Set grid for middle_frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)  # Log title
        self.rowconfigure(1, weight=5)  # Log box
        self.rowconfigure(2, weight=50)  # Spacer to push log box up

        # Title label
        main_label = tk.Label(self, text="Game Log", font=("Georgia", 17), fg="white", bg="black")
        main_label.grid(row=0, column=0, pady=0, padx=5, sticky="n")
        # Underline
        f = font.Font(main_label, main_label.cget("font"))
        f.configure(underline=True)
        main_label.configure(font=f)

        # Log text box
        self.log_text = tk.Text(self, height=12, width=40, bg="#1E1A2E", fg="white")
        self.log_text.grid(row=1, column=0, pady=(0, 0), padx=5, sticky="nsew")  # `pady=(0, 20)` moves it up

        # Dice roller instance
        self.dice_roller = dice_rolling.DiceRoll()
        self.dice_roller.set_dice(1)
        self.dice_roller.set_sides(20)

        # Roll button
        roll_button = tk.Button(self, text="Roll Dice", command=self.roll_dice, bg="black", highlightthickness=0, borderwidth=0)
        roll_button.grid(row=2, column=0)

    def roll_dice(self):
        result = self.dice_roller.dice_roll(self.dice_roller.dice, self.dice_roller.sides)
        self.log_text.insert("end", f"Rolling dice...\n")
        # Delay before showing the result (for dramatic effect)
        self.after(500, lambda: self.show_dice_result(result))

    def show_dice_result(self, result): 
        """Displays the dice roll result after a short delay."""
        self.log_text.insert("end", f"{self.notes_tab.name_contents.get()} rolled a: {result}\n")  # Append result to log
        self.log_text.see("end")

class MainLeftFrame(tk.Frame):
    def __init__(self, parent, notes_tab):
        super().__init__(parent, bg ="grey")

        self.notes_tab = notes_tab

        # Set up grid for left frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)
        self.rowconfigure(3, weight=5)
        self.rowconfigure(4, weight=5)
        self.rowconfigure(5, weight=40)

        # Character label
        left_label = tk.Label(self, text="Character", font=("Georgia", 17), fg="white", bg="grey")
        left_label.grid(row=0, column=0, pady=0, padx=5, sticky="n")
        # Underline
        f = font.Font(left_label, left_label.cget("font"))
        f.configure(underline=True)
        left_label.configure(font=f)

        # Image path for character pfp
        image_path = "blank-pfp.jpg"

        try:
            image = Image.open(image_path).convert("RGB")  # Convert to avoid transparency issues
            image = image.resize((180, 180), Image.Resampling.LANCZOS)  # Resize
            self.image_tk = ImageTk.PhotoImage(image)
        except Exception:
            self.image_tk = None  # Prevent crash if file is missing

        # Display image in a label
        if self.image_tk:
            image_label = tk.Label(self, image=self.image_tk, bg="black")
            image_label.grid(row=1, column=0, pady=0, sticky="n")

        # Character info labels
        self.char_name = tk.Label(self, text=f"Name: {self.notes_tab.name_contents.get()}", font=("Georgia", 14))
        self.char_name.grid(row=2, column=0, pady=0, sticky="n")
        self.char_race = tk.Label(self, text=f"Race: {self.notes_tab.race_contents.get()}", font=("Georgia", 14))
        self.char_race.grid(row=3, column=0, pady=0, sticky="n")
        self.char_class = tk.Label(self, text=f"Class: {self.notes_tab.class_contents.get()}", font=("Georgia", 14))
        self.char_class.grid(row=4, column=0, pady=0, sticky="n")


class MainRightFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="grey")

        # Set up grid for right frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        for i in range(1, 6):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

        # Add inventory label
        right_label = tk.Label(self, text="Inventory", font=("Georgia", 17), fg="white", bg="grey")
        right_label.grid(row=0, column=0, pady=5, sticky="n")
        # Underline
        f = font.Font(right_label, right_label.cget("font"))
        f.configure(underline=True)
        right_label.configure(font=f)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("D&D Companion App")
    myapp = GUI(root)
    myapp.mainloop()