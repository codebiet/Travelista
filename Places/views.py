from django.shortcuts import render, redirect

from Places.Scraping import scraping


def index(request):
    return render(request, 'Places/index.html')


def city(request):
    if request.GET:
        city_name = request.GET['city_name']
    else:
        return redirect('index')    

    city_info = scraping.city_info(city_name)

    context = {'city_info': city_info, 'city_name': city_name}

    return render(request, 'Places/city.html', context)


def places_to_visit(request, city_name=None):
    places = scraping.places_to_visit(city_name)

    context = {'places': places, 'city_name': city_name}

    return render(request, 'Places/places_to_visit.html', context)


def food(request, city_name=None):
    restaurants = scraping.food(city_name)
    
    context = {'restaurants': restaurants, 'city_name': city_name}

    return render(request, 'Places/food.html', context)
