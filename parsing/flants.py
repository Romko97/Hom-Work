import requests
from bs4 import BeautifulSoup
import csv
import subprocess

URL = 'https://lvov.mesto.ua/uk/rent/'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'accept':'*/*'}
HOST = 'https://lvov.mesto.ua'
FILES = 'flats.csv'
path_to_note = '/usr/share/applications/libreoffice-calc.desktop'
path_to_file = '~/Desktop/parsing/flats.csv'

def get_html(url, params = None):
    r = requests.get(url, headers=HEADERS, params=params)
    #print("функція get html - ", r)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='property')
    flats =[]
    for item in items:
        flats.append({
            'street':item.find('a', class_='title').get_text(strip = True).replace(', ',' '),
            'price': item.find('div', class_='price pull-right').get_text(strip = True),
            'link':item.find('a', class_='title').get('href')
        })
    #print("функція get_content - ", soup, items, flats)
    return flats

def save_file(items, path):
    with open(path,'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Вулиця','ціна','лінк',])
        for item in items:
            writer.writerow([item['street'],item['price'],item['link']])

def get_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('ul', class_='pagination')
    if pagination:
        return pagination[-1].get_text(strip = True)
    else:
        return 1 

def parse():
    html = get_html(URL)
    print("функція parse запущена")
    if html.status_code == 200:
        print("доступ до сторінки успішно встановлений")
        flats=[]
        pages_count = get_pages(html.text)
        for page in range(1, len(pages_count)+1):
            print(f'парсінг сторінки {page} із {len(pages_count)}')
            html = get_html(URL, params={'p': page})
            flats.extend(get_content(html.text))
        print(f'отримано дані про {len(flats)} квартир')
        save_file(flats, FILES)
        print("створено файл у папці")
        subprocess.call([path_to_note, path_to_file])
    else:
        print("Нема доступу до сторінки")

parse()

