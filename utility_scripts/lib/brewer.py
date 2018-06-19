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
    # plt.imshow(l, cmap=jams.get_brewer('hotcold_18lev'))


    
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
"""
from __future__ import print_function

# Define colormaps
# from .find_in_path import find_in_path
# cmapfile = find_in_path('brewer.cmaps') # in jams_python
import os
cmapfile = os.path.join(os.path.dirname(__file__), 'brewer.cmaps') # in jams_python/jams
exec(compile(open(cmapfile).read(), cmapfile, 'exec'))

sequential_maps = ['ylgn3','ylgn4','ylgn5','ylgn6','ylgn7','ylgn8','ylgn9','ylgnbu3','ylgnbu4',
                   'ylgnbu5','ylgnbu6','ylgnbu7','ylgnbu8','ylgnbu9','gnbu3','gnbu4','gnbu5',
                   'gnbu6','gnbu7','gnbu8','gnbu9','bugn3','bugn4','bugn5','bugn6','bugn7','bugn8',
                   'bugn9','pubugn3','pubugn4','pubugn5','pubugn6','pubugn7','pubugn8','pubugn9',
                   'pubu3','pubu4','pubu5','pubu6','pubu7','pubu8','pubu9','bupu3','bupu4','bupu5',
                   'bupu6','bupu7','bupu8','bupu9','rdpu3','rdpu4','rdpu5','rdpu6','rdpu7','rdpu8',
                   'rdpu9','purd3','purd4','purd5','purd6','purd7','purd8','purd9','orrd3','orrd4',
                   'orrd5','orrd6','orrd7','orrd8','orrd9','ylorrd3','ylorrd4','ylorrd5','ylorrd6',
                   'ylorrd7','ylorrd8','ylorrd9','ylorbr3','ylorbr4','ylorbr5','ylorbr6','ylorbr7',
                   'ylorbr8','ylorbr9','purples3','purples4','purples5','purples6','purples7','purples8',
                   'purples9','blues3','blues4','blues5','blues6','blues7','blues8','blues9','greens3',
                   'greens4','greens5','greens6','greens7','greens8','greens9','oranges3','oranges4',
                   'oranges5','oranges6','oranges7','oranges8','oranges9','reds3','reds4','reds5','reds6',
                   'reds7','reds8','reds9','greys3','greys4','greys5','greys6','greys7','greys8','greys9']

diverging_maps = ['puor3','puor4','puor5','puor6','puor7','puor8','puor9','puor10','puor11','brbg3',
                  'brbg4','brbg5','brbg6','brbg7','brbg8','brbg9','brbg10','brbg11','prgn3','prgn4',
                  'prgn5','prgn6','prgn7','prgn8','prgn9','prgn10','prgn11','piyg3','piyg4','piyg5',
                  'piyg6','piyg7','piyg8','piyg9','piyg10','piyg11','rdbu3','rdbu4','rdbu5','rdbu6',
                  'rdbu7','rdbu8','rdbu9','rdbu10','rdbu11','rdgy3','rdgy4','rdgy5','rdgy6','rdgy7',
                  'rdgy8','rdgy9','rdgy10','rdgy11','rdylbu3','rdylbu4','rdylbu5','rdylbu6','rdylbu7',
                  'rdylbu8','rdylbu9','rdylbu10','rdylbu11','spectral3','spectral4','spectral5',
                  'spectral6','spectral7','spectral8','spectral9','spectral10','spectral11',
                  'rdylgn3','rdylgn4','rdylgn5','rdylgn6','rdylgn7','rdylgn8','rdylgn9','rdylgn10',
                  'rdylgn11']

qualitative_maps = ['set33','set34','set35','set36','set37','set38','set39','set310','set311','set312',
                    'pastel13','pastel14','pastel15','pastel16','pastel17','pastel18','pastel19','set13',
                    'set14','set15','set16','set17','set18','set19','pastel23','pastel24','pastel25',
                    'pastel26','pastel27','pastel28','set23','set24','set25','set26','set27','set28',
                    'dark23','dark24','dark25','dark26','dark27','dark28','paired3','paired4','paired5',
                    'paired6','paired7','paired8','paired9','paired10','paired11','paired12','accent3',
                    'accent4','accent5','accent6','accent7','accent8']

osu_maps = ['bu7', 'bu10', 'step5',
            'brbu10', 'brbu12', 'budor12', 'budor18', 'drdbu12', 'drdbu18', 'bugn14', 'bugr8',
            'buor8', 'buor10', 'buor12', 'buor14', 'rdylbu11b', 'gnmg16',
            'cat12']

ncl_large_maps = ['BkBlAqGrYeOrReViWh200', 'BlAqGrYeOrRe', 'BlAqGrYeOrReVi200', 
                  'BlGrYeOrReVi200', 'BlRe', 'BlueRed', 'BlueRedGray', 'BlueWhiteOrangeRed',
                  'BlueYellowRed', 'BlWhRe', 'detail', 'example', 'extrema', 'GrayWhiteGray',
                  'GreenYellow', 'helix', 'helix1', 'hotres', 'ncview_default',
                  'OceanLakeLandSnow', 'psgcap', 'rainbow', 'rainbowwhitegray', 
                  'rainbowwhite', 'rainbowgray', 'testcmap', 'tbr_240_300',
                  'tbr_stdev_0_30', 'tbr_var_0_500', 'tbrAvg1', 'tbrStd1', 'tbrVar1',
                  'temp1', 'thelix', 'uniform', 'ViBlGrWhYeOrRe', 'wh_bl_gr_ye_re', 
                  'WhBlGrYeRe', 'WhBlReWh', 'WhViBlGrYeOrRe', 'WhViBlGrYeOrReWh', 
                  'WhiteBlue', 'WhiteBlueGreenYellowRed', 'WhiteGreen', 
                  'WhiteYellowOrangeRed', 'wxpEnIR', 'gauss', 'saw']

ncl_small_maps = ['amwg', 'amwg_blueyellowred', 'BlueDarkRed18', 
                  'BlueDarkOrange18', 'BlueGreen14', 'BrownBlue12', 
                  'Cat12', 'cosam12', 'cosam', 'cyclic', 'default',
                  'GreenMagenta16', 'gscyclic', 'gsdtol', 'gsltod',
                  'gui_default', 'hlu_default', 'hotcold_18lev',
                  'hotcolr_19lev', 'mch_default', 'nrl_sirkes', 
                  'perc2_9lev', 'percent_11lev', 'posneg_1', 'posneg_2',
                  'prcp_1', 'prcp_2', 'prcp_3', 'precip_11lev',
                  'precip_diff_12lev', 'precip_diff_1lev', 'precip2_15lev',
                  'precip2_17lev', 'precip3_16lev', 'precip4_11lev',
                  'precip4_diff_19lev', 'radar', 'radar_1', 'rh_19lev',
                  'so4_21', 'so4_23', 'spread_15lev', 'StepSeq25', 'sunshine_9lev',
                  'sunshine_diff_12lev', 'temp_19lev', 'temp_diff_18lev',
                  'temp_diff_1lev', 'topo_15lev', 'wgne15', 'wind_17lev']

ncl_meteo_swiss_maps = ['hotcold_18lev', 'hotcolr_19lev', 'mch_default', 'perc2_9lev',
                        'percent_11lev', 'precip2_15lev', 'precip2_17lev', 'precip3_16lev',
                        'precip4_11lev', 'precip4_diff_19lev', 'precip_11lev', 'precip_diff_12lev',
                        'precip_diff_1lev', 'rh_19lev', 'spread_15lev', 'sunshine_9lev', 'sunshine_diff_12lev',
                        't2m_29lev', 'temp_19lev', 'temp_diff_18lev', 'temp_diff_1lev', 'topo_15lev',
                        'wind_17lev']

mma_maps = ['dark_rainbow_6', 'dark_rainbow_8', 'dark_rainbow_12', 'dark_rainbow_16', 'dark_rainbow_256',
            'starry_night_colors_8','starry_night_colors_16','starry_night_colors_256',
            'gray_yellow_tones_8', 'gray_yellow_tones_16', 'gray_yellow_tones_256']

all_maps = sequential_maps + diverging_maps + qualitative_maps + osu_maps + ncl_large_maps + ncl_small_maps + ncl_meteo_swiss_maps + mma_maps

def capitalise(cname):
    ''' Search for colour map if not the right capitalisation is given.
        Ex.:     cmaps = [ capitalise(cc) for cc in cmaps ]
    '''
    if cname in all_maps:
        return cname
    else:
        lcmaps = [ c.lower() for c in all_maps ]
        if cname.lower() in lcmaps:
            return all_maps[lcmaps.index(cname.lower())]
        else:
            raise ValueError('Color map name not known: '+cname)            

def register_brewer(cname='all', reverse=False, grey=False, gray=False):
    '''Register colourmap(s) with Matplotlib
       Ex.: register_brewer('ygn3')
    '''
    import matplotlib.colors as col
    import matplotlib.cm as cm
    if cname.lower() == 'all':
        cmaps = all_maps
    elif cname.lower() == 'sequential':
        cmaps = sequential_maps
    elif cname.lower() == 'diverging':
        cmaps = diverging_maps
    elif cname.lower() == 'qualitative':
        cmaps = qualitative_maps
    elif cname.lower() == 'osu':
        cmaps = osu_maps
    elif cname.lower() == 'ncl_large':
        cmaps = ncl_large_maps
    elif cname.lower() == 'ncl_small':
        cmaps = ncl_small_maps
    elif cname.lower() == 'ncl_meteo_swiss':
        cmaps = ncl_meteo_swiss_maps
    elif cname.lower() == 'mma':
        cmaps = mma_maps
    else:
        cmaps = [cname]
    cmaps = [ capitalise(cc) for cc in cmaps ]
    for i in cmaps:
        d = {}
        if i in ncl_large_maps + ncl_small_maps + ncl_meteo_swiss_maps + mma_maps:
            exec('cpool = '+i, globals(), d)
        else:
            exec('cpool = [ tuple([k/255. for k in j]) for j in '+i+' ]', globals(), d)
        cpool = d['cpool']
        if reverse:
            cpool = cpool[::-1]
        if grey | gray:
            for j in range(len(cpool)):
                isgray = 0.2125 * cpool[j][0] + 0.7154 * cpool[j][1] + 0.072* cpool[j][2]
                cpool[j] = (isgray,isgray,isgray)
        cmap = col.ListedColormap(cpool, i)
        cm.register_cmap(cmap=cmap)


def print_brewer(names='all'):
    """
        Print names of known colour maps.

        Examples
        --------
        >>> print_brewer('qualitative')
        ['set33', 'set34', 'set35', 'set36', 'set37', 'set38', 'set39', 'set310', 'set311', 'set312', 'pastel13', 'pastel14', 'pastel15', 'pastel16', 'pastel17', 'pastel18', 'pastel19', 'set13', 'set14', 'set15', 'set16', 'set17', 'set18', 'set19', 'pastel23', 'pastel24', 'pastel25', 'pastel26', 'pastel27', 'pastel28', 'set23', 'set24', 'set25', 'set26', 'set27', 'set28', 'dark23', 'dark24', 'dark25', 'dark26', 'dark27', 'dark28', 'paired3', 'paired4', 'paired5', 'paired6', 'paired7', 'paired8', 'paired9', 'paired10', 'paired11', 'paired12', 'accent3', 'accent4', 'accent5', 'accent6', 'accent7', 'accent8']
    """
    if names.lower() == 'sequential':
        print(sequential_maps)
    elif names.lower() == 'diverging':
        print(diverging_maps)
    elif names.lower() == 'qualitative':
        print(qualitative_maps)
    elif names.lower() == 'osu':
        print(osu_maps)
    elif names.lower() == 'ncl_large':
        print(ncl_large_maps)
    elif names.lower() == 'ncl_small':
        print(ncl_small_maps)
    elif names.lower() == 'ncl_meteo_swiss':
        print(ncl_meteo_swiss_maps)
    elif names.lower() == 'mma':
        print(mma_maps)
    else:
        print('Sequential color maps')
        print(sequential_maps)
        print('')
        print('Diverging color maps')
        print(diverging_maps)
        print('')
        print('Qualitative color maps')
        print(qualitative_maps)
        print('')
        print('Oregon State University color maps')
        print(osu_maps)
        print('')
        print('NCL large color maps')
        print(ncl_large_maps)
        print('')
        print('NCL small color maps')
        print(ncl_small_maps)
        print('')
        print('NCL meteo swiss color maps')
        print(ncl_meteo_swiss_maps)
        print('')
        print('Mathematica color maps')
        print(mma_maps)

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
    if names:
        if names.lower() == 'sequential':
            return sequential_maps
        elif names.lower() == 'diverging':
            return diverging_maps
        elif names.lower() == 'qualitative':
            return qualitative_maps
        elif names.lower() == 'osu':
            return osu_maps
        elif names.lower() == 'ncl_large':
            return ncl_large_maps
        elif names.lower() == 'ncl_small':
            return ncl_small_maps
        elif names.lower() == 'ncl_meteo_swiss':
            return ncl_meteo_swiss_maps
        elif names.lower() == 'mma':
            return mma_maps
        else:
            cmaps = all_maps
            return cmaps
    else:
        cname = capitalise(cname)
        if rgb256:
            d = {}
            if cname in ncl_large_maps + ncl_small_maps + ncl_meteo_swiss_maps + mma_maps:
                exec('cpool = [ tuple([k*255. for k in j]) for j in '+cname+' ]', globals(), d)
            else:
                exec('cpool = '+cname, globals(), d)
            cpool = d['cpool']
            if reverse:
                cpool = cpool[::-1]
            if grey | gray:
                for j in range(len(cpool)):
                    isgray = 0.2125 * cpool[j][0] + 0.7154 * cpool[j][1] + 0.072* cpool[j][2]
                    cpool[j] = (isgray,isgray,isgray)
            return cpool
        # get colour tuple in 0-1
        elif rgb:
            d = {}
            if cname in ncl_large_maps + ncl_small_maps + ncl_meteo_swiss_maps + mma_maps:
                exec('cpool = '+cname, globals(), d)
            else:
                exec('cpool = [ tuple([k/255. for k in j]) for j in '+cname+' ]', globals(), d)
            cpool = d['cpool']
            if reverse:
                cpool = cpool[::-1]
            if grey | gray:
                for j in range(len(cpool)):
                    isgray = 0.2125 * cpool[j][0] + 0.7154 * cpool[j][1] + 0.072* cpool[j][2]
                    cpool[j] = (isgray,isgray,isgray)
            return cpool
        # register colour map with matplotlib
        else:
            import matplotlib.cm as cm
            register_brewer(cname,reverse=reverse, grey=grey, gray=gray)
            return cm.get_cmap(cname)


def plot_brewer(pngbase='brewer_colors_',reverse=False, grey=False, gray=False):
    '''Plot all colour bars in PNG files.
       Ex.: plot_brewer('brewer_', reverse=True)
    '''
    import numpy as np
    from position import position
    outtype = 'pdf'
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

    nmaps = len(sequential_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in sequential_maps:
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

    nmaps = len(diverging_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in diverging_maps:
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

    nmaps = len(qualitative_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in qualitative_maps:
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

    nmaps = len(osu_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in osu_maps:
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
    nmaps = len(ncl_large_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in ncl_large_maps:
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
    nmaps = len(ncl_small_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in ncl_small_maps:
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
    
    nmaps = len(ncl_meteo_swiss_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in ncl_meteo_swiss_maps:
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

    nmaps = len(mma_maps)
    npage = nrow*ncol
    zaehl = 0
    for kk in mma_maps:
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
        cc = get_brewer(kk,reverse=reverse, grey=grey, gray=gray)
        plt.pcolor(np.outer(np.arange(cc.N),np.ones(cc.N)),cmap=cc,linewidth=0,edgecolor='None')
        plt.setp(sub, title=kk)
        plt.setp(sub.title,fontsize=10, rotation=90, verticalalignment='bottom')
        zaehl += 1
    pngfile = pngbase+"{0:04d}".format(ifig)+".png"
    fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
    plt.close(fig)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    # import numpy as np
    # from autostring import astr
    # cc = get_brewer('blues4',rgb=True)
    # print(astr(np.array(cc[0]), 4))
    # #    ['0.9373' '0.9529' '1.0000']

    # cc = get_brewer('Blues4',rgb256=True)
    # print(cc[0])
    # #    (239, 243, 255)

    # cc = get_brewer('blues4',rgb256=True,reverse=True)
    # print(cc[-1])
    # #    (239, 243, 255)
    # print(cc[0])
    # #    (33, 113, 181)

    # cc = get_brewer('blues4',rgb256=True,grey=True)
    # print(astr(np.array(cc[0]), 4))
    # #    ['242.9897' '242.9897' '242.9897']

    # plot_brewer('test_', reverse=True)
    # plot_brewer('test_gray_', gray=True)

    # # Register and use colour map
    # from scipy import misc
    # lena = misc.lena()
    # from matplotlib.pylab import *
    # imshow(lena, cmap=mpl.cm.rainbow)
    # show()
    # register_brewer('ncl_meteo_swiss')
    # imshow(lena, cmap=mpl.cm.get_cmap('hotcold_18lev'))
    # show()
    # imshow(lena, cmap=get_brewer('BlueRedGray'))
    # show()

    # # Register and use colour map
    # from scipy import misc
    # lena = misc.lena()
    # from matplotlib.pylab import *
    # imshow(lena, cmap=mpl.cm.rainbow)
    # show()
    # jams.register_brewer('mma')
    # # jams.print_brewer('mma')
    # imshow(lena, mpl.cm.get_cmap('dark_rainbow_16'))
    # show()
