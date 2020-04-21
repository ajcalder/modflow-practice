# -*- coding: utf-8 -*-
"""
Preliminary Cosumnes Model Spin up
Michigan Bar to lower Rooney Ranch
Created on Thu Apr  2 17:59:11 2020

@author: Andrew
"""

import numpy as np
import flowpy.modflow as fpmf

# Define model extent, grid resolution and characteristics
# length of meters and time of seconds or minutes?
Lx = 14350. 
Ly = 7,608.
ztop = 10.
zbot = -50.
nlay = 1
nrow = 10 
ncol = 10
delr = Lx/ncol 
delc = Ly/ncol
delv = (ztop-zbot)/nlay
botm = np.linspace(ztop, zbot, nlay+1)
hk = 1.
vka = 1.
sy = 0.1
ss = 1.e-4
laytyp = 1
