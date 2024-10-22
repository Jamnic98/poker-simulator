from os import makedirs, path
import matplotlib.pyplot as plt
from settings import config

def save_plot(plot_name: str, output_directory: str=config['GRAPH_OUTPUT_DIR']) -> None:
    """ save graph as image to a specified directory """
    if not path.exists(output_directory):
        makedirs(output_directory)
    output_path = path.join(output_directory, f'{plot_name}.png')
    plt.savefig(output_path)
