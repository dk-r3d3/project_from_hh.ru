import csv
import requests
from bs4 import BeautifulSoup


def find_vacancies(city, key_word, page):  # функция для поиска вакансий по городу и названию вакансии
    url = 'https://api.hh.ru/vacancies'
    index_city = {'Барнаул': 11, 'Москва': 1}
    params = {
        'area': index_city[city],  # передаем значение словаря (индекс), т к поиск по индексу городов
        'text': f'NAME:{key_word}',  # ключевое слово по которому идет поиск в ЗАГОЛОВКЕ
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


def get_list_vacancy(city, key_word):
    page = 0
    count = 1
    while True:
        data = find_vacancies(city, key_word, page)
        count_page = data['pages']
        if count_page - 1 >= page:
            items = data['items']
            for i in items:
                print(f'{count}. {i["name"]} - {get_salary(i)} ')
                count += 1
            page += 1
        else:
            break


def get_csv_vacancy(city, key_word):

    names = []
    salary = []
    page = 0
    while True:
        data = find_vacancies(city, key_word, page)
        count_page = data['pages']
        if count_page - 1 >= page:
            items = data['items']
            for i in items:
                names.append(i["name"])
                salary.append(get_salary(i))
            page += 1
        else:
            break

    with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Name', 'Salary'])  # заголовки в таблице
        for names, salary in zip(names, salary):
            flatten = names, salary
            file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
            writer.writerow(flatten)
    file.close()
