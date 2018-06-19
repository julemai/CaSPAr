#!/usr/bin/env python

__all__ = ['sron_colors', 'sron_colours', 'sron_maps']

def ylorbr(x):
    """ Eq. 1 of sron_colourschemes.pdf """
    r = 1.0 - 0.392*(1.0 + erf((x - 0.869)/ 0.255))
    g = 1.021 - 0.456*(1.0 + erf((x - 0.527)/ 0.376))
    b = 1.0 - 0.493*(1.0 + erf((x - 0.272)/ 0.309))
    return r, g, b

def buylrd(x):
    """ Eq. 2 of sron_colourschemes.pdf """
    r = 0.237 - 2.13*x + 26.92*x**2 - 65.5*x**3 + 63.5*x**4 - 22.36*x**5
    g = ( (0.572 + 1.524*x - 1.811*x**2) / (1.0 - 0.291*x + 0.1574*x**2) )**2
    b = 1.0/(1.579 - 4.03*x + 12.92*x**2 - 31.4*x**3 + 48.6*x**4 - 23.36*x**5)
    return r, g, b

def rainbow(x):
    """ Eq. 3 of sron_colourschemes.pdf """
    r = (0.472 - 0.567*x + 4.05*x*x) / (1.0 + 8.72*x - 19.17*x*x + 14.1*x*x*x)
    g = 0.108932 - 1.22635*x + 27.284*x**2 - 98.577*x**3 + 163.3*x**4 - 131.395*x**5 + 40.634*x**6
    b = 1.0 / (1.97 + 3.54*x - 68.5*x**2 + 243.*x**3 - 297.*x**4 + 125.*x**5)
    return r, g, b

palette1        = [['#4477AA'],
                   ['#4477AA', '#CC6677'],
                   ['#4477AA', '#DDCC77', '#CC6677'],
                   ['#4477AA', '#117733', '#DDCC77', '#CC6677'],
                   ['#332288', '#88CCEE', '#117733', '#DDCC77', '#CC6677'],
                   ['#332288', '#88CCEE', '#117733', '#DDCC77', '#CC6677', '#AA4499'],
                   ['#332288', '#88CCEE', '#44AA99', '#117733', '#DDCC77', '#CC6677', '#AA4499'],
                   ['#332288', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77', '#CC6677',
                    '#AA4499'],
                   ['#332288', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77', '#CC6677',
                    '#882255', '#AA4499'],
                   ['#332288', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77', '#661100',
                    '#CC6677', '#882255', '#AA4499'],
                   ['#332288', '#6699CC', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77',
                    '#661100', '#CC6677', '#882255', '#AA4499'],
                   ['#332288', '#6699CC', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77',
                    '#661100', '#CC6677', '#AA4466', '#882255', '#AA4499']]
palette2_light  = ['#77AADD', '#77CCCC', '#88CCAA', '#DDDD77', '#DDAA77', '#DD7788', '#CC99BB']
palette2_medium = ['#4477AA', '#44AAAA', '#44AA77', '#AAAA44', '#AA7744', '#AA4455', '#AA4488']
palette2_dark   = ['#114477', '#117777', '#117744', '#777711', '#774411', '#771122', '#771155']
greysafe        = ['#809BC8', '#FF6666', '#FFCC66', '#64C204']
palette_ylorbr  = [['#FFF7BC', '#FEC44F', '#D95F0E'],
                   ['#FFFBD5', '#FED98E', '#FB9A29', '#CC4C02'],
                   ['#FFFBD5', '#FED98E', '#FB9A29', '#D95F0E', '#993404'],
                   ['#FFFBD5', '#FEE391', '#FEC44F', '#FB9A29', '#D95F0E', '#993404'],
                   ['#FFFBD5', '#FEE391', '#FEC44F', '#FB9A29', '#EC7014', '#CC4C02', '#8C2D04'],
                   ['#FFFFE5', '#FFF7BC', '#FEE391', '#FEC44F', '#FB9A29', '#EC7014', '#CC4C02',
                    '#8C2D04'],
                   ['#FFFFE5', '#FFF7BC', '#FEE391', '#FEC44F', '#FB9A29', '#EC7014', '#CC4C02',
                    '#993404', '#662506']]
palette_buylrd  = [['#99C7EC', '#FFFAD2', '#F5A275'],
                   ['#008BCE', '#B4DDF7', '#F9BD7E', '#D03232'],
                   ['#008BCE', '#B4DDF7', '#FFFAD2', '#F9BD7E', '#D03232'],
                   ['#3A89C9', '#99C7EC', '#E6F5FE', '#FFE3AA', '#F5A275', '#D24D3E'],
                   ['#3A89C9', '#99C7EC', '#E6F5FE', '#FFFAD2', '#FFE3AA', '#F5A275', '#D24D3E'],
                   ['#3A89C9', '#77B7E5', '#B4DDF7', '#E6F5FE', '#FFE3AA', '#F9BD7E', '#ED875E',
                    '#D24D3E'],
                   ['#3A89C9', '#77B7E5', '#B4DDF7', '#E6F5FE', '#FFFAD2', '#FFE3AA', '#F9BD7E',
                    '#ED875E', '#D24D3E'],
                   ['#3D52A1', '#3A89C9', '#77B7E5', '#B4DDF7', '#E6F5FE', '#FFE3AA', '#F9BD7E',
                    '#ED875E', '#D24D3E', '#AE1C3E'],
                   ['#3D52A1', '#3A89C9', '#77B7E5', '#B4DDF7', '#E6F5FE', '#FFFAD2', '#FFE3AA',
                    '#F9BD7E', '#ED875E', '#D24D3E', '#AE1C3E']]
palette_rainbow = [['#404096', '#57A3AD', '#DEA73A', '#D92120'],
                   ['#404096', '#529DB7', '#7DB874', '#E39C37', '#D92120'],
                   ['#404096', '#498CC2', '#63AD99', '#BEBC48', '#E68B33', '#D92120'],
                   ['#781C81', '#3F60AE', '#539EB6', '#6DB388', '#CAB843', '#E78532', '#D92120'],
                   ['#781C81', '#3F56A7', '#4B91C0', '#5FAA9F', '#91BD61', '#D8AF3D', '#E77C30',
                    '#D92120'],
                   ['#781C81', '#3F4EA1', '#4683C1', '#57A3AD', '#6DB388', '#B1BE4E', '#DFA53A',
                    '#E7742F', '#D92120'],
                   ['#781C81', '#3F479B', '#4277BD', '#529DB7', '#62AC9B', '#86BB6A', '#C7B944',
                    '#E39C37', '#E76D2E', '#D92120'],
                   ['#781C81', '#404096', '#416CB7', '#4D95BE', '#5BA7A7', '#6EB387', '#A1BE56',
                    '#D3B33F', '#E59435', '#E6682D', '#D92120'],
                   ['#781C81', '#413B93', '#4065B1', '#488BC2', '#55A1B1', '#63AD99', '#7FB972',
                    '#B5BD4C', '#D9AD3C', '#E68E34', '#E6642C', '#D92120']]
                                                                    
palette_rainbow_band = [['#882E72', '#B178A6', '#D6C1DE', '#1965B0', '#5289C7', '#7BAFDE', '#4EB265',
                         '#90C987', '#CAE0AB', '#F7EE55', '#F6C141', '#F1932D', '#E8601C', '#DC050C'],
                        ['#114477', '#4477AA', '#77AADD', '#117755', '#44AA88', '#99CCBB', '#777711',
                         '#AAAA44', '#DDDD77', '#771111', '#AA4444', '#DD7777', '#771144', '#AA4477',
                         '#DD77AA'],
                        ['#771155', '#AA4488', '#CC99BB', '#114477', '#4477AA', '#77AADD', '#117777',
                         '#44AAAA', '#77CCCC', '#777711', '#AAAA44', '#DDDD77', '#774411', '#AA7744',
                         '#DDAA77', '#771122', '#AA4455', '#DD7788'],
                        ['#771155', '#AA4488', '#CC99BB', '#114477', '#4477AA', '#77AADD', '#117777',
                         '#44AAAA', '#77CCCC', '#117744', '#44AA77', '#88CCAA', '#777711', '#AAAA44',
                         '#DDDD77', '#774411', '#AA7744', '#DDAA77', '#771122', '#AA4455', '#DD7788']]

def sron_colors(cmap='palette1', ncol=9, cname=None, rgb=False, rgb256=False, reverse=False):
    """
        Distinct colour palettes of Paul Tol at SRON - Netherlands Institute for Space Research


        Definition
        ----------
        def sron_colors(cmap='palette1', ncol=9, cname=None, rgb=False, rgb256=False, reverse=False):


        Input
        -----
        None

        
        Optional Input
        --------------
        cmap       Colour palette name
                   palette1:        1-12 colours; orignal palette is ncol=9
                   palette2:        more regular hue and saturation (21 colours)
                   palette2-light:  7 light colours of palette2
                   palette2-medium: 7 medium colours of palette2
                   palette2-dark:   7 darker colours of palette2
                   gray / grey:     4 colours optimized for printing in grey scale
                   ylorbr           3-9 colours from sron_maps('ylorbr')
                   buylrd           3-11 colours from sron_maps('buylrd')
                   rainbow          4-12 colours from sron_maps('rainbow')
                   banded-rainbow   14, 15, 18, 21 banded rainbow schemes 
        ncol       number of desired colors if palette1 (1-12)
        cname      if given, name of registered colormap
        rgb        if True, return RGB value tuple between 0 and 1
        rgb256     if True, return RGB value tuple between 0 and 255
        reverse    if True, reverse colormap


        Output
        ------
        matplotlip listed colormap of ncol colours


        Restrictions
        ------------
        None
        

        Examples
        --------
        >>> print(sron_colors('palette1', 3, rgb256=True))
        [(68, 119, 170), (221, 204, 119), (204, 102, 119)]

        >>> print(sron_colors('palette2-light', rgb256=True)[0])
        (119, 170, 221)

        >>> print(sron_colors('ylorbr', 4, rgb256=True, reverse=True)[0])
        (204, 76, 2)


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

        Copyright 2016 Matthias Cuntz


        History
        -------
        Written,  MC, May 2016
    """
    from color import hex2rgb01
    
    if cmap.lower() == 'palette1':
        assert (ncol>0) and (ncol<13), 'palette1 has 1-12 colours.'
        cols = []
        for i in palette1[ncol-1]:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'palette2':
        cols = []
        for i in range(7):
            cols.append(tuple(hex2rgb01(palette2_light[i])))
            cols.append(tuple(hex2rgb01(palette2_medium[i])))
            cols.append(tuple(hex2rgb01(palette2_dark[i])))
    elif cmap.lower() == 'palette2-light':
        cols = []
        for i in palette2_light:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'palette2-medium':
        cols = []
        for i in palette2_medium:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'palette2-dark':
        cols = []
        for i in palette2_dark:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'grey' or cmap.lower() == 'gray':
        cols = []
        for i in greysafe:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'ylorbr':
        assert (ncol>2) and (ncol<10), 'ylorbr has 3-9 colours.'
        cols = []
        for i in palette_ylorbr[ncol-3]:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'buylrd':
        assert (ncol>2) and (ncol<12), 'buylrd has 3-11 colours.'
        cols = []
        for i in palette_buylrd[ncol-3]:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'rainbow':
        assert (ncol>3) and (ncol<13), 'rainbow has 4-12 colours.'
        cols = []
        for i in palette_rainbow[ncol-4]:
            cols.append(tuple(hex2rgb01(i)))
    elif cmap.lower() == 'banded-rainbow':
        if ncol==14:
            psel = palette_rainbow_band[0]
        elif ncol==15:
            psel = palette_rainbow_band[1]
        elif ncol==18:
            psel = palette_rainbow_band[2]
        elif ncol==21:
            psel = palette_rainbow_band[3]
        else:
            raise ValueError('banded-rainbow palette has 14, 15, 18, or 21 colours.')
        cols = []
        for i in psel:
            cols.append(tuple(hex2rgb01(i)))
    else:
        raise ValueError('Colour palette not known: '+cmap)
            
    if reverse: cols = cols[::-1]
        
    if (not rgb) and (not rgb256):
        from matplotlib.colors import ListedColormap
        ccmap = ListedColormap(cols)
        if cname:
            from matplotlib.cm import register_cmap, get_cmap
            register_cmap(cname, ccmap)
            return get_cmap(cname)
        else:
            return ccmap
    else:
        if rgb256:
            from color import rgb012rgb
            return [ rgb012rgb(*i) for i in cols ]
        else:
            return cols


def sron_colours(*args, **kwargs):
    """
        Wrapper for sron_colors
        def sron_colors(cmap='palette1', ncol=9, cname=None, rgb=False, rgb256=False, reverse=False):
    """
    return sron_colors(*args, **kwargs)


def sron_maps(cmap, ncol=256, offset=0, upper=1,
              cname=None, rgb=False, rgb256=False, reverse=False, grey=False, gray=False):
    """
        Colour maps of Paul Tol at SRON - Netherlands Institute for Space Research


        Definition
        ----------
        def sron_maps(cmap, ncol=256, offset=0, upper=1,
                      cname=None, rgb=False, rgb256=False, reverse=False, grey=False, gray=False):


        Input
        -----
        cmap       Colour map name
                   buylrd:  blue-yellow-red diverging
                   rainbow: rainbow
                   ylorbr:  yellow-orange-red sequential
        

        Optional Input
        --------------
        ncol       number of desired colors
        offset     bottom fraction to exclude (0-1)
        upper      upper most fraction included (0-1)
        cname      if given, name of registered colormap
        rgb        if True, return RGB value tuple between 0 and 1
        rgb256     if True, return RGB value tuple between 0 and 255
        reverse    if True, reverse colormap
        grey       if True, return grey equivalent
        gray       same as grey


        Output
        ------
        matplotlip listed colormap of ncol colours


        Restrictions
        ------------
        None
        

        Examples
        --------
        cmap = sron_maps('rainbow', 256)
        
        cc = sron_maps('buylrd', 11, rgb=True)


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

        Copyright 2016 Matthias Cuntz


        History
        -------
        Written,  MC, May 2016
    """
    if cmap == 'ylorbr':
        from scipy.special import erf

    cols = []
    for i in range(ncol):
        x = offset + float(i)/float(ncol-1) * (upper-offset)
        if cmap == 'buylrd':
            cols.append(tuple(buylrd(x)))
        elif cmap == 'rainbow':
            cols.append(tuple(rainbow(x)))
        elif cmap == 'ylorbr':
            cols.append(tuple(ylorbr(x)))
        else:
            raise ValueError('Colour map not known: '+cmap)
            
    if reverse: cols = cols[::-1]

    if grey or gray:
        for i, cc in enumerate(cols):
            isgray = 0.2125*cc[0] + 0.7154*cc[1] + 0.072*cc[2]
            cols[i] = (isgray,isgray,isgray)
        
    if (not rgb) and (not rgb256):
        from matplotlib.colors import ListedColormap
        ccmap = ListedColormap(cols)
        if cname:
            from matplotlib.cm import register_cmap, get_cmap
            register_cmap(cname, ccmap)
            return get_cmap(cname)
        else:
            return ccmap
    else:
        if rgb256:
            from color import rgb012rgb
            return [ rgb012rgb(*i) for i in cols ]
        else:
            return cols

        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
