# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:35:54 2015

@author: everaldo
"""

def mult(a, b):
    if abs(b) > abs(a):
        return mult(b, a)
    if b < 0:
        return - mult(a, -b)
    if b == 0:
        return 0
    return a + mult(a, b - 1)