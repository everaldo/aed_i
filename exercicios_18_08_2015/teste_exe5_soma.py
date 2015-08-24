# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import unittest
from soma import soma

class TesteSoma(unittest.TestCase):
    
    def test_Soma(self):
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(0, 1), 1)
        self.assertEqual(soma(1, 0), 1)
        self.assertEqual(soma(10, 0), 10)
        self.assertEqual(soma(10, 10), 20)
        self.assertEqual(soma(100, 1000), 1100)
        self.assertEqual(soma(7, 7), 14)

        

        
if __name__ == '__main__':
    unittest.main()