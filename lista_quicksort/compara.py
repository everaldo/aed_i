



class Compara:

    MENOR = -1
    IGUAL = 0
    MAIOR = 1

    def __init__(self):
        super(Compara, self).__init__()
        self.num_comparacoes = 0


    def compara(self, x, y):
        self.num_comparacoes = self.num_comparacoes + 1
        if x < y:
            return self.__class__.MENOR
        if x > y:
            return self.__class__.MAIOR
        return self.__class__.IGUAL

    def conta_comparacao(self):
        self.num_comparacoes = self.num_comparacoes + 1
