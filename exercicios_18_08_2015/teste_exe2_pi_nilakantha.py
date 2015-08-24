# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import math
import unittest
from pinilakhanta import pi

class TestePI(unittest.TestCase):
    
    def test_PI(self):
        self.assertAlmostEqual(math.pi, pi())

if __name__ == '__main__':
    unittest.main()