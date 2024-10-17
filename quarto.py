# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa

class Quarto:
    # Método construtor do quarto
    def __init__(self, numero: int, categoria: str, diaria: float, consumo: list):
        self.__numero = numero
        self.__categoria = categoria
        self.__diaria = diaria
        self.__consumo = consumo

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def diaria(self):
        return self.__diaria
    
    @diaria.setter
    def diaria(self, diaria):
        self.__diaria = diaria 

    @property
    def consumo(self):
        return self.__consumo
    
    @consumo.setter
    def consumo(self, consumo):
        self.__consumo = consumo

    # Adiciona um produto consumido a lista de consumo
    def adiciona_consumo(self, produto: int):
        self.__consumo.append(produto)

    
    def lista_consumo(self):
        return self.__consumo

    # Calcula o valor total dos produtos consumidos
    def valor_total_consumo(self, produtos: list):
        total = 0
        for codigo in self.consumo:
            for produto in produtos:
                if produto.codigo == codigo:
                    total += produto.preco

        return total

    # Reseta a lista de consumo após o check-out
    def limpa_consumo(self):
        self.__consumo = []