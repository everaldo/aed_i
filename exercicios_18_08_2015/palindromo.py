# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:49:47 2015

@author: everaldo
"""

def palindromo(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return palindromo(s[1:-1])
    else:
        return False