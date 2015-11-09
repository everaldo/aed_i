

import unittest
from quicksort import QuickSort
from quicksort_pivoinicio import QuickSortPivoInicio
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


    
    def setUp(self):
        max = 10000
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



    def test_quicksort(self):
        self.is_ordenado(QuickSort(self.ordenado[:], 'QuickSort Ordenado'))
        self.is_ordenado(QuickSort(self.reverso[:], 'QuickSort Reverso'))
        self.is_ordenado(QuickSort(self.aleatorio1[:], 'QuickSort Aleatorio1'))
        self.is_ordenado(QuickSort(self.aleatorio2[:], 'QuickSort Aleatorio2'))
        self.is_ordenado(QuickSort(self.aleatorio3[:], 'QuickSort Aleatorio3'))
        self.is_ordenado(QuickSort(self.aleatorio4[:], 'QuickSort Aleatorio4'))

#    def test_quicksortpivoinicio(self):
#        self.is_ordenado(QuickSortPivoInicio(self.ordenado[:], 'QuickSortPivoInicio Ordenado'))
#        self.is_ordenado(QuickSortPivoInicio(self.reverso, 'QuickSortPivoInicio Reverso'))
#        self.is_ordenado(QuickSortPivoInicio(self.aleatorio1, 'QuickSortPivoInicio Aleatorio1'))
#        self.is_ordenado(QuickSortPivoInicio(self.aleatorio2, 'QuickSortPivoInicio Aleatorio2'))
#        self.is_ordenado(QuickSortPivoInicio(self.aleatorio3, 'QuickSortPivoInicio Aleatorio3'))
#        self.is_ordenado(QuickSortPivoInicio(self.aleatorio4, 'QuickSortPivoInicio Aleatorio4'))
#
#

    def test_smoketest(self):
        self.is_ordenado(SmokeTest(self.ordenado))
        self.is_ordenado(SmokeTest(self.reverso))
        self.is_ordenado(SmokeTest(self.aleatorio1))
        self.is_ordenado(SmokeTest(self.aleatorio2))
        self.is_ordenado(SmokeTest(self.aleatorio3))
        self.is_ordenado(SmokeTest(self.aleatorio4))





if __name__ == '__main__':
    unittest.main(verbosity=2)


