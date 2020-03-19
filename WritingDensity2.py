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

