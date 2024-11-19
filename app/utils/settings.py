from os import getcwd, path
# from matplotlib import use


# use('Agg')

cwd  = getcwd()

config = {
    "GRAPH_OUTPUT_DIR": path.join(cwd, 'images', 'graphs'),
    "RESULTS_DIR": path.join(cwd, 'results')
}
