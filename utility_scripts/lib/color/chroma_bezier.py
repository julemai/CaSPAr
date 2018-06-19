#!/usr/bin/env python
"""
    Python port of Bezier interpolation of chroma.js: https://github.com/gka/chroma.js
    a JavaScript library for color conversions:
    Copyright (c) 2011-2013, Gregor Aisch.


    Example
    -------
    import numpy as np
    from color import chroma_brewer, hex2rgb01

    import matplotlib as mpl
    from matplotlib.pylab import *

    fig = figure(figsize=(8,6))
    ax1 = fig.add_axes([0.05, 0.90, 0.9, 0.10])
    ax2 = fig.add_axes([0.05, 0.75, 0.9, 0.10])
    ax3 = fig.add_axes([0.05, 0.60, 0.9, 0.10])
    ax4 = fig.add_axes([0.05, 0.45, 0.9, 0.10])
    ax5 = fig.add_axes([0.05, 0.30, 0.9, 0.10])
    ax6 = fig.add_axes([0.05, 0.15, 0.9, 0.10])
    ax7 = fig.add_axes([0.05, 0.00, 0.9, 0.10])

    # 7 sequential colours of increasing luminance
    nn     = 7
    cc     = color.bezier(['black', 'red', 'yellow', 'white'], nn)
    cmap   = mpl.colors.ListedColormap(cc)
    norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    cb     = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm, orientation='horizontal')

    # 255 sequential colours of decreasing luminance
    cc     = color.bezier(['white', 'yellow', 'red', 'black'], reverse=True)
    cmap   = mpl.colors.ListedColormap(cc)
    norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    cb     = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, orientation='horizontal')

    # 9 diverging colours from 5 given colours, first increasing then decreasing luminance
    nn     = 9
    cc     = color.bezier(['darkred', 'deeppink', 'lightyellow', 'lightgreen', 'teal'], nn)
    cmap   = mpl.colors.ListedColormap(cc)
    norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    cb     = mpl.colorbar.ColorbarBase(ax3, cmap=cmap, norm=norm, orientation='horizontal')

    # 9 sequential colours of decreasing luminance
    nn     = 9
    cc     = color.bezier([ color.hex2rgb01(i) for i in color.chroma_brewer['Oranges'][::3] ], nn)
    cmap   = mpl.colors.ListedColormap(cc)
    norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    cb     = mpl.colorbar.ColorbarBase(ax4, cmap=cmap, norm=norm, orientation='horizontal')

    # 5 sequential colours of decreasing luminance registered as MyBrewer colour map with matplotlib
    nn     = 5
    cc     = color.bezier([ color.rgb2rgb01(*i) for i in [(255,255,178), (253,141,60), (189,0,38)] ], nn, cmap='MyBrewer')
    norm   = mpl.colors.BoundaryNorm(np.arange(nn+1), nn)
    cb     = mpl.colorbar.ColorbarBase(ax5, cmap=mpl.cm.get_cmap('MyBrewer'), norm=norm, orientation='horizontal')

    # 9 diverging colours from 3 given colours, first increasing then decreasing luminance
    nn     = 9
    cc     = color.bezier(['darkred', 'lightyellow', 'teal'], nn)
    cmap   = mpl.colors.ListedColormap(cc)
    norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    cb     = mpl.colorbar.ColorbarBase(ax6, cmap=cmap, norm=norm, orientation='horizontal')

    # 9 diverging colours from 3 given colours, first increasing then decreasing luminance
    # but interpolated in L*C*h space instead of L*a*b
    nn     = 9
    cc     = color.bezier(['darkred', 'lightyellow', 'teal'], nn, lch=True)
    cmap   = mpl.colors.ListedColormap(cc)
    norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    cb     = mpl.colorbar.ColorbarBase(ax7, cmap=cmap, norm=norm, orientation='horizontal')

    show()


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

    Copyright 2015 Matthias Cuntz


    History
    -------
    Written,  MC, Mar 2015
"""
import numpy as np
from color import col2rgb, lab2rgb, rgb2lab, rgb2rgb01, rgb012rgb, lch2rgb, rgb2lch

__all__ = ['bezier']

# ---------------------------------------------------------------------

def correct_lightness(func, *args):
    largs = list(args)
    L0  = largs[0]
    L1  = largs[-2]
    pol = L0 > L1
    t   = largs[-1]
    L_actual = func(*largs)
    L_ideal  = L0 + (L1 - L0) * t
    L_diff   = L_actual - L_ideal
    t0 = 0
    t1 = 1
    max_iter = 20
    niter = 0
    while (abs(L_diff) > 1e-2) and (niter < max_iter):
        if pol: L_diff *= -1
        if L_diff < 0:
            t0 = t
            t += (t1 - t) * 0.5
        else:
            t1 = t
            t += (t0 - t) * 0.5
        largs[-1] = t
        L_actual = func(*largs)
        L_diff   = L_actual - L_ideal
        niter += 1
    return t

# ---------------------------------------------------------------------

def bezier(icolors, ncol=255, correctlightness=True, reverse=False, cmap=None, lch=False):
    """
    interpolates between a set of colors using a bezier spline
    """
    # Bezier interpolation functions
    int2 = lambda c0, c1, t :         (1.-t)*c0 + t*c1
    int3 = lambda c0, c1, c2, t :     (1.-t)*(1.-t)*c0 + 2.*(1.-t)*t*c1 + t*t*c2
    int4 = lambda c0, c1, c2, c3, t : (1.-t)*(1.-t)*(1.-t)*c0 + 3.*(1.-t)*(1.-t)*t*c1 + 3.*(1.-t)*t*t*c2 + t*t*t*c3
    
    # Check
    assert ncol > 1, 'Number of interpolated colours must be > 1'

    # Convert colours to L*a*b
    if lch:
        colors = [ rgb2lch(*col2rgb(i)) for i in icolors ] # in lab
    else:
        colors = [ rgb2lab(*col2rgb(i)) for i in icolors ] # in lab

    # Check - 2
    icol = len(colors)
    if (icol > 5):
        raise ValueError('number of input colors > 5 not supported.')

    # Check sequential or diverging colours, i.e. check for increasing/decreasing lightness
    if (icol > 1):
        lights = np.array([ i[0] for i in colors ])
        dlight = np.diff(lights)
        if np.all(dlight < 0.) or np.all(dlight >= 0.):
            idiverge = False
            # if icol > 4:
            #     raise ValueError('only diverging colours supported in case of 5 input colours.')
        else:
            idiverge = True
            if icol == 4:
                print('ll',lights)
                raise ValueError('colours must have increasing or decreasing lightness in case of even number of colors: '+','+','.join([ str(i) for i in lights ]))

    # Interpolate colours
    if icol == 1:
        lab = [ colors[0] for i in range(ncol) ]
    elif icol == 2:
        lab0 = colors[0]
        lab1 = colors[1]
        # linear interpolation
        lab = list()
        for it in range(ncol):
            t = float(it)/float(ncol-1)
            if correctlightness: t = correct_lightness(int2, lab0[0], lab1[0], t)
            lab.append(tuple([ int2(lab0[i], lab1[i], t) for i in range(3) ]))
    elif icol == 3:
        if idiverge:
            assert (ncol % 2) == 1, 'number of colors has to be odd for bezier interpolation with 3 diverging colors.'
            ncol2 = ncol//2 + 1
            # two separate interpolations
            col1 = bezier(icolors[:2], ncol2)
            col2 = bezier(icolors[1:], ncol2)
            col1.extend(col2[1:])
            if lch:
                lab = [ rgb2lch(*rgb012rgb(*i)) for i in col1 ]
            else:
                lab = [ rgb2lab(*rgb012rgb(*i)) for i in col1 ]
        else:
            lab0 = colors[0]
            lab1 = colors[1]
            lab2 = colors[2]            
            # quadratic bezier interpolation
            lab = list()
            for it in range(ncol):
                t = float(it)/float(ncol-1)
                if correctlightness: t = correct_lightness(int3, lab0[0], lab1[0], lab2[0], t)
                lab.append(tuple([ int3(lab0[i], lab1[i], lab2[i], t) for i in range(3) ]))
    elif icol == 4:
        lab0 = colors[0]
        lab1 = colors[1]
        lab2 = colors[2]
        lab3 = colors[3]
        # cubic bezier interpolation
        lab = list()
        for it in range(ncol):
            t = float(it)/float(ncol-1)
            if correctlightness: t = correct_lightness(int4, lab0[0], lab1[0], lab2[0], lab3[0], t)
            lab.append(tuple([ int4(lab0[i], lab1[i], lab2[i], lab3[i], t) for i in range(3) ]))
    elif icol == 5:
        assert (ncol % 2) == 1, 'number of colors has to be odd for bezier interpolation with 5 colors.'
        ncol2 = ncol//2 + 1
        col1 = bezier(icolors[:3], ncol2)
        col2 = bezier(icolors[2:], ncol2)
        col1.extend(col2[1:])
        if lch:
            lab = [ rgb2lch(*rgb012rgb(*i)) for i in col1 ]
        else:
            lab = [ rgb2lab(*rgb012rgb(*i)) for i in col1 ]
    else:
        raise ValueError('number of input colors > 5 not supported.')

    # Reverse colours
    if reverse:
        lab = lab[::-1]

    # rgb [0-1]
    if lch:
        cout = [ rgb2rgb01(*lch2rgb(*i)) for i in lab ]
    else:
        cout = [ rgb2rgb01(*lab2rgb(*i)) for i in lab ]
     
    # Register colour map with matplotlib
    if cmap is not None:
        from matplotlib.colors import ListedColormap
        from matplotlib.cm import register_cmap
        iscmap = ListedColormap(cout, name=cmap, N=ncol)
        register_cmap(name=cmap, cmap=iscmap)

    return cout

# ---------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    # import numpy as np
    # from color import chroma_brewer, hex2rgb01

    # import matplotlib as mpl
    # from matplotlib.pylab import *

    # # L*a*b
    # fig = figure(figsize=(8,6))
    # ax1 = fig.add_axes([0.05, 0.85, 0.9, 0.10])
    # ax2 = fig.add_axes([0.05, 0.70, 0.9, 0.10])
    # ax3 = fig.add_axes([0.05, 0.55, 0.9, 0.10])
    # ax4 = fig.add_axes([0.05, 0.40, 0.9, 0.10])
    # ax5 = fig.add_axes([0.05, 0.25, 0.9, 0.10])
    # ax6 = fig.add_axes([0.05, 0.10, 0.9, 0.10])

    # nn     = 7
    # cc     = bezier(['black', 'red', 'yellow', 'white'], nn)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm, orientation='horizontal')

    # cc     = bezier(['white', 'yellow', 'red', 'black'], reverse=True)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, orientation='horizontal')

    # nn     = 9
    # cc     = bezier(['darkred', 'deeppink', 'lightyellow', 'lightgreen', 'teal'], nn)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax3, cmap=cmap, norm=norm, orientation='horizontal')

    # nn     = 9
    # cc     = bezier([ hex2rgb01(i) for i in chroma_brewer['Oranges'][::3] ], nn)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax4, cmap=cmap, norm=norm, orientation='horizontal')

    # nn     = 5
    # cc     = bezier([ rgb2rgb01(*i) for i in [(255,255,178), (253,141,60), (189,0,38)] ], nn, cmap='MyBrewer')
    # norm   = mpl.colors.BoundaryNorm(np.arange(nn+1), nn)
    # cb     = mpl.colorbar.ColorbarBase(ax5, cmap=mpl.cm.get_cmap('MyBrewer'), norm=norm, orientation='horizontal')

    # nn     = 9
    # cc     = bezier(['darkred', 'lightyellow', 'teal'], nn)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax6, cmap=cmap, norm=norm, orientation='horizontal')

    # # L*C*h
    # fig = figure(figsize=(8,6))
    # ax1 = fig.add_axes([0.05, 0.85, 0.9, 0.10])
    # ax2 = fig.add_axes([0.05, 0.70, 0.9, 0.10])
    # ax3 = fig.add_axes([0.05, 0.55, 0.9, 0.10])
    # ax4 = fig.add_axes([0.05, 0.40, 0.9, 0.10])
    # ax5 = fig.add_axes([0.05, 0.25, 0.9, 0.10])
    # ax6 = fig.add_axes([0.05, 0.10, 0.9, 0.10])

    # nn     = 7
    # cc     = bezier(['black', 'red', 'yellow', 'white'], nn, lch=True)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm, orientation='horizontal')

    # cc     = bezier(['white', 'yellow', 'red', 'black'], reverse=True, lch=True)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, orientation='horizontal')

    # nn     = 9
    # cc     = bezier(['darkred', 'deeppink', 'lightyellow', 'lightgreen', 'teal'], nn, lch=True)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax3, cmap=cmap, norm=norm, orientation='horizontal')

    # nn     = 9
    # cc     = bezier([ hex2rgb01(i) for i in chroma_brewer['Oranges'][::3] ], nn, lch=True)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax4, cmap=cmap, norm=norm, orientation='horizontal')

    # nn     = 5
    # cc     = bezier([ rgb2rgb01(*i) for i in [(255,255,178), (253,141,60), (189,0,38)] ], nn, cmap='MyBrewer', lch=True)
    # norm   = mpl.colors.BoundaryNorm(np.arange(nn+1), nn)
    # cb     = mpl.colorbar.ColorbarBase(ax5, cmap=mpl.cm.get_cmap('MyBrewer'), norm=norm, orientation='horizontal')

    # nn     = 9
    # cc     = bezier(['darkred', 'lightyellow', 'teal'], nn, lch=True)
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax6, cmap=cmap, norm=norm, orientation='horizontal')

    # show()
