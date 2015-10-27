#
# 27/10/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
# Fonte: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html
#

from compara import Compara
from troca import Troca

class ShellSort(Compara, Troca):

    def __init__(self, v, label):
        super(ShellSort, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        tamanhosublista = len(self.v)//2
        while tamanhosublista > 0:

          for inicio in range(tamanhosublista):
              self.insertionsort_intervalado(inicio, tamanhosublista)

          tamanhosublista = tamanhosublista // 2


    def insertionsort_intervalado(self, inicio, intervalo):
        for i in range(inicio + intervalo, len(self.v), intervalo):

            atual = self.v[i]
            pos = i

            while pos >= intervalo and \
                self.compara(self.v[pos - intervalo], atual) == Compara.MAIOR:
                self.conta_troca()
                self.v[pos] = self.v[pos - intervalo]
                pos = pos - intervalo

            if pos != i:
                self.conta_troca()
                self.v[pos] = atual

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')


