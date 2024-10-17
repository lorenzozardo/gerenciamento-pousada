# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa

from quarto import Quarto
from reserva import Reserva
from produto import Produto

class Pousada:
    # Método construtor de Pousada
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

    # Carrega os dados da pousada, seus quartos, reservas e produtos, a partir de arquivos .txt
    def carrega_dados(self):
        try:
            with open("pousada.txt", "r", encoding="utf-8") as f:
                self.__nome = f.readline()
                self.__contato = f.readline()

            with open("quarto.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    dados_quarto = linha.split(";")

                    numero = int(dados_quarto[0])
                    categoria = dados_quarto[1]
                    diaria = float(dados_quarto[2])

                    quarto = Quarto(numero, categoria, diaria, consumo=list)
                    self.__quartos.append(quarto)

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

            with open("produto.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    dados_produtos = linha.split(";")

                    codigo = int(dados_produtos[0])
                    nome = dados_produtos[1]
                    preco = float(dados_produtos[2])

                    produto = Produto(codigo, nome, preco)
                    self.__produtos.append(produto)

            print("Dados carregados com sucesso!")

        except:
            print(f"Erro ao carregar os dados.")


    # Salva os dados da pousada em arquivos .txt
    def Salva_dados(nome_arquivo):
        try:
            with open("reserva.txt", "r", encoding="utf-8") as f:
             linhas = f.readlines()

             novas_linhas = [linha for linha in linhas if not linha.strip().endswith(("C", "O"))]

            with open("reserva.txt", "w", encoding="utf-8") as f:
             f.writelines(novas_linhas)

            print(f"Linhas que terminam com 'C' ou 'O' foram removidas de {nome_arquivo} com sucesso!")

        except Exception as e:
         print(f"Erro ao tentar modificar o arquivo: {e}")


    # Verifica se o quarto está disponível para uma data específica
    def consulta_disponibilidade(self, data, numero_quarto):
        for reserva in self.__reservas:
            if reserva.quarto == numero_quarto and reserva.dia_inicio <= data <= reserva.dia_fim:
                return False
        return True

    # Consulta uma reserva específica por data, cliente e quarto
    def consulta_reserva(self, cliente: str):
        for reserva in self.__reservas:
            if reserva.cliente == cliente:
                print("")
                print(reserva.dia_inicio + " " + reserva.dia_fim+" "+reserva.cliente+" "+str(reserva.quarto)+" "+reserva.status)
            elif reserva.cliente != cliente:
                print("", end="")

    # Realiza uma reserva se o quarto estiver disponível no período solicitado
    def realiza_reserva(self, data_inicio: int, data_fim: int, cliente: str, quarto: Quarto):
        if self.consulta_disponibilidade(data_inicio, quarto):
            nova_reserva = Reserva(data_inicio, data_fim, cliente, quarto, "A")
            self.__reservas.append(nova_reserva)
            
            with open("reserva.txt", "a") as arquivo:
                linha = f"{data_inicio};{data_fim};{cliente};{quarto.numero};A"
                arquivo.write(linha)
            
            print("Reserva realizada com sucesso!")
            return True
        
        print("Quarto indisponível para as datas selecionadas.")
        return False

    # Cancela uma reserva do cliente
    def cancela_reserva(self, cliente: str):
        reservas_atualizadas = []
        reserva_encontrada = False
        
        with open("reserva.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
        for linha in linhas:
            dados = linha.strip().split(";")
            nome_cliente = dados[2]
            status = dados[4]
            
            if nome_cliente == cliente and status == "A":
                dados[4] = "C"
                reserva_encontrada = True

            linha_atualizada = ";".join(dados)+"\n"
            reservas_atualizadas.append(linha_atualizada)
        
        if reserva_encontrada:
            with open("reserva.txt", "w") as arquivo:
                arquivo.writelines(reservas_atualizadas)
            print(f"Reserva de {cliente} cancelada com sucesso!")
            return True
        else:
            print(f"Reserva ativa para {cliente} não encontrada.")
            return False
        

    # Realiza o check-in do cliente se houver uma reserva ativa
    def realiza_checkin(self, cliente: str):
        reservas_atualizadas = []
        reserva_encontrada = False
        
        with open("reserva.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
        for linha in linhas:
            dados = linha.strip().split(";")
            nome_cliente = dados[2]
            status = dados[4]
            
            if nome_cliente == cliente and status == "A":
                dados[4] = "I"
                reserva_encontrada = True

            linha_atualizada = ";".join(dados)+"\n"
            reservas_atualizadas.append(linha_atualizada)
        
        if reserva_encontrada:
            with open("reserva.txt", "w") as arquivo:
                arquivo.writelines(reservas_atualizadas)
            print(f"Check-in de {cliente} realizado com sucesso!")
            return True
        else:
            print(f"Reserva ativa para {cliente} não encontrada.")
            return False

    # Realiza o check-out do cliente e encerra a reserva
    def realiza_checkout(self, cliente: str):
        reservas_atualizadas = []
        reserva_encontrada = False
        
        with open("reserva.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
        for linha in linhas:
            dados = linha.strip().split(";")
            nome_cliente = dados[2]
            status = dados[4]
            
            if nome_cliente == cliente and status == "I":
                dados[4] = "O"
                reserva_encontrada = True

            linha_atualizada = ";".join(dados)+"\n"
            reservas_atualizadas.append(linha_atualizada)
        
        if reserva_encontrada:
            with open("reserva.txt", "w") as arquivo:
                arquivo.writelines(reservas_atualizadas)
            print(f"Check-out de {cliente} realizado com sucesso!")
            return True
        else:
            print(f"Check-in ativo para {cliente} não encontrada.")
            return False