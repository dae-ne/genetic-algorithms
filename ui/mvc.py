import tkinter as tk
from tkinter import ttk

from core.algorithms import AsyncGeneticAlgorithm
from core.enums import SelectionMethod
from ui.widgets import Selectbox


class OptionsModel:
    def __init__(self):
        self.__population_size = None
        self.__selection_method = None

    @property
    def population_size(self):
        return self.__population_size

    @population_size.setter
    def population_size(self, value):
        if value:
            self.__population_size = value
        else:
            raise ValueError("Empty population size")

    @property
    def selection_method(self):
        return self.__selection_method

    @selection_method.setter
    def selection_method(self, value):
        self.__selection_method = value
        if value:
            self.__selection_method = value
        else:
            raise ValueError("Empty selection method")

    def run_algorithm(self):
        algorithm_thread = AsyncGeneticAlgorithm(
            self.population_size,
            self.selection_method)
        algorithm_thread.start()


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=24)

        self.population_size_var = tk.StringVar(value=100)
        population_size_label = ttk.Label(self, text="Header")
        population_size_input = ttk.Spinbox(
            self,
            from_=0,
            to=1000,
            textvariable=self.population_size_var)

        self.selection_method_var = tk.StringVar(value=SelectionMethod.BEST)
        selection_method_label = ttk.Label(self, text="Header")
        selection_method_input = Selectbox(
            self,
            self.selection_method_var,
            values=(
                SelectionMethod.BEST,
                SelectionMethod.TOURNAMENT,
                SelectionMethod.ROULETTE))

        button = ttk.Button(
            self,
            text="Start",
            style="Accent.TButton",
            command=self.submit)

        inputs = (
            {
                "label": population_size_label,
                "input": population_size_input
            },
            {
                "label": selection_method_label,
                "input": selection_method_input
            },
        )

        for widget in inputs:
            widget["label"].pack(fill=tk.X, pady=(0, 4))
            widget["input"].pack(fill=tk.X, pady=(0, 16))

        button.pack(fill=tk.X, pady=(8, 0))

        self.controller = None

    def submit(self):
        self.controller.submit(
            self.population_size_var.get(),
            self.selection_method_var.get())

    def set_controller(self, controller):
        self.controller = controller


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def submit(self, population_size, selection_method):
        self.model.population_size = population_size
        self.model.selection_method = selection_method

        self.model.run_algorithm()
