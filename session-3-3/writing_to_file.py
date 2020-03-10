

from netCDF4 import Dataset
import numpy as np
import seawater as sw

#input: salinity, temperature, and pressure in form of netcdf file 
#1st: import data and get all 
dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1581373134952.nc')
salinity= (dataset['so'])
temp = (dataset['to'])
pressure = dataset['depth']
latitude = dataset['latitude']
longitude = dataset['longitude']

pressure3D = np.zeros((31,80,27))


firtst_layer=np.repeat(10,80*27).reshape(80,27)
second_layer=np.repeat(20,80*27).reshape(80,27)

for i in pressure[:]:
	values = (np.repeat(i,80*27).reshape((80,27)))

for i in range(0,31):
	pressure3D[i,:,:] = (np.repeat(pressure[i],80*27).reshape(80,27))

#print(pressure3D)



density = (sw.dens(salinity[:], temp[:], pressure3D[:]))

print(density.shape)
# to do 
# for i in range(0,10):
# 	for j in range(0,10):
# 		for k in range(0,10):
# 			print(i,j,k)

