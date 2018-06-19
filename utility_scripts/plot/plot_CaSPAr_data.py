#!/usr/bin/env python
from __future__ import print_function

# Copyright 2016-2018 Juliane Mai - juliane.mai(at)uwaterloo.ca
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

Plots CASAPAR data

Run with::

      run plot_CASPAR_data.py -i /Users/j6mai/Desktop/CASPAR/sample_data_new_attr/CaPA_coarse_2017100218.nc -v CaPA_coarse_A_PR_SFC -g CaPA_coarse_2017100218
      run plot_CASPAR_data.py -i /Users/j6mai/Desktop/CASPAR/sample_data_new_attr/CaLDAS_2017100200_000.nc  -v CaLDAS_A_I0_Profile  -g CaLDAS_2017100200_000

      
"""

# -------------------------------------------------------------------------
# Command line arguments
#

import argparse

pngbase   = ''
inputfile = ''
variable  = ''
pdffile   = ''
usetex    = False

parser  = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                  description='''Plots for CASPAR.''')
parser.add_argument('-g', '--pngbase', action='store',
                    default=pngbase, dest='pngbase', metavar='pngbase',
                    help='Name basis for png output files (default: open screen window).')
parser.add_argument('-p', '--pdffile', action='store',
                    default=pdffile, dest='pdffile', metavar='pdffile',
                    help='Name of pdf output file (default: open screen window).')
parser.add_argument('-t', '--usetex', action='store_true', default=usetex, dest="usetex",
                    help="Use LaTeX to render text in pdf.")

parser.add_argument('-v', '--variable', action='store', default=variable, dest='variable',
                    help="Name of variable which will be plotted.")
parser.add_argument('-i', '--inputfile', action='store', default=inputfile, dest='inputfile',
                    help="Name of NC file containing data.")

args            = parser.parse_args()
pngbase         = args.pngbase
pdffile         = args.pdffile
usetex          = args.usetex
variable        = args.variable
inputfile       = args.inputfile

if (pdffile != '') & (pngbase != ''):
    print('\nError: PDF and PNG are mutually exclusive. Only either -p or -g possible.\n')
    parser.print_usage()
    import sys
    sys.exit()

del parser, args

# -----------------------
# add subolder scripts/lib to search path
# -----------------------
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+'/../lib')

# import packages after help so that help with command line -h is fast
import numpy as np
import time
import xarray as xr
import pandas as pd

import color                      # in lib/
from position   import position   # in lib/
from str2tex    import str2tex    # in lib/

# -------------------------------------------------------------------------
# Customize plots
#

if (pdffile == ''):
    if (pngbase == ''):
        outtype = 'x'
    else:
        outtype = 'png'
else:
    outtype = 'pdf'

# Main plot
nrow        = 3           # # of rows of subplots per figure
ncol        = 1           # # of columns of subplots per figure
hspace      = 0.05        # x-space between subplots
vspace      = 0.04        # y-space between subplots
right       = 0.9         # right space on page
textsize    = 7           # standard text size
textsize_clock = 0.6*textsize        # standard text size
dxabc       = 0.95        # % of (max-min) shift to the right from left y-axis for a,b,c,... labels
dyabc       = 0.9         # % of (max-min) shift up from lower x-axis for a,b,c,... labels
dxabc_clock = 2.3         # % of (max-min) shift to the right from left y-axis for a,b,c,... labels
dyabc_clock = 0           # % of (max-min) shift up from lower x-axis for a,b,c,... labels
dxsig       = 1.23        # % of (max-min) shift to the right from left y-axis for a,b,c,... labels
dysig       = -0.05       # % of (max-min) shift up from lower x-axis for a,b,c,... labels

lwidth      = 1.5         # linewidth
elwidth     = 1.0         # errorbar line width
alwidth     = 1.0         # axis line width
glwidth     = 0.5         # grid line width
msize       = 1.0         # marker size
mwidth      = 1.0         # marker edge width
mcol1       = '0.0'       # primary marker colour
mcol2       = '0.4'                     # secondary
mcol3       = '0.0' # third
mcols       = ['0.0', '0.4', '0.4', '0.7', '0.7', '1.0']
lcol1       = color.colours('blue')   # primary line colour
lcol2       = '0.4'
lcol3       = '0.0'
lcols       = ['None', 'None', 'None', 'None', 'None', '0.0']
hatches     = [None, None, None, None, None, '//']
dobw      = False # True: black & white

# Legend
llxbbox       = 0.0         # x-anchor legend bounding box
llybbox       = 1.0        # y-anchor legend bounding box
llxbbox_clock = -0.2        # x-anchor legend bounding box clock_plot
llybbox_clock = 1.08        # y-anchor legend bounding box clock_plot
llrspace      = 0.          # spacing between rows in legend
llcspace      = 1.0         # spacing between columns in legend
llhtextpad    = 0.4         # the pad between the legend handle and text
llhlength     = 1.5         # the length of the legend handles
frameon       = False       # if True, draw a frame around the legend. If None, use rc

# PNG
dpi           = 600
transparent   = False
bbox_inches   = 'tight'
pad_inches    = 0.035

# Clock options
ymax          = 0.8
ntextsize     = textsize_clock # 'medium'   # normal textsize
# modules
bmod          = 0.5         # fraction of ymax from center to start module colours
alphamod      = 0.7         # alpha channel for modules
fwm           = 0.05         # module width to remove at sides
ylabel1       = 1.15        # position of module names
ylabel2       = 1.35        # position of class names
mtextsize     = 1.3*textsize_clock #'large' # 1.3*textsize # textsize of module labels
# bars
bpar          = 0.4         # fraction of ymax from center to start with parameter bars
fwb           = [0.7,0.4,0.3]  # width of bars
plwidth       = 0.5
# parameters in centre
bplabel       = 0.1        # fractional distance of ymax of param numbers in centre from 0-line
ptextsize     = textsize_clock/1.3 #'small' # 0.8*textsize # textsize of param numbers in centre
# yaxis
ytextsize     = textsize_clock/1.3 #'small' # 0.8*textsize # textsize of y-axis

import matplotlib as mpl
if (outtype == 'pdf'):
    mpl.use('PDF') # set directly after import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    # Customize: http://matplotlib.sourceforge.net/users/customizing.html
    mpl.rc('ps', papersize='a4', usedistiller='xpdf') # ps2pdf
    mpl.rc('figure', figsize=(8.27,11.69)) # a4 portrait
    if usetex:
        mpl.rc('text', usetex=True)
    else:
        mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
        #mpl.rc('font',**{'family':'serif','serif':['times']})
    mpl.rc('text.latex', unicode=True)
elif (outtype == 'png'):
    mpl.use('TkAgg') # set directly after import matplotlib
    import matplotlib.pyplot as plt
    mpl.rc('figure', figsize=(8.27,11.69)) # a4 portrait
    if usetex:
        mpl.rc('text', usetex=True)
    else:
        mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
        #mpl.rc('font',**{'family':'serif','serif':['times']})
    mpl.rc('text.latex', unicode=True)
    mpl.rc('savefig', dpi=dpi, format='png')
else:
    import matplotlib.pyplot as plt
    mpl.rc('figure', figsize=(4./5.*8.27,4./5.*11.69)) # a4 portrait
mpl.rc('font', size=textsize)
mpl.rc('lines', linewidth=lwidth, color='black')
mpl.rc('axes', linewidth=alwidth, labelcolor='black')
mpl.rc('path', simplify=False) # do not remove

from matplotlib.patches import Rectangle, Circle, Polygon
from mpl_toolkits.basemap import Basemap

# colors
if dobw:
    c = np.linspace(0.2, 0.85, nmod)
    c = np.ones(nmod)*0.7
    c = [ str(i) for i in c ]
    ocean_color = '0.1'
else:
    c = color.get_brewer('dark_rainbow_256', rgb=True)
    c = c[::-1] # reverse colors
    ocean_color = (151/256., 183/256., 224/256.)

cmap = mpl.colors.ListedColormap(c)

# use a colormap from Brewer module
cc        = color.get_brewer('gsdtol', rgb=True)[10:]
cmap_gray = mpl.colors.ListedColormap(cc)

if (True):

    # Latlon
    fname    = inputfile

    ds       = xr.open_dataset(fname)
    lon      = ds['lon'].data        # 1D or 2D field
    lat      = ds['lat'].data        # 1D or 2D field
    var      = ds[variable].data[0]  #       2D field
    product  = ds.attrs['product']

    if (product == 'GDPS' or product == 'GEPS'):
        lon = np.where(lon<0., lon+360., lon)
        lon[:,-1] = 359.999999   # this is a hack

    # first time step as a string in nice format
    timestep = ds['time'].data[0]                              # numpy.datetime64('2017-10-02T18:00:00.000000000')
    timestep = pd.to_datetime(str(timestep))                   # Timestamp('2017-10-02 18:00:00')
    timestep = timestep.strftime('%d %h %Y %H:%M:%S')+' UTC'   # '02 Oct 2017 18:00:00 UTC'

    # some variable properties
    unit      = ds[variable].attrs['units']
    longname  = ds[variable].attrs['long_name'] 

    # 1D lats and lons
    if (len(np.shape(lon)) == 1):
        nlat = lat.shape[0]
        nlon = lon.shape[0]
        lon       = np.array([ lon for ilat in range(nlat) ])
        lon[:,-1] = 359.999999   # this is a hack
        lat = np.transpose(np.array([ lat for ilon in range(nlon) ]))
    elif (len(np.shape(lon)) == 2):
        nlat = lat.shape[0]
        nlon = lon.shape[1]
    else:
        raise ValueError('plot_CASPAR_data: lon and lat has to be either 1D or 2D')
    
    # boundaries between lats and lons
    lonh = np.empty((nlat+1,nlon+1), dtype=np.float)
    lath = np.empty((nlat+1,nlon+1), dtype=np.float)
    dlon = np.diff(lon,axis=1)
    dlat = np.diff(lat,axis=0)
    lonh[0:nlat,0]      = lon[:,0]         - 0.5*dlon[:,0]          # 0
    lonh[0:nlat,1:nlon] = lonh[0:nlat,0:1] + np.cumsum(dlon,axis=1) # 1:nlon+1
    lonh[0:nlat,-1]     = lon[:,-1]        + 0.5*dlon[:,-1]         # nlon
    lonh[nlat,0:nlon+1] = lonh[nlat-1,0:nlon+1]                     # lower corner of box: assign last upper boundary
    lath[0,0:nlon]      = lat[0,:]         - 0.5*dlat[0,:]
    lath[1:nlat,0:nlon] = lath[0:1,0:nlon] + np.cumsum(dlat,axis=0)
    lath[-1,0:nlon]     = lat[-1,:]        + 0.5*dlat[-1,:]
    lath[0:nlat+1,nlon] = lath[0:nlat+1,nlon-1]

    # -------------------------------------------------------------------------
    # Plot
    # -------------------------------------------------------------------------

    if (outtype == 'pdf'):
        print('Plot PDF ', pdffile)
        pdf_pages = PdfPages(pdffile)
    elif (outtype == 'png'):
        print('Plot PNG ', pngbase)
    else:
        print('Plot X')
    # figsize = mpl.rcParams['figure.figsize']

    ifig = 0

    # -------------------------------------------------------------------------
    # Fig 1 :: map with color bar (whole domain)
    # -------------------------------------------------------------------------
    ifig += 1
    iplot = 0
    print('Plot - Fig ', ifig, ' ::  ')
    fig = plt.figure(ifig)

    # -------------------------------------------------------------------------
    # (1a) map:: glb
    # -------------------------------------------------------------------------
    iplot += 1
    sub    = fig.add_axes(position(nrow,ncol,1,hspace=hspace,vspace=vspace) )

    if (product == 'CaPA_coarse'):
        # Polar Stereographic Projection
        map = Basemap(projection='npstere',boundinglat=10,lon_0=270,resolution='c')
        parallels = np.arange(-80,80,20)
        meridians = np.arange(-360,1,40)
    elif (product == 'CaPA_fine'):
        # Polar Stereographic Projection
        map = Basemap(projection='npstere',boundinglat=10,lon_0=270,resolution='c')
        parallels = np.arange(-80,80,20)
        meridians = np.arange(-360,1,40)
    elif (product == 'GDPS'):
        # Miller projection
        map = Basemap(projection='mill',lon_0=180)
        # map = Basemap(projection='npstere',boundinglat=-10,lon_0=270,resolution='c')
        parallels = np.arange(-90,90,30)
        meridians = np.arange(-360,1,60)
    elif (product == 'GEPS'):
        # Miller projection
        map = Basemap(projection='mill',lon_0=180)
        parallels = np.arange(-90,90,30)
        meridians = np.arange(-360,1,60)
    elif (product == 'RDPS'):
        # Polar Stereographic Projection
        map = Basemap(projection='npstere',boundinglat=-10,lon_0=270,resolution='c')
        parallels = np.arange(-80,80,20)
        meridians = np.arange(-360,1,40)
    elif (product == 'REPS'):
        # Polar Stereographic Projection
        map = Basemap(projection='npstere',boundinglat=10,lon_0=270,resolution='c')
        parallels = np.arange(-80,80,20)
        meridians = np.arange(-360,1,40)
    elif (product == 'CaLDAS'):
        # Polar Stereographic Projection
        map = Basemap(projection='npstere',boundinglat=10,lon_0=270,resolution='c')
        parallels = np.arange(-80,80,20)
        meridians = np.arange(-360,1,40)
    elif (product == 'HRDPS'):
        # Polar Stereographic Projection
        map = Basemap(projection='npstere',boundinglat=10,lon_0=270,resolution='c')
        parallels = np.arange(-80,80,20)
        meridians = np.arange(-360,1,40)
    elif (product == ''):
        # Polar Stereographic Projection
        map = Basemap(projection='npstere',boundinglat=10,lon_0=270,resolution='c')
        parallels = np.arange(-80,80,20)
        meridians = np.arange(-360,1,40)
    else:
        raise ValueError('Product not implemented')
    
    # plot coastlines, draw label meridians and parallels.
    # labels = [left, right, top, bottom]
    map.drawcoastlines()
    map.drawparallels(parallels,labels=[1,0,0,0],linewidth=0.5)
    map.drawmeridians(meridians,labels=[0,1,0,1],linewidth=0.5)

    lon_unwrapped = lon

    # geo-referenced
    xx, yy = map(lon_unwrapped,lat)
    zz = var[:,:]  #var[0,:,:]
    variable_plot = map.pcolor(xx, yy, zz, cmap=cmap)

    # set title as time step
    sub.set_title(timestep,fontsize=textsize)

    # abc2plot(sub, dxabc, dyabc, iplot, lower=True, parenthesis='close',
    #          bold=True, large=True,
    #          mathrm=True, usetex=usetex,
    #          horizontalalignment='right', verticalalignment='bottom')

    # -------------------------------------------------------------------------
    # (1b) Colorbar
    # -------------------------------------------------------------------------
    iplot += 1
    sub    = fig.add_axes(position(1,1,1,hspace=hspace,vspace=vspace, left=0.3, right=0.7, top=0.642, bottom=0.632) )

    # minimal value
    var_minval = np.nanmin(var)
    var_maxval = np.nanmax(var)
    cbar = mpl.colorbar.ColorbarBase(sub, norm=mpl.colors.Normalize(vmin=var_minval, vmax=var_maxval), cmap=cmap, orientation='horizontal')
    cbar.set_label(variable+': '+longname+' [$'+str2tex(unit.replace('**','^').replace('-1','{-1}').replace('_','\_'),usetex=usetex)+'$]')
    
    if (outtype == 'pdf'):
        pdf_pages.savefig(fig)
        plt.close(fig)
    elif (outtype == 'png'):
        pngfile = pngbase+"{0:04d}".format(ifig)+".png"
        fig.savefig(pngfile, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
        plt.close(fig)

# -------------------------------------------------------------------------
# Finished
# -------------------------------------------------------------------------

if (outtype == 'pdf'):
    pdf_pages.close()
elif (outtype == 'png'):
    pass
else:
    plt.show()
    
