"""
8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
Информация о человеке: Фамилия, Имя, Телефон, Описание

Корректность и уникальность данных не обязательны.

Функционал программы
телефонный справочник хранится в памяти в процессе выполнения кода. Выберите наиболее удобную структуру данных для хранения справочника.

CRUD: Create, Read, Update, Delete

Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
Delete: Удаление записи из справочника. Выбор - как в Read.
экспорт данных в текстовый файл формата csv

импорт данных из текстового файла формата csv

Используйте функции для реализации значимых действий в программе

(*) Усложнение.

Сделать тесты для функций
Разделить на model-view-controller
"""

# user = ["name", "surname", "phone", "description"]
# dictionary = {
#     1: ["name", "surname", "phone", "description"],
#     2: ["name", "surname", "phone", "description"],
# }

from os.path import abspath, join, dirname


def input_user() -> list:
    user = []
    user.append(input("Input name: "))
    user.append(input("Input surname: "))
    user.append(input("Input phone: "))
    user.append(input("Input description: "))
    return user


def create(phone_dir: dict, idcc: int, user: list) -> dict:
    idcc += 1
    phone_dir[idcc] = user
    return phone_dir, idcc


# user1 = ["name1", "surname1", "phone1", "description1"]
# user2 = ["name2", "surname2", "phone2", "description2"]

# phone_dir, key_count = create(phone_dir, key_count, user1)
# phone_dir, key_count = create(phone_dir, key_count, user2)


def menu():
    key_count = 0
    phone_dir = dict()
    while True:
        print(
            """1 - create
2 - read
3 - update
4 - delete
5 - export
6 - import
7 - print"""
        )
        num = input("Operation: ")
        if num == "0":
            break
        elif num == "1":
            user = input_user()
            phone_dir, key_count = create(phone_dir, key_count, user)
        elif num == "2":
            searching = input("Start of surname: ")
            read(phone_dir, searching)
        elif num == "3":
            searching = input("Start of surname: ")
            print("New data (leave empty to not update)\n" + "-" * 20)
            name = input("Name: ")
            surname = input("Surname: ")
            phone = input("Phone: ")
            description = input("Description: ")
            phone_dir = update(
                phone_dir,
                searching,
                name if name != "" else None,
                surname if surname != "" else None,
                phone if phone != "" else None,
                description if description != "" else None,
            )
        elif num == "4":
            searching = input("Start of surname: ")
            phone_dir = delete(phone_dir, searching)
        elif num == "5":
            file_name = input("File name: ")
            export_phone_dir(phone_dir, file_name)
        elif num == "6":
            file_name = input("File name: ")
            phone_dir = import_data(file_name)
        elif num == "7":
            print(phone_dir)


def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + ".txt")
    with open(full_name, mode="w", encoding="utf-8") as file:
        for idc, user in phone_dir.items():
            file.write(f"{idc},{user[0]},{user[1]},{user[2]},{user[3]}\n")


def import_data(file_name: str) -> dict:
    phone_dir = dict()
    data = ""
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + ".txt")
    with open(full_name, mode="r", encoding="utf-8") as file:
        data = file.readlines()
    for line in data:
        values = line[:-1].split(",")
        phone_dir[int(values[0])] = values[1:]
    return phone_dir


def read(phone_dir: dict, searching: str):
    for idc, user in phone_dir.items():
        if user[1].startswith(searching):
            print(f"{idc},{user[0]},{user[1]},{user[2]},{user[3]}")


def update(
    phone_dir: dict,
    searching: int,
    name: str = None,
    surname: str = None,
    phone: str = None,
    description: str = None,
) -> dict:
    for _, user in phone_dir.items():
        if user[1].startswith(searching):
            if not name is None:
                user[0] = name
            if not surname is None:
                user[1] = surname
            if not phone is None:
                user[2] = phone
            if not description is None:
                user[3] = description
    return phone_dir


def delete(phone_dir: dict, searching: str) -> dict:
    for idc, user in phone_dir.items():
        if user[1].startswith(searching):
            phone_dir.pop(idc)
            print("\nSuccesfully deleted\n")
            break
    else:
        print("\nNothing to delete\n")

    return phone_dir


def menu_test():
    key_count = 0
    phone_dir = dict()
    user = ["q", "w", "e", "r"]
    phone_dir, key_count = create(phone_dir, key_count, user)
    print("Created new user:")
    print(phone_dir)


    print("Read function:")
    searching = "w"
    read(phone_dir, searching)

    searching = "w"
    phone_dir = update(phone_dir, searching, "a", "s", None, "f")
    print("Updated user:")
    print(phone_dir)

    export_phone_dir(phone_dir, "test")
    print("Exported phone_dir to file")

    delete(phone_dir, "s")
    print("Deleted user:")
    print(phone_dir)

    phone_dir = import_data("test")
    print("Imported phone_dir from file:")
    print(phone_dir)

# menu_test()
menu()