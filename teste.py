# -*- coding: utf-8 -*-

class Teste:
    def __init__(self, nome):
         self._nome = nome

    @property
    def nome(self):
         # Este código é executado quando alguém for
         # ler o valor de self.nome
         return self._nome

    @nome.setter
    def nome(self, nome):
        if(isinstance(nome, str)):
            self._nome = nome
        else:
            raise TypeError('Parameter \'nome\' <type \'Str\'> is expected but found is: ' + str(type(nome)))

try:
    t = Teste('casa')
    print(t.nome)
    t.nome = 15
    print(t.nome)
except TypeError as err:
    print(args[0])
