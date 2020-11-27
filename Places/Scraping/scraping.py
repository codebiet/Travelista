from bs4 import BeautifulSoup as bs
import requests

def city_info(city_name):
    try:
        url = 'https://www.holidify.com/places/' + city_name
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')
        
        city_image_link = soup.find('div', class_= 'atf-cover-image')['style'][23:-3]

        location = soup.find('div', class_='col-12 col-lg-6 right')
        city_heading = location.find('h1').text
        state_and_country = location.find_all('b')[1:3]
        state = state_and_country[0].text[1:-1]
        country = state_and_country[1].text[1:]

        covid_details = location.find('div', class_='mb-40 font-smaller').text[6:-12].replace('  \n\t', ', ')

        contents = soup.find('div', class_='col-lg-8 pr-lg-2')
        # para_heading = contents.find('h2').text[2:-2]
        para = ' '.join([i.text[1:] for i in contents.find('div', class_='readMoreText').find_all('p')[0:3:2]])

        return city_image_link, city_heading, state, country, covid_details, para

    except:
        return [], [], [], [], [], [], []

def places_to_visit(city_name):
    try:    
        url = 'https://www.holidify.com/places/' + city_name + '/sightseeing-and-things-to-do.html'
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')
        cards = soup.find_all('div', class_="card content-card animation-slide-up")

        headings, links, photo_links, texts = [], [], [], []

        total_places, lim = 0, 30
        for card in cards:

            headings.append(card.find('h3').text)

            links.append(card.find('a')['href'])

            photo_links.append(card.find('img', class_="card-img-top lazy")['data-original'])

            texts.append(card.find('p', class_='card-text').text)

            total_places += 1
            if total_places == lim:
                break

        return headings, links, photo_links, texts, total_places

    except:
        return [], [], [], []

def food(city_name):

    try:
        url = 'https://www.holidify.com/places/' + city_name+ '/restaurants-places-to-eat-local-cuisine.html'
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')

        cards = soup.find('div', class_='row no-gutters mb-50 negative-margin-mobile').find_all('div', class_='col-12 col-md-6 pr-md-3')
        
        photo_links, restaurants_info, total_restaurants, lim = [], [], 0, 30

        for card in cards:

            if card.find('img') != None:
                photo_links.append(card.find('img', class_="card-img-top lazy")['data-original'])
            else:
                photo_links.append('')

            restaurants_info.append([i for i in card.text.split('\n') if i not in ['', ' ', '                        ']])

            total_restaurants += 1
            if total_restaurants == lim:
                break
            
        return restaurants_info, photo_links, total_restaurants

    except:
        return [], [], 0

