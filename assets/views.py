from django.shortcuts import render, redirect
from .forms import CurrencyAssetForm
from .models import CurrencyAssetEntry
from django.db.models import Max
from django.http import HttpResponse
from .local_settings import TCMB_EVDS_API_KEY, EVDS_API_URL_EUR_A, EVDS_API_URL_USD_A, EVDS_API_URL_GLD
import requests
from datetime import datetime
import dateutil.relativedelta
import matplotlib
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from .models import CurrencyAssetEntry


def currency_asset_view(request):
    user = request.user

    headers = {'key':TCMB_EVDS_API_KEY}

    if request.method == 'POST':
        form = CurrencyAssetForm(request.POST)
        if form.is_valid():
            print("Valid Form Assets")
            new_entry = form.save(commit=False)
            end_date = new_entry.date
            start_date = end_date - dateutil.relativedelta.relativedelta(months=1)
            if (new_entry.currency_type == "USD"):
                response = requests.get(EVDS_API_URL_USD_A.format(start = end_date.strftime('%d-%m-%Y'), end = end_date.strftime('%d-%m-%Y')), headers=headers)
                if response.status_code == 200:
                    json_data = response.json()
                    last_element = json_data["items"][-1]
                    new_entry.exchange_rate = last_element["TP_DK_USD_A"]
            elif (new_entry.currency_type == "EUR"):
                response = requests.get(EVDS_API_URL_EUR_A.format(start = end_date.strftime('%d-%m-%Y'), end = end_date.strftime('%d-%m-%Y')), headers=headers)
                if response.status_code == 200:
                    json_data = response.json()
                    last_element = json_data["items"][-1]
                    new_entry.exchange_rate = last_element["TP_DK_EUR_A"]
            elif (new_entry.currency_type == "GLD"):
                response = requests.get(EVDS_API_URL_GLD.format(start = start_date.strftime('%d-%m-%Y'), end = end_date.strftime('%d-%m-%Y')), headers=headers)
                if response.status_code == 200:
                    json_data = response.json()
                    last_element = json_data["items"][-1]
                    new_entry.exchange_rate = last_element["TP_MK_KUL_YTL"]
            new_entry.owner = user.username 
            new_entry.save()
        else:
           print(form.errors)      
    else:
        form = CurrencyAssetForm()
    
    latest_entries = (
        CurrencyAssetEntry.objects
        .values('currency_type')            # Group by currency_type
        .annotate(latest_date=Max('date'))  # Get the max date for each currency_type
    )

    # Now get the complete object based on the latest date for each currency type
    latest_assets = CurrencyAssetEntry.objects.filter(
        date__in=[entry['latest_date'] for entry in latest_entries]
    )

    return render(request, 'list.html', {'entries': latest_assets, 'form': form, 'user': user.username})

def currency_line_chart(request, currency_type):
    matplotlib.use('Agg')  # Use Agg backend for rendering without GUI

    entries = CurrencyAssetEntry.objects.filter(currency_type=currency_type.upper())
    dates = [entry.date for entry in entries]
    amounts = [entry.amount for entry in entries]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker='o', linestyle='-', color='b', label=f'{currency_type} Amount')
    plt.title(f'{currency_type} Amount Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    context = {'chart': image_base64, 'currency_type': currency_type}
    return render(request, 'currency_chart.html', context)


def update_entry(request, pk):
    entry = CurrencyAssetEntry.objects.get(id=pk)
    form = CurrencyAssetForm(instance=entry)

    if request.method == 'POST':
        form = CurrencyAssetForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('/assets')

    context = {'form': form}
    return render(request, 'assets/update.html', context)


def delete_entry(request, pk):
    entry = CurrencyAssetEntry.objects.get(id=pk)
    entry.delete()
    return redirect('/assets')