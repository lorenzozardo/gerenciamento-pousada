# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa
from pousada import Pousada

# Menu printado
def exibir_menu():
    print("\nMenu:")
    print("1 - Consultar disponibilidade")
    print("2 - Consultar reserva")
    print("3 - Realizar reserva")
    print("4 - Cancelar reserva")
    print("5 - Realizar check-in")
    print("6 - Realizar check-out")
    print("7 - Registrar consumo")
    print("8 - Salvar")
    print("0 - Sair")


# Função principal que gerencia o sistema, interagindo com o menu printado
def main():
    pousada = Pousada()
    pousada.carrega_dados()

    print(f"\nBem-vindo à {pousada.__str__()}")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = input("Informe a data (DD/MM/AAAA): ")
            numero_quarto = int(input("Informe o número do quarto: "))
            if pousada.consulta_disponibilidade(data, numero_quarto):
                print("Quarto disponível.")
            else:
                print("Quarto não disponível.")

        elif opcao == "2":
            cliente = input("Informe o nome do cliente: ")
            pousada.consulta_reserva(cliente)

        elif opcao == "3":
            data_inicio = input("Informe a data inicial (DD/MM/AAAA): ")
            data_fim = input("Informe a data final (DD/MM/AAAA): ")
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            quarto = None
            for q in pousada.quartos:
                if q.numero == numero_quarto:
                   quarto = q
                   break 
            if quarto:
                pousada.realiza_reserva(data_inicio, data_fim, cliente, quarto)
            else:
                print("Quarto não encontrado.")
                if quarto:
                    pousada.realiza_reserva(data_inicio, data_fim, cliente, quarto)
                else:
                    print("Quarto não encontrado.")

        elif opcao == "4":
            cliente = input("Informe o nome do cliente: ")
            pousada.cancela_reserva(cliente)

        elif opcao == "5":
            cliente = input("Informe o nome do cliente: ")
            pousada.realiza_checkin(cliente)

        elif opcao == "6":
            cliente = input("Informe o nome do cliente: ")
            pousada.realiza_checkout(cliente)

        elif opcao == "7":
            cliente = input("Informe o nome do cliente: ")
            pousada.registra_consumo(cliente)

        elif opcao == "8":
            pousada.Salva_dados()

        elif opcao == "0":
            print("Salvando dados antes de sair...")
            pousada.Salva_dados()
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()