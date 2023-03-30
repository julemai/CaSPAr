# The Canadian Surface Prediction Archive (CaSPAr): A Platform to Enhance Environmental Modeling in Canada and Globally
*by Juliane Mai, Kurt C. Kornelsen, Bryan A. Tolson, Vincent Fortin, Nicolas Gasset and Djamel Bouhemhem, David Schäfer, Michael Leahy, François Anctil, and Paulin Coulibaly*

Please find the French version of this README [here](README_fr.md). 
Veuillez trouver la version française de ce README [ici](README_fr.md).

## Abstract
The Canadian Surface Prediction Archive (CaSPAr) is an archive of numerical weather predictions issued by Environment and Climate Change Canada. Amongst the products archived on a daily basis are five operational numerical weather forecasts, three operational analyses, and one reanalysis product. The products have an hourly to daily temporal and 2.5 km to 50 km spatial resolution. To date, September 2019, the archive contains 394 TB of data while 368 GB of new data are added every night (status: Feb 2020). The data is archived in CF-1.6 compliant NetCDF4 format. The archive is available [online](https://caspar-data.ca) since June 2017 and allows users to precisely request data according to their needs, i.e. spatial cropping based on a standard shape or uploaded shapefile of the domain of interest, selection of forecast horizons, variables as well as issue dates. The degree of customization in CaSPAr is a unique feature relative to other publically accessible numerical weather prediction archives and it minimizes user download requirements and local processing time. We benchmark the processing time and required storage of such requests based on 216 test scenarios. We also demonstrate how CaSPAr data can be employed to analyze extreme rainfall events. CaSPAr provides access to data that is fundamental for evaluating numerical weather prediction models and demonstrating the improvement in products such as flood and energy demand forecasting systems. 

## Overview
This documentation is designed to be a living technical document with relation to the development of the CaSPAr archive and web-portal. This documentation will grow over time and include methods to download access and make use of CaSPAr Data sets.

We encourage all users to fork and share their codes.

Helpful pages:
* [How to get started and download your first data](https://github.com/julemai/CaSPAr/wiki/How-to-get-started-and-download-your-first-data)
* [Available products](https://github.com/julemai/CaSPAr/wiki/Available-products)
* [CaSPAr file naming convention and variables](https://github.com/julemai/CaSPAr/wiki/CaSPAr-file-naming-convention-and-variables)
* [Introduction of Reading and Writing NetCDF files](https://github.com/julemai/CaSPAr/wiki/Introduction-of-Reading-and-Writing-NetCDF-files)
* [Pre- and Postprocessing scripts](https://github.com/julemai/CaSPAr/tree/master/utility_scripts)

## Citation
Mai et al. (2020).<br>
The Canadian Surface Prediction Archive (CaSPAr): A Platform to Enhance Environmental Modeling in Canada and Globally.<br>
*Bulletin of the American Meteorological Society*, https://doi.org/10.1175/BAMS-D-19-0143.1.

