from os import path
from settings import config

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(1, 11)
y = np.square(x)
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
import os

plot_file_name = 'test_plot_4.png'

graph_img_output_dir = path.join(config['IMG_DIR'], 'graphs')

if not os.path.exists(graph_img_output_dir):
    os.makedirs(graph_img_output_dir)
    
plt.savefig(os.path.join(graph_img_output_dir, plot_file_name))
