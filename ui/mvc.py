import tkinter as tk
from tkinter import ttk

from apoor import fdir
from automapper import mapper

from core.algorithms import AsyncGeneticAlgorithm
from core.models import SelectionMethod, AlgorithmOptions, CrossoverMethod, MutationMethod
from ui.widgets import Selectbox


class OptionsModel:
    def __init__(self):
        self.__range_from = None
        self.__range_to = None
        self.__population_size = None
        self.__number_of_bits = None
        self.__epochs_amount = None
        self.__best_to_take = None
        self.__elite_strategy_amount = None
        self.__crossover_probability = None
        self.__mutation_probability = None
        self.__inversion_probability = None
        self.__selection_method = None
        self.__crossover_method = None
        self.__mutation_method = None
        self.__maximization = None

    @property
    def range_from(self):
        return self.__range_from

    @range_from.setter
    def range_from(self, value):
        if value != int(value):
            raise ValueError("")

        self.__range_from = value

    @property
    def range_to(self):
        return self.__range_to

    @range_to.setter
    def range_to(self, value):
        if value != int(value):
            raise ValueError("")

        self.__range_to = value

    @property
    def population_size(self):
        return self.__population_size

    @population_size.setter
    def population_size(self, value):
        if value != int(value):
            raise ValueError("")

        self.__population_size = value

    @property
    def number_of_bits(self):
        return self.__number_of_bits

    @number_of_bits.setter
    def number_of_bits(self, value):
        if value != int(value):
            raise ValueError("")

        self.__number_of_bits = value

    @property
    def epochs_amount(self):
        return self.__epochs_amount

    @epochs_amount.setter
    def epochs_amount(self, value):
        if value != int(value):
            raise ValueError("")

        self.__epochs_amount = value

    @property
    def best_to_take(self):
        return self.__best_to_take

    @best_to_take.setter
    def best_to_take(self, value):
        if value != int(value):
            raise ValueError("")

        self.__best_to_take = value

    @property
    def elite_strategy_amount(self):
        return self.__elite_strategy_amount

    @elite_strategy_amount.setter
    def elite_strategy_amount(self, value):
        if value != int(value):
            raise ValueError("")

        self.__elite_strategy_amount = value

    @property
    def crossover_probability(self):
        return self.__crossover_probability

    @crossover_probability.setter
    def crossover_probability(self, value):
        if value != int(value):
            raise ValueError("")

        self.__crossover_probability = value

    @property
    def mutation_probability(self):
        return self.__mutation_probability

    @mutation_probability.setter
    def mutation_probability(self, value):
        if value != int(value):
            raise ValueError("")

        self.__mutation_probability = value

    @property
    def inversion_probability(self):
        return self.__inversion_probability

    @inversion_probability.setter
    def inversion_probability(self, value):
        if value != int(value):
            raise ValueError("")

        self.__inversion_probability = value

    @property
    def selection_method(self):
        return self.__selection_method

    @selection_method.setter
    def selection_method(self, value):
        if not True:
            raise ValueError("")

        self.__selection_method = value

    @property
    def crossover_method(self):
        return self.__crossover_method

    @crossover_method.setter
    def crossover_method(self, value):
        if not True:
            raise ValueError("")

        self.__crossover_method = value

    @property
    def mutation_method(self):
        return self.__mutation_method

    @mutation_method.setter
    def mutation_method(self, value):
        if not True:
            raise ValueError("")

        self.__mutation_method = value

    @property
    def maximization(self):
        return self.__maximization

    @maximization.setter
    def maximization(self, value):
        if value != bool(value):
            raise ValueError("")

        self.__maximization = value

    def run_algorithm(self):
        options = mapper.to(AlgorithmOptions).map(self)
        algorithm_thread = AsyncGeneticAlgorithm(options)
        algorithm_thread.start()


class View(ttk.Frame):
    GRID_GAP_X = 16
    GRID_GAP_Y = 8

    def __init__(self, parent):
        super().__init__(parent, padding=16)

        number_of_columns = 3

        for column_index in range(number_of_columns):
            self.columnconfigure(column_index, weight=1)

        self.range_from = self.add_spinbox(0, "Range from", 0, 100, 0, 0)
        self.range_to = self.add_spinbox(0, "Range to", 0, 100, 0, 1)
        self.population_size = self.add_spinbox(20, "Population size", 0, 100, 0, 2)
        self.number_of_bits = self.add_spinbox(20, "Number of bits", 0, 100, 0, 3)
        self.epochs_amount = self.add_spinbox(100, "Epochs amount", 0, 100, 0, 4)

        self.best_to_take = self.add_spinbox(0, "Best to take", 0, 100, 1, 0)
        self.elite_strategy_amount = self.add_spinbox(0, "Elite Strategy amount", 0, 100, 1, 1)
        self.crossover_probability = self.add_spinbox(0, "Crossover probability [%]", 0, 100, 1, 2)
        self.mutation_probability = self.add_spinbox(0, "Mutation probability [%]", 0, 100, 1, 3)
        self.inversion_probability = self.add_spinbox(0, "Inversion probability [%]", 0, 100, 1, 4)

        self.selection_method = self.add_selectbox(
            SelectionMethod.BEST,
            fdir(SelectionMethod),
            "Selection method",
            2, 0)

        self.crossover_method = self.add_selectbox(
            CrossoverMethod.ONE_POINT,
            fdir(CrossoverMethod),
            "Crossover method",
            2, 1)

        self.mutation_method = self.add_selectbox(
            MutationMethod.ONE_POINT,
            fdir(MutationMethod),
            "Mutation method",
            2, 2)

        self.maximization = tk.StringVar()

        checkbox = ttk.Checkbutton(
            self,
            text="Maximization",
            variable=self.maximization,
            onvalue="1",
            offvalue="")

        checkbox.grid(column=2, row=3, sticky=tk.SW, padx=self.GRID_GAP_X, pady=self.GRID_GAP_Y)

        button = ttk.Button(
            self,
            text="Start",
            style="Accent.TButton",
            command=self.submit)

        button.grid(column=2, row=4, sticky=tk.SE, padx=self.GRID_GAP_X, pady=self.GRID_GAP_Y)

        self.controller = None

    def submit(self):
        self.controller.submit(
            int(self.range_from.get()),
            int(self.range_to.get()),
            int(self.population_size.get()),
            int(self.number_of_bits.get()),
            int(self.epochs_amount.get()),
            int(self.best_to_take.get()),
            int(self.elite_strategy_amount.get()),
            int(self.crossover_probability.get()),
            int(self.mutation_probability.get()),
            int(self.inversion_probability.get()),
            self.selection_method.get(),
            self.crossover_method.get(),
            self.mutation_method.get(),
            bool(self.maximization.get()))

    def set_controller(self, controller):
        self.controller = controller

    def add_spinbox(self, value, text, from_, to, column, row):
        variable = tk.StringVar(value=value)
        frame = ttk.Frame(self)
        label = ttk.Label(frame, text=text)
        input_ = ttk.Spinbox(frame, from_=from_, to=to, textvariable=variable)

        self.set_component(frame, label, input_, column, row)
        return variable

    def add_selectbox(self, value, possible_values, text, column, row):
        variable = tk.StringVar(value=value)
        frame = ttk.Frame(self)
        label = ttk.Label(frame, text=text)
        input_ = Selectbox(frame, variable, values=possible_values)

        self.set_component(frame, label, input_, column, row)
        return variable

    def set_component(self, frame, label, input_, column, row):
        label.pack(fill=tk.X)
        input_.pack(fill=tk.X, pady=(4, 0))
        frame.grid(column=column, row=row, sticky=tk.EW, padx=self.GRID_GAP_X, pady=self.GRID_GAP_Y)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def submit(self,
               range_from,
               range_to,
               population_size,
               number_of_bits,
               epochs_amount,
               best_to_take,
               elite_strategy_amount,
               crossover_probability,
               mutation_probability,
               inversion_probability,
               selection_method,
               crossover_method,
               mutation_method,
               maximization):
        self.model.range_from = range_from
        self.model.range_to = range_to
        self.model.population_size = population_size
        self.model.number_of_bits = number_of_bits
        self.model.epochs_amount = epochs_amount
        self.model.best_to_take = best_to_take
        self.model.elite_strategy_amount = elite_strategy_amount
        self.model.crossover_probability = crossover_probability
        self.model.mutation_probability = mutation_probability
        self.model.inversion_probability = inversion_probability
        self.model.selection_method = selection_method
        self.model.crossover_method = crossover_method
        self.model.mutation_method = mutation_method
        self.model.maximization = maximization

        self.model.run_algorithm()