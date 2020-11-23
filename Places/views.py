from django.shortcuts import render
from django.http import HttpResponse
from Places.Scraping import scraping

def index(request):

    return render(request, 'Places/index.html')

def places_to_visit(request):

    city_name = request.GET['city_name']

    city_data = scraping.places(city_name)

    content = {'headings': city_data[0], 'links': city_data[1], 'photo_links': city_data[2], 'texts': city_data[3], 'num': range(city_data[4])}

    return render(request, 'Places/places_to_visit.html', content)
