import requests
import csv
from bs4 import BeautifulSoup


r = requests.get('https://www.marvel.com/v1/pagination/'
                 'grid_cards?offset=0&limit=2667&entityType=character&sortField=title&sortDirection=asc')
data = r.json()
character = data['data']['results']['data']
main_link = 'https://www.marvel.com'
with open('B:\GitHub\parser\character.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['link']
    writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)

    for row in range(10):
        # names = character[i]['secondary_text']
        # sNames = character[i]["headline"]
        links = main_link + character[row]['link']['link']
        writer.writerow({'link': links})

# Создает и записывает ссылки в файл
with open('B:\GitHub\parser\character.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    def getHero(link):
        a = []
        characterLink = requests.get(link)
        soup = BeautifulSoup(characterLink.text, 'html.parser')

        try:
            name = soup.find('span', class_='masthead__eyebrow').text

        except AttributeError:
            name = soup.find('span', class_='masthead__headline').text
        a.append(name)
        data = soup.find_all('li', class_='railBioInfo__Item')

        for i in data:
            universe = i.find('ul', class_='railBioLinks')
            for j in universe:
                character = universe.find('li').text
            a.append(character)
        # print(a)
        return a

    # Считывает ссылки и формирует информацию для записии
    def record(a):
        with open('B:\GitHub\parser\Marvel character.csv', 'a', encoding='utf-8') as f:
            fieldnames = ['names', 'UNIVERSE', 'OTHER', 'EDUCATION', 'PLACE', 'KNOWN']
            writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)

            try:
                writer.writerow(
                    {'names': Marvel_character[0], 'UNIVERSE': Marvel_character[1],
                     'OTHER': Marvel_character[2], 'EDUCATION': Marvel_character[3],
                     'PLACE': Marvel_character[4], 'KNOWN': Marvel_character[6]})

            except IndexError:
                fieldnames = ['names']
                writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
                writer.writerow({'names': f'{Marvel_character[0]}: Нет данных герое!'})


    for row in reader:
        if str(*row) == '':
            continue
        Marvel_character = getHero(str(*row))
        record(Marvel_character)