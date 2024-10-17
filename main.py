from pousada import Pousada

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

def main():
    pousada = Pousada()
    pousada.carrega_dados()

    print(f"\nBem-vindo à {pousada.nome}{pousada.contato}")

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
            data = input("Informe a data (DD/MM/AAAA): ")
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            pousada.consulta_reserva(data, cliente, numero_quarto)

        elif opcao == "3":
            data_inicio = input("Informe a data inicial (DD/MM/AAAA): ")
            data_fim = input("Informe a data final (DD/MM/AAAA): ")
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            quarto = next((q for q in pousada.quartos if q.numero == numero_quarto), None)
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
            produto = input("Informe o nome do produto: ")
            quantidade = int(input("Informe a quantidade: "))
            pousada.registra_consumo(cliente, produto, quantidade)

        elif opcao == "8":
            pousada.salva_dados("pousada.txt", "quarto.txt", "reserva.txt", "produto.txt")
            print("Dados salvos com sucesso.")

        elif opcao == "0":
            print("Salvando dados antes de sair...")
            pousada.salva_dados("pousada.txt", "quarto.txt", "reserva.txt", "produto.txt")
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()