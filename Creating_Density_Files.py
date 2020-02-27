from netCDF4 import Dataset
import numpy as np
import seawater as sw

dataset = Dataset(r'/Users/brownscholar/Desktop/marine_c.nc')

sal = dataset['so']
temp = dataset['to']
depth = dataset['depth']
time = dataset['time']

#[:] means everything (all the data)
print(depth[:])