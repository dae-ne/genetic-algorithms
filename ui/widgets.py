import tkinter as tk
from tkinter import ttk


class Input(tk.Entry):
    def __init__(self, master=None, value=None, placeholder="input", color="grey"):
        # vcmd = (master.register(self.validate), "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")
        super().__init__(master, textvariable=value)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        self.set_placeholder()

    def set_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

    def focus_in(self, *_):
        if self["fg"] == self.placeholder_color:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def focus_out(self, *_):
        if not self.get():
            self.set_placeholder()

    def validate(self, value):
        if value:
            try:
                float(value)
                return True
            except ValueError:
                return False
        else:
            return False


class Select(ttk.Combobox):
    def __init__(self, master=None, value=None, values=None):
        super().__init__(master, textvariable=value)

        self["state"] = "readonly"
        self["values"] = values
