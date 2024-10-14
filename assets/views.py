from django.shortcuts import render
from .forms import CurrencyAssetForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the new app!")

def currency_asset_view(request):
    if request.method == 'POST':
        form = CurrencyAssetForm(request.POST)
        if form.is_valid():
            # Handle form data here (e.g., save it to the database)
            pass
    else:
        form = CurrencyAssetForm()

    return render(request, 'currency_asset_form.html', {'form': form})
