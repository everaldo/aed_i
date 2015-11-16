

class Troca:

    def __init__(self):
        super(Troca, self).__init__()
        self.num_trocas = 0


    def troca(self, v, i, j):
        self.num_trocas = self.num_trocas + 1
        v[i], v[j] = v[j], v[i]


    def conta_troca(self):
        self.num_trocas = self.num_trocas + 1
