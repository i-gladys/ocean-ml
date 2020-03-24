from netCDF4 import Dataset
import numpy as np 
import seawater as sw 
import datetime as td
import tricubic

dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1574699840388.nc')
salinity = dataset['so']
temperture = dataset['to']
pressure = dataset['depth']
latitude = dataset['latitude']
longitude = dataset['longitude']
time = dataset['time']
dynamic_height = dataset['zo']
dynamic_height = dynamic_height[:] * 100

def interp(startgrid):
	nump_depth = 30 #to avoid problems with seafloor depths
	z_step = 10
	depth_list = [10, 20,  30, 50, 75, 100, 125, 150, 200, 250, 300, 400, 500, 600, 
	700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1750, 2000, 2500, 
	3000, 3500, 4000, 4500, 5000]

	new_depth = np.arrange(z_step,(num_depths+1)*z_step,z_step)
	new_depth_index = []
	left = 0
	right = 1
	for i in range(0,len(new_depth)):
		target_value = new_depth[i]
		if target_value > depth_list[right]:
			right += 1
			left += 1
		left_value = depth_list[left]
		right_value = depth_list[right]
		a = target_value-left_value
		b = right_value-left_value
		new_index = a/b+left
		new_depth_index.append(new_index)
		#start grid is shape lat, lon, depth
		lat = startgrid.shape[1]
		lon = startgrid.shape[2]
		depth = startgrid.shape[0]

	interp_grid = np.zeros((len(new_depth_index),lat,lon))
	ip = tricubic.tricubic(list(startgrid),[depth,lat,lon])

	for i in range(0,lat):
		for j in range(0,lon):
			for k in range(0,len(new_depth_index)):
				res = ip.ip([new_depth_index[k],i,j])
				interp_grid[k,i,j] = res
	return interp_grid

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

pressure3D = np.zeros((31,80,27))

for i in range(0,31):
	pressure3D[i,:,:] = (np.repeat(pressure[i],80*27).reshape(80,27))

print(pressure3D)

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


