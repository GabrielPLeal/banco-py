from models.client import Client
from utils.helper import format_monetary_value


class Account:

    code: int = 1001

    def __init__(self, client: Client) -> None:
        self.__number: int = Account.code
        self.__client: client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._calc_total_balance
        Account.code += 1

    @property
    def number(self) -> int:
        return self.__number

    @property
    def client(self) -> Client:
        return self.__client

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        self.__balance = value

    @property
    def limit(self) -> float:
        return self.__limit

    @limit.setter
    def limit(self, value: float) -> None:
        self.__limit = value

    @property
    def balance_total(self) -> float:
        return self.__total_balance

    @balance_total.setter
    def balance_total(self, value: float) -> None:
        self.__total_balance = value

    @property
    def _calc_total_balance(self) -> float:
        return self.balance + self.limit

    def deposit(self, value: float) -> None:
        if value > 0:
            self.balance += value
            self.balance_total = self._calc_total_balance
            print(' Depósito realizado com sucesso '.upper().center(30, '-'))
        else:
            print('Erro ao efetuar depósito. Tente novamente')

    def withdraw(self, value: float) -> None:
        if 0 < value <= self.balance_total:
            if self.balance >= value:
                self.balance -= value
            else:
                restante: float = self.balance - value
                self.limit += restante
                self.balance = 0
            self.balance_total = self._calc_total_balance
            print(' Saque realizado com sucesso '.upper().center(30, '-'))
        else:
            print('Erro ao efetuar saque. Tente novamente')

    def transfer(self, destino: object, value: float) -> None:
        if 0 < value <= self.balance_total:
            if self.balance >= value:
                self.balance -= value
            else:
                restante: float = self.balance - value
                self.limit += restante
                self.balance = 0
            self.balance_total = self._calc_total_balance
            destino.balance += value
            destino.balance_total = destino._calc_total_balance
            print(' Transferência realizada com sucesso '.upper().center(30, '-'))
        else:
            print('Erro ao efetuar transferência. Tente novamente')

    def __str__(self) -> str:
        return (f"Número da Conta: {self.number} \n"
                f"Cliente: {self.client.name} \n"
                f"Saldo Total: {format_monetary_value(self.balance_total)}")
