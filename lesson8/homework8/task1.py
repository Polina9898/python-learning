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


def search(book, search_str):
    for name in book:
        name_string = f'{name} {book[name]}'


phone_book = read_phone_book(phone_book_filename)

print(phone_book)