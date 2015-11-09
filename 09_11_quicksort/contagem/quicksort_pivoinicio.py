#
# 09/11/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
# https://en.wikipedia.org/wiki/Quicksort
# https://pt.wikipedia.org/wiki/Quicksort
# http://visualgo.net/sorting.html
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

from compara import Compara
from troca import Troca
class QuickSortPivoInicio(Compara, Troca):

    def __init__(self, v, label):
        super(QuickSortPivoInicio, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        self.quicksort(0, len(self.v) - 1)


    def quicksort(self, inicio, fim):
        pass
        #PASS - Em implementação


    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')


