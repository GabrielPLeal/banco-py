from datetime import date
from utils.helper import convert_str_date, convert_date_str


class Client:

    counter: int = 101

    def __init__(self, name: str, email: str, cpf: str, birth_date: str) -> None:
        self.__codigo = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birth_date: date = convert_str_date(birth_date)
        self.__registration_date: date = date.today()
        Client.counter += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def birth_date(self) -> str:
        return convert_date_str(self.__birth_date)

    @property
    def data_cadastro(self) -> str:
        return convert_date_str(self.__registration_date)

    def __str__(self) -> str:
        return (f"Código: {self.codigo} \n"
                f"name: {self.name} \n"
                f"Data de Nascimento: {self.birth_date} \n"
                f"Cadastro: {self.data_cadastro}")
