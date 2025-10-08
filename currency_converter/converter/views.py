from django.shortcuts import render
from .models import Currency
from .utils import update_currency_rates
from decimal import Decimal


def home(request):
    return render(request, 'home.html')


def contacts(requests):
    return render(request, 'contacts.html')


def converter(request):
    date = update_currency_rates()
    currencies = Currency.objects.all()
