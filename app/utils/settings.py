from os import getcwd, path
from matplotlib import use

use('Agg')

config = {
    "GRAPH_OUTPUT_DIR": path.join(getcwd(), 'images', 'graphs')
}
