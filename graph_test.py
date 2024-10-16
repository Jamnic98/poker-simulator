from os import makedirs, path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from settings import config

plot_file_name = 'test_plot.png'
graph_img_output_dir = config['GRAPH_OUTPUT_DIR']

# create the graph
x = np.arange(1, 100)
y = np.sin(x)
data = pd.DataFrame({
    'x': x,
    'y': y
})

bar = sns.barplot(x=x, y=y)
bar.plot()

# plt.plot(
#     data['x'],
#     data['y'],
#     marker='o',
#     linestyle='-',
#     color='b'
# )

# plt.title('Test Plot')
# plt.xlabel('X Values')
# plt.ylabel('Y Values')


# # save graph as image
if not path.exists(graph_img_output_dir):
    makedirs(graph_img_output_dir)
    
plt.savefig(path.join(graph_img_output_dir, plot_file_name))
