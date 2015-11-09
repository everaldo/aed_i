#
# 09/11/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
# https://en.wikipedia.org/wiki/Quicksort
# https://pt.wikipedia.org/wiki/Quicksort
# http://visualgo.net/sorting.html
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

from compara import Compara
from troca import Troca

class QuickSort(Compara, Troca):

    def __init__(self, v, label):
        super(QuickSort, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        self.quicksort(0, len(self.v) - 1)


    def quicksort(self, inicio, fim):
        if inicio >= fim:
            return None
        i = inicio
        j = fim
        pivo = self.v[inicio + (fim - inicio) // 2]
        while i < j:
            self.conta_comparacao()
            while self.v[i] < pivo:
                self.conta_comparacao()
                i = i + 1
            self.conta_comparacao()
            while self.v[j] >  pivo:
                self.conta_comparacao()
                j = j - 1
            if i <= j:
                self.troca(self.v, i, j)
                i = i + 1
                j = j - 1
        self.quicksort(inicio, j)
        self.quicksort(i, fim)

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')


