#!/usr/bin/env python
"""
    Provide UFZ colours.


    Provided colours
    ----------------
    Can be accessed also with colours(list of colours)
    ufzdarkblue, ufzblue, ufzlightblue,
    ufzred, ufzorange, ufzyellow,
    ufzdarkgreen, ufzgreen, ufzlightgreen,
    ufzgray1, ufzgray2, ufzgray3,
    ufzgrey1, ufzgrey2, ufzgrey3,
    ufzdarkgray, ufzgray, ufzlightgray,
    ufzdarkgrey, ufzgrey, ufzlightgrey,
    ufzblack, ufzwhite,
    darkblue=ufzdarkblue, blue=ufzblue, lightblue=ufzlightblue,
    red=ufzred, orange=ufzorange, yellow=ufzyellow,
    darkgreen=ufzdarkgreen, green=ufzgreen, lightgreen=ufzlightgreen,
    gray1=ufzgray1, gray2=ufzgray2, gray3=ufzgray3,
    grey1=ufzgrey1, grey2=ufzgrey2, grey3=ufzgrey3,
    darkgray=ufzdarkgray, gray=ufzgray, lightgray=ufzlightgray,
    darkgrey=ufzdarkgrey, grey=ufzgrey, lightgrey=ufzlightgrey,
    black=ufzblack, white=ufzwhite


    Example
    -------
    >>> import numpy as np
    >>> from autostring import astr
    >>> from color.colours import colours
    >>> print(astr(np.array(color.ufzdarkblue), 4))
    ['0.0000' '0.2431' '0.4314']

    >>> print(colours('ufzdarkblue', rgb256=True))
    (0.0, 62.0, 110.0)

    >>> print(colours(names=True)[0:3])
    ['ufzdarkblue', 'ufzblue', 'ufzlightblue']

    >>> print(astr(np.array(color.colours('UFZDARKBLUE')), 4))
    ['0.0000' '0.2431' '0.4314']

    >>> print(astr(np.array(color.colours('DarkBlue')), 4))
    ['0.0000' '0.2431' '0.4314']

    >>> print(color.colours(['orange','ufzdarkblue'], rgb256=True))
    [(207.0, 104.0, 0.0), (0.0, 62.0, 110.0)]


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

    Copyright 2015 Matthias Cuntz


    History
    -------
    Written,  MC, Mar 2015
"""
from __future__ import print_function

__all__ = ['ufzdarkblue', 'ufzblue', 'ufzlightblue',
           'ufzred', 'ufzorange', 'ufzyellow',
           'ufzdarkgreen', 'ufzgreen', 'ufzlightgreen',
           'ufzgray1', 'ufzgray2', 'ufzgray3',
           'ufzgrey1', 'ufzgrey2', 'ufzgrey3',
           'ufzdarkgray', 'ufzgray', 'ufzlightgray',
           'ufzdarkgrey', 'ufzgrey', 'ufzlightgrey',
           'ufzblack', 'ufzwhite',
           'darkblue', 'blue', 'lightblue',
           'red', 'orange', 'yellow',
           'darkgreen', 'green', 'lightgreen',
           'gray1', 'gray2', 'gray3',
           'grey1', 'grey2', 'grey3',
           'darkgray', 'gray', 'lightgray',
           'darkgrey', 'grey', 'lightgrey',
           'black', 'white']

# ---------------------------------------------------------------------

ufzdarkblue   = (  0./255.,  62./255., 110./255.)
ufzblue       = (  0./255.,  88./255., 156./255.)
ufzlightblue  = (  0./255., 162./255., 224./255.)
ufzred        = (212./255.,  45./255.,  18./255.)
ufzorange     = (207./255., 104./255.,   0./255.)
ufzyellow     = (230./255., 175./255.,  17./255.)
ufzdarkgreen  = ( 20./255.,  77./255.,  40./255.)
ufzgreen      = (169./255., 181./255.,   9./255.)
ufzlightgreen = ufzgreen
ufzgray1      = ( 81./255.,  81./255.,  81./255.)
ufzgray2      = (156./255., 156./255., 156./255.)
ufzgray3      = (185./255., 185./255., 185./255.)
ufzgrey1      = ufzgray1
ufzgrey2      = ufzgray2
ufzgrey3      = ufzgray3
ufzdarkgray   = ufzgray1
ufzgray       = ufzgray2
ufzlightgray  = ufzgray3
ufzdarkgrey   = ufzgray1
ufzgrey       = ufzgray2
ufzlightgrey  = ufzgray3
ufzblack      = (  0./255.,   0./255.,   0./255.)
ufzwhite      = (255./255., 255./255., 255./255.)

# In Emacs copy ori and query-replace-regexp
# ^\([[:alnum:]]*\).*  ->  \1 = \1
# ^ufz  ->
darkblue   = ufzdarkblue
blue       = ufzblue
lightblue  = ufzlightblue
red        = ufzred
orange     = ufzorange
yellow     = ufzyellow
darkgreen  = ufzdarkgreen
green      = ufzgreen
lightgreen = ufzlightgreen
gray1      = ufzgray1
gray2      = ufzgray2
gray3      = ufzgray3
grey1      = ufzgrey1
grey2      = ufzgrey2
grey3      = ufzgrey3
darkgray   = ufzdarkgray
gray       = ufzgray
lightgray  = ufzlightgray
darkgrey   = ufzdarkgrey
grey       = ufzgrey
lightgrey  = ufzlightgrey
black      = ufzblack
white      = ufzwhite

# ---------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
