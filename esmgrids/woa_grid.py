
from __future__ import print_function

import numpy as np
import netCDF4 as nc
from .base_grid import BaseGrid

class WoaGrid(BaseGrid):

    def __init__(self, grid_def,mask_file=None):

        with nc.Dataset(grid_def) as f:
            x_t = f.variables['lon'][:]
            y_t = f.variables['lat'][:]
            if 'depth' in f.variables:
                depth = f.variables['depth'][:]
            else:
                depth = None
            if 't_an' in f.variables:
                mask = f.variables['t_an'][0, :, :, :].mask
            else:
                mask = None

        if depth is not None:
            super(WoaGrid, self).__init__(x_t=x_t, y_t=y_t, mask_t=mask, levels=depth,
                                          description='WOA 1 degree grid')
        else:
            super(WoaGrid, self).__init__(x_t=x_t, y_t=y_t, mask_t=mask, description='WOA 1 degree grid')
