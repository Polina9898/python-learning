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
phone_book = dict()

def read_phone_book(path, book):
    with os.open(path, 'r') as line:
        record = line.split()

        if (record.length > 1):
            book[' '.join(record[0:-1])] = record[-1]


def write_phone_book(path, book):
    os.remove(path)

    with os.open(path, 'w') as file:
        for name in book:
            phone = book[name]
            file.write(f'{name} {phone}\n')


def search(book, search_str):
    for name in book:
        name_string = f'{name} {book[name]}'
