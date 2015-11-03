

import unittest
from shellsort import ShellSort
from shellsortciura import ShellSortCiura
from mergesort import MergeSort
from smoke_test import SmokeTest
from random import shuffle, randint
from array import array

# Para criar um array de 1000 elementos, do tipo inteiro
# a = array('l', (randint(0, 100) for i in range(1000)))

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



    def test_shellsort_ciura(self):
        self.is_ordenado(ShellSortCiura(self.ordenado, 'ShellSortCiura Ordenado'))
        self.is_ordenado(ShellSortCiura(self.reverso, 'ShellSortCiura Reverso'))
        self.is_ordenado(ShellSortCiura(self.aleatorio1, 'ShellSortCiura Aleatorio1'))
        self.is_ordenado(ShellSortCiura(self.aleatorio2, 'ShellSortCiura Aleatorio2'))
        self.is_ordenado(ShellSortCiura(self.aleatorio3, 'ShellSortCiura Aleatorio3'))
        self.is_ordenado(ShellSortCiura(self.aleatorio4, 'ShellSortCiura Aleatorio4'))

    def test_shellsort(self):
        self.is_ordenado(ShellSort(self.ordenado, 'ShellSort Ordenado'))
        self.is_ordenado(ShellSort(self.reverso, 'ShellSort Reverso'))
        self.is_ordenado(ShellSort(self.aleatorio1, 'ShellSort Aleatorio1'))
        self.is_ordenado(ShellSort(self.aleatorio2, 'ShellSort Aleatorio2'))
        self.is_ordenado(ShellSort(self.aleatorio3, 'ShellSort Aleatorio3'))
        self.is_ordenado(ShellSort(self.aleatorio4, 'ShellSort Aleatorio4'))


    def test_mergesort(self):
        self.is_ordenado(MergeSort(self.ordenado, 'MergeSort Ordenado'))
        self.is_ordenado(MergeSort(self.reverso, 'MergeSort Reverso'))
        self.is_ordenado(MergeSort(self.aleatorio1, 'MergeSort Aleatorio1'))
        self.is_ordenado(MergeSort(self.aleatorio2, 'MergeSort Aleatorio2'))
        self.is_ordenado(MergeSort(self.aleatorio3, 'MergeSort Aleatorio3'))
        self.is_ordenado(MergeSort(self.aleatorio4, 'MergeSort Aleatorio4'))




    def test_smoketest(self):
        self.is_ordenado(SmokeTest(self.ordenado))
        self.is_ordenado(SmokeTest(self.reverso))
        self.is_ordenado(SmokeTest(self.aleatorio1))
        self.is_ordenado(SmokeTest(self.aleatorio2))
        self.is_ordenado(SmokeTest(self.aleatorio3))
        self.is_ordenado(SmokeTest(self.aleatorio4))





if __name__ == '__main__':
    unittest.main(verbosity=2)


