import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import seaborn as sns
from utils.graph import save_plot

# create the graph
x = np.arange(1, 10)
y = np.square(x)

bar_plot = sns.barplot(x=x, y=y)
bar_plot.plot()

# plt.plot(data['x'], data['y'])
plt.title('Graph')
plt.xlabel('X')
plt.ylabel('Y')
# plt.show()
save_plot('custom_plot')
