# encoding: utf-8
#
# Prof. Everaldo Gomes - everaldo.gomes@pucpr.br
# Data: 02/09/2015
#
#


class LinkedList:

    def __init__(self, value = None):
        self.value = value
        self.next = None

    def is_empty(self):
        return self.value == None


    def size(self):
        if self.is_empty():
            return 0
        else:
            if not self.next is None:
                return 1 + self.next.size()
            else:
                return 1


    def head(self):
        return self


    def tail(self):
        return LinkedList()


    def append(self, value):
        if self.value is None:
            self.value = value
        elif self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.append(value)
        

    def prepend(self, value):
        if self.value is None:
            self.value = value
        else:
            link = LinkedList(self.value)
            link.next = self.next
            self.value = value
            self.next = link


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




