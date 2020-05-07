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


"""

Converts list of coordinates (in degrees) to a shapefile that can be uploaded to CaSPAr.

Polygon does not need to be closed.

Requires shapefile package which can be installed using "pip install pyshp". 
For further details see: https://code.google.com/archive/p/pyshp/

History
-------
Written,  JM, May 2020

"""

import shapefile
import sys


def coords2shapefile(filename,coords):
    
    """
    Converts given coordinates into shapefile that can be uploaded to CaSPAr.

    Parameters
    ----------
    filename: str
        Name of the shapefile (without any extension). Files that will be produced are:
        <filename>.dbf
        <filename>.prj
        <filename>.shp
        <filename>.shx
        Zip these four files to upload to CaSPAr.

    coords: array
        2-D Array of coordinates of a single polygon. CaSPAr does not support
        multiple polygons. Polygon does not need to be closed. The shapefile package is 
        checking and copies automatically the first point to the end if polygon is not closed.
        Example:
        [[-123,50], [-118,40], [-118,44], [-113,44]]              # unclosed geometry
        [[-123,50], [-118,40], [-118,44], [-113,44],[-123,50]]    # closed geometry

    Returns
    -------
    None

    """

    # -----------------------
    # Check if polygon is clockwise:
    #       Use "shapefile.signed_area()" method to determine if a ring is clockwise or counter-clockwise
    #       Value >= 0 means the ring is counter-clockwise.
    #       Value <  0 means the ring is clockwise
    #       The value returned is also the area of the polygon.
    # -----------------------
    area = shapefile.signed_area(coords)

    if area >= 0:
        coords.reverse()    # transform counter-clockwise to clockwise
    
    if sys.version_info < (3,0,0):
        # ------------------------
        # Create a polygon shapefile
        # ------------------------
        # Found under:
        #     https://code.google.com/archive/p/pyshp/
        w = shapefile.Writer(shapefile.POLYGON)
        
        # an arrow-shaped polygon east of Vancouver, Seattle, and Portland
        w.poly([coords])   
        w.field('FIRST_FLD','C','40')
        w.record('First','Polygon')
        w.save(filename)
    else:
        # ------------------------
        # Create a polygon shapefile
        # ------------------------
        # Found under:
        #     https://code.google.com/archive/p/pyshp/
        w = shapefile.Writer(target=filename) 
        
        # an arrow-shaped polygon east of Vancouver, Seattle, and Portland
        w.poly([coords])   
        w.field('FIRST_FLD','C','40')
        w.record('First','Polygon')
        w.close()
        
    
    # ------------------------
    # Write projection information
    # ------------------------
    # Found under:
    #     https://code.google.com/archive/p/pyshp/wikis/CreatePRJfiles.wiki
    prj = open("%s.prj" % filename, "w")
    epsg = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]'
    prj.write(epsg)
    prj.close()

    return

if __name__ == '__main__':
    # import doctest
    # doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    coords = [[-123,50], [-118,40], [-118,44], [-113,44]]
    filename = 'polygon.shp'

    coords2shapefile(filename,coords)
