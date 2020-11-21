from django.shortcuts import render
from django.http import HttpResponse
from Places.Scraping import scraping

def index(requests):

    context = {'headings': scraping.headings, 'links': scraping.links, 'photo_links': scraping.photo_links, 'texts': scraping.texts, 'num': range(scraping.num)}     # scraping.num = 30

    return render(requests, 'Places/index.html', context)
