class FormController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def submit(self, population_size, selection_method):
        self.model.population_size = population_size
        self.model.selection_method = selection_method

        self.model.run_algorithm()
