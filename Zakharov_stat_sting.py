def only_letters(tested_string):
    """Фукция провеяет состоит ли строка только из букв английского алфавита"""
    for letter in tested_string:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True


def input_validation(str_test):
    """Фукция провеяет ввод пользователя"""
    while not only_letters(str_test):
        print("У вас ошибка")
        str_test = input("Введите строку состаящую только из английских букв: 'abcdefghijklmnopqrstuvwxyz' \n").lower()
    return str_test


def fill_dict(str_test):
    """Фукция провеяет ввод пользователя"""
    dict_test = {}.fromkeys(str_test, 0)
    for let in str_test:
        dict_test[let] += 1
    return dict_test


def print_all_stat(dict_test):
    """Функция печает кол-во повторений всех букв в строке"""
    for i in dict_test:
        print(f'буква {i} повторялась : {dict_test[i]}')
    print('')


def get_max_pair(dict_letters):
    """Функция создает словарь из максимально повторяющихся букв или буквы"""
    dict_max_repeat = {}
    return dict_max_repeat


def print_stat(length_dict):
    """Функция печает букву или буквы с максимальным кол-во повторений строке"""
    if length_dict > 1:
        print(f'Несколько символов имеют одинаковое кол-во повторений:')
    for i in dict_max_pair:
        print(f'буква {i} повторялась максимальное кол-во раз: {dict_max_pair[i]}')


str_letters = input("Введите строку состаящую только из английских букв: \n").lower()
str_user = input_validation(str_letters)
dict_repeat = fill_dict(str_user)
print_all_stat(dict_repeat)
dict_max_pair = get_max_pair(dict_repeat)
print_stat(len(dict_max_pair))