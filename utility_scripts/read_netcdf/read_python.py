#!/usr/bin/env python
from __future__ import print_function

# Copyright 2016-2020 Juliane Mai - juliane.mai(at)uwaterloo.ca
#
# License
# This file is part of Juliane Mai's personal code library.
#
# Juliane Mai's personal code library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Juliane Mai's personal code library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with Juliane Mai's personal code library.  If not, see <http://www.gnu.org/licenses/>.
#


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


