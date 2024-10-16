# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa

class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    def __self__(self):
        return f"{self.codigo},{self.nome},{self.preco}"