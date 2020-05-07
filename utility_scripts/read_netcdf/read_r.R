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

# Read a NetCDF file with R

# NetCDF4 package
library(ncdf4)                   

# open file
ncin <- nc_open("NetCDF_R.nc")  

# view header
ncid

# attributes of a variable
ncatt_get(ncin,"lat")

# read the variable "lat"
lat = ncvar_get(ncin,"lat")

# get precipitation value of one grid cell for all time steps
#    index lat = 1
#    index lon = 3
#    index time = all
pre_lat_lon = ncvar_get(ncin,"pre")[3, 1, ]


