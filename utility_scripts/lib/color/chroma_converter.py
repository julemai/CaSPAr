#!/usr/bin/env python
"""
    Python port of conversions of chroma.js: https://github.com/gka/chroma.js
    a JavaScript library for color conversions:
    Copyright (c) 2011-2013, Gregor Aisch.


    Example
    -------
    >>> import color
    >>> print(color.rgb2hex(1, 101, 201))
    #0165c9

    >>> print(color.hex2rgb(color.rgb2hex(1, 101, 201)))
    (1, 101, 201)

    >>> print(color.hsi2rgb(*color.rgb2hsi(1, 101, 201)))
    (1, 101, 201)

    >>> print(color.hsl2rgb(*color.rgb2hsl(1, 101, 201)))
    (1, 101, 201)

    >>> print(color.hsv2rgb(*color.rgb2hsv(1, 101, 201)))
    (1, 101, 201)

    >>> print(color.lab2rgb(*color.rgb2lab(1, 101, 201)))
    (1, 101, 201)

    >>> print(color.lch2rgb(*color.rgb2lch(1, 101, 201)))
    (1, 101, 201)


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
from math import floor, cos, sin, sqrt, acos, atan2
from color import limit

__all__ = ['rgb2hex',   'hex2rgb',   'hex2rgb01', # convert between hexadecimal and rgb colour representations
           'rgb2hsi',   'hsi2rgb',   'hsi2rgb01',
           'rgb2hsl',   'hsl2rgb',   'hsl2rgb01',
           'rgb2hsv',   'hsv2rgb',   'hsv2rgb01',
           'rgb2lab',   'lab2rgb',   'lab2rgb01',
           'lab2lch',   'lch2lab',
           'rgb2lch',   'lch2rgb',   'lch2rgb01',
           'rgb2rgb01', 'rgb012rgb',
           'col2rgb',   'col2rgb01']

# math
Pi    = 3.141592653589793238462643383279502884197    # Pi
Pi3   = 1.0471975511965977461542144610931676280656   # Pi/3
TwoPi = 6.283185307179586476925286766559005768394    # 2*Pi

# D65 standard referent
X = 0.950470
Y = 1.
Z = 1.088830

# Notes - bug fixes compared to chroma.js
# in rgb_xyz
#     if (r/255) <= 0.04045:
# to
#     r = float(r) / 255.
#     if r <= 0.03928:
# 0.03928 fits with luminance and it gives in reverse 0.00304 from xyz_rgb
#
# in rgb2hsv
#     if delta == 0.:
#         return (0., 0., v)
#
# in hsi2rgb
#     r = limit(i*r*3.)*255.
#     g = limit(i*g*3.)*255.
#     b = limit(i*b*3.)*255.
# to
#     r = round(limit(i*r*3.)*255.)
#     g = round(limit(i*g*3.)*255.)
#     b = round(limit(i*b*3.)*255.)

# ---------------------------------------------------------------------
# Converters
# ---------------------------------------------------------------------

def rgb2hex(r,g,b):
    """ Convert between RGB [0-255] and hex string """
    xr = hex(r)[2:]
    xg = hex(g)[2:]
    xb = hex(b)[2:]
    sr = '0'+str(xr) # can be 0x1 instead of 0x01
    sg = '0'+str(xg)
    sb = '0'+str(xb)
    return "#"+sr[-2:]+sg[-2:]+sb[-2:]

# ---------------------------------------------------------------------

def hex2rgb(hex):
    """ Convert between hex string and RGB [0-255] """
    from matplotlib.colors import ColorConverter
    cc = ColorConverter()
    return rgb012rgb(*cc.to_rgb(hex))

# ---------------------------------------------------------------------

def hex2rgb01(hex):
    """ Convert between hex string and RGB [0-1] """
    return rgb2rgb01(*hex2rgb(hex))

# ---------------------------------------------------------------------

def rgb2hsi(r,g,b):
    """ Convert between RGB [0-255] and HSI """
    # borrowed from http://hummer.stanford.edu/museinfo/doc/examples/humdrum/keyscape2/rgb2hsi.cpp
    r = float(r) / 255.
    g = float(g) / 255.
    b = float(b) / 255.
    mini = min(r,g,b)
    i = (r+g+b) / 3.
    if i == 0:
        s = 0.
    else:
        s = 1. - mini/i
    if s == 0.:
        h = 0.
    else:
        h  = ((r-g)+(r-b)) / 2.
        h /= sqrt((r-g)*(r-g) + (r-b)*(g-b))
        h  = acos(h)
        if b > g:
            h = TwoPi - h
        h /= TwoPi
    return (h*360., s, i)

# ---------------------------------------------------------------------

def hsi2rgb(h,s,i):
    """ Convert between HSI and RGB [0-255] """
    # borrowed from http://hummer.stanford.edu/museinfo/doc/examples/humdrum/keyscape2/hsi2rgb.cpp
    f = lambda x, y : (1.+y*cos(TwoPi*x)/cos(Pi3-TwoPi*x))/3.
    # select 
    h /= 360.
    if h < 1./3.:
        b = (1.-s)/3.
        r = f(h, s)
        g = 1. - (b+r)
    elif (h >= 1./3.) & (h < 2./3.):
        h -= 1./3.
        r  = (1.-s)/3.
        g  = f(h, s)
        b  = 1 - (r+g)
    elif (h > 2./3.):
        h -= 2./3.
        g  = (1.-s)/3.
        b  = f(h, s)
        r  = 1. - (g+b)
    r = round(limit(i*r*3.)*255.)
    g = round(limit(i*g*3.)*255.)
    b = round(limit(i*b*3.)*255.)
    # out
    return (int(r), int(g), int(b))

# ---------------------------------------------------------------------

def hsi2rgb01(h,s,i):
    """ Convert between HSI and RGB [0-1] """
    return rgb2rgb01(*hsi2rgb(h,s,i))

# ---------------------------------------------------------------------

def rgb2hsl(r,g,b):
    """ Convert between RGB [0-255] and HSL """
    r = float(r) / 255.
    g = float(g) / 255.
    b = float(b) / 255.
    
    mini = min(r, g, b)
    maxi = max(r, g, b)
    l = (maxi + mini) / 2.
    if maxi == mini:
        s = 0.
        h = float('nan')
    else:
        if l < 0.5:
            s = (maxi - mini) / (maxi + mini)
        else:
            s = (maxi - mini) / (2. - maxi - mini)
            
        if r == maxi:
            h = (g - b) / (maxi - mini)
        elif (g == maxi):
            h = 2. + (b - r) / (maxi - mini)
        elif (b == maxi):
            h = 4. + (r - g) / (maxi - mini)

    h *= 60.
    if h < 0.:
        h += 360.

    return (h, s, l)

# ---------------------------------------------------------------------

def hsl2rgb(h,s,l):
    """ Convert between HSL and RGB [0-255] """
    h = float(h)
    s = float(s)
    l = float(l)
    if s == 0:
        r = l*255.
        g = l*255.
        b = l*255.
    else:
        t3 = [0.,0.,0.]
        c  = [0.,0.,0.]
        if l < 0.5:
            t2 = l * (1.+s)
        else:
            t2 = l + s - l*s
        t1 = 2. * l - t2
        h /= 360.
        t3[0] = h + 1./3.
        t3[1] = h
        t3[2] = h - 1./3.
        for i in range(3):
            if t3[i] < 0.:
                t3[i] += 1.
            elif t3[i] > 1.:
                t3[i] -= 1.

            if (6. * t3[i]) < 1.:
                c[i] = t1 + (t2 - t1) * 6. * t3[i]
            elif (2. * t3[i]) < 1.:
                c[i] = t2
            elif (3. * t3[i]) < 2.:
                c[i] = t1 + (t2 - t1) * ((2./3.) - t3[i]) * 6.
            else:
                c[i] = t1
        r = round(c[0]*255.)
        g = round(c[1]*255.)
        b = round(c[2]*255.)
    # out
    return (int(r), int(g), int(b))

# ---------------------------------------------------------------------

def hsl2rgb01(h,s,l):
    """ Convert between HSL and RGB [0-1] """
    return rgb2rgb01(*hsl2rgb(h,s,l))

# ---------------------------------------------------------------------

def rgb2hsv(r,g,b):
    """ Convert between RGB [0-255] and HSV """
    r = float(r)
    g = float(g)
    b = float(b)
    mini = min(r, g, b)
    maxi = max(r, g, b)
    delta = maxi - mini
    v = maxi / 255.
    if delta == 0.:
        return (0., 0., v)
    if maxi == 0:
        return (float('nan'), 0., v)
    # else
    s = delta / maxi
    if r == maxi: h = (g - b) / delta
    if g == maxi: h = 2. + (b - r) / delta
    if b == maxi: h = 4. + (r - g) / delta
    h *= 60.
    if h < 0: h += 360.
    return (h, s, v)

# ---------------------------------------------------------------------

def hsv2rgb(h,s,v):
    """ Convert between HSV and RGB [0-255] """
    h = float(h)
    s = float(s)
    v = float(v)
    v *= 255.
    if s == 0:
        r = v
        g = v
        b = v
    else:
        if h == 360:
            h = 0
        elif h > 360:
            h -= 360
        elif h < 0:
            h += 360
        h /= 60.
        i = floor(h)
        f = h - i
        p = v * (1. - s)
        q = v * (1. - s * f)
        t = v * (1. - s * (1. - f))
        i = int(i)
        if i == 0:
            r = v
            g = t
            b = p
        elif i == 1:
            r = q
            g = v
            b = p
        elif i == 2:
            r = p
            g = v
            b = t
        elif i == 3:
            r = p
            g = q
            b = v
        elif i == 4:
            r = t
            g = p
            b = v
        elif i == 5:
            r = v
            g = p
            b = q
    r = round(r)
    g = round(g)
    b = round(b)
    # out
    return (int(r), int(g), int(b))

# ---------------------------------------------------------------------

def hsv2rgb01(h,s,v):
    """ Convert between HSV and RGB [0-1] """
    return rgb2rgb01(*hsv2rgb(h,s,v))

# ---------------------------------------------------------------------

def rgb_xyz(r):
    r = float(r) / 255.
    if r <= 0.03928:
        return r / 12.92
    else:
        return ((r + 0.055) / 1.055)**2.4

# ---------------------------------------------------------------------

def xyz_lab(x):
    if x > 0.008856:
        return x**(1./3.)
    else:
        return 7.787037*x + 4./29.
    
# ---------------------------------------------------------------------

def rgb2lab(r,g,b):
    """ Convert between RGB [0-255] and Lab """
    r = rgb_xyz(float(r))
    g = rgb_xyz(float(g))
    b = rgb_xyz(float(b))
    x = xyz_lab((0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / X)
    y = xyz_lab((0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / Y)
    z = xyz_lab((0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / Z)
    return (116. * y - 16., 500. * (x - y), 200. * (y - z))

# ---------------------------------------------------------------------

def lab_xyz(x):
    if x > 0.206893034:
        return x*x*x
    else:
        return (x - 4./29.) / 7.787037

# ---------------------------------------------------------------------

def xyz_rgb(r):
    if r <= 0.00304:
        return round(255.* (12.92 * r))
    else:
        return round(255.* (1.055 * r**(1./2.4) - 0.055))

# ---------------------------------------------------------------------

def lab2rgb(l,a,b):
    """ Convert between Lab and RGB [0-255] """
    l = float(l)
    a = float(a)
    b = float(b)
    # adapted to match d3 implementation
    y = (l + 16.) / 116.
    x = y + a / 500.
    z = y - b / 200.
    x = lab_xyz(x) * X
    y = lab_xyz(y) * Y
    z = lab_xyz(z) * Z
    r = xyz_rgb( 3.2404542 * x - 1.5371385 * y - 0.4985314 * z)
    g = xyz_rgb(-0.9692660 * x + 1.8760108 * y + 0.0415560 * z)
    b = xyz_rgb( 0.0556434 * x - 0.2040259 * y + 1.0572252 * z)
    r = limit(r, 0., 255.)
    g = limit(g, 0., 255.)
    b = limit(b, 0., 255.)
    # out
    return (int(r), int(g), int(b))

# ---------------------------------------------------------------------

def lab2rgb01(l,a,b):
    """ Convert between Lab and RGB [0-1] """
    return rgb2rgb01(*lab2rgb(l,a,b))

# ---------------------------------------------------------------------

def lab2lch(l,a,b):
    """ Convert between Lab and LcH """
    c = sqrt(a * a + b * b)
    h = atan2(b, a) / Pi * 180.
    return (l, c, h)

# ---------------------------------------------------------------------

def lch2lab(l,c,h):
    """
    Convert between LcH and Lab
    
    Convert from a qualitative parameter h and a quantitative parameter l to a 24-bit pixel.
    These formulas were invented by David Dalrymple to obtain maximum contrast without going
    out of gamut if the parameters are in the range 0-1.
    A saturation multiplier was added by Gregor Aisch.
    """
    h = h * Pi / 180.
    a = cos(h) * c
    b = sin(h) * c
    return (l, a, b)

# ---------------------------------------------------------------------

def rgb2lch(r,g,b):
    """ Convert between RGB [0-255] and LcH """
    return lab2lch(*rgb2lab(r,g,b))

# ---------------------------------------------------------------------

def lch2rgb(l,c,h):
    """ Convert between LcH and RGB [0-255] """
    r, g, b = lab2rgb(*lch2lab(l,c,h))
    return (limit(r,0,255), limit(g,0,255), limit(b,0,255))

# ---------------------------------------------------------------------

def lch2rgb01(l,c,h):
    """ Convert between LcH and RGB [0-1] """
    return rgb2rgb01(*lch2rgb(l,c,h))

# ---------------------------------------------------------------------

def rgb2rgb01(r, g, b):
    """ Convert between RGB [0-255] and RGB [0-1] """
    return tuple([ float(i)/255. for i in [r,g,b] ])

# ---------------------------------------------------------------------

def rgb012rgb(r, g, b):
    """ Convert between RGB [0-1] and RGB [0-255] """
    return tuple([ int(round(float(i)*255.)) for i in [r,g,b] ])

# ---------------------------------------------------------------------

def col2rgb01(color):
    """ Convert any colour known by matplotlib (plus RGB [0-255]) to RGB [0-1] """
    import numpy as np
    from matplotlib.colors import ColorConverter
    cc = ColorConverter()
    
    # try matplotlib converter first
    try:
        colors = cc.to_rgb(color)
    except:
        # Must be rgb 0-255.
        # In any other case, the colour systems are indistinguishable
        if isinstance(color, (list, tuple, np.array)):
            if len(color) > 3:
                raise ValueError('Cannot interpret color (1).')
            colors = rgb2rgb01(*list(color))
        else:
            raise ValueError('Cannot interpret color (2).')
    
    return colors

# ---------------------------------------------------------------------

def col2rgb(color):
    """ Convert any colour known by matplotlib to RGB [0-255] """
    return rgb012rgb(*col2rgb01(color))

# ---------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    # import numpy as np
    # print(hex2rgb(rgb2hex(1, 101, 201)))
    # print(hsi2rgb(*rgb2hsi(1, 101, 201)))
    # print(hsl2rgb(*rgb2hsl(1, 101, 201)))
    # print(hsv2rgb(*rgb2hsv(1, 101, 201)))
    # print(lab2rgb(*rgb2lab(1, 101, 201)))
    # print(lch2rgb(*rgb2lch(1, 101, 201)))
