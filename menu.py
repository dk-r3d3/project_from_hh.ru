import pprint
from view import find_vacancies,\
    get_salary,\
    get_list_vacancy, \
    get_csv_vacancy


desc = "Меню:\n 1. Получить список вакансий по городу и ключевому слову\n " \
       "2. Получить Excel-таблицу со списком вакансий\n " \
       "3. Завершение работы"


def menu():
    item: int = 0
    while item != 3:
        print(desc)
        try:
            item = int(input("Введите пункт меню: "))
            if item < 3:
                if item == 1:
                    list_city = {1: 'Барнаул', 2: 'Москва'}
                    city = int(input(f"Введите индекс города из списка (1-Барнаул, 2-Москва): "))
                    key_word = input("Введите ключевое слово для поиска: ")
                    get_list_vacancy(list_city[city], key_word)
                if item == 2:
                    list_city = {1: 'Барнаул', 2: 'Москва'}
                    city = int(input(f"Введите индекс города из списка (1-Барнаул, 2-Москва): "))
                    key_word = input("Введите ключевое слово для поиска: ")
                    print(get_csv_vacancy(list_city[city], key_word))
        except ValueError:
            print("Введите целочисленный тип")

    # get_list_vacancy('Барнаул', url)
