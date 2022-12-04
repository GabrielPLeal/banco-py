from typing import List
from time import sleep

from models.account import Account
from models.client import Client
from utils.helper import (
    back_menu,
    check_has_accounts,
    client_account,
    create_account_message,
    search_account_by_number
)


accounts: List[Account] = []

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

    option: int = int(input('Opção: '))

    if option == 1:
        create_account()
    if option == 2:
        make_withdraw()
    if option == 3:
        make_deposit()
    if option == 4:
        make_transfer()
    if option == 5:
        list_accounts()
    if option == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def create_account() -> None:
    print('Informe os dados do cliente: ')
    name: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('Cpf do cliente: ')
    birth_date: str = input('Data de nascimento do cliente [dd/mm/yyyy]: ')

    new_client: Client = Client(name, email, cpf, birth_date)
    account: Account = client_account(new_client, accounts)

    message: str = f"Cliente {new_client.name} já possuí uma conta."

    if not account:
        account: Account = Account(new_client)
        accounts.append(account)
        message = 'Conta criada com sucesso.'

    create_account_message(account, message)
    back_menu(menu)

def make_withdraw() -> None:
    check_has_accounts(accounts, menu)
    
    number: int = int(input('Informe o número da sua conta: '))
    account: Account = search_account_by_number(number, accounts, menu)

    value: float = float(input('Informe o valor do saque: '))
    account.withdraw(value)
    
    back_menu(menu)

def make_deposit() -> None:
    check_has_accounts(accounts, menu)

    number: int = int(input('Informe o número da sua conta: '))
    account: Account = search_account_by_number(number, accounts, menu)
    
    value: float = float(input('Informe o valor de depósito: '))
    account.deposit(value)

    back_menu(menu)


def make_transfer() -> None:
    check_has_accounts(accounts, menu)

    origin_number: int = int(input('Informe o número da sua conta: '))
    origin_account: Account = search_account_by_number(origin_number, accounts, menu)
    
    destiny_number: int = int(input('Informe o número da conta de destino: '))
    destiny_account: Account = search_account_by_number(destiny_number, accounts, menu)

    value: float = float(input('Informe o valor da transferência: '))
    origin_account.transfer(destiny_account, value)

    back_menu(menu)


def list_accounts() -> None:
    check_has_accounts(accounts, menu)
 
    print(' Contas Cadastradas '.center(30, '-'))
    for account in accounts:
        print(account)
        print(''.ljust(30, '-'))
        sleep(1)

    back_menu(menu)

if __name__ == '__main__':
    main()
