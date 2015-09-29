# -*- coding: utf-8 -*-

"""

@author: Everaldo Gomes
@email: everaldo.gomes@pucpr.br


Início da Implementação: 16/09/2015 - 00h35

"""


import unittest
from lista import Lista
from random import randint
from sys import maxsize, getrecursionlimit, setrecursionlimit


setrecursionlimit(maxsize)


class TestLista(unittest.TestCase):

    def setUp(self):
        """Esse método é invocado antes de cada Teste. Prepara o ambiente"""
        self.MAX_VALUE = 10000
        self.lista_vazia = Lista()
        self.x = randint(0, maxsize)
        self.lista_um = Lista(self.x)
        self.n = randint(100, 500)
        self.lista = Lista(self.x)
        self.python_list = list()
        self.python_list.append(self.x)
        for i in range(0, self.n):
            element = randint(0, self.MAX_VALUE)
            self.python_list.append(element)
            self.lista.append(element)
        self.n += 1 #conta o elemento x


    def test_construtor(self):
        """O construtor deve receber um valor ou None"""
        self.assertIs(type(self.lista_um), Lista)
        self.assertIs(type(self.lista_vazia), Lista)


    def test_bool_false(self):
        """Uma Lista Vazia retorna False"""
        self.assertFalse(bool(self.lista_vazia))
        self.assertFalse(self.lista_vazia)
        self.assertFalse(self.lista_vazia.__bool__())

    def test_bool_true(self):
        """Uma Lista Vazia retorna True"""
        self.assertTrue(bool(self.lista_um))
        self.assertTrue(self.lista_um)
        self.assertTrue(self.lista_um.__bool__())


    def test_empty_list(self):
        """Uma Lista Vazia retorna True para is_empty"""
        self.assertTrue(self.lista_vazia.is_empty())

    def test_not_empty_list(self):
        """Uma Lista Não Vazia retorna False para is_empty"""
        self.assertFalse(self.lista_um.is_empty())

    
    def test_len_empty_list(self):
        """Uma Lista Vazia tem tamanho 0"""
        self.assertEqual(len(self.lista_vazia), 0)

    def test_len_one_element_list(self):
        """Uma Lista com 1 elemento tem tamanho 1"""
        self.assertEqual(len(self.lista_um), 1)

    #Este Teste só funciona quando append tiver sido implementado
    def test_len_arbitrary_size_list(self):
        """Uma Lista com n elementos tem tamanho n"""
        #self.assertEqual(len(self.lista), self.n)

    def test_list_head_empty_list(self):
        """Uma Lista vazia tem None na cabeça"""
        self.assertIsNone(self.lista_vazia.head())

    def test_list_head_one_element_list(self):
        """Uma Lista com 1 elemento tem o primeiro elemento na cabeça"""
        self.assertEqual(self.lista_um.head(), self.x)

    def test_list_head_n_elements_list(self):
        """Uma Lista com n elementos tem o primeiro elemento na cabeça"""
        self.assertEqual(self.lista.head(), self.x)

    def test_list_tail_empty_list(self):
        """Uma Lista vazia tem como Cauda uma Lista Vazia, que é False e tem len zero"""
        self.assertFalse(self.lista_vazia.tail())
        self.assertTrue(self.lista_vazia.tail().is_empty())
        self.assertEqual(len(self.lista_vazia.tail()), 0)

    def test_list_tail_one_element_list(self):
        """Uma Lista com 1 elemento tem como Cauda uma Lista Vazia, que é False e tem len 0"""
        self.assertFalse(self.lista_um.tail())
        self.assertTrue(self.lista_um.tail().is_empty())
        self.assertEqual(len(self.lista_um.tail()), 0)

    def test_list_tail_n_elements_list(self):
        """Uma Lista com n elementos tem como Cauda uma Lista com Tamanho n - 1, True e Não Vazia"""
        self.assertTrue(self.lista.tail())
        self.assertFalse(self.lista.tail().is_empty())
        self.assertEqual(len(self.lista.tail()), len(self.lista) - 1)

    def test_append_turns_empty_list_into_one_element_list(self):
        """Append numa lista vazia transforma numa lista com 1 elemento, com Cabeça"""
        lista_vazia = Lista()
        self.assertFalse(lista_vazia)
        self.assertTrue(lista_vazia.is_empty())
        self.assertEqual(len(lista_vazia), 0)
        self.assertEqual(lista_vazia.head(), None)
        lista_vazia.append(self.x)
        self.assertTrue(lista_vazia)
        self.assertFalse(lista_vazia.is_empty())
        self.assertEqual(len(lista_vazia), 1)
        self.assertEqual(lista_vazia.head(), self.x)

    def test_append_n_elements_list_makes_appended_last_element(self):
        """Append numa lista de n elementos torna o elemento inserido o último"""
        appended = randint(0, 10000)
        self.lista.append(appended)
        cauda = self.lista.tail()
        #iterates over list until it has one element
        while cauda:
          anterior = cauda
          cauda = cauda.tail()
        self.assertEqual(anterior.head(), appended)

    def test_append_n_elements_list_increases_length_by_one(self):
        """Append numa lista de n elementos aumenta seu tamanho em 1"""
        appended = randint(0, 10000)
        size = len(self.lista)
        self.lista.append(appended)
        new_size = len(self.lista)
        self.assertEqual(size + 1, new_size)
        self.assertEqual(self.n + 1, new_size)


    def test_prepend_turns_empty_list_into_one_element_list(self):
        """Prepend numa lista vazia transforma numa lista com 1 elemento, com Cabeça"""
        lista_vazia = Lista()
        self.assertFalse(lista_vazia)
        self.assertTrue(lista_vazia.is_empty())
        self.assertEqual(len(lista_vazia), 0)
        self.assertEqual(lista_vazia.head(), None)
        lista_vazia.prepend(self.x)
        self.assertTrue(lista_vazia)
        self.assertFalse(lista_vazia.is_empty())
        self.assertEqual(len(lista_vazia), 1)
        self.assertEqual(lista_vazia.head(), self.x)

    def test_prepend_n_elements_list_makes_prepended_first_element(self):
        """Prepend numa lista de n elementos torna o elemento inserido o primeiro"""
        prepended = randint(0, 10000)
        old_head = self.lista.head()
        self.lista.prepend(prepended)
        self.assertEqual(self.lista.head(), prepended)
        self.assertNotEqual(self.lista.head(), old_head)
        self.assertEqual(self.lista.tail().head(), old_head)

    def test_prepend_n_elements_list_increases_length_by_one(self):
        """Prepend numa lista de n elementos aumenta seu tamanho em 1"""
        prepended = randint(0, 10000)
        size = len(self.lista)
        self.lista.prepend(prepended)
        new_size = len(self.lista)
        self.assertEqual(size + 1, new_size)
        self.assertEqual(self.n + 1, new_size)


    def test_two_empty_lists_are_equals(self):
        """Duas listas vazias são iguais"""
        self.assertEqual(self.lista_vazia, Lista())
        self.assertEqual(Lista(),Lista())

    def test_two_lists_with_same_elements_are_equals(self):
        """Duas listas distintas com os mesmos elementos são iguais"""
        lista1 = Lista()
        lista2 = Lista()
        self.assertEqual(lista1, lista2)
        for i in range(0, 30): # operações caras :-) append e __eq__
            x = randint(0, 10000)
            self.assertEqual(lista1, lista2)
            lista1.append(x)
            self.assertNotEqual(lista1, lista2)
            lista2.append(x)
            self.assertEqual(lista1, lista2)

    def test_empty_list_n_elements_list_not_equals(self):
        """Uma lista vazia não é igual à uma lista com n elementos"""
        self.assertNotEqual(self.lista_vazia, self.lista)
        self.assertFalse(self.lista_vazia == self.lista)
        self.assertFalse(self.lista == self.lista_vazia)

    def test_str_empty_list(self):
        """Uma lista vazia deve ser representada pela string []"""
        self.assertEqual(str(self.lista_vazia), "[]")

    def test_str_one_element_list(self):
        """Uma lista com somente um elemento x deve ser representada por [x]"""
        self.assertEqual(str(self.lista_um), "[" + str(self.x) + "]")

    def test_str_n_elements_list(self):
        """Uma lista com n elementos imprime como uma lista python"""
        self.assertEqual(str(self.lista), str(self.python_list))

    def test_extend_empty_list(self):
        """Extend numa lista vazia mantém o tamanho igual da segunda lista"""
        lista = Lista()
        self.assertEqual(len(lista), 0)
        lista.extend(Lista())
        self.assertEqual(len(lista), 0)
        size = len(self.lista)
        self.lista_vazia.extend(self.lista)
        self.assertEqual(len(self.lista_vazia), size)

    def test_extend_one_element_list(self):
        """Extend numa lista com 1 elemento resulta num tamanho agregado das duas listas"""
        lista = Lista(42)
        size_um = len(self.lista_um)
        size = len(lista)
        self.lista_um.extend(lista)
        self.assertEqual(len(self.lista_um), size_um + size)

    def test_extend_n_elements_list(self):
        """Extend numa lista com n elementos resulta num tamanho agregado das duas listas"""
        m = randint(200, 400)
        lista = Lista()
        for i in range(0, m):
            lista.append(randint(0, 100))
        size = len(lista)
        size_n = len(self.lista)
        self.assertNotEqual(len(self.lista), size + size_n)
        self.lista.extend(lista)
        self.assertEqual(len(self.lista), size + size_n)

    def test_clear_remove_all_elements(self):
        self.assertEqual(len(self.lista_vazia), 0)
        self.assertNotEqual(len(self.lista_um), 0)
        self.assertNotEqual(len(self.lista), 0)

        self.lista_vazia.clear()
        self.lista_um.clear()
        self.lista.clear()

        self.assertEqual(len(self.lista_vazia), 0)
        self.assertEqual(len(self.lista_um), 0)
        self.assertEqual(len(self.lista), 0)
          
        self.assertEqual(self.lista_um.head(), None)
        self.assertEqual(self.lista.head(), None)
        self.assertEqual(self.lista.tail(), Lista())

    
    def test_contains(self):
        """Verifica se um elemento está na lista"""
        for i in self.python_list:
            not_in_list = (i + self.MAX_VALUE) * 2
            self.assertTrue(i in self.lista)
            self.assertTrue(not_in_list not in self.lista)
            self.assertTrue(self.lista.__contains__(i))
            self.assertFalse(self.lista.__contains__(not_in_list))


    def test_get_item_empty_list(self):
        """Qualquer chave numa lista vazia retorna um erro"""
        with self.assertRaises(KeyError):
            self.lista_vazia[0]
        

    def test_get_item_out_of_bounds(self):
        """Qualquer chave fora dos limites retorna um erro"""
        with self.assertRaises(KeyError):
            self.lista_um[1]
        with self.assertRaises(KeyError):
            size = len(self.lista)
            self.lista[size]
        
    def test_get_item_bounds(self):
        """A primeira chave retorna a cabeça, len - 1 retorna a última"""
        self.assertEqual(self.lista_um.head(), self.lista_um[0])
        self.assertEqual(self.lista_um.head(), self.lista_um[len(self.lista_um) - 1])
        self.assertEqual(self.lista.head(), self.lista[0])
        ultimo_lista = self.python_list[-1]
        self.assertEqual(ultimo_lista, self.lista[len(self.lista) - 1])


    def test_get_rand_position(self):
        """Uma chave aleatória dentro dos limites retorna corretamente"""
        i = randint(0, len(self.lista))
        self.assertEqual(self.lista[i], self.python_list[i])

    def test_get_item_brute_force(self):
        """Testa get item para todos os indices"""
        for i in range(0, self.n):
            self.assertEqual(self.lista[i], self.python_list[i])


    def test_del_item_empty_list(self):
        """Qualquer chave deletada numa lista vazia retorna um erro"""
        with self.assertRaises(KeyError):
            del self.lista_vazia[0]
        

    def test_del_item_out_of_bounds(self):
        """Qualquer chave deletada fora dos limites retorna um erro"""
        with self.assertRaises(KeyError):
            del self.lista_um[1]
        with self.assertRaises(KeyError):
            size = len(self.lista)
            del self.lista[size]
        
    def test_del_item_bounds(self):
        """Deletar a primeira chave faz a segunda ser a primeira. A última, a penúltima ser a última"""
        self.assertEqual(self.lista_um.head(), self.lista_um[0])
        del self.lista_um[0]
        self.assertEqual(self.lista_um.head(), None)
        self.assertEqual(self.lista_um, Lista())
        
        del self.lista[0]
        self.assertEqual(self.lista.head(), self.python_list[1])
      
        del self.lista[len(self.lista) - 1]
        ultimo_lista = self.python_list[-2]
        self.assertEqual(ultimo_lista, self.lista[len(self.lista) - 1])


    def test_del_rand_position(self):
        """Deletar uma chave aleatória dentro dos limites retorna corretamente"""
        i = randint(0, len(self.lista) - 1)
        del self.lista[i]
        self.assertEqual(self.lista[i], self.python_list[i + 1])

    def test_del_item_brute_force(self):
        """Testa del item para lista inteira"""
        for i in range(0, self.n):
            del self.lista[0]
        self.assertEqual(self.lista, Lista())
        with self.assertRaises(KeyError):
            del self.lista[0]
 

    def test_insert_empty_list(self):
        """Inserção numa lista vazia gera erro. Só pode ser usado append ou prepend nelas"""
        with self.assertRaises(KeyError):
            self.lista_vazia.insert(0, self.x)

    def test_insert_first_position(self):
        """Inserção funciona na primeira posição, desde que a lista não seja vazia"""
        y = randint(0, self.MAX_VALUE)
        old_head = self.lista_um.head()
        self.lista_um.insert(0, y)
        self.assertEqual(self.lista_um.head(), y)
        self.assertEqual(self.lista_um.tail().head(), old_head)

    def test_insert_random_position(self):
        """Inserção numa posição aleatória entre 1 e len(lista) -1"""
        i = randint(1, len(self.lista) - 1)
        y = randint(0, self.MAX_VALUE)
        self.lista.insert(i, y)
        self.assertEqual(self.lista[i], y)
        self.assertEqual(self.lista[i - 1], self.python_list[i - 1])
        self.assertEqual(self.lista[i + 1], self.python_list[i])


    def test_insert_makes_list(self):
        """Inserção pode ser usada para construir uma lista igual a já existente"""
        lista = Lista(self.python_list[-1])
        for y in reversed(self.python_list[:-1]):
            lista.insert(0, y)
        self.assertEqual(lista, self.lista)

    def test_index_empty_list(self):
        """Index de lista vazia retorna um erro"""
        with self.assertRaises(ValueError):
            self.lista_vazia.index(self.x)

    def test_index_one_element_list_returns_0(self):
        """Index numa lista com um elemento retorna 0"""
        self.assertEqual(self.lista_um.index(self.x), 0)

    def test_index_n_elements_list(self):
        """Index de uma lista com n elementos retorna o índice correto"""
        random_index = randint(0, len(self.lista))
        random_element = self.python_list[random_index]
        self.assertEqual(self.lista.index(random_element), random_index)

    def test_index_brute_force(self):
        """Testa o índice de todos os elementos da lista - a lista não pode ter repetidos"""
        lista = Lista()
        for i in range(0, 100):
            lista.append(i)
        for i in range(0, len(lista)):
            self.assertEqual(i, lista.index(lista[i]))

    def test_count_empty_list(self):
        """Count numa lista vazia sempre retorna zero"""
        x = randint(0, maxsize)
        self.assertEqual(self.lista_vazia.count(x), 0)

    def test_count_one_element_list(self):
        """Count numa lista com 1 elemento pode retornar zero ou 1, depende se existe"""
        head = self.lista_um.head()
        self.assertEqual(self.lista_um.count(head), 1)
        self.assertEqual(self.lista_um.count(head - 1), 0)

    def test_count_n_elements_list_same_element(self):
        """Count numa lista com o mesmo elemento retorna o tamanho da lista"""
        x = randint(0, maxsize)
        lista = Lista()
        for i in range(0, self.MAX_VALUE):
            lista.prepend(x)
        self.assertEqual(lista.count(x), len(lista))

    def test_count_same_behavior_python_count(self):
        """Count retorna o mesmo valor que o count do python"""
        for i in range(0, len(self.lista)):
            self.assertEqual(self.lista.count(self.lista[i]), \
              self.python_list.count(self.python_list[i]))

    def test_remove_item_empty_list(self):
        """Qualquer chave removida numa lista vazia retorna um erro"""
        with self.assertRaises(KeyError):
            x = randint(0, self.MAX_VALUE)
            self.lista_vazia.remove(x)
        

    def test_remove_item_one_element_list(self):
        """Remover a cabeça de uma lista de um elemento a torna numa lista vazia"""
        head = self.lista_um.head()
        self.lista_um.remove(head)
        self.assertEqual(self.lista_um, Lista())      



    def test_remove_rand_position(self):
        """Remover um elemento aleatório dentro dos limites diminui o tamanho em 1"""
        lista = Lista()
        for i in range(0, self.MAX_VALUE):
            lista.prepend(i)
        size = len(lista)
        i = randint(0, size - 1)
        x =  lista[i]
        lista.remove(x)
        self.assertEqual(len(lista), size - 1)

    def test_remove_item_brute_force(self):
        """Testa remove item para lista inteira"""
        for i in range(0, self.n):
            self.lista.remove(self.lista[0])
        self.assertEqual(self.lista, Lista())
        with self.assertRaises(KeyError):
            self.lista.remove(i)

    def test_reversed_empty_list(self):
        """O reverso de uma lista vazia é uma lista vazia"""
        self.assertEqual(reversed(self.lista_vazia), self.lista_vazia)
      
    def test_reversed_one_element_list(self):
        """O reverso de uma lista com 1 elemento é ela mesma"""
        self.assertEqual(reversed(self.lista_um), self.lista_um)

    def test_reversed_n_elements_list(self):
        """O reverso de uma lista com n elementos, o último é o primeiro e vice-versa"""
        self.assertEqual(reversed(self.lista).head(), self.python_list[-1])
        nova_lista = reversed(self.lista)
        ultimo = nova_lista[len(nova_lista) - 1]
        self.assertEqual(ultimo, self.lista.head())


    def test_reversed_str_n_elements_list(self):
        """Testa a impressão de uma lista reversa de n elementos"""
        self.assertEqual(str(reversed(self.lista)), str(list(reversed(self.python_list))))

if __name__ == '__main__':
    unittest.main(verbosity=2)
