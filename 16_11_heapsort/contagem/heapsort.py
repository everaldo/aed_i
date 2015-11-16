#
# 16/11/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#
#
# Baseado em: https://pt.wikipedia.org/wiki/Heapsort#C.C3.B3digo_em_python
#

from compara import Compara
from troca import Troca
class HeapSort(Compara, Troca):

    def __init__(self, v, label):
        super(HeapSort, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        for inicio in range((len(self.v) - 1) // 2, -1, -1):
            self.siftdown(inicio, len(self.v) - 1)

        for fim in range(len(self.v) - 1, 0, -1):
            self.troca(self.v, fim, 0)
            self.siftdown(0, fim - 1)



    #peneira
    def siftdown(self, inicio, fim):
        raiz = inicio
        x = self.v[raiz]
        while True:
            filho = raiz * 2 + 1
            if filho > fim:
                break
            # Encontra filho mais valioso
            self.conta_comparacao()
            if filho + 1 <= fim and self.v[filho] < self.v[filho + 1]:
                filho += 1
            self.conta_comparacao()
            if x >= self.v[filho]:
                break
            self.conta_troca()
            self.v[raiz] = self.v[filho]
            raiz = filho
        self.conta_troca()
        self.v[raiz] = x

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')


