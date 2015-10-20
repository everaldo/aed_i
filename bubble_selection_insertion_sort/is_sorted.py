#
# 20/10/2015 - everaldo.gomes@pucpr.br
#
# Funções para verificar se uma lista está ordenada
#


def is_sorted(v):
    if len(v) == 0 or len(v) == 1:
        return True
    return v[0] <= v[1] and is_sorted(v[1:])


## versão iterativa

def is_sorted2(v):
    for i in range(0, len(v) - 1):
        if v[i] <= v[i+1]:
            return False
    return True
