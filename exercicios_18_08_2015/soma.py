# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:27:49 2015

@author: everaldo
"""

def soma(a, b):
    if b > a:
        return soma(b, a)
    if b == 0:
        return a
    return soma(a + 1, b - 1)