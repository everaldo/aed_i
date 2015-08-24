# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:00:50 2015

@author: everaldo
"""


# Método de Gregory-Leibnitz
#"""π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) .."""
# Demora muito para convergir. Use precisão de 0.1


def calcula_pi(i):
    sinal = (-1) ** i
    n = 2 * i + 1
    termo = sinal * (4.0/n)
    if abs(termo) < 0.1:
        return 0
    return termo + calcula_pi(i + 1)

def pi():
   """π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) .."""
   i = 0
   return calcula_pi(i)