% Copyright 2016-2020 Juliane Mai - juliane.mai(at)uwaterloo.ca
%
% License
% This file is part of Juliane Mai's personal code library.
%
% Juliane Mai's personal code library is free software: you can redistribute it and/or modify
% it under the terms of the GNU Lesser General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
% Juliane Mai's personal code library is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
% GNU Lesser General Public License for more details.

% You should have received a copy of the GNU Lesser General Public License
% along with Juliane Mai's personal code library.  If not, see <http://www.gnu.org/licenses/>.
%

% Read a NetCDF file with Matlab                 

% attributes of a variable
ncdisp('NetCDF_Matlab.nc');

% read the variable "lat"
lat = ncread('NetCDF_Matlab.nc','lat');

% get precipitation value of one grid cell [1,3] for all time steps
%    [1,3,1] indicates start of reading (lon=1, lat=3, time=1)
%    [1,1,3] indicates steps read in each direction 
%              lon=1  ... one longitude is read
%              lat=1  ... one latitude is read
%              time=3 ... three time steps are read
pre_lat_lon = ncread('NetCDF_Matlab.nc','pre',[1 3 1],[1 1 3]);


% above returns a 3-dimensional array
% to squeeze this into a 1-dimensional time series do:
pre_lat_lon_time_series = squeeze (pre_lat_lon);

