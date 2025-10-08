import requests
from datetime import datetime
from decimal import Decimal
from .models import Currency


def update_currency_rates():
    url = 'сылка'
    response = requests.get(url)
    data = response.json()
    
    data = datetime.strptime(data['Date'], '%Y=%M-%dT%H:%M:%S%z').date()