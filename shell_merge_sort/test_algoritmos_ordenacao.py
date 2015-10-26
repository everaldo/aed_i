

import unittest
from shellsort import shellsort
from mergesort import mergesort
from random import shuffle, randint
from array import array

# Para criar um array de 1000 elementos, do tipo inteiro
# a = array('l', (randint(0, 100) for i in range(1000)))

class TestAlgoritmosOrdenacao(unittest.TestCase):


    def is_ordenado(self, l, funcao):
        funcao(l)
        self.assertEqual(l, self.ordenado)

    
    def setUp(self):
        max = 100
        self.lista = list(range(0, max))
        self.ordenado = sorted(self.lista)
        self.reverso = list(reversed(self.ordenado))
        self.aleatorio1 = list(range(0, max))
        shuffle(self.aleatorio1)
        self.aleatorio2 = list(range(0, max))
        shuffle(self.aleatorio2)
        self.aleatorio3 = list(range(0, max))
        shuffle(self.aleatorio3)
        self.aleatorio4 = list(range(0, max))
        shuffle(self.aleatorio4)


    def test_shellsort(self):
        self.is_ordenado(self.ordenado, shellsort)
        self.is_ordenado(self.reverso, shellsort)
        self.is_ordenado(self.aleatorio1, shellsort)
        self.is_ordenado(self.aleatorio2, shellsort)
        self.is_ordenado(self.aleatorio3, shellsort)
        self.is_ordenado(self.aleatorio4, shellsort)


    def test_mergesort(self):
        self.is_ordenado(self.ordenado, mergesort)
        self.is_ordenado(self.reverso, mergesort)
        self.is_ordenado(self.aleatorio1, mergesort)
        self.is_ordenado(self.aleatorio2, mergesort)
        self.is_ordenado(self.aleatorio3, mergesort)
        self.is_ordenado(self.aleatorio4, mergesort)




    def test_smoketest(self):
        self.is_ordenado(self.ordenado, list.sort)
        self.is_ordenado(self.reverso, list.sort)
        self.is_ordenado(self.aleatorio1, list.sort)
        self.is_ordenado(self.aleatorio2, list.sort)
        self.is_ordenado(self.aleatorio3, list.sort)
        self.is_ordenado(self.aleatorio4, list.sort)




if __name__ == '__main__':
    unittest.main(verbosity=2)


