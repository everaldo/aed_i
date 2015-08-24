# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import math
import unittest
from pileibniz import pi

class TestePI(unittest.TestCase):
    
    def test_PI(self):
        """Calcula o valor de PI com 1 casa de precisão
        utilizando o método de Grégory-Leibniz"""
        self.assertAlmostEqual(math.pi, pi(), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
