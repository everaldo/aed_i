

import unittest
from bubblesort import bubblesort
from insertionsort import insertionsort, insertionsort2
from selectionsort import selectionsort
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


    def test_bubblesort(self):
        self.is_ordenado(self.ordenado, bubblesort)
        self.is_ordenado(self.reverso, bubblesort)
        self.is_ordenado(self.aleatorio1, bubblesort)
        self.is_ordenado(self.aleatorio2, bubblesort)
        self.is_ordenado(self.aleatorio3, bubblesort)
        self.is_ordenado(self.aleatorio4, bubblesort)


    def test_selectionsort(self):
        self.is_ordenado(self.ordenado, selectionsort)
        self.is_ordenado(self.reverso, selectionsort)
        self.is_ordenado(self.aleatorio1, selectionsort)
        self.is_ordenado(self.aleatorio2, selectionsort)
        self.is_ordenado(self.aleatorio3, selectionsort)
        self.is_ordenado(self.aleatorio4, selectionsort)


    def test_insertionsort(self):
        self.is_ordenado(self.ordenado, insertionsort)
        self.is_ordenado(self.reverso, insertionsort)
        self.is_ordenado(self.aleatorio1, insertionsort)
        self.is_ordenado(self.aleatorio2, insertionsort)
        self.is_ordenado(self.aleatorio3, insertionsort)
        self.is_ordenado(self.aleatorio4, insertionsort)



    def test_insertionsort2(self):
        self.is_ordenado(self.ordenado, insertionsort2)
        self.is_ordenado(self.reverso, insertionsort2)
        self.is_ordenado(self.aleatorio1, insertionsort2)
        self.is_ordenado(self.aleatorio2, insertionsort2)
        self.is_ordenado(self.aleatorio3, insertionsort2)
        self.is_ordenado(self.aleatorio4, insertionsort2)



    def test_smoketest(self):
        self.is_ordenado(self.ordenado, list.sort)
        self.is_ordenado(self.reverso, list.sort)
        self.is_ordenado(self.aleatorio1, list.sort)
        self.is_ordenado(self.aleatorio2, list.sort)
        self.is_ordenado(self.aleatorio3, list.sort)
        self.is_ordenado(self.aleatorio4, list.sort)




if __name__ == '__main__':
    unittest.main(verbosity=2)


