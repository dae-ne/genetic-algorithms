import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from matplotlib.figure import Figure
from pubsub import pub

from core.events import AlgorithmFinishedEvent, EventListener


class AlgorithmFinishedPlotEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handler, AlgorithmFinishedEvent.EVENT_NAME)

    @staticmethod
    def __handler(event: AlgorithmFinishedEvent):
        window = tk.Toplevel()

        # prepare data
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, window)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, window)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
