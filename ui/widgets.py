from tkinter import ttk


class Selectbox(ttk.Combobox):
    def __init__(self, master=None, textvariable=None, values=None):
        super().__init__(master, textvariable=textvariable)

        self["state"] = "readonly"
        self["values"] = values
