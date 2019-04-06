from sample import main

# Instantiate UI
class_ui = main.UI(main.tk.Frame)

class Pressed(main.UI):
    def __init__(self):
        def button_press(self):
            self.button_press()
            # If address entry is empty
            if (class_ui.py_entry):
                main.tk.messagebox.showerror("Error", "Address entry field was left blank.")
                return self
            else:
                print("Button pressed!")
                return self
        