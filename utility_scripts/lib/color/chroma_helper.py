#!/usr/bin/env python
"""
    Python port of helper functions of chroma.js: https://github.com/gka/chroma.js
    a JavaScript library for color conversions:
    Copyright (c) 2011-2013, Gregor Aisch.


    Example
    -------
    >>> import color
    >>> print(color.limit(-1))
    0

    >>> print(color.limit(2))
    1

    >>> print(color.limit(267, mini=0, maxi=255))
    255

    >>> print(color.luminance(*(0,0,0)))
    0.0

    >>> print(color.luminance(*(255,255,255)))
    1.0

    >>> print(color.luminance(*(255,0,0)))
    0.2126


    chroma.js License
    -----------------
    chroma.js - JavaScript library for color conversions

    Copyright (c) 2011-2013, Gregor Aisch
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
       list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation
       and/or other materials provided with the distribution.

    3. The name Gregor Aisch may not be used to endorse or promote products
       derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL GREGOR AISCH OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
    INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
    BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
    NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
    EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    
    JAMS License
    -----------
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

    Copyright 2012-2013 Matthias Cuntz


    History
    -------
    Written,  MC, Mar 2015
"""

__all__ = ['limit', 'luminance']

# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def limit(x, mini=0, maxi=1):
    return max(min(x, maxi), mini)

# ---------------------------------------------------------------------

def luminance_x(x):
    x = float(x) / 255.
    if x <= 0.03928:
       return x/12.92
    else:
       return ((x+0.055)/1.055)**2.4

# ---------------------------------------------------------------------

def luminance(r,g,b):
    # relative luminance
    # see http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
    r = luminance_x(r)
    g = luminance_x(g)
    b = luminance_x(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

# ---------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
