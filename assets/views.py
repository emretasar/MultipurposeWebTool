from django.shortcuts import render, redirect
from .forms import CurrencyAssetForm
from .models import CurrencyAssetEntry
from django.db.models import Max
from django.http import HttpResponse


def currency_asset_view(request):
    user = request.user
    entries = CurrencyAssetEntry.objects.all()

    if request.method == 'POST':
        form = CurrencyAssetForm(request.POST)
        if form.is_valid():
            print("Valid Form Assets")
            new_entry = form.save(commit=False)
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
'''
    entries_to_display = []
    entries_to_display.append(entries.filter(currency_type ="TRY").order_by)
    entries_to_display.append(entries.filter(currency_type ="USD"))
    entries_to_display.append(entries.filter(currency_type ="GLD"))
'''

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