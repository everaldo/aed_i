


from compara import Compara
from troca import Troca

class SmokeTest(Compara, Troca):

    def __init__(self, v):
        self.v = v


    def sort(self):
      list.sort(self.v)

    def report(self):
      pass
