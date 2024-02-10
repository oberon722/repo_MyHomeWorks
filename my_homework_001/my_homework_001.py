# ДОМАШНЕЕ ЗАДАНИЕ К 12.02.2024
# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла
# в другой.
# выполнена доработка кода урока №8.


import os
from csv import DictReader, DictWriter


class CustomNameError(Exception):
    def __init__(self, txt):
        self.txt = txt


class PhoneError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_user_data():
    while True:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise CustomNameError('Не валидная длина имени! ')
            last_name = input('Введите Фамилию: ')
            phone_number = int(input('Введите номер телефона в формате 8хххххххххх: '))
            if len(str(phone_number)) < 11:
                raise PhoneError('Неверная длина номера! ')
        except ValueError:
            print('Вы вводите символы вместо цифр! ')
            continue
        except CustomNameError as err:
            print(err)
            continue
        except PhoneError as err:
            print(err)
            continue
        else:
            return first_name, last_name, phone_number


def create_file(file_name):
    with open(file_name, 'w', encoding='utf8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    if not os.path.exists(file_name):
        print('Файл не существует!')
        return []

    with open(file_name, encoding='utf8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):
    user_data = get_user_data()
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == str(user_data[2]):
            print('Такой пользователь уже существует!')
            return
    obj = {'Имя': user_data[0], 'Фамилия': user_data[1], 'Телефон': user_data[2]}
    res.append(obj)

    with open(file_name, 'w', encoding='utf8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def copy_row_to_target(row_number, file_name):
    phone_data = read_file('phone.csv')
    if row_number <= len(phone_data):
        with open(file_name, 'a', encoding='utf8', newline='') as target_file:
            f_writer = DictWriter(target_file, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writerow(phone_data[row_number - 1])
    else:
        print('Строки с таким номером не существует.')


def main():
    file_name_phone = 'phone.csv'
    file_name_target = 'target.csv'

    print('Основные команды Пользователя:')
    print('w - создаем новую запись в телефонный справочник;')
    print('r - создаем файл телефонного справочника;')
    print('p - копируем строку с номером n в файл target.csv')

    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not os.path.exists(file_name_phone):
                create_file(file_name_phone)
            write_file(file_name_phone)
            print('Данные успешно записаны!')
        elif command == 'r':
            if not os.path.exists(file_name_phone):
                print('Файл не существует! Создайте файл!')
                continue
            print(read_file(file_name_phone))
        elif command == 'p':
            row_number = int(input('Введите номер строки для копирования: '))
            copy_row_to_target(row_number, file_name_target)


if __name__ == "__main__":
    main()
