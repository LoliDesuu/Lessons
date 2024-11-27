# int() --> int(input()) - преобразование ввода str в тип int целых чисел
# float()
# bool()

# salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
# print(round(sum(salary)/len(salary), 2), '- средняя зарплата в компании.' )
# print(round(max(salary), 2), '- максимальная зарплата в компании.' )
# print(round(min(salary), 2), '- минимальная зарплата в компании.' )
#
# names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
# zipped = dict(zip(names, salary))
# print(zipped['Денис'], '- это зарплата Дениса.')
#
# a = [0, 0, 0, 0]
# b = '0'
# print(id(b))
#
# def helper():
#     """
#     Это функция-помощник.
#     """
#     pass
#
# print(helper.__doc__)

# Максимум в списке
# Подсчёт чётных чисел в списке
# Уникальный список

def max_in_list(list_):
    max_ = list_[0]
    for elem in list_:
        if elem > max_ :
            max_ = elem
    return max_

print(max_in_list([-1, -53, -415, -42, -4]))

def sum_of_even(*list_):
    sum_ = 0
    for elem in list_:
        if elem == 0:
            continue
        if elem % 2 == 0:
            sum_ += 1
    return sum_

print(sum_of_even(42, 45, 245, 34, 32, 0))

def unique_list(*list_):
    new_list = []
    for elem in list_:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

print(unique_list(1, 2, 3 ,4, 5, 6, 7, 8, 1, 2, 3 ,4, 5, 6, 7, 8))
