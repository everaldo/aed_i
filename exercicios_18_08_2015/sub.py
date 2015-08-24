# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:29:59 2015

@author: everaldo
"""

def sub(a, b):
    if abs(b) > abs(a):
        return sub(-b, a)
    if b == 0:
        return a
    return sub(a - 1, b - 1)
        