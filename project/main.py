import tkinter as tk

import os
import geocoder
import time

from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

assets_path = "./assets/"

class UI(tk.Frame):
    def __init__(self, parent):
        super(UI, self).__init__()
        #tk.Frame.__init__(self, parent)

        parent.title("geo-location-data")
        parent.geometry("800x600")

        py_label = tk.Label(parent, text="Enter an address:", font=("Helvetica", 12))
        py_label.place(x=0, y=0)

        self.py_entry = tk.Entry(parent, font=("Helvetica", 12))
        self.py_entry.place(x=130, y=2)

        # Pressed button image
        self.button_pressed = Image.open(assets_path + "b_pressed.png")
        self.button_pressed = ImageTk.PhotoImage(self.button_pressed)

        # Unpressed button image
        self.button_unpressed = Image.open(assets_path + "b_unpressed.png")
        self.button_unpressed = ImageTk.PhotoImage(self.button_unpressed)
                
        self.py_button = tk.Button(parent, font=("Helvetica", 12), width=16, height=16, borderwidth=0, command=self.button_press)
        self.py_button.config(image=self.button_unpressed)
        self.py_button.place(x=320, y=2)

    # Function for fetching geo locational data
    # WIP
    def button_press_fetch(self):
        # If address entry is empty
        if (self.py_entry.index("end") == 0):
            tk.messagebox.showerror("Error", "Address entry field was left blank.")
        else:
            print("Button pressed!")
    
    def button_pressed_func(self):
        self.py_button.config(image=self.button_pressed)
        self.py_button.after(100, self.button_unpressed_func)

    def button_unpressed_func(self):
        self.py_button.config(image=self.button_unpressed)

    def button_press(self):
        self.button_pressed_func()
        self.button_press_fetch()

if __name__ == "__main__":
    root = tk.Tk()
    UI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
