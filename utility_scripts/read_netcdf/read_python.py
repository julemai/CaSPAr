# Read a NetCDF file with Python

# load packages
import netCDF4 as nc4            # to work with netCDFs
import numpy   as np             # to perform numerics
import time

# open file
ncid = nc4.Dataset('NetCDF_Python.nc', 'r')

# display general information of variables and dimensions in file
print(ncid)

# display information about specific variable in file
print(ncid.variables['lat'])

# read data of variable
lat = ncid.variables['lat'][:]
print(lat)

# get precipitation value of one grid cell for all time steps
#    index lat = 1
#    index lon = 3
#    index time = all = :
pre_lat_lon = ncid.variables['pre'][:, 0, 2]
print(pre_lat_lon)


