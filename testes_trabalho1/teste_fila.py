# -*- coding: utf-8 -*-

"""

@author: Everaldo Gomes
@email: everaldo.gomes@pucpr.br


Início da Implementação: 20/09/2015 - 13h22

"""


import unittest
from fila import Fila
#from teste_lista import TestLista
from random import randint
from sys import maxsize, getrecursionlimit, setrecursionlimit
from collections import deque

setrecursionlimit(maxsize)


class TesteFila(unittest.TestCase):

    def setUp(self):
        """Esse método é invocado antes de cada Teste. Prepara o ambiente"""
        self.MAX_VALUE = 10000
        self.fila_vazia = Fila()
        self.x = randint(0, maxsize)
        self.fila_um = Fila()
        self.fila_um.enqueue(self.x)
        self.max = randint(100, 500)
        self.fila = Fila()
        self.fila.enqueue(self.x)
        self.fila_limite = Fila(self.max)
        self.python_deque = deque()
        for i in range(0, self.max):
            element = randint(0, self.MAX_VALUE)
            self.python_deque.append(element)
            self.fila_limite.enqueue(element)


    def test_construtor(self):
        """O construtor deve receber um valor max ou None"""
        self.assertIsInstance(self.fila_um, Fila)
        self.assertIsInstance(self.fila_vazia, Fila)
        self.assertIsInstance(self.fila, Fila)
        self.assertIsInstance(self.fila_limite, Fila)

    def test_bool_false(self):
        """Uma Fila Vazia retorna False"""
        self.assertFalse(bool(self.fila_vazia))
        self.assertFalse(self.fila_vazia)
        self.assertFalse(self.fila_vazia.__bool__())

    def test_bool_true(self):
        """Uma Fila com 1 elemento  retorna True"""
        self.assertTrue(bool(self.fila_um))
        self.assertTrue(self.fila_um)
        self.assertTrue(self.fila_um.__bool__())


    def test_empty_queue(self):
        """Uma Fila Vazia retorna True para is_empty"""
        self.assertTrue(self.fila_vazia.is_empty())

    def test_not_empty_queue(self):
        """Uma Fila Não Vazia retorna False para is_empty"""
        self.assertFalse(self.fila_um.is_empty())

    
    def test_len_empty_queue(self):
        """Uma Fila Vazia tem tamanho 0"""
        self.assertEqual(len(self.fila_vazia), 0)

    def test_len_one_element_queue(self):
        """Uma Fila com 1 elemento tem tamanho 1"""
        self.assertEqual(len(self.fila_um), 1)

    #Este Teste só funciona quando enqueue tiver sido implementado
    def test_len_arbitrary_size_queue(self):
        """Uma Fila com n elementos tem tamanho n"""
        self.assertEqual(len(self.fila_limite), self.max)


    def test_first_empty_queue(self):
        """Uma Fila vazia retorna uma Exceção quando first é invocado"""
        with self.assertRaises(Exception):
            self.fila_vazia.first()

    def test_first_one_element_queue(self):
        """Uma Fila com 1 elemento retorna o elemento com first"""
        self.assertEqual(self.fila_um.first(), self.x)

    def test_first_n_elements_queue(self):
        """Uma Fila com n elementos retorna o primeiro a ter sido inserido com first"""
        self.assertEqual(self.fila_limite.first(), self.python_deque.popleft())

    def test_first_doesnt_change_queue_len(self):
        """O método first é idempotente e não altera o tamanho da fila"""
        size = len(self.fila_limite)
        self.assertEqual(len(self.fila_limite), size)
        self.fila_limite.first()
        self.fila_limite.first()
        self.fila_limite.first()
        self.fila_limite.first()
        self.fila_limite.first()
        self.assertEqual(len(self.fila_limite), size)

    def test_last_empty_queue(self):
        """Uma Fila vazia retorna uma Exceção quando last é invocado"""
        with self.assertRaises(Exception):
            self.fila_vazia.last()

    def test_last_one_element_queue(self):
        """Uma Fila com 1 elemento retorna o elemento com last"""
        self.assertEqual(self.fila_um.last(), self.x)

    def test_last_n_elements_queue(self):
        """Uma Fila com n elementos retorna o último a ter sido inserido com last"""
        self.assertEqual(self.fila_limite.last(), self.python_deque.pop())

    def test_last_doesnt_change_queue_len(self):
        """O método last é idempotente e não altera o tamanho da fila"""
        size = len(self.fila_limite)
        self.assertEqual(len(self.fila_limite), size)
        self.fila_limite.last()
        self.fila_limite.last()
        self.fila_limite.last()
        self.fila_limite.last()
        self.fila_limite.last()
        self.assertEqual(len(self.fila_limite), size)

    def test__eq__empty_queues(self):
        """Duas filas vazias são iguais"""
        self.assertEqual(Fila(), Fila())
        #o argumento é a capacidade da fila
        self.assertEqual(Fila(5), Fila(10))


    def test__eq__n_elements_queues(self):
        """Duas filas com os mesmos elementos são iguais"""
        x = randint(100, 500)
        fila1 = Fila()
        fila2 = Fila()
        for i in range(0, x):
            element = randint(0, self.MAX_VALUE)
            fila1.enqueue(element)
            fila2.enqueue(element)
            self.assertEqual(fila1, fila2)
        self.assertEqual(fila1, fila2)

    def test_str_empty_queue(self):
        """Uma fila vazia deve ser representada pela string []"""
        self.assertEqual(str(self.fila_vazia), "[]")

    def test_str_one_element_queue(self):
        """Uma fila com somente um elemento x deve ser representada por [x]"""
        self.assertEqual(str(self.fila_um), "[" + str(self.x) + "]")

    def test_str_n_elements_queue(self):
        """Uma fila com n elementos imprime todos os elementos"""
        """Nossa implementação insere no começo e retira no final,
        mas também é possível inserir no final e retirar no começo"""
        fila = Fila()
        fila.enqueue(1)
        fila.enqueue(2)
        fila.enqueue(3)
        fila.enqueue(4)
        self.assertEqual(str(fila), "[4, 3, 2, 1]")

    def test_clear_remove_all_elements(self):
        """clear remove todos os elementos da fila"""
        self.assertEqual(len(self.fila_vazia), 0)
        self.assertNotEqual(len(self.fila_um), 0)
        self.assertNotEqual(len(self.fila_limite), 0)

        self.fila_vazia.clear()
        self.fila_um.clear()
        self.fila_limite.clear()

        self.assertEqual(len(self.fila_vazia), 0)
        self.assertEqual(len(self.fila_um), 0)
        self.assertEqual(len(self.fila_limite), 0)
          
 
    def test_enqueue(self):
        """enqueue aumenta o tamanho da fila em 1"""
        element = randint(0, self.MAX_VALUE)
        self.assertEqual(len(self.fila_vazia), 0)
        self.assertEqual(len(self.fila_um), 1)
        self.fila_vazia.enqueue(element)
        self.fila_um.enqueue(element)
        self.assertEqual(len(self.fila_vazia), 1)
        self.assertEqual(len(self.fila_um), 2)


    def test_enqueue_full_queue(self):
        """enqueue numa lista cheia gera um erro"""
        with self.assertRaises(Exception):
            element = randint(0, self.MAX_VALUE)
            self.fila_limite.enqueue(element)


    def test_dequeue(self):
        """dequeue diminui o tamanho da fila em 1"""
        self.assertEqual(len(self.fila_um), 1)
        self.fila_um.dequeue()
        self.assertEqual(len(self.fila_um), 0)
        self.assertEqual(self.fila_um, Fila())


        size = len(self.fila_limite)
        self.fila_limite.dequeue()
        self.assertEqual(len(self.fila_limite), size - 1)
        

    def test_dequeue_empty_queue(self):
        """dequeue numa lista vazia gera um erro"""
        with self.assertRaises(Exception):
            self.fila_vazia.dequeue()

    def test_enqueue_dequeue_1(self):
        """teste de integração pipeline de filas"""
        fila1 = Fila()
        fila2 = Fila()
        fila3 = Fila()
        fila4 = Fila()
        for i in range(0, self.max):
            fila1.enqueue(i)
            fila2.enqueue(fila1.dequeue())
            fila3.enqueue(fila2.dequeue())
            fila4.enqueue(fila3.dequeue())
            self.assertEqual(i, fila4.dequeue())

if __name__ == '__main__':
    unittest.main(verbosity=2)
