import os


def view_table(data):
    print(f'|{"Имя":20}|{"Возраст":20}|')
    print('_' * 43)
    for person in data:
        print(f'|{person["name"]:20}|{person["age"]:<20}|')
    print('_' * 43)


def clear_table(data: list):
    data.clear()


spisok = [{'name': 'Pavel', 'age': '30'}, {'name': 'Andrey', 'age': '22'},
          {'name': 'Egor', 'age': '27'}]
view_table(spisok)

answer = input("Хочешь добавить данных?\n")
if answer.lower() == 'да':
    print("Если хочешь завершить ввод данных, то введи 0")
    while True:
        data = input("Введи имя возраст разделенные пробелом: ")
        if data == "0":
            print("Пользователь ввел все, что хотел")
            break
        sep_data = data.split()
        if len(sep_data) != 2:
            print("Должно быть 2 значения: Имя Возраст")
            continue
        if not sep_data[0].isalpha():
            print("Имя должно быть из букв")
            continue
        if not sep_data[1].isdigit():
            print("Возраст должен быть из цифр")
            continue

        spisok.append({'name': sep_data[0], 'age': float(sep_data[1])})

    view_table(spisok)

os.system('cls')

answer = input("Хочешь очистить данные?\n")
if answer.lower() == 'да':
    clear_table(spisok)
    view_table(spisok)