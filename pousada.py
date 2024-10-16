# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa

from quarto import Quarto
from reserva import Reserva
from produto import Produto

class Pousada:
    def __init__(self, nome: str = "", contato: str = ""):
        self.__nome = nome
        self.__contato = contato
        self.__quartos = []
        self.__reservas = []
        self.__produtos = []
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, contato):
        self.__contato = contato 

    @property
    def quartos(self):
        return self.__quartos

    # Carrega os dados da pousada, seus quartos, reservas e produtos, a partir de arquivos .txt
    def carrega_dados(self):
        try:
            # Carrega os dados da pousada
            with open("pousada.txt", "r", encoding="utf-8") as f:
                self.__nome = f.readline()
                self.__contato = f.readline()

            # Carrega os dados dos quartos
            with open("quarto.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    dados_quarto = linha.split(";")

                    numero = int(dados_quarto[0])
                    categoria = dados_quarto[1]
                    diaria = float(dados_quarto[2])

                    quarto = Quarto(numero, categoria, diaria, consumo=list)
                    self.__quartos.append(quarto)

            # Carrega os dados das reservas
            with open("reserva.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    dados_reservas = linha.split(";")

                    dia_inicio = dados_reservas[0]
                    dia_fim = dados_reservas[1]
                    cliente = dados_reservas[2]
                    categoria_quarto = int(dados_reservas[3])
                    status = dados_reservas[4]

                    reserva = Reserva(dia_inicio, dia_fim, cliente, categoria_quarto, status)
                    self.__reservas.append(reserva)

            # Carrega os dados das produtos
            with open("produto.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    dados_produtos = linha.split(";")

                    codigo = int(dados_produtos[0])
                    nome = dados_produtos[1]
                    preco = float(dados_produtos[2])

                    produto = Produto(codigo, nome, preco)
                    self.__produtos.append(produto)

            print("Dados carregados com sucesso!")

        # Caso ocorra um erro ao carregar os dados de algum arquivo, exibe a mensagem de erro
        except:
            print(f"Erro ao carregar os dados.")


    # Salva os dados da pousada, seus quartos, reservas e produtos em arquivos .txt
    def salva_dados(self, arquivo_pousada: str, arquivo_quartos: str, arquivo_reservas: str, arquivo_produtos: str):
        try:
            # Salva os dados da pousada
            with open(arquivo_pousada, "w") as f:
                f.write(f"{self.__nome}\n")
                f.write(f"{self.__contato}\n")

            # Salva os dados dos quartos
            with open(arquivo_quartos, "w") as f:
                for quarto in self.__quartos:
                    f.write(f"{quarto.numero()};{quarto.categoria()};{quarto.diaria()}")

            # Salva os dados das reservas
            with open(arquivo_reservas, "w") as f:
                for reserva in self.__reservas:
                    f.write(f"{reserva.dia_inicio()};{reserva.dia_fim()};{reserva.cliente()};{reserva.quarto()};{reserva.status()}")

            # Salva os dados dos produtos
            with open(arquivo_produtos, "w") as f:
                for produto in self.__produtos:
                    f.write(f"{produto.codigo()};{produto.nome()};{produto.preco()}")
        
            print("Dados salvos com sucesso!")

        # Caso ocorra um erro ao tentar salvar os dados de algum arquivo, exibe a mensagem de erro
        except:
            print("Erro ao salvar os dados.")

    # Verifica se o quarto está disponível para uma data específica
    def consulta_disponibilidade(self, data, numero_quarto):
        for reserva in self.__reservas:
            if reserva.quarto().numero_quarto() == numero_quarto and reserva.dia_inicio() <= data <= reserva.dia_fim():
                return False
        return True

    # Consulta uma reserva específica por data, cliente e quarto
    def consulta_reserva(self, data: int, cliente: str, quarto: Quarto):
        for reserva in self.__reservas:
            if reserva.quarto == quarto and reserva.cliente == cliente and data >= reserva.data_inicio and data <= reserva.data_fim:
                return reserva
        return None

    # Realiza uma reserva se o quarto estiver disponível no período solicitado
    def realiza_reserva(self, data_inicio: int, data_fim: int, cliente: str, quarto: Quarto):
        if self.consulta_disponibilidade(data_inicio, quarto):
            nova_reserva = Reserva(data_inicio, data_fim, cliente, quarto, "A")
            self.__reservas.append(nova_reserva)
            print("Reserva realizada com sucesso!")
            return True
        
        print("Quarto indisponível para as datas selecionadas.")
        return False

    # Cancela uma reserva do cliente
    def cancela_reserva(self, cliente: str):
        for reserva in self.__reservas:
            if reserva.cliente == cliente and reserva.status == "A":
                reserva.status = "C"
                print(f"Reserva de {cliente} cancelada.")
                return True
        print(f"Nenhuma reserva ativa encontrada para {cliente}.")
        return False

    # Realiza o check-in do cliente se houver uma reserva ativa
    def realiza_checkin(self, cliente: str):
        for reserva in self.__reservas:
            if reserva.cliente == cliente and reserva.status == "A":
                reserva.status = "I"
                print(f"Check-in realizado para o cliente {cliente}!")
                return True
            
        print(f"Erro! Cliente {cliente} não possui nenhuma reserva ativa.")
        return False

    # Realiza o check-out do cliente e encerra a reserva
    def realiza_checkout(self, cliente: str):
        for reserva in self.__reservas:
            if reserva.cliente == cliente and reserva.status == "I":
                reserva.status = "O"
                print(f"Check-out do cliente {cliente} realizado com sucesso!")
                return True
        print(f"Check-out do cliente {cliente} não pode ser realizado.")
        return False