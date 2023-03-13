# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона
# данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программане должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os

phone_book_filename = 'phonebook.txt'

def read_phone_book(path):
    book = []

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            record = line.split()

            if (len(record) < 2):
                continue
            
            book.append({
                'id': len(book) + 1,
                'name': ' '.join(record[0:-1]),
                'phone': record[-1]
            })

    return book


def write_phone_book(path, book):
    if (os.path.exists(path)):
        os.remove(path)

    with open(path, 'w', encoding='utf-8') as file:
        for record in book:
            name = record['name']
            phone = record['phone']
            file.write(f'{name} {phone}\n')

def print_book(book):
    for id, rec in enumerate(book):
        print(f'{rec["id"]}. {rec["name"]} {rec["phone"]}')


def search(book, text):
    return filter(lambda rec: text in rec['name'] or text in rec['phone'], book)

def main_menu():
    selected = input('''
Main menu:
0. Exit
1. Show all
2. Search

Select action: ''')

    match selected:
        case '1':
            print_book(read_phone_book(phone_book_filename))

        case '2':
            text = input('Search text: ')
            book = read_phone_book(phone_book_filename)
            print_book(search(book, text))

        case '0':
            exit(0)

    input()


while True:
    main_menu()
