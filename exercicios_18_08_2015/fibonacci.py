# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:26:39 2015

@author: everaldo
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)