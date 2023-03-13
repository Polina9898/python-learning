# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона
# данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os
import sys

def main():
    book_filename = 'phonebook.txt'

    if (len(sys.argv) > 1):
        book_filename = sys.argv[1]

    book = read_phone_book(book_filename, [])

    while True:
        main_menu(book_filename, book)


def main_menu(book_filename, book):
    action = input('''
Main menu:
0. Exit
1. Show all
2. Search
3. Add
4. Update
5. Delete

Select action: ''')

    match action:
        case '1':
            print_book(book)

        case '2':
            text = input('Search text: ')
            print_book(search(book, text))

        case '3':
            action_add(book)
            write_phone_book(book_filename, book)

        case '4':
            action_update(book)
            write_phone_book(book_filename, book)

        case '5':
            action_delete(book)
            write_phone_book(book_filename, book)
            read_phone_book(book_filename, book)

        case '0':
            exit(0)

    input('...')


def action_add(book):
    print('Add new contact:')
    name = input('Name: ')
    phone = input('Phone: ')

    add(book, name, phone)
    print(f'New contact added:\n{len(book)}. {name} {phone}')


def action_update(book):
    id = readId(book)

    if (id is None):
        return
    
    rec = book[id]

    print(f'{rec["name"]} {rec["phone"]}')

    doEdit = True
                 
    while doEdit:  
        mode = input('''
What do you need to edit?
0. Exit editing (save)
1. Name
2. Phone

Select mode: ''')

        match mode:
            case '0':
                doEdit = False

            case '1':
                rec['name'] = input("Enter new name: ")

            case '2':
                rec['phone'] = input("Enter new phone: ")


def action_delete(book):
    id = readId(book)

    if (id is None):
        return
    
    del book[id]
    print("Contact was removed")


def print_book(book):
    for id, rec in enumerate(book):
        print(f'{rec["id"]}. {rec["name"]} {rec["phone"]}')


def search(book, text):
    text = text.lower()
    return [rec for rec in book if text in rec['name'].lower() or text in rec['phone'].lower()]


def add(book, name, phone):
    book.append({
        'id': len(book) + 1,
        'name': name,
        'phone': phone
    })


def readId(book):
    id = int(input("Contact ID: ")) - 1

    if id < 0 or id >= len(book):
        print(f'Contact with ID={id} doesn\'t exist')
        return None
    
    return id


def read_phone_book(path, book):
    book.clear()

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            record = line.split()

            if (len(record) < 2):
                continue

            name = ' '.join(record[0:-1])
            phone = record[-1]

            add(book, name, phone)

    return book


def write_phone_book(path, book):
    if (os.path.exists(path)):
        os.remove(path)

    with open(path, 'w', encoding='utf-8') as file:
        for record in book:
            name = record['name']
            phone = record['phone']
            file.write(f'{name} {phone}\n')

main()