

from compara import Compara
from troca import Troca

class SelectionSort(Compara, Troca):

    def __init__(self, v, label):
        super(SelectionSort, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        for i in range(0, len(self.v) - 1):
            pos = i
            for j in range(i + 1, len(self.v)):
                if self.compara(self.v[pos], self.v[j]) == Compara.MAIOR:
                    pos = j
            if pos != i:
                self.troca(self.v, i, pos)

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')

