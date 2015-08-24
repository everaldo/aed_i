# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:14:13 2015

@author: everaldo
"""

import time

def mdc(a, b):
    if b > a:
        return mdc(b, a)
    if a % b == 0:
        return b
    return  mdc(b, a % b)
    