import csv

from matplotlib import pyplot as plt
from pubsub import pub

from core.events import EventListener, DataSavedEvent


class PlotEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, DataSavedEvent.__name__)

    @staticmethod
    def __handle(event: DataSavedEvent):
        epoch = []
        best = []
        average = []
        std = []
        with open(event.file_name) as file:
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                epoch.append(int(row["epoch"]))
                best.append(float(row["best"]))
                average.append(float(row["average"]))
                std.append(float(row["std"]))

        PlotEventListener.__create_best_plot(epoch, best, event.directory + "/best.png")
        PlotEventListener.__create_average_plot(epoch, average, std, event.directory + "/average.png")

    @staticmethod
    def __create_best_plot(epochs, bests, file_name):
        fig = plt.figure(figsize=(14, 8))

        plt.xlabel("epoch")
        plt.ylabel("best score")
        plt.title("Best score in each epoch")

        plt.plot(epochs, bests)

        plt.savefig(file_name)
        plt.close(fig)

    @staticmethod
    def __create_average_plot(epochs, averages, stds, file_name):
        fig = plt.figure(figsize=(14, 8))

        plt.xlabel("epoch")
        plt.ylabel("average score")
        plt.title("Average score with standard deviation in each epoch")

        plt.errorbar(epochs, averages, yerr=stds, ecolor='r', elinewidth=0.7, linewidth=1, capsize=1)

        plt.savefig(file_name)
        plt.close(fig)
