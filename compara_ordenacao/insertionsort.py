from compara import Compara
from troca import Troca

class InsertionSort(Compara, Troca):

    def __init__(self, v, label):
        super(InsertionSort, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        for i in range(1, len(self.v)):
            pos = i
            while pos > 0 and self.compara(self.v[pos], self.v[pos - 1]) == Compara.MENOR:
                self.troca(self.v, pos, pos - 1)
                pos = pos - 1


    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')

class InsertionSort2(Compara, Troca):

    def __init__(self, v, label):
        super(InsertionSort2, self).__init__()
        self.v = v
        self.label = label


    def sort(self):
        for i in range(1, len(self.v)):
            pos = i
            x = self.v[i]
            while pos > 0 and self.compara(x, self.v[pos - 1]) == Compara.MENOR:
                #vamos convencionar que a cópia não é igual a troca
                #mas é um caso discutível. Testar contando
                self.conta_troca()
                self.v[pos] = self.v[pos - 1]
                pos = pos - 1
            if pos != i:
                self.conta_troca()
                self.v[pos] = x

    def report(self):
        print('Nome: ', self.label)
        print('Tamanho do vetor:', len(self.v))
        print('Número de Comparações:', self.num_comparacoes)
        print('Número de Trocas:', self.num_trocas)
        print('--------------------------')


