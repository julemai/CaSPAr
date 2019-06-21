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


