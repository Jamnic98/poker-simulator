from os import getcwd, path


project_settings = {
    "TOP_CARDS_COUNT": None,
}

cwd  = getcwd()
config = {
    "GRAPHS_DIR": path.join(cwd, 'images', 'graphs'),
    "RESULTS_DIR": path.join(cwd, 'results'),
    "LOG_DIR": path.join(cwd, 'logs')
}
