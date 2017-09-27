#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('..')
from keplerOrbit import KeplerOrbit


plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
#plt.figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k')
#plt.figure(num=None, figsize=(6, 6), dpi=80, edgecolor='k')

pbinary      = 111.100000  #// Orbital period (days)
pbdot        = 0.000000    #// Derivative of Orbital period (days/days)
#epoch_type   = P   // P=Periaston epoch, T=epoch of l=M+omega=Pi/2
epoch        = 2453613.500000  #// Epoch (JD)
axsini       = 267.000000  #// Projected semimajor axis (light-sec)
periapse     = 130.000000  #// Argument of periapse (deg)
apsidalrate  = 0.000000  #// Rate of change of arg. of periapse (deg/year)
eccentricity = 0.470000  #// Eccentricity
#egress       = 0.000000  // Binary phase at end of eclipse (cycles)
#ingress      = 1.000000  // Binary phase at begining of eclipse (cycle)

Omega=0.0
incl =90.0

mjd0_JD = 2400000.5 
if mjd0_JD < epoch :
    epoch_mjd = epoch - mjd0_JD
else :
    epoch_mjd = epoch 

#epoch_mjd = binaryepoch - 2400000.5

Omega=0.0
incl =90.0

ko = KeplerOrbit()
ko.setOrbitalElements(axsini, pbinary, eccentricity, epoch_mjd, Omega, periapse, incl);

mjd_start = 55050
mjd_end   = 56000
mjd_step  = 1


vmjd = np.arange(mjd_start, mjd_end, mjd_step)
nv = len(vmjd)
vdplr = np.zeros(nv)
for idx in range(nv) :
    mjd = vmjd[idx]
    #dplr = ko.getDopplerFactor(mjd)
    dplr = ko.getDopplerFactor(mjd)-1
    vdplr[idx] = dplr

plt.plot(vmjd, vdplr)
#plt.axes().set_aspect('equal', 'datalim')

plt.show()

