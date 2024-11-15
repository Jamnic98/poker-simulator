from os import makedirs, path
from numpy import array
import seaborn as sns
import matplotlib.pyplot as plt
from app.utils.settings import config


class Graph:
    def __init__(self, title, x_label: str='x', y_label: str='y'):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    @staticmethod
    def save_plot(plot_name, output_directory: str=config['GRAPH_OUTPUT_DIR']) -> None:
        """ save graph as image to a specified directory """
        if not path.exists(output_directory):
            makedirs(output_directory)
        plt.savefig(path.join(output_directory, f'{plot_name}.png'))

    @staticmethod
    def show() -> None:
        plt.show()

    @staticmethod
    def reset() -> None:
        plt.clf()

    def plot_data(self, x: array, y: array,):
        # create the graph
        bar_plot = sns.barplot(x=x, y=y)
        bar_plot.plot()
        # plot labels
        plt.xlabel(self.x_label)
        plt.xticks(rotation=90)
        plt.ylabel(self.y_label)
        plt.title(self.title)
