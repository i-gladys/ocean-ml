from netCDF4 import Dataset
import numpy as np
import seawater as sw 
import datetime as td
import tricubic 
#import interpolate

dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset['depth']
temperture = dataset['to']
salinity = dataset['so']
dynamic_height = dataset['zo']

def interp(startgrid):
	num_depths = 30 # to avoid problems with seafloor depth
	z_step = 10 
	depth = [10, 20, 30, 50, 75, 100, 125, 150, 200, 250, 300, 400, 500, 600, 
    700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1750, 2000, 2500, 
    3000, 3500, 4000, 4500, 5000]

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

dynamic_height = dynamic_height * 100

main_density_file = open('density_file.txt',"w")
start = td.date(1950,1,1)

for k in (0,1356):
	hours = td.timedelta(hours=int(time[i])) 
	after = start - hours
	date = after.strftime("%y")+ after.strftime("%m")+ after.strftime("%d")
	density_time = open("density_time"+str(date)+".txt","w")
	density_time.write("\t30\n\t80\t27")
	density_at_time = interp(density[i,:,:,:])
	dh_interp = interp(dynamic_height)
	interpheightfile = open('dh_'+ date + '.gr', 'w')
	for i in range(0,30): 
		for j in range(0,80):
			for c in range(0,27): 
				main_density_file.write(str(density_at_time[i,j,c])+'\n')

	main_density_file.close()

	return interp_grid
 
#
# for i in range(0,4):
#     my_file = open("file-"+str(i)+".txt","w")
#     my_file.write("this file has writing in it\n")
#     my_file.close()
