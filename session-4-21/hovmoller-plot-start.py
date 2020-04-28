from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')
w = dataset['w']
print(w.shape)

#depth = 0
#latitude = 20.125

lat = dataset['latitude']
plt.title("hovmoller diagram at latitude = " + str(lat[9]))

first_plot = w[:, 9, :, 0]
first_plot = np.swapaxes(first_plot, 0, 1)
print(first_plot.shape)

cmap = cm.get_cmap('bwr')
plt.pcolormesh(first_plot, cmap = cmap)
plt.show()