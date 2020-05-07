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

import netCDF4 as nc4            # to work with netCDFs
import numpy   as np             # to perform numerics
import time

pre      = np.array([ [ [ -9999.0, 1.0,     2.0, 1.0 ],
                        [     1.0, 1.0,     0.0, 0.0 ] ],
                      [ [ -9999.0, 0.0,     0.0, 0.0 ],
                        [     0.0, 0.0,     0.0, 0.0 ] ],
                      [ [ -9999.0, 4.0,     4.0, 1.0 ],
                        [     1.0, 1.0, -9999.0, 0.0 ] ] ])

lat_data = np.array(  [ [ 50.0, 50.0, 50.0, 50.0 ],
                        [ 49.0, 49.0, 49.0, 49.0 ] ])
lon_data = np.array(  [ [ -110.0, -109.0, -108.0, -107.0 ],
                        [ -110.0, -109.0, -108.0, -107.0 ] ])

grid_ID  = np.array(  [ [ 120.0, 121.0, 125.0, 130.0 ],
                        [ 122.0, 124.0, 140.0, 131.0 ] ])

T_data  = np.array(     [ 0,6,18 ])

ncid = nc4.Dataset("NetCDF_Python.nc", "w", format="NETCDF4")

dimid_X = ncid.createDimension('nlon',2)
dimid_Y = ncid.createDimension('nlat',4)
dimid_T = ncid.createDimension('time',3)

# Variables
time_varid = ncid.createVariable('time','i4',('time',),zlib=True)

# Attributes
time_varid.long_name     = 'time'
time_varid.units         = 'hours since 2018-01-01 00:00:00'
time_varid.calendar      = 'gregorian'
time_varid.standard_name = 'time'
time_varid.axis          = 'T'

# Write data
time_varid[:] = T_data

# Variables
lat_varid = ncid.createVariable('lat','f8',('nlon','nlat',),zlib=True)
lon_varid = ncid.createVariable('lon','f8',('nlon','nlat',),zlib=True)

# Attributes
lat_varid.long_name      = 'latitude'
lon_varid.long_name      = 'longitude'
lat_varid.units          = 'degrees_north'
lon_varid.units          = 'degrees_east'
lat_varid.standard_name  = 'latitude'
lon_varid.standard_name  = 'longitude'

# Write data
lat_varid[:] = lat_data
lon_varid[:] = lon_data

# Variable
pre_varid     = ncid.createVariable('pre',    'f8',('time','nlon','nlat',),zlib=True)
grid_ID_varid = ncid.createVariable('grid_ID','f8',(       'nlon','nlat',),zlib=True)

# Attributes
pre_varid.long_name       = 'Precipitation'
grid_ID_varid.long_name   = 'Grid ID (numbering grid cells from 1 to N)'
pre_varid.units           = 'mm'
grid_ID_varid.units       = '1'
pre_varid.coordinates     = 'lon lat'
grid_ID_varid.coordinates = 'lon lat'

# Write data
pre_varid[:]     = pre
grid_ID_varid[:] = grid_ID

ncid.Conventions = 'CF-1.6'
ncid.License     = 'The data were written by me. They are under GPL.'
ncid.history     = 'Created ' + time.ctime(time.time())
ncid.source      = 'Written by CaSPAr test script (https://github.com/kckornelsen/CaSPAR_Public).'

ncid.close()
