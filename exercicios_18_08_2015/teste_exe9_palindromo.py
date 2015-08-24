# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:07:25 2015

@author: everaldo
"""

import unittest
from palindromo import palindromo

class TestePalindromo(unittest.TestCase):
    
    def test_Palindromo(self):
        self.assertTrue(palindromo(''))
        self.assertTrue(palindromo('a'))
        self.assertTrue(palindromo('ss'))
        self.assertTrue(palindromo('asa'))
        self.assertFalse(palindromo('abcde'))
        self.assertFalse(palindromo('sa'))
        self.assertFalse(palindromo('asas'))       



if __name__ == '__main__':
    unittest.main()