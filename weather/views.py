from django.shortcuts import render, redirect
import requests
from .models import Location
from .forms import LocationForm
from .utils import get_weather_info


def weather(request):

    locations = Location.objects.all()
    weathers = []
    for location in locations:
        latitude = location.latitude
        longtitude = location.longtitude
        condition, info = get_weather_info(latitude, longtitude)

        weather = dict({"loc":location, "con": condition, 'info': info})
        weathers.append(weather)

    if request.method == "POST":
        form = LocationForm(request.POST)	
        if form.is_valid():
            form.save()
            latest_created_condition, latest_created_info = get_weather_info(locations.last().latitude, locations.last().longtitude)
            weather = dict({"loc":locations.last(), "con": latest_created_condition, 'info': latest_created_info})
            weathers.append(weather)
            context = {'weathers':weathers}
            return redirect('/weather')
    else:
        form = LocationForm()
        context = {'weathers':weathers, 'form':form}
        return render(request, 'weather/weather.html', context)

def delete_location(request, pk):
	item = Location.objects.get(id=pk)
	item.delete()
	return redirect('/weather')