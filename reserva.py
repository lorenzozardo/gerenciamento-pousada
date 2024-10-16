# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa

from quarto import Quarto

class Reserva:
    def __init__(self, dia_inicio: int, dia_fim: int, cliente: str, quarto: Quarto, status: str):
        self.__dia_inicio = dia_inicio
        self.__dia_fim = dia_fim
        self.__cliente = cliente
        self.__quarto = quarto
        self.__status = status

    @property
    def dia_inicio(self):
        return self.__dia_inicio
    
    @dia_inicio.setter
    def dia_inicio(self, dia_inicio):
        self.__dia_inicio = dia_inicio

    @property
    def dia_fim(self):
        return self.__dia_fim
    
    @dia_fim.setter
    def dia_fim(self, dia_fim):
        self.__dia_fim = dia_fim

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def quarto(self):
        return self.__quarto
    
    @quarto.setter
    def quarto(self, quarto):
        self.__quarto = quarto
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    def __str__(self):
        return f"{self.__inicio},{self.__fim},{self.__cliente},{self.__quarto.get_numero()},{self.__status}"