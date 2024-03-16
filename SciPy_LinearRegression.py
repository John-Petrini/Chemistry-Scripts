"""Abstracts computation and encapsulates regression statistics
Intended to modularize SciPy data processing"""

import numpy as np
from scipy import stats

class LinearDataModel:
    def __init__(self, x_var, y_var):
        self.x_var = x_var
        self.y_var = y_var
        self._inputValidation()
        self._processInputs()
        
    def _inputValidation(self):
        if not isinstance(self.x_var, (list, np.ndarray)): # checks input against type: (list, n-dimensional array)
            raise TypeError('x_var is not list or numpy array')
        if not isinstance(self.y_var, (list, np.ndarray)):
            raise TypeError('y_var is not list or numpy array')
        if len(self.y_var) != len(self.x_var):
            raise valueError('input data of inequal size')
    
    def _processInputs(self): # computing regression statistics
        self.slope, self.intercept, self.r_value, self.p_value, self.std_error = stats.linregress(self.x_var, self.y_var)

    def getStats(self): # returns dictionary of elements
        return {
            'slope': self.slope,
            'intercept': self.intercept,
            'r_value': self.r_value,
            'p_value': self.p_value,
            'std_error': self.std_error
        }
