

from compara import Compara
from troca import Troca

class BubbleSort(Compara, Troca):

    def __init__(self, v, label):
        super(BubbleSort, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        for i in range(0, len(self.v) - 1):
            for j in range(0, len(self.v) - 1 - i):
                if self.compara(self.v[j], self.v[j + 1]) == Compara.MAIOR:
                    self.troca(self.v, j, j + 1)


    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')
