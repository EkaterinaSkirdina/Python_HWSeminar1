from random import *
# Задача 1. 
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# ПРОШЛОЕ РЕШЕНИЕ

# def get_list(n):
#     new_list = []
#     for i in range(n):
#         new_list.append(random.randint(-n, n))
#     return new_list

# def find_sum_el(some_list):
#     sum_el = 0
#     for i in range(len(some_list)):
#         if i % 2 == 0:
#             i += 1
#         else:
#             sum_el += some_list[i]
#     return sum_el

# my_list = get_list(7)
# print(my_list)
# print(find_sum_el(my_list))

# my_list = [23, 45, 73, 1, 4, 3, 9]
# sumEl = 0

# НОВОЕ РЕШЕНИЕ

# nums = [randint(1, 10) for n in range(7)]          # List Comprehension()
# print(nums)

# lst = [nums[index] for index in range(1, len(nums), 2)]
# print(f'{sum(lst)}')

# Задача 2. 
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# ПРОШЛОЕ РЕШЕНИЕ
# my_text = 'абви аку дзщабв куку абв дада'
# my_list = [i for i in my_text.split() if 'абв' not in i]           # List comprehension()
# print(' '.join(my_list))

# # НОВОЕ РЕШЕНИЕ
# st = 'лдофы фдылабв аБв дловфы абвыдфлоф'.split()     
# print(st)
# st = list(filter(lambda x: not 'абв' in x.lower(), st))            # Lambda() / filter()
# print(' '.join(st))



# Задача 3. 
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# ПРОШЛОЕ РЕШЕНИЕ

# n = list("1115566773322")

# list = n
# print(list)

# list_count = []
# for i in list:
#     count = 0
#     for k in list:
#         if k == i:
#             count += 1
#     list_count.append(count)
# print(list_count)

# result = []
# for i in range(len(list_count)):
#     if list_count[i] == 1:
#         result.append(list[i])
# print(result)

# НОВОЕ РЕШЕНИЕ

# lst = list(map(int, input("Введите числа через пробел:\n").split()))    #  map()
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]                    # List comprehension()
# print(f"Список из неповторяющихся элементов: {new_lst}")


# Задача 4. 
# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# ПРОШЛОЕ РЕШЕНИЕ

# from random import randint
# import random

# k = int(input('Задайте натуральную степень k: '))

# result = ''
# koef = []
# for i in range(k):
#     koef.append(randint(0, 100))

# i = 0
# j = 0
# while k > 1:
#     if koef[i] != 0:
#         result += (f'{koef[i]}*x^{k} + ')
#     k -= 1
#     i += 1


# if koef[-1] != 0:
#     result += (f'{koef[-1]}= 0')
# else:
#     result += ('= 0')
# with open('Task4.txt', 'w', encoding='utf8') as file:
#     file.write(f'Список коэффициентов: {koef}\nМногочлен: {result}')
# print(f'Список коэффициентов: {koef}\nМногочлен: {result}')

# НОВОЕ РЕШЕНИЕ

# import random

# k = int(input('Задайте натуральную степень k: '))
# koef = [random.randint(0,100) for i in range(k + 1)]
# print(koef)

# result = [f'{j}*x^{i}' for i, j in enumerate(koef)]        # List comprehension() / enumerate()
# result = result[5: 1:-1]
# result = ' + '.join(result)
# if koef[-1] != 0:
#     result += (f'{koef[-1]} = 0')
# else:
#     result += (' = 0')
# print(result, end='')
# with open('Task4.txt', 'w', encoding='utf8') as file:
#     file.write(f'Список коэффициентов: {koef}\nМногочлен: {result}')


# Задача 5. 
# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# ПРОШЛОЕ РЕШЕНИЕ

# def get_list(n):
#     new_list = []
#     for i in range(n):
#         new_list.append(round(random.uniform(0, 10), 2))
#     return new_list

# def get_frac_part(some_list):
#     some_list2 = []
#     for i in range(len(some_list)):
#         some_list[i] = round(some_list[i] - int(some_list[i]), 2)
#         some_list2.append(some_list[i])
#     return some_list2

# def diff_max_min(some_list2):
#     d = 0
#     d = max(some_list2) - min(some_list2)
#     return d

# my_list = get_list(5)
# print(my_list)
# my_list2 = get_frac_part(my_list)
# print(diff_max_min(my_list2))

# НОВОЕ РЕШЕНИЕ
lst = list(map(float, input("Введите числа через пробел:\n").split()))      # map()
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]                      # List Comprehension()
res = max(new_lst) - min(new_lst)
print(round(res,2))