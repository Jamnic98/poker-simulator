from os import getcwd, path
from matplotlib import use


use('Agg')

cwd  = getcwd()

config = {
    "GRAPHS_DIR": path.join(cwd, 'images', 'graphs'),
    "RESULTS_DIR": path.join(cwd, 'results'),
    "LOG_DIR": path.join(cwd, 'logs'),
    "TOP_CARDS_COUNT": 10
}
