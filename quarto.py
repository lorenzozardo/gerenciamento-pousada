# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa

class Quarto:
    def __init__(self, numero: int, categoria: str, diaria: float):
        self.__numero = numero
        self.__categoria = categoria
        self.__diaria = diaria
        self.__consumo = []

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

    def adiciona_consumo(self, valor: int):
        self.__consumo.append(valor)

    def lista_consumo(self):
        return self.__consumo

    def valor_total_consumo(self):
        return sum(self.__consumo)

    def limpa_consumo(self):
        self.__consumo.clear()