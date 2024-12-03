from enum import Enum
import datetime
import requests
from .local_settings import TCMB_EVDS_API_KEY, EVDS_API_URL_EXCHANGE, USD_A_SERIES, EUR_A_SERIES, GLD_SERIES


ExchangeType = Enum('Exchange', [('TRY', 1), ('USD', 2), ('GLD', 3),  ('EUR', 4)])

def get_exchange_rates_info(exchange_type : ExchangeType, start_date : datetime.date, end_date: datetime.date):
    headers = {'key':TCMB_EVDS_API_KEY}
    if (exchange_type.name == 'USD'):
        response = requests.get(EVDS_API_URL_EXCHANGE.format(exchange = USD_A_SERIES, start = start_date.strftime('%d-%m-%Y'), end = end_date.strftime('%d-%m-%Y')), headers=headers)
    elif (exchange_type.name == 'GLD'):
        response = requests.get(EVDS_API_URL_EXCHANGE.format(exchange = EUR_A_SERIES, start = start_date.strftime('%d-%m-%Y'), end = end_date.strftime('%d-%m-%Y')), headers=headers)
    elif (exchange_type.name == 'EUR'):
        response = requests.get(EVDS_API_URL_EXCHANGE.format(exchange = GLD_SERIES, start = start_date.strftime('%d-%m-%Y'), end = end_date.strftime('%d-%m-%Y')), headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        elements = json_data["items"]
        return elements

def get_latest_exchange_rate(exchange_type : ExchangeType, start_date : datetime.date, end_date: datetime.date):
    headers = {'key':TCMB_EVDS_API_KEY}
    if (exchange_type.name == 'USD'):
        series = USD_A_SERIES
    elif (exchange_type.name == 'GLD'):
        series = GLD_SERIES
    elif (exchange_type.name == 'EUR'):
        series = EUR_A_SERIES

    response = requests.get(EVDS_API_URL_EXCHANGE.format(exchange = series, start = start_date.strftime('%d-%m-%Y'), end = end_date.strftime('%d-%m-%Y')), headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        elements = json_data["items"]
        if list(elements).__len__ != 0:
            series = series.replace(".", "_")
            for idx in range(1, 4):
                if series in list(elements)[-idx]:
                    str_value = list(elements)[-idx][series.replace(".", "_")]
                    return float(str_value)        
