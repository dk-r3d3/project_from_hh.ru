import csv
import requests
from bs4 import BeautifulSoup


def find_vacancies(city, page, url):  # функция для поиска вакансий по городу и названию вакансии
    index_city = {'Барнаул': 11, 'Москва': 1}
    params = {
        'area': index_city[city],  # передаем значение словаря (индекс), т к поиск по индексу городов
        'text': 'NAME:PYTHON',  # ключевое слово по которому идет поиск в ЗАГОЛОВКЕ
        'page': page  # страница, на которой идет поиск
    }
    response = requests.get(url, params=params)
    js = response.json()
    return js  # получили список вакансий с заданными параметрами в формате JSON


def get_salary(vacancy):  # получили зарплату из ВАКАНСИИ
    salary = vacancy['salary']
    if salary is None:
        return 'Зп не указана'
    else:
        return salary['from']


def get_list_vacancy(city, url):
    page = 0
    count = 1
    while True:
        data = find_vacancies(city, page, url=url)
        count_page = data['pages']
        if count_page - 1 >= page:
            items = data['items']
            for i in items:
                print(f'{count}. {i["name"]} - {get_salary(i)} ')
                count += 1
            page += 1
        else:
            break


url = 'https://api.hh.ru/vacancies'
get_list_vacancy('Москва', url)
