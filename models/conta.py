from models.cliente import Cliente
from utils.helper import formata_valor_monetario


class Conta:

    codigo: int = 1001

    def __init__(self, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcular_saldo_total
        Conta.codigo += 1

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcular_saldo_total(self) -> float:
        return self.saldo + self.limite

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self._calcular_saldo_total
            print(' Depósito realizado com sucesso '.upper().center(30, '-'))
        else:
            print('Erro ao efetuar depósito. Tente novamente')

    def sacar(self, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                restante: float = self.saldo - valor
                self.limite += restante
                self.saldo = 0
            self.saldo_total = self._calcular_saldo_total
            print(' Saque realizado com sucesso '.upper().center(30, '-'))
        else:
            print('Erro ao efetuar saque. Tente novamente')

    def transferir(self, destino: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                restante: float = self.saldo - valor
                self.limite += restante
                self.saldo = 0
            self.saldo_total = self._calcular_saldo_total
            destino.saldo += valor
            destino.saldo_total = destino.calcular_saldo_total
            print(' Transferência realizada com sucesso '.upper().center(30, '-'))
        else:
            print('Erro ao efetuar transferência. Tente novamente')

    def __str__(self) -> str:
        return (f"Número da Conta: {self.numero} \n"
                f"CLiente: {self.cliente.nome} \n"
                f"Saldo Total: {formata_valor_monetario(self.saldo_total)}")
