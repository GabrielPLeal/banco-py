from typing import List
from time import sleep

from models.conta import Conta
from models.cliente import Cliente


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print(''.ljust(50, '='))
    print(' ATM '.center(50, '='))
    print(' Leal Bank '.center(50, '='))
    print(''.ljust(50, '='))

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input('Opção: '))

    if opcao == 1:
        criar_conta()
    if opcao == 2:
        efetuar_saque()
    if opcao == 3:
        efetuar_deposito()
    if opcao == 4:
        efetuar_transferencia()
    if opcao == 5:
        listar_contas()
    if opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('Cpf do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente [dd/mm/yyyy]: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    _verifica_cliente_conta(cliente)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print(''.ljust(30, '='))
    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print(''.ljust(30, '-'))
    print(conta)
    _volta_menu()


def efetuar_saque() -> None:
    if contas:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrado a conta com o número {numero}')
    else:
        print('Ainta não existem contas cadastradas')
    _volta_menu()


def efetuar_deposito() -> None:
    if contas:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor de depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrado a conta com o número {numero}')
    else:
        print('Ainta não existem contas cadastradas')
    _volta_menu()


def efetuar_transferencia() -> None:
    if contas:
        numero_origem: int = int(input('Informe o número da sua conta: '))
        conta_origem: Conta = buscar_conta_numero(numero_origem)
        if conta_origem:
            numero_destino: int = int(input('Informe o número da conta de destino: '))
            conta_destino: Conta = buscar_conta_numero(numero_destino)
            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))
                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta destino com o número {numero_destino} não foi encontrada.')
        else:
            print(f'A sua conta com o número {numero_origem} não foi encontrada.')
    else:
        print('Ainta não existem contas cadastradas')
    _volta_menu()


def listar_contas() -> None:
    if contas:
        print(' Contas Cadastradas '.center(30, '-'))
        for conta in contas:
            print(conta)
            print(''.ljust(30, '-'))
            sleep(1)
    else:
        print('Não existem contas cadastradas')
    _volta_menu()


def buscar_conta_numero(numero: int) -> Conta:
    for conta in contas:
        if conta.numero == numero:
            return conta


def _verifica_cliente_conta(cliente: Cliente) -> None:
    if contas:
        conta_listada: List = list(filter(lambda conta: conta.cliente.cpf == cliente.cpf, contas))

        if conta_listada:
            print(''.ljust(30, '='))
            print(f"Cliente {cliente.nome} já possuí uma conta.")
            print('Dados da conta: ')
            print(''.ljust(30, '-'))
            print(conta_listada[0])
            _volta_menu()


def _volta_menu() -> None:
    sleep(2)
    menu()


if __name__ == '__main__':
    main()
