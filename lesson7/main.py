# Функция count_calls подсчитывающая вызовы остальных функций.

calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

def is_contains(string, list):
    count_calls()
    for elem in list:
        elem.lower() == string
        return True
    return False


# Проверки:
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
