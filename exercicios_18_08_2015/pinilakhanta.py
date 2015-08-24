# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:13:11 2015

@author: everaldo
"""

# Método de Gregory-Leibnitz
#"""π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) .."""
# Demora muito para convergir. Use precisão de 0.1

# Método de Nilakantha - converge mais rápido
# """π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)"""


def calcula_pi(i):
    sinal = (-1) ** i
    n1 = 2 * i + 2
    n2 = 2 * i + 3
    n3 = 2 * i + 4
    termo = sinal * (4.0/(n1 * n2 * n3))
    if abs(termo) < 0.00000001:
        return 3
    return termo + calcula_pi(i + 1)

def pi():
   """π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)"""
   i = 0
   return calcula_pi(i)