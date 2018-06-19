#!/usr/bin/env python
"""
    Register colourmaps with Matplotlib or return RGB values.
    Colour maps include Cynthia Brewer's colour maps,
    maps from the Geography department of Oregon State University,
    and maps from PyNGL, the Python port of the NCAR Command Language (NCL).

    Provides also a routine to plot the colormaps.


    Definition
    ----------
    Register colormap with Matplotlib and get colormap handle
        def get_brewer(cname=None, names=False, rgb=False, rgb256=False, reverse=False, grey=False, gray=False):
    Register colormap with Matplotlib
        def register_brewer(cname='all', reverse=False, grey=False, gray=False):
    Print available colormap names
        def print_brewer(names='all'):
    Plot all colormaps in png files
       def plot_brewer(pngbase='brewer_colors_',reverse=False, grey=False, gray=False):


    Input
    -----
    None


    Optional Input
    --------------
    get_brewer
        cname      Name of colormap
        names      Return list of colormap names
                   if 'sequential': return sequential colormap names
                   if 'diverging': return diverging colormap names
                   if 'qualitative': return qualitative colormap names
                   if 'osu': return Oregon State University colormap names
                   if 'ncl_large': return ncl large colormap names with more than 50 colors
                   if 'ncl_small': return ncl small colormap names with more than 50 colors
                   if 'ncl_meteo_swiss': return ncl small colormap names from Meteo Swiss
                   if 'mma': return Mathematica colour maps
                   else: return sequential+diverging+qualitative+osu+ncl_large+ncl_small+ncl_meteo_swiss+mma colormap names
        rgb        if True: return RGB value tuple between 0 and 1
        rgb256     if True: return RGB value tuple between 0 and 255
        reverse    if True: reverse colormaps
        grey       if True: return grey equivalent
        gray       Same as grey
    plot_brewer
        pngbase    Name of png file bases. png files will be named pngbase001, pngbase002, ...
                   (default: 'brewer_colors_')
        reverse    if True: reverse colormaps
        grey       if True: return grey equivalent
        gray       Same as grey
    print_brewer
        names      Print colormap names (default: 'all')
                   if 'sequential': print sequential colormap names
                   if 'diverging': print diverging colormap names
                   if 'qualitative': print qualitative colormap names
                   if 'osu': print Oregon State University colormap names
                   if 'ncl_large': print ncl colormap names with more than 50 colors
                   if 'ncl_small': print ncl colormap names with less than 50 colors
                   if 'ncl_meteo_swiss': print ncl small colormap names from Meteo Swiss
                   if 'mma': return Mathematica colour maps
                   else: print sequential+diverging+qualitative+osu+ncl_large+ncl_small+ncl_meteo_swiss+mma colormap names
    register_brewer
        cname      Colormap to register colormaps (default: 'all')
                   if 'all': registers all sequential+diverging+qualitative+osu+ncl_large+ncl_small+ncl_meteo_swiss+mma colormaps
        reverse    if True: reverse colormaps
        grey       if True: return grey equivalent
        gray       Same as grey


    Output
    ------
    matplotlib colormap instance or tuple with RGB values


    References
    ----------
    Colourmaps by Cynthia A. Brewer, Geography, Pennsylvania State University
      http://colorbrewer2.org
    Values copied from
      http://www.personal.psu.edu/cab38/ColorBrewer/ColorBrewer_all_schemes_RGBonly4_withPalette_and_Macro.xls
    Colourmaps from Geography, University of Oregon
      http://geography.uoregon.edu/datagraphics/color_scales.htm
    Colourmaps from PyNGL, the Python interface to the NCAR Command Language (NCL)
      http://www.pyngl.ucar.edu/Graphics/color_table_gallery.shtml
    

    Examples
    --------
    # Print
    # print_brewer('diverging')

    # Plot
    # plot_brewer('brew_')

    # Get Names
    # names = get_brewer(names='sequential')

    # Register colour map and get colour map handle
    # cc = get_brewer('RdYlBu11')
    # plt.pcolormesh(np.outer(np.arange(cc.N), np.ones(cc.N)), cmap=cc)

    # Get RGB colours of colour map
    # cc = get_brewer('blues4', rgb=True)
    # mark1 = sub.plot(x, y)
    # plt.setp(mark1, linestyle='None', marker='o', markeredgecolor=cc[0], markerfacecolor='None')

    # Register and use colour map
    # from scipy import misc
    # lena = misc.lena()
    # plt.imshow(l, cmap=mpl.cm.rainbow)
    # register_brewer('ncl_meteo_swiss')
    # plt.imshow(l, cmap=mpl.cm.get_cmap('hotcold_18lev'))
    # plt.imshow(l, cmap=get_brewer('hotcold_18lev'))

    >>> import numpy as np
    >>> import jams
    >>> from autostring import astr
    >>> qua = list(color.brewer_qualitative.keys())
    >>> qua.sort()
    >>> print(qua[0:7])
    ['accent3', 'accent4', 'accent5', 'accent6', 'accent7', 'accent8', 'dark23']

    >>> print(astr(np.array(color.get_brewer('blues4', rgb=True)[0]), 4))
    ['0.9373' '0.9529' '1.0000']

    >>> print(color.get_brewer('Blues4', rgb256=True)[0])
    (239, 243, 255)

    >>> cc = color.get_brewer('bLuEs4', rgb256=True, reverse=True)
    >>> print(cc[-1])
    (239, 243, 255)
    >>> print(cc[0])
    (33, 113, 181)

    >>> print(astr(np.array(color.get_brewer('blues4', rgb256=True, grey=True)[0]), 4))
    ['242.9897' '242.9897' '242.9897']

    
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

    Copyright 2012-2013 Matthias Cuntz


    History
    -------
    Written,  MC, Sep 2012
    Modified, MC, Feb 2013 - ported to Python 3
              MC, Jun 2013 - include Uni Oregon colours
              ST, Mar 2014 - include NCL color maps; define_brewer -> register_brewer
              MC, MAr 2014 - colour maps in extra file brewer.cmaps
              JM, Sep 2014 - color maps of Mathematica
              MC, Oct 2016 - print_brewers outputs sorted lists
              MC, Nov 2016 - ported to Python 3, mostly dict.keys() into list(dict.keys())
"""
from __future__ import print_function

from color import brewer_sequential, brewer_diverging, brewer_qualitative
from color import oregon_sequential, oregon_diverging, oregon_qualitative
from color import ncl_large, ncl_small, ncl_meteo_swiss, mathematica

__all__ = ['get_brewer', 'register_brewer', 'print_brewer', 'plot_brewer']

# -------------------------------------------------------------------------------------------------

oregon = oregon_sequential.copy()
oregon.update(oregon_diverging)
oregon.update(oregon_qualitative)

all_maps = brewer_sequential.copy()
all_maps.update(brewer_diverging)
all_maps.update(brewer_qualitative)
all_maps.update(oregon_sequential)
all_maps.update(oregon_diverging)
all_maps.update(oregon_qualitative)
all_maps.update(ncl_large)
all_maps.update(ncl_small)
all_maps.update(ncl_meteo_swiss)
all_maps.update(mathematica)

all255_maps = brewer_sequential.copy()
all255_maps.update(brewer_diverging)
all255_maps.update(brewer_qualitative)
all255_maps.update(oregon_sequential)
all255_maps.update(oregon_diverging)
all255_maps.update(oregon_qualitative)

# -------------------------------------------------------------------------------------------------

def capitalise(cname):
    ''' Search for colour map if not the right capitalisation is given.
        Ex.:     cmaps = [ capitalise(cc) for cc in cmaps ]
    '''
    if cname in all_maps:
        return cname
    else:
        lcmaps = [ c.lower() for c in list(all_maps.keys()) ]
        if cname.lower() in lcmaps:
            return list(all_maps.keys())[lcmaps.index(cname.lower())]
        else:
            raise ValueError('Color map name not known: '+cname)            

# -------------------------------------------------------------------------------------------------

def register_brewer(cname='all', reverse=False, grey=False, gray=False):
    '''Register colourmap(s) with Matplotlib
       Ex.: register_brewer('ygn3')
    '''
    from matplotlib.colors import ListedColormap
    from matplotlib.cm import register_cmap
    from color import rgb2rgb01
    if cname.lower() == 'all':
        cmaps = all_maps
    elif cname.lower() == 'sequential':
        cmaps = brewer_sequential
    elif cname.lower() == 'diverging':
        cmaps = brewer_diverging
    elif cname.lower() == 'qualitative':
        cmaps = brewer_qualitative
    elif cname.lower() == 'osu':
        cmaps = oregon
    elif cname.lower() == 'ncl_large':
        cmaps = ncl_large
    elif cname.lower() == 'ncl_small':
        cmaps = ncl_small
    elif cname.lower() == 'ncl_meteo_swiss':
        cmaps = ncl_meteo_swiss
    elif cname.lower() == 'mma' or cname.lower() == 'mathematica':
        cmaps = mathematica
    else:
        cmaps = [cname]
    cmaps = [ capitalise(cc) for cc in cmaps ]
    for i in cmaps:
        cpool = all_maps[i][:]
        if i in all255_maps:
            cpool = [ rgb2rgb01(*j) for j in cpool ]
        if reverse:
            cpool = cpool[::-1]
        if grey or gray:
            for j in range(len(cpool)):
                isgray = 0.2125 * cpool[j][0] + 0.7154 * cpool[j][1] + 0.072* cpool[j][2]
                cpool[j] = (isgray,isgray,isgray)
        cmap = ListedColormap(cpool, i)
        register_cmap(cmap=cmap)

# -------------------------------------------------------------------------------------------------

def print_brewer(names='all'):
    """
        Print names of known colour maps.

        Examples
        --------
        >>> print_brewer('qualitative')
        ['accent3', 'accent4', 'accent5', 'accent6', 'accent7', 'accent8', 'dark23', 'dark24', 'dark25', 'dark26', 'dark27', 'dark28', 'paired10', 'paired11', 'paired12', 'paired3', 'paired4', 'paired5', 'paired6', 'paired7', 'paired8', 'paired9', 'pastel13', 'pastel14', 'pastel15', 'pastel16', 'pastel17', 'pastel18', 'pastel19', 'pastel23', 'pastel24', 'pastel25', 'pastel26', 'pastel27', 'pastel28', 'set13', 'set14', 'set15', 'set16', 'set17', 'set18', 'set19', 'set23', 'set24', 'set25', 'set26', 'set27', 'set28', 'set310', 'set311', 'set312', 'set33', 'set34', 'set35', 'set36', 'set37', 'set38', 'set39']
    """
    if names.lower() == 'sequential':
        pp = list(brewer_sequential.keys())
        pp.sort()
        print(pp)
    elif names.lower() == 'diverging':
        pp = list(brewer_diverging.keys())
        pp.sort()
        print(pp)
    elif names.lower() == 'qualitative':
        pp = list(brewer_qualitative.keys())
        pp.sort()
        print(pp)
    elif names.lower() == 'osu':
        pp = list(oregon.keys())
        pp.sort()
        print(pp)
    elif names.lower() == 'ncl_large':
        pp = list(ncl_large.keys())
        pp.sort()
        print(pp)
    elif names.lower() == 'ncl_small':
        pp = list(ncl_small.keys())
        pp.sort()
        print(pp)
    elif names.lower() == 'ncl_meteo_swiss':
        pp = list(ncl_meteo_swiss.keys())
        pp.sort()
        print(pp)
    elif names.lower() == 'mma' or names.lower() == 'mathematica':
        pp = list(mathematica.keys())
        pp.sort()
        print(pp)
    else:
        print('Sequential color maps')
        pp = list(brewer_sequential_maps.keys())
        pp.sort()
        print(pp)
        print('')
        print('Diverging color maps')
        pp = list(brewer_diverging_maps.keys())
        pp.sort()
        print(pp)
        print('')
        print('Qualitative color maps')
        pp = list(brewer_qualitative_maps.keys())
        pp.sort()
        print(pp)
        print('')
        print('Oregon State University color maps')
        pp = list(oregon.keys())
        pp.sort()
        print(pp)
        print('')
        print('NCL large color maps')
        pp = list(ncl_large.keys())
        pp.sort()
        print(pp)
        print('')
        print('NCL small color maps')
        pp = list(ncl_small.keys())
        pp.sort()
        print(pp)
        print('')
        print('NCL meteo swiss color maps')
        pp = list(ncl_meteo_swiss.keys())
        pp.sort()
        print(pp)
        print('')
        print('Mathematica color maps')
        pp = list(mathematica.keys())
        pp.sort()
        print(pp)

# -------------------------------------------------------------------------------------------------

def get_brewer(cname=None, names=False, rgb=False, rgb256=False, reverse=False, grey=False, gray=False):
    """
        Get colour map either as registered handle or as RGB values (0-255 or 0-1).

        Examples
        --------
        >>> import numpy as np
        >>> from autostring import astr
        >>> cc = get_brewer('blues4',rgb=True)
        >>> print(astr(np.array(cc[0]), 4))
        ['0.9373' '0.9529' '1.0000']

        >>> cc = get_brewer('Blues4',rgb256=True)
        >>> print(cc[0])
        (239, 243, 255)

        >>> cc = get_brewer('bLuEs4',rgb256=True,reverse=True)
        >>> print(cc[-1])
        (239, 243, 255)
        >>> print(cc[0])
        (33, 113, 181)

        >>> cc = get_brewer('blues4',rgb256=True,grey=True)
        >>> print(astr(np.array(cc[0]), 4))
        ['242.9897' '242.9897' '242.9897']
    """
    from color import rgb2rgb01, rgb012rgb
    if names:
        if names.lower() == 'sequential':
            return list(brewer_sequential.keys())
        elif names.lower() == 'diverging':
            return list(brewer_diverging.keys())
        elif names.lower() == 'qualitative':
            return list(brewer_qualitative.keys())
        elif names.lower() == 'osu':
            return list(oregon.keys())
        elif names.lower() == 'ncl_large':
            return list(ncl_large.keys())
        elif names.lower() == 'ncl_small':
            return list(ncl_small.keys())
        elif names.lower() == 'ncl_meteo_swiss':
            return list(ncl_meteo_swiss.keys())
        elif names.lower() == 'mma' or names.lower() == 'mathematica':
            return list(mathematica.keys())
        else:
            cmaps = list(all_maps.keys())
            return cmaps
    else:
        cname = capitalise(cname)
        cpool = all_maps[cname][:]
        if (not rgb) and (not rgb256):
            # register colour map with matplotlib
            from matplotlib.cm import get_cmap
            register_brewer(cname, reverse=reverse, grey=grey, gray=gray)
            return get_cmap(cname)
        elif rgb:
            # tuple 0-1
            if cname in all255_maps:
                cpool = [ rgb2rgb01(*i) for i in cpool ]
        elif rgb256:
            # tuple 0-255
            if cname not in all255_maps:
                cpool = [ rgb012rgb(*i) for i in cpool ]
        if reverse:
            cpool = cpool[::-1]
        if grey or gray:
            for j in range(len(cpool)):
                isgray = 0.2125 * cpool[j][0] + 0.7154 * cpool[j][1] + 0.072* cpool[j][2]
                cpool[j] = (isgray,isgray,isgray)
        return cpool

# -------------------------------------------------------------------------------------------------

def plot_brewer(pngbase='brewer_colors_',reverse=False, grey=False, gray=False):
    '''Plot all colour bars in PNG files.
       Ex.: plot_brewer('brewer_', reverse=True)
    '''
    import numpy as np
    from position import position
    outtype = 'png'
    nrow       = 5           # # of rows of subplots per figure
    ncol       = 14          # # of columns of subplots per figure
    hspace     = 0.01        # x-space between subplots
    wspace     = 0.08        # y-space between subplots
    textsize   = 10          # standard text size
    lwidth     = 1.0         # axis line width
    alwidth    = 1.0         # axis line width
    dpi         = 300
    transparent = False
    bbox_inches = 'tight'
    pad_inches  = 0
    import matplotlib as mpl
    mpl.use('Agg') # set directly after import matplotlib
    import matplotlib.pyplot as plt
    mpl.rc('figure', figsize=(8.27,11.69)) # a4 portrait
    #mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    mpl.rc('font',**{'family':'serif','serif':['times']})
    mpl.rc('text.latex', unicode=True)
    mpl.rc('savefig', dpi=dpi, format='png')
    mpl.rc('font', size=textsize)
    mpl.rc('lines', linewidth=lwidth, color='black')
    mpl.rc('axes', linewidth=alwidth, labelcolor='black')
    mpl.rc('path', simplify=False) # do not remove

    figsize = mpl.rcParams['figure.figsize']
    ifig = 0

    nmaps = len(brewer_sequential)
    npage = nrow*ncol
    zaehl = 0
    for kk in brewer_sequential:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "Sequential", ha="center", size=12)
        cc = get_brewer(kk, reverse=reverse, grey=grey, gray=gray)
        plt.pcolormesh(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc)
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)

    nmaps = len(brewer_diverging)
    npage = nrow*ncol
    zaehl = 0
    for kk in brewer_diverging:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "Diverging", ha="center", size=12)
        cc = get_brewer(kk,reverse=reverse, grey=grey, gray=gray)
        plt.pcolormesh(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc)
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)

    nmaps = len(brewer_qualitative)
    npage = nrow*ncol
    zaehl = 0
    for kk in brewer_qualitative:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "Qualitative", ha="center", size=12)
        cc = get_brewer(kk,reverse=reverse, grey=grey, gray=gray)
        plt.pcolormesh(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc)
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)

    nmaps = len(oregon)
    npage = nrow*ncol
    zaehl = 0
    for kk in oregon:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "Oregon State University (OSU)", ha="center", size=12)
        cc = get_brewer(kk,reverse=reverse, grey=grey, gray=gray)
        plt.pcolormesh(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc)
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)

    nrow       = 1  # only one row for ncl large maps
    ncol       = 14
    nmaps = len(ncl_large)
    npage = nrow*ncol
    zaehl = 0
    for kk in ncl_large:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace,top=0.85))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "ncl_large_maps", ha="center", size=12)
        cc = get_brewer(kk,reverse=reverse, grey=grey, gray=gray)
        plt.pcolor(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc,linewidth=0,edgecolor='None')
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)
    
    nrow       = 2 # set to two for ncl small maps
    ncol       = 14
    nmaps = len(ncl_small)
    npage = nrow*ncol
    zaehl = 0
    for kk in ncl_small:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace,top=0.85))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "ncl_small_maps", ha="center", size=12)
        cc = get_brewer(kk,reverse=reverse, grey=grey, gray=gray)
        plt.pcolor(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc,linewidth=0,edgecolor='None')
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)
    
    nmaps = len(ncl_meteo_swiss)
    npage = nrow*ncol
    zaehl = 0
    for kk in ncl_meteo_swiss:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace,top=0.85))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "ncl_meteo_swiss_maps", ha="center", size=12)
        cc = get_brewer(kk,reverse=reverse, grey=grey, gray=gray)
        plt.pcolor(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc,linewidth=0,edgecolor='None')
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)

    nmaps = len(mathematica)
    npage = nrow*ncol
    zaehl = 0
    for kk in mathematica:
        if zaehl % npage == 0:
            if zaehl != 0:
                pngfile = pngbase+"{0:04d}".format(ifig)+".png"
                fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
                plt.close(fig)
            ifig += 1
            iplot = 0
            print('Page ', ifig)
            fig = plt.figure(ifig)
        iplot += 1
        sub = fig.add_axes(position(nrow,ncol,iplot,hspace=hspace,wspace=wspace,top=0.85))
        sub.axis('off')
        if iplot == 1:
            fig.text(0.5, 0.97, "mma_maps", ha="center", size=12)
        cc = get_brewer(kk, reverse=reverse, grey=grey, gray=gray)
        plt.pcolor(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc,linewidth=0,edgecolor='None')
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)

# -------------------------------------------------------------------------------------------------
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    # import numpy as np
    # from position import position
    # from autostring import astr
    # cc = get_brewer('blues4', rgb=True)
    # print(astr(np.array(cc[0]), 4))
    # #    ['0.9373' '0.9529' '1.0000']

    # cc = get_brewer('Blues4', rgb256=True)
    # print(cc[0])
    # #    (239, 243, 255)

    # cc = get_brewer('blues4', rgb256=True, reverse=True)
    # print(cc[-1])
    # #    (239, 243, 255)
    # print(cc[0])
    # #    (33, 113, 181)

    # cc = get_brewer('blues4',rgb256=True,grey=True)
    # print(astr(np.array(cc[0]), 4))
    # #    ['242.9897' '242.9897' '242.9897']

    # # plot_brewer('test_', reverse=True)
    # # plot_brewer('test_gray_', gray=True)

    # # Register and use colour map
    # from scipy import misc
    # lena = misc.lena()
    # from matplotlib.pylab import *
    # figure()
    # imshow(lena, cmap=mpl.cm.rainbow)
    # show()
    # figure()
    # register_brewer('ncl_meteo_swiss')
    # imshow(lena, cmap=mpl.cm.get_cmap('hotcold_18lev'))
    # show()
    # figure()
    # imshow(lena, cmap=get_brewer('BlueRedGray'))
    # show()

    # # Register and use colour map
    # from scipy import misc
    # lena = misc.lena()
    # from matplotlib.pylab import *
    # figure()
    # imshow(lena, cmap=mpl.cm.rainbow)
    # show()
    # figure()
    # register_brewer('mathematica')
    # # print_brewer('mathematica')
    # imshow(lena, mpl.cm.get_cmap('dark_rainbow_16'))
    # show()
