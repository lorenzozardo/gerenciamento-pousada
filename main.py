# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa
# A função main deve conter apenas a manipulação do menu.

from pousada import Pousada
from quarto import Quarto
from reserva import Reserva

def exibir_menu():
    print("\nMenu:")
    print("1 - Consultar disponibilidade")
    print("2 - Consultar reserva")
    print("3 - Realizar reserva")
    print("4 - Cancelar reserva")
    print("5 - Realizar check-in")
    print("6 - Realizar check-out")
    print("0 - Sair")

def main():
    # Inicializando a pousada com dados fictícios (ou carregue de arquivo usando `carrega_dados`)
    pousada = Pousada("Pousada do Sol", "contato@pousadasol.com")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Consultar disponibilidade
            data = int(input("Informe a data (em formato de número inteiro): "))
            numero_quarto = int(input("Informe o número do quarto: "))
            quarto = next((q for q in pousada.quartos if q.numero == numero_quarto), None)
            if quarto:
                disponibilidade = pousada.consulta_disponibilidade(data, quarto)
                if disponibilidade:
                    print(f"O quarto {numero_quarto} está disponível na data {data}.")
                else:
                    print(f"O quarto {numero_quarto} está indisponível na data {data}.")
            else:
                print("Quarto não encontrado.")

        elif opcao == "2":
            # Consultar reserva
            data = int(input("Informe a data (em formato de número inteiro): "))
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            quarto = next((q for q in pousada.quartos if q.numero == numero_quarto), None)
            if quarto:
                reserva = pousada.consulta_reserva(data, cliente, quarto)
                if reserva:
                    print(f"Reserva encontrada: Cliente {reserva.cliente}, "
                          f"Quarto {reserva.quarto.numero}, "
                          f"Período: {reserva.dia_inicio} a {reserva.dia_fim}, Status: {reserva.status}.")
                else:
                    print("Nenhuma reserva encontrada para os dados fornecidos.")
            else:
                print("Quarto não encontrado.")

        elif opcao == "3":
            # Realizar reserva
            data_inicio = int(input("Informe a data de início: "))
            data_fim = int(input("Informe a data de fim: "))
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            quarto = next((q for q in pousada.quartos if q.numero == numero_quarto), None)
            if quarto:
                sucesso = pousada.realiza_reserva(data_inicio, data_fim, cliente, quarto)
                if sucesso:
                    print(f"Reserva realizada com sucesso para o cliente {cliente}.")
                else:
                    print(f"Não foi possível realizar a reserva para o cliente {cliente}.")
            else:
                print("Quarto não encontrado.")

        elif opcao == "4":
            # Cancelar reserva
            cliente = input("Informe o nome do cliente: ")
            sucesso = pousada.cancela_reserva(cliente)
            if sucesso:
                print(f"Reserva do cliente {cliente} cancelada com sucesso.")
            else:
                print(f"Não foi possível cancelar a reserva do cliente {cliente}.")

        elif opcao == "5":
            # Realizar check-in
            cliente = input("Informe o nome do cliente: ")
            sucesso = pousada.realiza_checkin(cliente)
            if sucesso:
                print(f"Check-in realizado para o cliente {cliente}.")
            else:
                print(f"Não foi possível realizar o check-in do cliente {cliente}.")

        elif opcao == "6":
            # Realizar check-out
            cliente = input("Informe o nome do cliente: ")
            sucesso = pousada.realiza_checkout(cliente)
            if sucesso:
                print(f"Check-out realizado para o cliente {cliente}.")
            else:
                print(f"Não foi possível realizar o check-out do cliente {cliente}.")

        elif opcao == "0":
            # Sair
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()