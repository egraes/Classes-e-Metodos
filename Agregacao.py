class Carrinho:
    def __init__(self):
        self.produtos = []
        
    def adiciona (self,produto):
        self.produtos.append(produto)
    def lista(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self,nome,valor):
        
        self.nome = nome
        self.valor = valor
    

carrinho = Carrinho()
p1 = Produto('Caneca', 15)
p2 = Produto('Camiseta', 25)


carrinho.adiciona(p1)
carrinho.adiciona(p2)
carrinho.adiciona(p1)
carrinho.adiciona(p2)
carrinho.adiciona(p2)


carrinho.lista()
print(carrinho.soma_total())
