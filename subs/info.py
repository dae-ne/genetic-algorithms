import tkinter as tk
from tkinter import ttk

from pubsub import pub

from core.events import EventListener, AlgorithmFinishedEvent


class StatsEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, AlgorithmFinishedEvent.__name__)

    @staticmethod
    def __handle(event: AlgorithmFinishedEvent):
        window = tk.Toplevel()
        window.title(f"info - {event.time_finished}")
        window.resizable(False, False)

        last_generation = event.generations[-1]

        frame = ttk.Frame(window, padding=(16, 8))
        frame.pack()

        data = [
            ("Execution time", f"{event.execution_time} s"),
            ("Best candidate", last_generation.get_best_candidate(event.options.maximization)),
            ("Average score", last_generation.get_average_score()),
            ("Standard deviation", last_generation.get_standard_deviation()),
            ("Output path", f"./output/{event.time_finished}/")
        ]

        for i in range(len(data)):
            for j in range(2):
                label = ttk.Label(frame, text=data[i][j], wraplength=400, padding=(24, 16))
                label.grid(row=i, column=j)
