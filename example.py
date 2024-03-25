"""
Напишите код который собирает данные в категории со всех х страниц и сохраняет всё в таблицу по
примеру предыдущего степа
"""
import csv
import requests
from bs4 import BeautifulSoup


def get_soup(url):  # получаем сап, функция для многократного использования
    response = requests.get(url=url)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_all_pages(url):  # получаем все ссылки на страницы с товаром, функция для использования по КОНКРЕТНОМУ АДРЕСУ
    soup = get_soup(url + 'index4_page_1.html')
    pages = [url + page['href'] for page in soup.find(name='div', attrs='pagen').find_all('a')]
    return pages

url = 'https://parsinger.ru/html/'
print(get_all_pages(url))


def script_from_list(names):  # скрипт для преобразования списка СПИСКОВ в один список !!!
    all_names = []
    for j in range(len(names)):
        for a in range(len(names[j])):
            all_names.append(names[j][a])
    return all_names


with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Name', 'Price', 'Brand', 'Form-factor', 'Container', 'Size'])  # заголовки в таблице

    url = 'https://parsinger.ru/html/'
    pages = get_all_pages(url)

    names = []
    description = []
    prices = []

    for i in pages:
        soup = get_soup(i)
        names.append([name.text for name in soup.find_all(name='a', attrs='name_item')])
        description.append([desc.text.split('\n') for desc in soup.find_all(name='div', attrs='description')])
        prices.append([price.text for price in soup.find_all(name='p', attrs='price')])

    all_names = script_from_list(names)
    all_prices = script_from_list(prices)
    all_descriptions = script_from_list(description)

    for all_names, all_prices, all_descriptions in zip(all_names, all_prices, all_descriptions):
        flatten = all_names, all_prices, *[x.split(':')[1].strip() for x in all_descriptions if x]
        file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
        writer.writerow(flatten)
file.close()