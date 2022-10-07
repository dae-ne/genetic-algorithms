import tkinter as tk
from tkinter import ttk

from core.enums import SelectionMethod
from ui.widgets import Input, Select


class FormView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(16, 0, 16, 8))

        label = ttk.Label(self, text="Header")

        self.population_size_var = tk.StringVar()
        input1 = Input(self, self.population_size_var, placeholder="placeholder")

        self.selection_method_var = tk.StringVar()
        self.selection_method_var.set(SelectionMethod.BEST)
        select = Select(self, self.selection_method_var, values=(
            SelectionMethod.BEST,
            SelectionMethod.TOURNAMENT,
            SelectionMethod.ROULETTE))

        button = ttk.Button(self, text="Start", command=self.submit)

        label.pack(fill=tk.X, pady=16)
        for widget in (input1, select):
            widget.pack(fill=tk.X, pady=(0, 8))
        button.pack(fill=tk.X)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def submit(self):
        self.controller.submit(
            self.population_size_var.get(),
            self.selection_method_var.get())
