# encoding: utf-8
#
# Prof. Everaldo Gomes - everaldo.gomes@pucpr.br
# Data: 02/09/2015
#
#


### Renomeie este arquivo para linkedlist.py

# Implemente os métodos: size, head, tail, append e prepend


class LinkedList:

    def __init__(self, value = None):
        self.value = value
        self.next = None

    def is_empty(self):
        pass

    def size(self):
        pass

    def head(self):
        pass

    def tail(self):
        pass

    def append(self, value):
        pass

    def prepend(self, value):
        pass

    def __eq__(self, other):
        if not type(other) is LinkedList:
            return False
        if other.is_empty():
            if self.is_empty():
                return True;
            else:
                return False
        if other.value == self.value and \
            other.next  == self.next:
              return True
        else:
              return False


    def __str__(self):
        return "[" + str(self.__str_values__()) + "]"

    def __str_values__(self):
        if self.is_empty():
            return ""
        elif self.next is None:
            return str(self.value)
        else:
            return str(self.value) + ", " + self.next.__str_values__()




