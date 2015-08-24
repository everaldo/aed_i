# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import unittest
from mdc import mdc

class TesteMDC(unittest.TestCase):
    
    def test_MDC(self):
        self.assertEqual(mdc(2, 3), 1)
        self.assertEqual(mdc(2, 4), 2)
        self.assertEqual(mdc(4, 2), 2)
        self.assertEqual(mdc(10, 10000), 10)

        
if __name__ == '__main__':
    unittest.main()