#!/usr/bin/env python
# from __future__ import print_function

# Copyright 2016-2024 Juliane Mai - juliane.mai(at)uwaterloo.ca
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

# load the `ncdf4` and the `CFtime` packages
library(ncdf4)
library(CFtime)

fillvalue <- 1e32

# -----------------------------------------
# dimensions
# -----------------------------------------
nlon3 <- 2
nlat3 <- 4
nt3 <- 3

# -----------------------------------------
# generate lons, lats and set time
# -----------------------------------------
lon3    <- array(0.0, dim=c(nlon3,nlat3))
lon3[1:nlon3,1] <- -110.0
lon3[1:nlon3,2] <- -109.0
lon3[1:nlon3,3] <- -108.0
lon3[1:nlon3,4] <- -107.0

lat3    <- array(0.0, dim=c(nlon3,nlat3))
lat3[1,1:nlat3] <- 50.0
lat3[2,1:nlat3] <- 49.0

time3   <- as.array(c(0,6,18))
tunits3 <- "hours since 2018-01-01 00:00:00"

# -----------------------------------------
# create arrays
# -----------------------------------------
pre    <- array(fillvalue, dim=c(nlon3,nlat3,nt3))
pre[  2,1,1] = 1.0  # row, column, time
pre[1:2,2,1] = 1.0
pre[  1,3,1] = 2.0
pre[  2,3,1] = 0.0
pre[  1,4,1] = 1.0
pre[  2,4,1] = 0.0

pre[  2,1,2] = 0.0
pre[1:2,2,2] = 0.0
pre[1:2,3,2] = 0.0
pre[1:2,4,2] = 0.0

pre[2,1,3] = 1.0
pre[1,2,3] = 4.0
pre[2,2,3] = 1.0
pre[1,3,3] = 4.0
pre[1,4,3] = 1.0
pre[2,4,3] = 0.0

# pre      = np.array([ [ [ -9999.0, 1.0,     2.0, 1.0 ],
#                         [     1.0, 1.0,     0.0, 0.0 ] ],
#                       [ [ -9999.0, 0.0,     0.0, 0.0 ],
#                         [     0.0, 0.0,     0.0, 0.0 ] ],
#                       [ [ -9999.0, 4.0,     4.0, 1.0 ],
#                         [     1.0, 1.0, -9999.0, 0.0 ] ] ])


# -----------------------------------------
# create  netCDF filename
# -----------------------------------------

# path and file name, set dname
ncfname <- "NetCDF_R.nc"
dname <- "pre"  # note: pre means precipitation (not previous)

if (file.exists(ncfname)) {
   file.remove( ncfname )
}


# -----------------------------------------
# Then define the contents of the file:
# -----------------------------------------

# create and write the netCDF file -- ncdf4 version
# define dimensions
londim <- ncdim_def("nlon","",1:nlon3,create_dimvar=FALSE) 
latdim <- ncdim_def("nlat","",1:nlat3,create_dimvar=FALSE) 
timedim <- ncdim_def("time",tunits3,as.double(time3))

# define variables
dlname <- "latitude"
lat_def <- ncvar_def("lat","degrees_north",list(londim,latdim),fillvalue,dlname,prec="double")

dlname <- "longitude"
lon_def <- ncvar_def("lon","degrees_east",list(londim,latdim),fillvalue,dlname,prec="double")

dlname <- "Precipitation"
pre_def <- ncvar_def("pre","mm",list(londim,latdim,timedim),fillvalue,dlname,prec="double")

# create netCDF file and put arrays
ncout <- nc_create(ncfname,list(lat_def,lon_def,pre_def),force_v4=TRUE)

# put variables
ncvar_put(ncout,lat_def,lat3)
ncvar_put(ncout,lon_def,lon3)
ncvar_put(ncout,pre_def,pre)

# put additional attributes into dimension and data variables
ncatt_put(ncout,"lon","axis","X") 
ncatt_put(ncout,"lon","long_name","longitude") 
ncatt_put(ncout,"lon","standard_name","longitude") 

ncatt_put(ncout,"lat","axis","Y")
ncatt_put(ncout,"lat","long_name","latitude")
ncatt_put(ncout,"lat","standard_name","latitude")

ncatt_put(ncout,"time","axis","T")
ncatt_put(ncout,"time","calendar","gregorian")
ncatt_put(ncout,"time","standard_name","time")

ncatt_put(ncout,pre_def$name,"coordinates","lat lon")

# add global attributes
ncatt_put(ncout,0,"title","test data written with R")
ncatt_put(ncout,0,"institution","University of Waterloo")
ncatt_put(ncout,0,"License", "The data were written by me. They are under GPL.")
ncatt_put(ncout,0,"source","Written by CaSPAr test script found on caspar-data.ca")
history <- paste("Created", date(), sep=", ")
ncatt_put(ncout,0,"history",history)
ncatt_put(ncout,0,"Conventions","CF-1.6")

# Get a summary of the created file:
ncout


