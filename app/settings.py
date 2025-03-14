from os import getcwd, path


cwd  = getcwd()
config = {
    "GRAPHS_DIR": path.join(cwd, 'images', 'graphs'),
    "RESULTS_DIR": path.join(cwd, 'results'),
    "LOG_DIR": path.join(cwd, 'logs')
}
