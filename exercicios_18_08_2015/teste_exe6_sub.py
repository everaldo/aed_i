# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import unittest
from sub import sub

class TesteSub(unittest.TestCase):
    
    def test_Sub(self):
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(0, 1), -1)
        self.assertEqual(sub(1, 0), 1)
        self.assertEqual(sub(10, 0), 10)
        self.assertEqual(sub(10, 10), 0)
        self.assertEqual(sub(100, 1000), -1100)
        self.assertEqual(sub(7, 2), 5)


if __name__ == '__main__':
    unittest.main()