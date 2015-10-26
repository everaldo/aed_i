#
# 26/10/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
# Fonte: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
#


def mergesort(l):
    if len(l) > 1:
        meio = len(l) // 2
        esquerda = l[:meio]
        direita = l[meio:]

        mergesort(esquerda)
        mergesort(direita)

        i, j, k = 0, 0, 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                l[k] = esquerda[i]
                i = i + 1
            else:
                l[k] = direita[j]
                j = j + 1
            k = k + 1

        while i < len(esquerda):
            l[k]= esquerda[i]
            i = i + 1
            k = k + 1

        while j < len(direita):
            l[k] = direita[j]
            j = j + 1
            k = k + 1


