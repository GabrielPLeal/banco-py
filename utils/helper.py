from datetime import date, datetime


def converte_data_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def converte_str_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_valor_monetario(valor: float) -> str:
    return f'R$ {valor:,.2f}'

