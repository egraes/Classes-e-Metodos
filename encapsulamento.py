class BaseDedados:
    def __init__(self):
        self.__dados = {}
    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes']={id: nome}
        else:
            self.__dados['clientes'].update({id:nome})
    def lista_clientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(id,nome)
    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]


bd = BaseDedados()

bd.inserir_cliente(1,'Eduardo')
bd.inserir_cliente(2,'Joao')
bd.inserir_cliente(3,'Maria')
bd.inserir_cliente(4,'Pedro')

bd.lista_clientes()
print()
bd.apaga_cliente(3)
bd.lista_clientes()