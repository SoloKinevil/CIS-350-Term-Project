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
        self.master = master
        self.pack()
        self.create_widgets()

        # Start application
        self.run()

    def create_widgets(self):
        # Initialize all widgets and labels

        # ENTRY WIDGET
        # Read in saved_contents to updated user notes
        f = open('saved_contents.txt', 'r')
        self.saved_contents = f.read()
        f.close()

        # Initialize entry values for NOTES
        self.entry = tk.Entry()
        self.contents = tk.StringVar()
        self.contents.set(self.saved_contents)
        self.entry.pack()

    def run(self):

        # Tell the entry widget to watch this variable.
        self.entry["textvariable"] = self.contents

        # Saves new user input to text document when return it pressed
        self.entry.bind('<Key-Return>', self.save_contents)

    def save_contents(self, *args):
        # Function to save users stored information
        self.saved_contents = self.contents.get()
        f = open('saved_contents.txt', 'w')
        f.write(self.saved_contents)
        f.close()

# class export()

# class import()

root = tk.Tk()
myapp = GUI(root)
myapp.mainloop()