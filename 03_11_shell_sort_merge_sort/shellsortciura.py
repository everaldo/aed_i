#
# 03/11/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
# Fonte: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html
#
# https://en.wikipedia.org/wiki/Shellsort#Pseudocode 
#
# Essa versão utiliza a sequência de intervalos definida por Marcin Ciura
#
# [701, 301, 132, 57, 23, 10 , 4, 1]
#
# Essa sequência é empírica e foi obtida através de inúmeros testes
# 
# Melhor número médio de comparações


from compara import Compara
from troca import Troca

class ShellSortCiura(Compara, Troca):

    def __init__(self, v, label):
        super(ShellSortCiura, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        intervalos = [701, 301, 132, 57, 23, 10, 4, 1]
        for intervalo in intervalos:
          for inicio in range(intervalo):
              self.insertionsort_intercalado(inicio, intervalo)



    def insertionsort_intercalado(self, inicio, intervalo):
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


