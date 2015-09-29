# -*- coding: utf-8 -*-

"""

@author: Everaldo Gomes
@email: everaldo.gomes@pucpr.br


Início da implementação: 29/09/2015 - 14h48
"""


import unittest
from pilha import Pilha
#from teste_lista import TestLista
from random import randint
from sys import maxsize, getrecursionlimit, setrecursionlimit
from collections import deque

setrecursionlimit(maxsize)


class TestePilha(unittest.TestCase):

    def setUp(self):
        """Esse método é invocado antes de cada Teste. Prepara o ambiente"""
        self.MAX_VALUE = 10000
        self.pilha_vazia = Pilha()
        self.x = randint(0, maxsize)
        self.pilha_um = Pilha()
        self.pilha_um.push(self.x)
        self.max = randint(100, 500)
        self.pilha = Pilha()
        self.pilha.push(self.x)
        self.pilha_limite = Pilha(self.max)
        self.python_deque = deque()
        for i in range(0, self.max):
            element = randint(0, self.MAX_VALUE)
            self.python_deque.append(element)
            self.pilha_limite.push(element)


    def test_construtor(self):
        """O construtor deve receber um valor max ou None"""
        self.assertIsInstance(self.pilha_um, Pilha)
        self.assertIsInstance(self.pilha_vazia, Pilha)
        self.assertIsInstance(self.pilha, Pilha)
        self.assertIsInstance(self.pilha_limite, Pilha)

    def test_bool_false(self):
        """Uma Pilha Vazia retorna False"""
        self.assertFalse(bool(self.pilha_vazia))
        self.assertFalse(self.pilha_vazia)
        self.assertFalse(self.pilha_vazia.__bool__())

    def test_bool_true(self):
        """Uma Pilha com 1 elemento  retorna True"""
        self.assertTrue(bool(self.pilha_um))
        self.assertTrue(self.pilha_um)
        self.assertTrue(self.pilha_um.__bool__())


    def test_empty_stack(self):
        """Uma Pilha Vazia retorna True para is_empty"""
        self.assertTrue(self.pilha_vazia.is_empty())

    def test_not_empty_stack(self):
        """Uma Pilha Não Vazia retorna False para is_empty"""
        self.assertFalse(self.pilha_um.is_empty())

    
    def test_len_empty_stack(self):
        """Uma Pilha Vazia tem tamanho 0"""
        self.assertEqual(len(self.pilha_vazia), 0)

    def test_len_one_element_stack(self):
        """Uma Pilha com 1 elemento tem tamanho 1"""
        self.assertEqual(len(self.pilha_um), 1)

    #Este Teste só funciona quando push tiver sido implementado
    def test_len_arbitrary_size_stack(self):
        """Uma Pilha com n elementos tem tamanho n"""
        self.assertEqual(len(self.pilha_limite), self.max)


    def test_peek_empty_stack(self):
        """Uma Pilha vazia retorna uma Exceção quando peek é invocado"""
        with self.assertRaises(Exception):
            self.pilha_vazia.peek()

    def test_peek_one_element_stack(self):
        """Uma Pilha com 1 elemento retorna o elemento com peek"""
        self.assertEqual(self.pilha_um.peek(), self.x)

    def test_peek_n_elements_stack(self):
        """Uma Pilha com n elementos retorna o último a ter sido inserido com peek"""
        self.assertEqual(self.pilha_limite.peek(), self.python_deque.pop())

    def test_peek_doesnt_change_stack_len(self):
        """O método peek é idempotente e não altera o tamanho da pilha"""
        size = len(self.pilha_limite)
        self.assertEqual(len(self.pilha_limite), size)
        self.pilha_limite.peek()
        self.pilha_limite.peek()
        self.pilha_limite.peek()
        self.pilha_limite.peek()
        self.pilha_limite.peek()
        self.assertEqual(len(self.pilha_limite), size)

    def test__eq__empty_stacks(self):
        """Duas pilhas vazias são iguais"""
        self.assertEqual(Pilha(), Pilha())
        #o argumento é a capacidade da pilha
        self.assertEqual(Pilha(5), Pilha(10))


    def test__eq__n_elements_stacks(self):
        """Duas pilhas com os mesmos elementos são iguais"""
        x = randint(100, 500)
        pilha1 = Pilha()
        pilha2 = Pilha()
        for i in range(0, x):
            element = randint(0, self.MAX_VALUE)
            pilha1.push(element)
            pilha2.push(element)
            self.assertEqual(pilha1, pilha2)
        self.assertEqual(pilha1, pilha2)

    def test_str_empty_stack(self):
        """Uma pilha vazia deve ser representada pela string []"""
        self.assertEqual(str(self.pilha_vazia), "[]")

    def test_str_one_element_stack(self):
        """Uma pilha com somente um elemento x deve ser representada por [x]"""
        self.assertEqual(str(self.pilha_um), "[" + str(self.x) + "]")

    def test_str_n_elements_stack(self):
        """Uma pilha com n elementos imprime todos os elementos"""
        """Nossa implementação insere no começo e retira no começo,
        mas também é possível inserir no final e retirar no final"""
        pilha = Pilha()
        pilha.push(1)
        pilha.push(2)
        pilha.push(3)
        pilha.push(4)
        self.assertEqual(str(pilha), "[4, 3, 2, 1]")

    def test_clear_remove_all_elements(self):
        """clear remove todos os elementos da pilha"""
        self.assertEqual(len(self.pilha_vazia), 0)
        self.assertNotEqual(len(self.pilha_um), 0)
        self.assertNotEqual(len(self.pilha_limite), 0)

        self.pilha_vazia.clear()
        self.pilha_um.clear()
        self.pilha_limite.clear()

        self.assertEqual(len(self.pilha_vazia), 0)
        self.assertEqual(len(self.pilha_um), 0)
        self.assertEqual(len(self.pilha_limite), 0)
          
 
    def test_push(self):
        """push aumenta o tamanho da pilha em 1"""
        element = randint(0, self.MAX_VALUE)
        self.assertEqual(len(self.pilha_vazia), 0)
        self.assertEqual(len(self.pilha_um), 1)
        self.pilha_vazia.push(element)
        self.pilha_um.push(element)
        self.assertEqual(len(self.pilha_vazia), 1)
        self.assertEqual(len(self.pilha_um), 2)


    def test_push_full_stack(self):
        """push numa pilha cheia gera um erro"""
        with self.assertRaises(Exception):
            element = randint(0, self.MAX_VALUE)
            self.pilha_limite.push(element)


    def test_pop(self):
        """pop diminui o tamanho da pilha em 1"""
        self.assertEqual(len(self.pilha_um), 1)
        self.pilha_um.pop()
        self.assertEqual(len(self.pilha_um), 0)
        self.assertEqual(self.pilha_um, Pilha())


        size = len(self.pilha_limite)
        self.pilha_limite.pop()
        self.assertEqual(len(self.pilha_limite), size - 1)
        

    def test_pop_empty_stack(self):
        """pop numa pilha vazia gera um erro"""
        with self.assertRaises(Exception):
            self.pilha_vazia.pop()

    def test_push_pop_1(self):
        """teste de integração pipeline de pilhas"""
        pilha1 = Pilha()
        pilha2 = Pilha()
        pilha3 = Pilha()
        pilha4 = Pilha()
        for i in range(0, self.max):
            pilha1.push(i)
            pilha2.push(pilha1.pop())
            pilha3.push(pilha2.pop())
            pilha4.push(pilha3.pop())
            self.assertEqual(i, pilha4.pop())



if __name__ == '__main__':
    unittest.main(verbosity=2)
