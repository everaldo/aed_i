# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import unittest
from divisao import divisao

class TesteDivisao(unittest.TestCase):
    
    def test_Divisao(self):
        self.assertEqual(divisao(10, 1), 10)
        self.assertEqual(divisao(5, 2), 2)
        self.assertEqual(divisao(1, 3), 0)
        self.assertEqual(divisao(10, 5), 2)
        self.assertEqual(divisao(10, 10), 1)
        self.assertEqual(divisao(12, 4), 3)
        self.assertEqual(divisao(7, 2), 3)


if __name__ == '__main__':
    unittest.main()