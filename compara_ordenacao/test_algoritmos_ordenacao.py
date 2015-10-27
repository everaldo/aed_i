

import unittest
from bubblesort import BubbleSort
from selectionsort import SelectionSort
from insertionsort import InsertionSort, InsertionSort2
from shellsort import ShellSort
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


    def test_bubblesort(self):
        self.is_ordenado(BubbleSort(self.ordenado, 'BubbleSort Ordenado'))
        self.is_ordenado(BubbleSort(self.reverso, 'BubbleSort Reverso'))
        self.is_ordenado(BubbleSort(self.aleatorio1, 'BubbleSort Aleatorio1'))
        self.is_ordenado(BubbleSort(self.aleatorio2, 'BubbleSort Aleatorio2'))
        self.is_ordenado(BubbleSort(self.aleatorio3, 'BubbleSort Aleatorio3'))
        self.is_ordenado(BubbleSort(self.aleatorio4, 'BubbleSort Aleatorio4'))

    def test_selectionsort(self):
        self.is_ordenado(SelectionSort(self.ordenado, 'SelectionSort Ordenado'))
        self.is_ordenado(SelectionSort(self.reverso, 'SelectionSort Reverso'))
        self.is_ordenado(SelectionSort(self.aleatorio1, 'SelectionSort Aleatorio1'))
        self.is_ordenado(SelectionSort(self.aleatorio2, 'SelectionSort Aleatorio2'))
        self.is_ordenado(SelectionSort(self.aleatorio3, 'SelectionSort Aleatorio3'))
        self.is_ordenado(SelectionSort(self.aleatorio4, 'SelectionSort Aleatorio4'))

    def test_insertionsort(self):
        self.is_ordenado(InsertionSort(self.ordenado, 'InsertionSort Ordenado'))
        self.is_ordenado(InsertionSort(self.reverso, 'InsertionSort Reverso'))
        self.is_ordenado(InsertionSort(self.aleatorio1, 'InsertionSort Aleatorio1'))
        self.is_ordenado(InsertionSort(self.aleatorio2, 'InsertionSort Aleatorio2'))
        self.is_ordenado(InsertionSort(self.aleatorio3, 'InsertionSort Aleatorio3'))
        self.is_ordenado(InsertionSort(self.aleatorio4, 'InsertionSort Aleatorio4'))


    def test_insertionsort2(self):
        self.is_ordenado(InsertionSort2(self.ordenado, 'InsertionSort2 Ordenado'))
        self.is_ordenado(InsertionSort2(self.reverso, 'InsertionSort2 Reverso'))
        self.is_ordenado(InsertionSort2(self.aleatorio1, 'InsertionSort2 Aleatorio1'))
        self.is_ordenado(InsertionSort2(self.aleatorio2, 'InsertionSort2 Aleatorio2'))
        self.is_ordenado(InsertionSort2(self.aleatorio3, 'InsertionSort2 Aleatorio3'))
        self.is_ordenado(InsertionSort2(self.aleatorio4, 'InsertionSort2 Aleatorio4'))


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


