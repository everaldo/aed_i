# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import unittest
from mult import mult

class TesteMult(unittest.TestCase):
    
    def test_Mult(self):
        self.assertEqual(mult(0, 0), 0)
        self.assertEqual(mult(0, 1), 0)
        self.assertEqual(mult(1, 0), 0)
        self.assertEqual(mult(10, 5), 50)
        self.assertEqual(mult(10, 10), 100)
        self.assertEqual(mult(10, -5), -50)
        self.assertEqual(mult(-10, 5), -50)
        self.assertEqual(mult(-10, -10), 100)
        self.assertEqual(mult(100, 1000), 100000)
        self.assertEqual(mult(7, 2), 14)


if __name__ == '__main__':
    unittest.main()