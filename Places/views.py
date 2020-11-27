from django.shortcuts import render
from django.http import HttpResponse
from Places.Scraping import scraping

def index(request):

    return render(request, 'Places/index.html')

def city(request):
    city_name = request.GET['city_name']
    city_data = scraping.city_info(city_name)

    content = {'city_image_link': city_data[0], 'city_heading': city_data[1], 'state': city_data[2], 'country': city_data[3], 'covid_details': city_data[4], 'para': city_data[5], 'city_name': city_name}

    return render(request, 'Places/city.html', content)

def places_to_visit(request, city_name):

    city_data = scraping.places_to_visit(city_name)

    content = {'headings': city_data[0], 'links': city_data[1], 'photo_links': city_data[2], 'texts': city_data[3], 'num': range(city_data[4])}

    return render(request, 'Places/places_to_visit.html', content)

def food(request, city_name):

    city_data = scraping.food(city_name)

    content = {'restaurants_info': city_data[0], 'photo_links': city_data[1], 'total_restaurants': range(city_data[2])}

    return render(request, 'Places/food.html', content)