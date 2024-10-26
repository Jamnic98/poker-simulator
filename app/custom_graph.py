import numpy as np
# import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def graph_data():  # data: pd.DataFrame=None):
    # create the graph
    x = np.arange(1, 10)
    y = np.square(x)
    bar_plot = sns.barplot(x=x, y=y)
    bar_plot.plot()
    # plot labels
    plt.title('Graph')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
