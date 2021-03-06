#
# 24/11/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#

from compara import Compara
from troca import Troca
from random import randint
class QuickSortRandom(Compara, Troca):

    def __init__(self, v, label):
        super(QuickSortRandom, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        self.quicksort(0, len(self.v) - 1)


    def quicksort(self, inicio, fim):
        if inicio < fim:
            p = self.particao(inicio, fim)
            self.quicksort(inicio, p - 1)
            self.quicksort(p + 1, fim)


    def particao(self, inicio, fim):
        random_index = randint(inicio, fim)
        self.troca(self.v, random_index, fim)
        pivo = self.v[fim]
        i = inicio
        for j in range(inicio, fim):
            self.conta_comparacao()
            if self.v[j] <= pivo:
                self.troca(self.v, i, j)
                i = i + 1
        self.troca(self.v, i, fim)
        return i

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')


