import tkinter as tk

from db.events import AlgorithmFinishedDbEventListener
from plot.events import AlgorithmFinishedPlotEventListener
from ui.controllers import FormController
from ui.models import FormModel
from ui.styles import AppStyles
from ui.views import FormView


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Genetic Algorithms")
        self.minsize(300, 0)
        self.resizable(False, False)

        model = FormModel()
        view = FormView(self)
        controller = FormController(model, view)
        view.set_controller(controller)

        view.pack(fill=tk.BOTH)

        styles = AppStyles()
        styles.set_defaults()

        db_event_listener = AlgorithmFinishedDbEventListener()
        plot_event_listener = AlgorithmFinishedPlotEventListener()

        for listener in (db_event_listener, plot_event_listener):
            listener.listen()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
