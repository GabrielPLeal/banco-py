from typing import List, Callable
from datetime import date, datetime
from time import sleep


def convert_date_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')

def convert_str_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

def format_monetary_value(valor: float) -> str:
    return f'R$ {valor:,.2f}'

def back_menu(menu: Callable) -> None:
    sleep(2)
    menu()

def check_has_accounts(accounts: List[object], menu: callable):
    if not accounts:
        print('Ainta não existem contas cadastradas')
        back_menu(menu)
    
def client_account(client: object, accounts: List[object]) -> object:
    listed_account: List[object] = list(filter(lambda account: account.client.cpf == client.cpf, accounts))
    if listed_account:
        return listed_account[0]

def create_account_message(account: object, message: str):
    print(''.ljust(30, '='))
    print(message)
    print('Dados da conta: ')
    print(''.ljust(30, '-'))
    print(account)

def search_account_by_number(number: int, accounts: List[object], menu) -> object:
    account = list(filter(lambda account: account.number == number, accounts))
    
    if not account:
        print(f'Não foi encontrado a conta com o número {number}')
        back_menu(menu)
    
    return account[0]
