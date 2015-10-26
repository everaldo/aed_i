#
# 26/10/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
# Fonte: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html
#




def shellsort(l):
    tamanhosublista = len(l)//2
    while tamanhosublista > 0:

      for inicio in range(tamanhosublista):
        insertionsort_intervalado(l, inicio, tamanhosublista)

      tamanhosublista = tamanhosublista // 2

def insertionsort_intervalado(l ,inicio, intervalo):
    for i in range(inicio + intervalo, len(l), intervalo):

        atual = l[i]
        pos = i

        while pos >= intervalo and l[pos - intervalo] > atual:
            l[pos] = l[pos - intervalo]
            pos = pos - intervalo

        l[pos] = atual

