from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset['depth']
temperture = dataset['to']
salinity = dataset['so']

#print(pressure.shape)
#print(temperture.shape)
#print(salinity.shape)

pressure_3d = np.zeros((31,80,27))

#for depth_level in pressure:
	#print(np.repeat(depth_level,80*27).reshape((80,27)))


for i in range(0,31):
	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
	#print(pressure_3d[i,:,:])
	
density = sw.dens(salinity[0,:,:,:],temperture[0,:,:,:],pressure_3d[:])
#print(density.shape)

density_file = open('density_file.txt',"w")

for i in range(0,31): 
    for j in range(0,80):
        for c in range(0,27): 
            print(density[i,j,c])
            density_file.write(str(density[i,j,c])+'\n')
density_file.close()
