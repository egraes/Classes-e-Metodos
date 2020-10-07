class Escritor:
    def __init__(self,nome):
        self.__nome = nome
        self.__ferramenta = None
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self,marca):
        self.__marca = marca
    def escrever():
        print('Caneta está escrevendo...')

    @property
    def marca(self):
        return self.__marca

class Lapis:
    def __init__(self,marca):
        self.__marca = marca
    def escrever():
        print('Lápis esta escrevendo...')
    @property
    def marca(self):
        return self.__marca

escritor = Escritor('Eduardo')
caneta   = Caneta('Bic')
lapis    = Lapis('Faber')
escritor.ferramenta = Caneta



print(escritor.nome)
print(caneta.marca)
print(lapis.marca)

escritor.ferramenta.escrever()
