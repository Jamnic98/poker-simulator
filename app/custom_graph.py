import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# from utils.graph import save_plot
# from settings import config

# create the graph
x = np.arange(1, 10)
y = x
data = pd.DataFrame({
    'x': x,
    'y': y
})

bar = sns.barplot(x=x, y=y)
bar.plot()

# plt.plot(data['x'], data['y'])
plt.title('Graph')
plt.xlabel('X')
plt.ylabel('Y')
# plt.show()
# save_plot('custom_plot')
