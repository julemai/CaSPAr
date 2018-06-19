#!/usr/bin/env python
"""
    Python port of colors of chroma.js: https://github.com/gka/chroma.js
    a JavaScript library for color conversions:
    Copyright (c) 2011-2013, Gregor Aisch.

    It includes colors from colorbrewer2.org:
    Copyright (c) 2002 Cynthia Brewer, Mark Harrower,
    and The Pennsylvania State University.

    And named colors taken from X11 Color Names
    http://www.w3.org/TR/css3-color/#svg-color


    Example
    -------
    >>> import color
    >>> print(color.chroma_brewer['OrRd'])
    ['#fff7ec', '#fee8c8', '#fdd49e', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#b30000', '#7f0000']

    >>> print(color.chroma_x11['indigo'])
    #4b0082


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


    Colorbrewer License
    -------------------
    Copyright (c) 2002 Cynthia Brewer, Mark Harrower, 
    and The Pennsylvania State University.

    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at	
    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, 
    software distributed under the License is distributed on an 
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
    either express or implied. See the License for the specific 
    language governing permissions and limitations under the License.


    X11 Information
    ---------------
    Named colors are taken from X11 Color Names.
    http://www.w3.org/TR/css3-color/#svg-color

    
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

__all__ = ['chroma_brewer', 'chroma_x11']

# -------------------------------------------------------------------------------------------------

# http://colorbrewer2.org
chroma_brewer = {
    'OrRd': ['#fff7ec', '#fee8c8', '#fdd49e', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#b30000', '#7f0000'],
    'PuBu': ['#fff7fb', '#ece7f2', '#d0d1e6', '#a6bddb', '#74a9cf', '#3690c0', '#0570b0', '#045a8d', '#023858'],
    'BuPu': ['#f7fcfd', '#e0ecf4', '#bfd3e6', '#9ebcda', '#8c96c6', '#8c6bb1', '#88419d', '#810f7c', '#4d004b'],
    'Oranges': ['#fff5eb', '#fee6ce', '#fdd0a2', '#fdae6b', '#fd8d3c', '#f16913', '#d94801', '#a63603', '#7f2704'],
    'BuGn': ['#f7fcfd', '#e5f5f9', '#ccece6', '#99d8c9', '#66c2a4', '#41ae76', '#238b45', '#006d2c', '#00441b'],
    'YlOrBr': ['#ffffe5', '#fff7bc', '#fee391', '#fec44f', '#fe9929', '#ec7014', '#cc4c02', '#993404', '#662506'],
    'YlGn': ['#ffffe5', '#f7fcb9', '#d9f0a3', '#addd8e', '#78c679', '#41ab5d', '#238443', '#006837', '#004529'],
    'Reds': ['#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d', '#a50f15', '#67000d'],
    'RdPu': ['#fff7f3', '#fde0dd', '#fcc5c0', '#fa9fb5', '#f768a1', '#dd3497', '#ae017e', '#7a0177', '#49006a'],
    'Greens': ['#f7fcf5', '#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#006d2c', '#00441b'],
    'YlGnBu': ['#ffffd9', '#edf8b1', '#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8', '#253494', '#081d58'],
    'Purples': ['#fcfbfd', '#efedf5', '#dadaeb', '#bcbddc', '#9e9ac8', '#807dba', '#6a51a3', '#54278f', '#3f007d'],
    'GnBu': ['#f7fcf0', '#e0f3db', '#ccebc5', '#a8ddb5', '#7bccc4', '#4eb3d3', '#2b8cbe', '#0868ac', '#084081'],
    'Greys': ['#ffffff', '#f0f0f0', '#d9d9d9', '#bdbdbd', '#969696', '#737373', '#525252', '#252525', '#000000'],
    'YlOrRd': ['#ffffcc', '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', '#bd0026', '#800026'],
    'PuRd': ['#f7f4f9', '#e7e1ef', '#d4b9da', '#c994c7', '#df65b0', '#e7298a', '#ce1256', '#980043', '#67001f'],
    'Blues': ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b'],
    'PuBuGn': ['#fff7fb', '#ece2f0', '#d0d1e6', '#a6bddb', '#67a9cf', '#3690c0', '#02818a', '#016c59', '#014636'],
    'Spectral': ['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2'],
    'RdYlGn': ['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850', '#006837'],
    'RdBu': ['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#f7f7f7', '#d1e5f0', '#92c5de', '#4393c3', '#2166ac', '#053061'],
    'PiYG': ['#8e0152', '#c51b7d', '#de77ae', '#f1b6da', '#fde0ef', '#f7f7f7', '#e6f5d0', '#b8e186', '#7fbc41', '#4d9221', '#276419'],
    'PRGn': ['#40004b', '#762a83', '#9970ab', '#c2a5cf', '#e7d4e8', '#f7f7f7', '#d9f0d3', '#a6dba0', '#5aae61', '#1b7837', '#00441b'],
    'RdYlBu': ['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4', '#313695'],
    'BrBG': ['#543005', '#8c510a', '#bf812d', '#dfc27d', '#f6e8c3', '#f5f5f5', '#c7eae5', '#80cdc1', '#35978f', '#01665e', '#003c30'],
    'RdGy': ['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#ffffff', '#e0e0e0', '#bababa', '#878787', '#4d4d4d', '#1a1a1a'],
    'PuOr': ['#7f3b08', '#b35806', '#e08214', '#fdb863', '#fee0b6', '#f7f7f7', '#d8daeb', '#b2abd2', '#8073ac', '#542788', '#2d004b'],
    'Set2': ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3'],
    'Accent': ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666'],
    'Set1': ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999'],
    'Set3': ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f'],
    'Dark2': ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666'],
    'Paired': ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928'],
    'Pastel2': ['#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9', '#fff2ae', '#f1e2cc', '#cccccc'],
    'Pastel1': ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc', '#e5d8bd', '#fddaec', '#f2f2f2']
    }

# -------------------------------------------------------------------------------------------------

# http://www.w3.org/TR/css3-color/#svg-color
chroma_x11 = {
    'indigo': "#4b0082",
    'gold': "#ffd700",
    'hotpink': "#ff69b4",
    'firebrick': "#b22222",
    'indianred': "#cd5c5c",
    'yellow': "#ffff00",
    'mistyrose': "#ffe4e1",
    'darkolivegreen': "#556b2f",
    'olive': "#808000",
    'darkseagreen': "#8fbc8f",
    'pink': "#ffc0cb",
    'tomato': "#ff6347",
    'lightcoral': "#f08080",
    'orangered': "#ff4500",
    'navajowhite': "#ffdead",
    'lime': "#00ff00",
    'palegreen': "#98fb98",
    'darkslategrey': "#2f4f4f",
    'greenyellow': "#adff2f",
    'burlywood': "#deb887",
    'seashell': "#fff5ee",
    'mediumspringgreen': "#00fa9a",
    'fuchsia': "#ff00ff",
    'papayawhip': "#ffefd5",
    'blanchedalmond': "#ffebcd",
    'chartreuse': "#7fff00",
    'dimgray': "#696969",
    'black': "#000000",
    'peachpuff': "#ffdab9",
    'springgreen': "#00ff7f",
    'aquamarine': "#7fffd4",
    'white': "#ffffff",
    'orange': "#ffa500",
    'lightsalmon': "#ffa07a",
    'darkslategray': "#2f4f4f",
    'brown': "#a52a2a",
    'ivory': "#fffff0",
    'dodgerblue': "#1e90ff",
    'peru': "#cd853f",
    'lawngreen': "#7cfc00",
    'chocolate': "#d2691e",
    'crimson': "#dc143c",
    'forestgreen': "#228b22",
    'darkgrey': "#a9a9a9",
    'lightseagreen': "#20b2aa",
    'cyan': "#00ffff",
    'mintcream': "#f5fffa",
    'silver': "#c0c0c0",
    'antiquewhite': "#faebd7",
    'mediumorchid': "#ba55d3",
    'skyblue': "#87ceeb",
    'gray': "#808080",
    'darkturquoise': "#00ced1",
    'goldenrod': "#daa520",
    'darkgreen': "#006400",
    'floralwhite': "#fffaf0",
    'darkviolet': "#9400d3",
    'darkgray': "#a9a9a9",
    'moccasin': "#ffe4b5",
    'saddlebrown': "#8b4513",
    'grey': "#808080",
    'darkslateblue': "#483d8b",
    'lightskyblue': "#87cefa",
    'lightpink': "#ffb6c1",
    'mediumvioletred': "#c71585",
    'slategrey': "#708090",
    'red': "#ff0000",
    'deeppink': "#ff1493",
    'limegreen': "#32cd32",
    'darkmagenta': "#8b008b",
    'palegoldenrod': "#eee8aa",
    'plum': "#dda0dd",
    'turquoise': "#40e0d0",
    'lightgrey': "#d3d3d3",
    'lightgoldenrodyellow': "#fafad2",
    'darkgoldenrod': "#b8860b",
    'lavender': "#e6e6fa",
    'maroon': "#800000",
    'yellowgreen': "#9acd32",
    'sandybrown': "#f4a460",
    'thistle': "#d8bfd8",
    'violet': "#ee82ee",
    'navy': "#000080",
    'magenta': "#ff00ff",
    'dimgrey': "#696969",
    'tan': "#d2b48c",
    'rosybrown': "#bc8f8f",
    'olivedrab': "#6b8e23",
    'blue': "#0000ff",
    'lightblue': "#add8e6",
    'ghostwhite': "#f8f8ff",
    'honeydew': "#f0fff0",
    'cornflowerblue': "#6495ed",
    'slateblue': "#6a5acd",
    'linen': "#faf0e6",
    'darkblue': "#00008b",
    'powderblue': "#b0e0e6",
    'seagreen': "#2e8b57",
    'darkkhaki': "#bdb76b",
    'snow': "#fffafa",
    'sienna': "#a0522d",
    'mediumblue': "#0000cd",
    'royalblue': "#4169e1",
    'lightcyan': "#e0ffff",
    'green': "#008000",
    'mediumpurple': "#9370db",
    'midnightblue': "#191970",
    'cornsilk': "#fff8dc",
    'paleturquoise': "#afeeee",
    'bisque': "#ffe4c4",
    'slategray': "#708090",
    'darkcyan': "#008b8b",
    'khaki': "#f0e68c",
    'wheat': "#f5deb3",
    'teal': "#008080",
    'darkorchid': "#9932cc",
    'deepskyblue': "#00bfff",
    'salmon': "#fa8072",
    'darkred': "#8b0000",
    'steelblue': "#4682b4",
    'palevioletred': "#db7093",
    'lightslategray': "#778899",
    'aliceblue': "#f0f8ff",
    'lightslategrey': "#778899",
    'lightgreen': "#90ee90",
    'orchid': "#da70d6",
    'gainsboro': "#dcdcdc",
    'mediumseagreen': "#3cb371",
    'lightgray': "#d3d3d3",
    'mediumturquoise': "#48d1cc",
    'lemonchiffon': "#fffacd",
    'cadetblue': "#5f9ea0",
    'lightyellow': "#ffffe0",
    'lavenderblush': "#fff0f5",
    'coral': "#ff7f50",
    'purple': "#800080",
    'aqua': "#00ffff",
    'whitesmoke': "#f5f5f5",
    'mediumslateblue': "#7b68ee",
    'darkorange': "#ff8c00",
    'mediumaquamarine': "#66cdaa",
    'darksalmon': "#e9967a",
    'beige': "#f5f5dc",
    'blueviolet': "#8a2be2",
    'azure': "#f0ffff",
    'lightsteelblue': "#b0c4de",
    'oldlace': "#fdf5e6"
    }

# -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    # import numpy as np

    # import matplotlib as mpl
    # from matplotlib.pylab import *
    # fig = figure(figsize=(8,6))
    # # ax1 = fig.add_axes([0.05, 0.85, 0.9, 0.10])
    # # ax2 = fig.add_axes([0.05, 0.70, 0.9, 0.10])
    # # ax3 = fig.add_axes([0.05, 0.55, 0.9, 0.10])
    # ax4 = fig.add_axes([0.05, 0.40, 0.9, 0.10])
    # # ax5 = fig.add_axes([0.05, 0.25, 0.9, 0.10])
    # # ax6 = fig.add_axes([0.05, 0.10, 0.9, 0.10])

    # cc     = chroma_brewer['Oranges']
    # cmap   = mpl.colors.ListedColormap(cc)
    # norm   = mpl.colors.BoundaryNorm(np.arange(cmap.N+1), cmap.N)
    # cb     = mpl.colorbar.ColorbarBase(ax4, cmap=cmap, norm=norm, orientation='horizontal')

    # show()
