

import unittest
from heapsort import HeapSort
from smoke_test import SmokeTest
from random import shuffle, randint
from array import array
from sys import maxsize, setrecursionlimit

# Para criar um array de 1000 elementos, do tipo inteiro
# a = array('l', (randint(0, 100) for i in range(1000)))

setrecursionlimit(1000000)


class TestAlgoritmosOrdenacao(unittest.TestCase):


    def is_ordenado(self, algoritmo):
        algoritmo.sort()
        self.assertEqual(algoritmo.v, self.ordenado)
        algoritmo.report()
        #print(algoritmo.v) # para imprimir na tela

    
    def setUp(self):
        max = 10000
        #max = 50 # para imprimir na tela
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



    def test_heapsort(self):
        self.is_ordenado(HeapSort(self.ordenado[:], 'HeapSort Ordenado'))
        self.is_ordenado(HeapSort(self.reverso[:], 'HeapSort Reverso'))
        self.is_ordenado(HeapSort(self.aleatorio1[:], 'HeapSort Aleatorio1'))
        self.is_ordenado(HeapSort(self.aleatorio2[:], 'HeapSort Aleatorio2'))
        self.is_ordenado(HeapSort(self.aleatorio3[:], 'HeapSort Aleatorio3'))
        self.is_ordenado(HeapSort(self.aleatorio4[:], 'HeapSort Aleatorio4'))


    def test_smoketest(self):
        self.is_ordenado(SmokeTest(self.ordenado))
        self.is_ordenado(SmokeTest(self.reverso))
        self.is_ordenado(SmokeTest(self.aleatorio1))
        self.is_ordenado(SmokeTest(self.aleatorio2))
        self.is_ordenado(SmokeTest(self.aleatorio3))
        self.is_ordenado(SmokeTest(self.aleatorio4))





if __name__ == '__main__':
    unittest.main(verbosity=2)


