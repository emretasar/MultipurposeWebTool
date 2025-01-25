from django.shortcuts import render, redirect
from .forms import CurrencyAssetForm
from .models import CurrencyAssetEntry
from django.db.models import Max
import dateutil.relativedelta
import matplotlib
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from .models import CurrencyAssetEntry
from .evds import get_latest_exchange_rate, ExchangeType


def currency_asset_view(request):
    user = request.user

    if request.method == 'POST':
        form = CurrencyAssetForm(request.POST)
        if form.is_valid():
            print("Valid Form Assets")
            new_entry = form.save(commit=False)
            end_date = new_entry.date
            start_date = end_date - dateutil.relativedelta.relativedelta(months=1)
            if (new_entry.currency_type == "USD"):
                new_entry.exchange_rate = get_latest_exchange_rate(ExchangeType.USD, start_date, end_date)
            elif (new_entry.currency_type == "EUR"):
                new_entry.exchange_rate = get_latest_exchange_rate(ExchangeType.EUR, start_date, end_date)
            elif (new_entry.currency_type == "GLD"):
                new_entry.exchange_rate = get_latest_exchange_rate(ExchangeType.GLD, start_date, end_date)
            new_entry.owner = user.username 
            new_entry.save()
        else:
           print(form.errors)      
    else:
        form = CurrencyAssetForm()
    
    latest_entries = (
        CurrencyAssetEntry.objects
        .filter(owner=user.username)     # Filter by owner first
        .values('currency_type')           # Group by currency_type
        .annotate(latest_date=Max('date')) # Get the max date for each currency_type
    )

    # Now get the complete object based on the latest date for each currency type
    latest_assets = CurrencyAssetEntry.objects.filter(
        date__in=[entry['latest_date'] for entry in latest_entries]
    )

    return render(request, 'list.html', {'entries': latest_assets, 'form': form, 'user': user.username})

def currency_line_chart(request, currency_type):
    user = request.user

    matplotlib.use('Agg')  # Use Agg backend for rendering without GUI

    entries = CurrencyAssetEntry.objects.filter(owner=user.username, currency_type=currency_type).order_by('date')
    dates = [entry.date for entry in entries]
    amounts = [entry.amount for entry in entries]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker='o', linestyle='-', color='b', label=f'{currency_type} Amount', linewidth=6)
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

def distribution_pie_chart(request):
    user = request.user
    
    matplotlib.use('Agg')  # Use Agg backend for rendering without GUI

    latest_entries = (
        CurrencyAssetEntry.objects
        .filter(owner=user.username)
        .values('currency_type')           
        .annotate(latest_date=Max('date'))  
    )

    latest_assets = CurrencyAssetEntry.objects.filter(
        date__in=[entry['latest_date'] for entry in latest_entries]
    )

    currency_types = [entry.currency_type for entry in latest_assets]
    amounts = [entry.amount for entry in latest_assets]
    exchange_rates = [entry.exchange_rate for entry in latest_assets]
    date = latest_assets[0].date

    currency_to_trys = []
    for idx, amount in enumerate(amounts):
        currency_to_trys.append(float(amount) * float(exchange_rates[idx]))

    fig, ax = plt.subplots()
    ax.pie(currency_to_trys, labels=currency_types, autopct='%1.1f%%',
    pctdistance=1.25, labeldistance=.6)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    context = {'chart': image_base64, 'date': date}
    return render(request, 'distribution_pie.html', context)

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