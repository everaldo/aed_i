# encoding: utf-8
#
# Prof. Everaldo Gomes - everaldo.gomes@pucpr.br
# Data: 02/09/2015
#
#



import unittest
import random
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):


    def setUp(self):
        """Test setup"""
        self.empty_list = LinkedList()
        self.A_LIST_HEAD = 42
        self.a_list = LinkedList(self.A_LIST_HEAD)



    def test_new_list(self):
        """A criação de uma Nova Lista"""
        self.assertIsInstance(self.empty_list, LinkedList)


    def test_new_list_empty(self):
        """Uma Nova Lista criada sem parâmetros é vazia"""
        self.assertTrue(self.empty_list.is_empty())


    def test_empty_list_equality(self):
        """Listas Vazias são iguais"""
        a = LinkedList()
        b = LinkedList()
        self.assertEqual(self.empty_list, a)
        self.assertEqual(self.empty_list, b)
        self.assertEqual(a, b)


    def test_new_list_not_empty_with_value(self):
        """Uma Nova Lista criada com parâmetros é não-vazia"""
        self.assertFalse(self.a_list.is_empty())


    def test_empty_list_size(self):
        """Uma Lista vazia possui tamanho zero"""
        self.assertEqual(self.empty_list.size(), 0)

    def test_a_list_with_one_element_size_is_one(self):
        """Uma Lista com um elemento possui tamanho 1"""
        self.assertEqual(self.a_list.size(), 1)

    def test_a_list_head_is_the_first_element(self):
        """A cabeça de uma lista é seu primeiro elemento"""
        """Caso a lista seja vazia, o valor da cabeça é None"""
        self.assertEqual(self.empty_list.head().value,None)
        self.assertEqual(self.a_list.head().value, self.A_LIST_HEAD)


    def test_a_list_tail_is_the_rest_of_the_list(self):
        """A cauda de uma lista são todos os elementos menos a cabeça"""
        """Caso a lista seja vazia ou tenha somente um elemento,
            a Cauda é uma Lista Vazia"""
        self.assertEqual(self.empty_list.tail(),LinkedList())
        self.assertEqual(self.a_list.tail(), LinkedList() )


    def test_append_changes_list_size(self):
        """Append insere um elemento no final da lista"""
        """A operação append aumenta o tamanho da lista em 1"""
        size = self.a_list.size()
        self.a_list.append(55)
        new_size = size + 1
        self.assertEqual(self.a_list.size(), new_size)


    def test_append_changes_list_size_multiple_elements(self):
        """X appends aumentam o tamanho da lista em X elementos"""
        size = self.a_list.size()
        x = random.randint(1, 200)
        for i in range(0, x):
            value = random.randint(1, 10000)
            self.a_list.append(value)
        new_size = size + x
        self.assertEqual(self.a_list.size(), new_size)


    def test_append_empty_list_appended_element_is_head(self):
        """Append numa lista vazia torna o novo elemento a cabeça da lista"""
        self.assertTrue(self.empty_list.is_empty())
        self.assertTrue(self.empty_list.head().is_empty())
        x = 42
        self.empty_list.append(x)
        self.assertEqual(self.empty_list.head().value, x)


    def test_prepend_changes_list_size(self):
        """Prepend insere um elemento no início da lista"""
        """A operação prepend aumenta o tamanho da lista em 1"""
        size = self.a_list.size()
        self.a_list.prepend(98)
        new_size = size + 1
        self.assertEqual(self.a_list.size(), new_size)


    def test_prepend_changes_list_size_multiple_elements(self):
        """X prepends aumentam o tamanho da lista em X elementos"""
        size = self.a_list.size()
        x = random.randint(1, 200)
        for i in range(0, x):
            value = random.randint(1, 10000)
            self.a_list.prepend(value)
        new_size = size + x
        self.assertEqual(self.a_list.size(), new_size)


    def test_prepend_empty_list_prepended_element_is_head(self):
        """Prepend numa lista vazia torna o novo elemento a cabeça da lista"""
        self.assertTrue(self.empty_list.is_empty())
        self.assertTrue(self.empty_list.head().is_empty())
        x = 42
        self.empty_list.prepend(x)
        self.assertEqual(self.empty_list.head().value, x)


    def test_head_size_plus_tail_size_is_equal_list_size(self):
        """O tamanho da cabeça mais o tamanho da cauda é igual o tamanho da lista"""
        random_list = self.create_random_list()
        size = random_list.size()
        head_size = random_list.head().size()
        tail_size = random_list.tail().size()
        self.assertEqual(size, head_size + tail_size)



    def test_str_empty_list(self):
        """Uma lista vazia imprime como []"""
        self.assertEqual(str(self.empty_list), '[]')

    def test_str_one_element_list(self):
        """Uma lista com 1 elemento imprime como [X]"""
        self.assertEqual(str(self.a_list), '[' + str(self.A_LIST_HEAD) + ']')

    def test_str_multiple_elements(self):
        list = LinkedList(0)
        list.append(1)
        list.append(1)
        list.append(2)
        list.append(3)
        list.append(5)
        list.append(8)
        self.assertEqual(str(list), '[0, 1, 1, 2, 3, 5, 8]')



    def create_random_list(self):
        random_list = LinkedList()
        x = random.randint(1, 200)
        for i in range(0, x):
            value = random.randint(1, 10000)
            random_list.append(value)
        return random_list


if __name__ == '__main__':
    unittest.main(verbosity=2)

