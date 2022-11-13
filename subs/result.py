from pubsub import pub
from tkinter import messagebox

from core.events import EventListener, AlgorithmFinishedEvent


class ResultEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, AlgorithmFinishedEvent.__name__)

    @staticmethod
    def __handle(event: AlgorithmFinishedEvent):
        solution = event.generations[-1].get_best_candidate(maximization=event.options.maximization)

        info = "Solution found in {:.5f}s\n\nf({:.5f}, {:.5f}) = {:.5f}".format(
            event.execution_time, solution.chromosomes[0].decode_to_decimal(),
            solution.chromosomes[1].decode_to_decimal(), solution.score)

        messagebox.showinfo("Result info", info)
