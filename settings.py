import matplotlib
from os import getcwd, path

matplotlib.use('Agg')

config = {
    "GRAPH_OUTPUT_DIR": path.join(getcwd(), 'graphs')
}
