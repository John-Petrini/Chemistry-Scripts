"""Abstracts computation and encapsulates regression statistics
Intended to modularize NP data processing"""

import numpy as np
class PolynomialDataModel:
    def __init__(self, x_var, y_var, order=None):
        self.x_var = x_var
        self.y_var = y_var
        self.order = order
        self._inputValidation()
        self._processInputs()
        
    def _inputValidation(self):
        if not isinstance(self.x_var, (list, np.ndarray)): # checks input against type: (list, n-dimensional array)
            raise TypeError('x_var is not list or numpy array')
        if not isinstance(self.y_var, (list, np.ndarray)):
            raise TypeError('y_var is not list or numpy array')
        if len(self.y_var) != len(self.x_var):
            raise valueError('input data of inequal size')
        if self.order == 0 or self.order is None or not isinstance(self.order, int):
            self.order = 2
            print('default power of 2 utilized')
            
    def _processInputs(self):
        self.poly_model = np.polyfit(self.x_var, self.y_var, self.order)
        
    def getStats(self):
        return self.poly_model
