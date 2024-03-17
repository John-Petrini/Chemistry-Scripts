"""Module for power law fitting of data"""

import numpy as np 
from scipy.optimize import curve_fit

class PowerLawModel:
    def __init__(self, x_var, y_var):
        self.x_var = x_var
        self.y_var = y_var
        self._inputValidation()
        self._processInputs()
        
    def _inputValidation(self):
        if not isinstance(self.x_var, (list, np.ndarray)):
            raise TypeError('x_var is not list or numpy array')
        if not isinstance(self.y_var, (list, np.ndarray)):
            raise TypeError('y_var is not list or numpy array')
        if len(self.x_var) != len(self.y_var):
            raise ValueError('input data of inequal size')
        
    def _processInputs(self):
        self.popt, self.pcov = curve_fit(self._power_function, self.x_var, self.y_var)

        """popt is list of values for [exponent, scalar]
        pcov is list of lists for [variance, covariance] of [exponent, scalar]"""
        
        
    def _power_function(self, x, a, b):
        return a * np.power(x, b)
    
    def getStats(self):
        variance_list = self.pcov[0] # variances for  [exponent, scalar]
        covariance_list = self.pcov[1] # covarianves for [exponent, scalar]
        
        return {
            'exponent': self.popt[0],
            'exponent_variance': variance_list[0],
            'exponent_covariance': covariance_list[0],
            'scalar': self.popt[1],
            'scalar_variance': variance_list[1],
            'scalar_covcariance': covariance_list[1]
        }
