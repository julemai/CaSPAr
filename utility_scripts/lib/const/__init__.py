#!/usr/bin/env python
"""
    Provides physical, mathematical, computational, and isotope constants.


    Definition
    ----------
    Pi = 3.141592653589793238462643383279502884197
    ...
    Define the following constants:
        Mathematical
            Pi, Pi2, Pi3, TwoPi, Sqrt2
        Physical
            Gravity, T0, P0, T25, sigma, R, Na, REarth
        Isotope
            R13VPDB, R18VSMOW, R2VSMOW
        Computational
            tiny, huge, eps
        Material
            mmol_co2, mmol_h2o, mmol_air
            density_quartz, cheat_quartz, cheat_water, cheat_air, latentheat_vaporization


    Examples
    --------
    area = const.Pi * radius**2


    License
    -------
    This file is part of the JAMS Python package.

    The JAMS Python package is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The JAMS Python package is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with the JAMS Python package (cf. gpl.txt and lgpl.txt).
    If not, see <http://www.gnu.org/licenses/>.

    Copyright 2014 Matthias Cuntz


    History
    -------
    Written,  MC, Oct 2014
"""
from .const import Pi, Pi2, Pi3, TwoPi, Sqrt2
from .const import Gravity, T0, P0, T25, sigma, R, Na, REarth
from .const import mmol_co2, mmol_h2o, mmol_air
from .const import density_quartz, cheat_quartz, cheat_water, cheat_air, latentheat_vaporization
from .const import R13VPDB, R18VSMOW, R2VSMOW
from .const import tiny, huge, eps

# Information
__author__   = "Matthias Cuntz"
__version__  = '1.1'
__revision__ = "Revision: 2071"
__date__     = 'Date: 24.03.2015'
