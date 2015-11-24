#
# 24/11/2015 - Everaldo Gomes - everaldo.gomes@pucpr.br
#

from compara import Compara
from troca import Troca
class QuickSortNinther(Compara, Troca):

    def __init__(self, v, label):
        super(QuickSortNinther, self).__init__()
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
        ninther_index = self.get_ninther_index(inicio, fim)
        self.troca(self.v, ninther_index, fim)
        pivo = self.v[fim]
        i = inicio
        for j in range(inicio, fim):
            self.conta_comparacao()
            if self.v[j] <= pivo:
                self.troca(self.v, i, j)
                i = i + 1
        self.troca(self.v, i, fim)
        return i


    def get_ninther_index(self, inicio, fim):
        if fim <= inicio:
            return fim
        if (fim - inicio) < 9:
            return fim
        meio = inicio + ((fim - inicio) // 2)

        mediana_ord1 = sorted([(inicio, self.v[inicio]), (inicio + 1, self.v[inicio + 1]), \
                        (inicio + 2, self.v[inicio + 2])], key=lambda x: x[1])
        mediana1 = mediana_ord1[1]

        mediana_ord2 = sorted([(meio, self.v[meio]), (meio + 1, self.v[meio + 1]), \
                        (meio -1, self.v[meio -1])], key=lambda x: x[1])
        mediana2 = mediana_ord2[1]

        mediana_ord3 = sorted([(fim, self.v[fim]), (fim -1, self.v[fim -1]), \
                        (fim - 2, self.v[fim -2])], key=lambda x: x[1])
        mediana3 = mediana_ord3[1]


        ordenado = sorted([mediana1, mediana2 , mediana3], key=lambda x: x[1])
        return ordenado[1][0]

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')


