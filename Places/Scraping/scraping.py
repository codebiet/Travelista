from bs4 import BeautifulSoup as bs
import requests

def places(city_name):
    url = 'https://www.holidify.com/places/' + city_name + '/sightseeing-and-things-to-do.html'
    page = requests.get(url)

    soup = bs(page.content, 'html.parser')
    cards = soup.find_all('div', class_="card content-card animation-slide-up")

    headings, links, photo_links, texts = [], [], [], []

    max_num, num = 30, 0
    for card in cards:

        headings.append(card.find('h3').text)

        links.append(card.find('a')['href'])

        photo_links.append(card.find('img', class_="card-img-top lazy")['data-original'])

        texts.append(card.find('p', class_='card-text').text)

        num += 1
        if num == max_num:
            break
    
    return headings, links, photo_links, texts, num
