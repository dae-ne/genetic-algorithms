import tkinter as tk

import sv_ttk

from subs.db import DbEventListener
from subs.plot import PlotEventListener
from ui.mvc import OptionsModel, View, Controller


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Genetic Algorithms")
        self.minsize(600, 0)
        self.resizable(False, True)

        model = OptionsModel()
        view = View(self)
        controller = Controller(model, view)

        view.set_controller(controller)

        view.pack(fill=tk.BOTH)

        sv_ttk.use_dark_theme()

        event_listeners = (
            PlotEventListener(),
            DbEventListener())

        for event_listener in event_listeners:
            event_listener.listen()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
