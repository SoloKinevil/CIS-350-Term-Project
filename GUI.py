'''
CIS 350 - Dungeons and Dragons Companion App
Shayan, Phoenix and Ian

This file contains the constructors for the GUI. The GUI will allow user input to export and input character
data as well as specific inventories and notes.
'''

import tkinter as tk
from tkinter import *

class GUI(tk.Frame):
    # Constructor for user GUI and format
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()  # Call to create all widgets before run

        # Start application
        self.run()

    # This function initializes all widgets and labels
    def create_widgets(self):

        # ENTRY WIDGET
        # Read in saved_contents to updated user notes
        f = open('saved_contents.txt', 'r')
        self.saved_contents = f.read()
        f.close()

        # Initialize Entry values for NOTES
        self.entry = tk.Entry()  # Starts tk entry field

        self.contents = tk.StringVar()
        self.contents.set(self.saved_contents)  # Sets the entry field to previous notes
        self.entry.pack()

    # This function runs GUI and allows for user input
    def run(self):

        # Widget follows changes
        self.entry["textvariable"] = self.contents

        # Saves new user changes to text document when return it pressed
        self.entry.bind('<Key-Return>', self.save_contents)

    # This function saves the users stored information
    def save_contents(self, *args):
        self.saved_contents = self.contents.get()
        f = open('saved_contents.txt', 'w')
        f.write(self.saved_contents)
        f.close()

# class export()

# class import()

root = tk.Tk()
root.title("D&D Companion App")
root.geometry("300x300")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

myapp = GUI(root)
myapp.mainloop()