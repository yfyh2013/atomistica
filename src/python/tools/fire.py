# ======================================================================
# Atomistica - Interatomic potential library
# https://github.com/pastewka/atomistica
# Lars Pastewka, lars.pastewka@iwm.fraunhofer.de, and others.
# See the AUTHORS file in the top-level Atomistica directory.
#
# Copyright (2005-2013) Fraunhofer IWM
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ======================================================================

#! /usr/bin/env python

import sys

import numpy as np

from ase.io import write
from ase.optimize import FIRE
from mdcore.io import read

import mdcore

###

# Default parameters
potstr = 'Tersoff'
fmax = 1e-3
outfn = 'fire.traj'

###

import getopt
optlist, args = getopt.getopt(sys.argv[1:], '',
                              [ 'pot=', 'fmax=', 'outfn=' ])

assert len(args) == 1
infn = args[0]
for key, value in optlist:
    if key == '--pot':
        potstr = value
    elif key == '--fmax':
        fmax = float(value)
    elif key == '--outfn':
        outfn = value

###

print '# infn = ', infn
print '# outfn = ', outfn
print '# pot = ', potstr
print '# fmax = ', fmax

###

a = read(infn)

print '{0} atoms.'.format(len(a))

potclass = getattr(mdcore, potstr)
a.set_calculator(potclass())

FIRE(a).run(fmax=fmax)

write(outfn, a)