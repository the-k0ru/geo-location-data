import tkinter as tk
import os.path
import geocoder

from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

global button_img

class UI(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window

    # Create window
    window = tk.Tk()

    # Set window title
    window.title("geo-location-data")

    # Set window geometry
    window.geometry("800x600")

    # Addres entry label
    py_label = tk.Label(window, text="Enter an addres:", font=("Helvetica", 12))
    py_label.place(x=0, y=0)

    # Addres entry label
    py_entry = tk.Entry(window, font=("Helvetica", 12))
    py_entry.place(x=130, y=2)

    button_img = Image.open(r'.\assets\button_normal.png')
    resized_button_img = button_img.resize((16, 16))
    resized_button_img.save('resized_button_img.png')

    def button_pressed(self, event=None):
        # Blank entry field
        if (UI.py_entry.index("end") == 0):
            messagebox.showerror("Error", "Entry field was left blank.")
        else:
            print("test")
    
    # Address entry button
    py_button = tk.Button(window, font=("Helvetica", 12), width=16, height=16, command=button_pressed, image=resized_button_img)
    py_button.place(x=320, y=2)

if __name__ == "__main__":
    root = tk.Tk()

    UI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
