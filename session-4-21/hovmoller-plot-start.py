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
#print(first_plot.shape)

cmap = cm.get_cmap('bwr')
plt.pcolormesh(first_plot, cmap = cmap)
#plt.show()

#make arrays
sub_array_1 = np.arange(0,25).reshape((5,5))
sub_array_2 = np.arange(25,50).reshape((5,5))
sub_array_3 = np.arange(75,100).reshape((5,5))
#make colormap
top = cm.get_cmap('Blues_r')
bottom = cm.get_cmap('Reds')
newcolors = np.vstack((top(np.linspace(0, 1, 10)),
                       bottom(np.linspace(0, 1, 10))))
newcmp = ListedColormap(newcolors, name='RedBlue')
#plot array with colorbar
plt.pcolormesh(sub_array_1,cmap=newcmp)
plt.pcolormesh(sub_array_2,cmap=newcmp)
plt.pcolormesh(sub_array_3,cmap=newcmp)
plt.colorbar()

fig, ax = plt.subplots(3,1) #(nrows,ncolumns)
ax[0].pcolormesh(sub_array_1,cmap=newcmp)
ax[1].pcolormesh(sub_array_2,cmap=newcmp)
ax[2].pcolormesh(sub_array_3,cmap=newcmp)

#plt.show()
