# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:46:57 2015

@author: everaldo
"""

def divisao(a, b):
    if b == 1:
        return a
    if b > a:
        return 0
    if a - b == 0:
        return 1
    return 1 + divisao(a - b, b)