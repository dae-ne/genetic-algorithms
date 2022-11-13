import csv
import os
import time

from pubsub import pub

from core.events import EventListener, AlgorithmFinishedEvent, DataSavedEvent


class DbEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, AlgorithmFinishedEvent.__name__)

    @staticmethod
    def __handle(event: AlgorithmFinishedEvent):
        directory_name = time.strftime("%Y-%m-%d %H-%M-%S")
        os.mkdir(directory_name)

        file_name = directory_name + "/results.csv"
        with open(file_name, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            writer.writerow(["epoch", "best", "average", "std"])

            for epoch, generation in enumerate(event.generations):
                writer.writerow([epoch,
                                 generation.get_best_candidate(maximization=event.options.maximization).score,
                                 generation.get_average_score(),
                                 generation.get_standard_deviation()])

        event = DataSavedEvent(directory_name, file_name)
        pub.sendMessage(DataSavedEvent.__name__, event=event)
