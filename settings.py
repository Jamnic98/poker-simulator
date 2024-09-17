import matplotlib
from os import getcwd, path

matplotlib.use('Agg')

config = {
    "IMG_DIR": path.join(getcwd(), 'images')
}
