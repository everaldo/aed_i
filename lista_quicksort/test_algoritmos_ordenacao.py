

import unittest
from quicksort import QuickSort
from quicksortrandom import QuickSortRandom
from quicksortmedian import QuickSortMedian
from quicksortninther import QuickSortNinther
from quicksortlomuto import QuickSortLomuto
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
        self.ordenado = sorted(self.lista[:])
        self.reverso = list(reversed(self.ordenado[:]))
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

    def test_quicksortrandom(self):
        self.is_ordenado(QuickSortRandom(self.ordenado[:], 'QuickSortRandom Ordenado'))
        self.is_ordenado(QuickSortRandom(self.reverso[:], 'QuickSortRandom Reverso'))
        self.is_ordenado(QuickSortRandom(self.aleatorio1[:], 'QuickSortRandom Aleatorio1'))
        self.is_ordenado(QuickSortRandom(self.aleatorio2[:], 'QuickSortRandom Aleatorio2'))
        self.is_ordenado(QuickSortRandom(self.aleatorio3[:], 'QuickSortRandom Aleatorio3'))
        self.is_ordenado(QuickSortRandom(self.aleatorio4[:], 'QuickSortRandom Aleatorio4'))

    def test_quicksortlomuto(self):
        self.is_ordenado(QuickSortLomuto(self.ordenado[:], 'QuickSortLomuto Ordenado'))
        self.is_ordenado(QuickSortLomuto(self.reverso[:], 'QuickSortLomuto Reverso'))
        self.is_ordenado(QuickSortLomuto(self.aleatorio1[:], 'QuickSortLomuto Aleatorio1'))
        self.is_ordenado(QuickSortLomuto(self.aleatorio2[:], 'QuickSortLomuto Aleatorio2'))
        self.is_ordenado(QuickSortLomuto(self.aleatorio3[:], 'QuickSortLomuto Aleatorio3'))
        self.is_ordenado(QuickSortLomuto(self.aleatorio4[:], 'QuickSortLomuto Aleatorio4'))

    def test_quicksortmedian(self):
        self.is_ordenado(QuickSortMedian(self.ordenado[:], 'QuickSortMedian Ordenado'))
        self.is_ordenado(QuickSortMedian(self.reverso[:], 'QuickSortMedian Reverso'))
        self.is_ordenado(QuickSortMedian(self.aleatorio1[:], 'QuickSortMedian Aleatorio1'))
        self.is_ordenado(QuickSortMedian(self.aleatorio2[:], 'QuickSortMedian Aleatorio2'))
        self.is_ordenado(QuickSortMedian(self.aleatorio3[:], 'QuickSortMedian Aleatorio3'))
        self.is_ordenado(QuickSortMedian(self.aleatorio4[:], 'QuickSortMedian Aleatorio4'))


    def test_quicksortmedian(self):
        self.is_ordenado(QuickSortNinther(self.ordenado[:], 'QuickSortNinther Ordenado'))
        self.is_ordenado(QuickSortNinther(self.reverso[:], 'QuickSortNinther Reverso'))
        self.is_ordenado(QuickSortNinther(self.aleatorio1[:], 'QuickSortNinther Aleatorio1'))
        self.is_ordenado(QuickSortNinther(self.aleatorio2[:], 'QuickSortNinther Aleatorio2'))
        self.is_ordenado(QuickSortNinther(self.aleatorio3[:], 'QuickSortNinther Aleatorio3'))
        self.is_ordenado(QuickSortNinther(self.aleatorio4[:], 'QuickSortNinther Aleatorio4'))


    def test_smoketest(self):
        self.is_ordenado(SmokeTest(self.ordenado))
        self.is_ordenado(SmokeTest(self.reverso))
        self.is_ordenado(SmokeTest(self.aleatorio1))
        self.is_ordenado(SmokeTest(self.aleatorio2))
        self.is_ordenado(SmokeTest(self.aleatorio3))
        self.is_ordenado(SmokeTest(self.aleatorio4))





if __name__ == '__main__':
    unittest.main(verbosity=2)


