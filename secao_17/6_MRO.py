"""
POO - Method Resolution Order (MRO)

É a ordem de execução dos métodos.

Em Python, a gente pode conferir a ordem de execução dos métodos (MNRO) de 3 formas:
    - Via propriedade de classe __mro__
    - Via método mro()
    - Via help()
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou{self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):  # a ordem dos argumentos influencia o MRO

    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim('tux')
# print(tux.cumprimentar())  # a ordem vai influenciar essa saída

print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))
