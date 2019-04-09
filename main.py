import tkinter as tk

import os
import geocoder

from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

import project.pressed

assets_path = "./assets/"

class UI(tk.Frame):
    def __init__(self, parent):
        super(UI, self).__init__()
        #tk.Frame.__init__(self, parent)

        parent.title("geo-location-data")
        parent.geometry("800x600")

        py_label = tk.Label(parent, text="Emter an addres:", font=("Helvetica", 12))
        py_label.place(x=0, y=0)

        self.py_entry = tk.Entry(parent, font=("Helvetica", 12))
        self.py_entry.place(x=130, y=2)

        button_normal_img = Image.open(assets_path + "button_normal.png")

        button_normal_img_resize = button_normal_img.resize((16, 16), Image.BILINEAR)
        button_normal_img_resize_format = "resized_button_normal" + ".png"

        path_for_button_normal = os.path.join(assets_path, button_normal_img_resize_format)

        button_normal_img_resize.save(path_for_button_normal)
    
        button_normal_img_r_open = Image.open(assets_path + "resized_button_normal.png")
        button_normal_img_r_open = ImageTk.PhotoImage(button_normal_img_r_open)

        project.pressed.Pressed().button_press() # pylint: disable=no-member

        #class_pressed.button_press()

        # ADD COMMAND #
        py_button = tk.Button(parent, font=("Helvetica", 12), width=16, height=16, image=button_normal_img_r_open)
        py_button.place(x=320, y=2)

if __name__ == "__main__":
    root = tk.Tk()
    UI(root).pack(side="top", fill="both", expand=True)
    #class_pressed = pressed.Pressed()
    root.mainloop()
