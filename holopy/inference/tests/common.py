# Copyright 2011-2016, Vinothan N. Manoharan, Thomas G. Dimiduk,
# Rebecca W. Perry, Jerome Fung, and Ryan McGorty, Anna Wang
#
# This file is part of HoloPy.
#
# HoloPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HoloPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HoloPy.  If not, see <http://www.gnu.org/licenses/>.

from holopy.inference import prior
from holopy.inference.model import Model
from holopy.scattering import Sphere

class SimpleModel(Model):
    def __init__(self, x=prior.Uniform(0, 1, name='x')):
        self._parameters = [x]
        self.parameter_name = x.name
        self.constraints = []
        self.noise_sd = 1

    def _residuals(self, pars, data, noise):
        return self.lnposterior(pars, data, None)

    def lnposterior(self, par_vals, data, dummy):
        x = par_vals
        return -((x[self.parameter_name]-data)**2).sum()
