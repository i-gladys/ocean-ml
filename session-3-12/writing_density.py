from netCDF4 import Dataset
import numpy as np
import seawater as sw 
import datetime as td
import tricubic 
import interpolate

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
	
density = sw.dens(salinity[:,:,:,:],temperture[:,:,:,:],pressure_3d[:])
density = density - 1000
print(density.shape)

main_density_file = open('density_file.txt',"w")
start = td.date(1950,1,1)

for k in (0,1356):
	hours = td.timedelta(hours=int(time[i]))
	after = start - hours
	date = after.strftime("%y")+ after.strftime("%m")+ after.strftime("%d")
	density_time = open("density_time"+str(date)+".txt","w")
	density_at_time = interp(density[i,:,:,:])
	for i in range(0,30): 
		for j in range(0,80):
			for c in range(0,27): 
				main_density_file.write(str(density_at_time[i,j,c])+'\n')
	main_density_file.close()

#
# for i in range(0,4):
#     my_file = open("file-"+str(i)+".txt","w")
#     my_file.write("this file has writing in it\n")
#     my_file.close()
