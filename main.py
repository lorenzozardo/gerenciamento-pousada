# Lorenzo Zardo Danzmann e João Victor Cardoso Barbosa
# A função main deve conter apenas a manipulação do menu.

from pousada import Pousada
from quarto import Quarto
from reserva import Reserva
from produto import Produto

def main():
    pousada = Pousada()
    pousada.carrega_dados()

    while True:
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

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = input("Informe a data (YYYY-MM-DD): ")
            numero_quarto = int(input("Informe o número do quarto: "))
            
            if pousada.consulta_disponibilidade(data, numero_quarto):
                quarto = None
                for q in pousada.quartos:
                    if q.numero == numero_quarto:
                        quarto = q
                        break
                
                if quarto:
                    print(f"Quarto {quarto.numero}, Categoria: {quarto.categoria}, Diária: {quarto.diaria}")
                else:
                    print("Quarto não encontrado.")
            else:
                print("Quarto indisponível na data informada.")

        elif opcao == "2":
            data = input("Informe uma data (YYYY-MM-DD) ou deixe em branco: ")
            cliente = input("Informe o nome do cliente ou deixe em branco: ")
            numero_quarto = input("Informe o número do quarto ou deixe em branco: ")

            reservas = []
            for reserva in pousada.reservas:
                if ((data == "" or reserva.dia_inicio <= data <= reserva.dia_fim) and
                    (cliente == "" or reserva.cliente == cliente) and
                    (numero_quarto == "" or reserva.quarto.numero == int(numero_quarto))):
                    reservas.append(reserva)

            if reservas:
                for reserva in reservas:
                    print(f"Reserva de {reserva.cliente} - Início: {reserva.dia_inicio}, Fim: {reserva.dia_fim}, Quarto: {reserva.quarto.numero}, Status: {reserva.status}")
            else:
                print("Nenhuma reserva encontrada.")

        elif opcao == "3":
            data_inicio = input("Informe a data de início (YYYY-MM-DD): ")
            data_fim = input("Informe a data de fim (YYYY-MM-DD): ")
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))

            quarto = None
            for q in pousada.quartos:
                if q.numero == numero_quarto:
                    quarto = q
                    break

            if quarto:
                if pousada.realiza_reserva(data_inicio, data_fim, cliente, quarto):
                    print("Reserva realizada com sucesso.")
            else:
                print("Quarto não encontrado.")

        elif opcao == "4":
            cliente = input("Informe o nome do cliente: ")
            if pousada.cancela_reserva(cliente):
                print("Reserva cancelada com sucesso.")
            else:
                print("Nenhuma reserva ativa encontrada.")

        elif opcao == "5":
            cliente = input("Informe o nome do cliente: ")
            if pousada.realiza_checkin(cliente):
                print("Check-in realizado com sucesso.")
            else:
                print("Nenhuma reserva ativa encontrada.")

        elif opcao == "6":
            cliente = input("Informe o nome do cliente: ")
            if pousada.realiza_checkout(cliente):
                print("Check-out realizado com sucesso.")
            else:
                print("Nenhuma reserva em check-in encontrada.")

        elif opcao == "7":
            cliente = input("Informe o nome do cliente: ")

            if pousada.realiza_checkin(cliente):
                print("Produtos disponíveis na copa:")
                for produto in pousada.produtos:
                    print(f"{produto.codigo} - {produto.nome}: R${produto.preco}")

                codigo_produto = int(input("Informe o código do produto desejado: "))

                # Verifica se o código do produto existe
                if codigo_produto in [produto.codigo for produto in pousada.produtos]:
                    quarto = None
                    for q in pousada.quartos:
                        if q.numero == cliente.quarto:
                            quarto = q
                            break
                    
                    if quarto:
                        quarto.adiciona_consumo(codigo_produto)
                        print("Consumo registrado.")
                    else:
                        print("Quarto não encontrado.")
                else:
                    print("Produto não encontrado.")
            else:
                print("Nenhuma reserva ativa encontrada.")

        elif opcao == "8":
            pousada.salva_dados("pousada.txt", "quarto.txt", "reserva.txt", "produto.txt")
            print("Dados salvos com sucesso.")

        elif opcao == "0":
            print("Saindo do sistema...")
            pousada.salva_dados("pousada.txt", "quarto.txt", "reserva.txt", "produto.txt")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
