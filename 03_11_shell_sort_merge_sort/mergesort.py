#
# 27/10/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
# Fonte: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
#

from compara import Compara
from troca import Troca

class MergeSort(Compara, Troca):

    def __init__(self, v, label = ''):
        super(MergeSort, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        if len(self.v) > 1:
            meio = len(self.v) // 2
            esquerda = self.v[:meio]
            direita = self.v[meio:]

            esquerda = MergeSort(esquerda)
            esquerda.sort()
            direita = MergeSort(direita)
            direita.sort()

            # Agrega números de comparações e trocas da recursividade
            self.num_comparacoes = self.num_comparacoes + \
              esquerda.num_comparacoes + direita.num_comparacoes

            self.num_trocas = self.num_trocas + \
              esquerda.num_trocas + direita.num_trocas


            # Descarta classe de ordenação, retorna apenas vetores ordenados
            esquerda = esquerda.v
            direita  = direita.v


            i, j, k = 0, 0, 0
            while i < len(esquerda) and j < len(direita):
                if self.compara(esquerda[i], direita[j]) == Compara.MENOR:
                    self.v[k] = esquerda[i]
                    i = i + 1
                else:
                    self.v[k] = direita[j]
                    j = j + 1
                k = k + 1
                self.conta_troca()

            while i < len(esquerda):
                self.v[k]= esquerda[i]
                i = i + 1
                k = k + 1
                self.conta_troca()

            while j < len(direita):
                self.v[k] = direita[j]
                j = j + 1
                k = k + 1
                self.conta_troca()

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')

