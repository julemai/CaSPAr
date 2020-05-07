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


%% defining the variables 
T_data   =  [ 0; 6; 18];
lat_data =  [ 50.0, 50.0, 50.0, 50.0 ;
              49.0, 49.0, 49.0, 49.0 ];
lon_data =  [ -110.0, -109.0, -108.0, -107.0;
              -110.0, -109.0, -108.0, -107.0 ];

% timestep t=1:  2018-01-01 00:00:00
pre (:,:,1) = [ -9999.0, 1.0,     2.0, 1.0;
                    1.0, 1.0,     0.0, 0.0 ];

% timestep t=2:  2018-01-01 06:00:00
pre (:,:,2) = [ -9999.0, 0.0,     0.0, 0.0 ;
                    0.0, 0.0,     0.0, 0.0 ];

% timestep t=3:  2018-01-01 18:00:00
pre (:,:,3) = [ -9999.0, 4.0,     4.0, 1.0 ;
                   1.0, 1.0, -9999.0, 0.0 ];

grid_ID     = [ 120.0, 121.0, 125.0, 130.0 ;
                122.0, 124.0, 140.0, 131.0 ];

%% writing the NetCDF file
% creating the file
ncid = netcdf.create('NetCDF_Matlab.nc','NETCDF4');   % Matlab
% diminutions 
dimid_X = netcdf.defDim(ncid,'nlon',2);
dimid_Y = netcdf.defDim(ncid,'nlat',4);
dimid_T = netcdf.defDim(ncid,'time',3); 

% Variable time
time_varid = netcdf.defVar(ncid,'time','NC_INT', dimid_T);
T_data     = [    0;      6;     18];

% Attributes for variable time
netcdf.putAtt(ncid,time_varid ,'long_name','time');
netcdf.putAtt(ncid,time_varid ,'units','hours since 2018-01-01 00:00:00');
netcdf.putAtt(ncid,time_varid ,'calendar','gregorian');
netcdf.putAtt(ncid,time_varid ,'standard_name','time');
netcdf.putAtt(ncid,time_varid ,'axis','T');

% Write data
netcdf.endDef(ncid);
% % if dimid_T = netcdf.defDim(ncid,'time',3); is used
netcdf.putVar(ncid,time_varid,T_data)
% % if dimid_T = netcdf.defDim(ncid,'time', netcdf.getConstant('NC_UNLIMITED')); is used
% netcdf.putVar(ncid,time_varid,[0],[3],T_data)

% Variables
netcdf.reDef(ncid);
lat_varid = netcdf.defVar(ncid,'lat','NC_DOUBLE',[dimid_X dimid_Y]);
lon_varid = netcdf.defVar(ncid,'lon','NC_DOUBLE',[dimid_X dimid_Y]);

% Attributes
netcdf.putAtt(ncid,lat_varid,'long_name',    'latitude');
netcdf.putAtt(ncid,lon_varid,'long_name',    'longitude');
netcdf.putAtt(ncid,lat_varid,'units',        'degrees_north');
netcdf.putAtt(ncid,lon_varid,'units',        'degrees_east');
netcdf.putAtt(ncid,lat_varid,'standard_name','latitude');
netcdf.putAtt(ncid,lon_varid,'standard_name','longitude');

% Write data
netcdf.endDef(ncid);
netcdf.putVar(ncid,lat_varid,lat_data)
netcdf.putVar(ncid,lon_varid,lon_data)

% Variable
netcdf.reDef(ncid);
pre_varid     = netcdf.defVar(ncid,'pre',    'NC_DOUBLE',[dimid_X dimid_Y dimid_T]);
grid_ID_varid = netcdf.defVar(ncid,'grid_ID','NC_DOUBLE',[dimid_X dimid_Y]);

% Attributes
netcdf.putAtt(ncid,pre_varid,'long_name',  'Precipitation');
netcdf.putAtt(ncid,grid_ID_varid,  'long_name',  'Grid ID (numbering grid cells from 1 to N)');
netcdf.putAtt(ncid,pre_varid,'units',      'mm');
netcdf.putAtt(ncid,grid_ID_varid,  'units',      '1');
netcdf.putAtt(ncid,pre_varid,'coordinates','lon lat');
netcdf.putAtt(ncid,grid_ID_varid,  'coordinates','lon lat');

% Write data
netcdf.endDef(ncid);
netcdf.putVar(ncid,pre_varid,    pre)
netcdf.putVar(ncid,grid_ID_varid,grid_ID)
netcdf.reDef(ncid);
netcdf.putAtt(ncid,netcdf.getConstant('NC_GLOBAL'),'Conventions','CF-1.6');
netcdf.putAtt(ncid,netcdf.getConstant('NC_GLOBAL'),'License',    'The data were written by me. They are under GPL.');
netcdf.putAtt(ncid,netcdf.getConstant('NC_GLOBAL'),'history',    ['Created ',datestr(datetime('now'))]);
netcdf.putAtt(ncid,netcdf.getConstant('NC_GLOBAL'),'source',     'Written by CaSPAr test script (https://github.com/kckornelsen/CaSPAR_Public).');
netcdf.endDef(ncid);
netcdf.close(ncid)