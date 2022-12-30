# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# РЕШЕНИЕ

from math import pi

d = int(input("Задайте точность для числа Пи:\n"))
print(f'число Пи c заданной точностью {d} равно {round(pi, d)}')


# Задача 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# РЕШЕНИЕ

# n = int(input('Введите число N: '))
# list = []
# a = n
# if n > 1:
#     restart = True
#     while restart:
#         restart = False
#         for i in range (2, n+1):
#             if n%i == 0:
#                 list.append(i)
#                 n = int(n/i)
#                 restart = True
#                 break

#     print(f'Простые множители числа {a} - {list}')
# elif n == 1:
#     print(f'Простые множители числа {a} - [1]')
# else:
#     print(f'Вы ввели не правильное число')

# Задача 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# РЕШЕНИЕ

# 1 вар
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# 2 Вар
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

# Задача 4. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# РЕШЕНИЕ

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
#         result += (f'{koef[i]}x**{k} + ')
#     k -= 1
#     i += 1


# if koef[-1] != 0:
#     result += (f'{koef[-1]}= 0')
# else:
#     result += ('= 0')
# with open('Task4.txt', 'w', encoding='utf8') as file:
#     file.write(f'Список коэффициентов: {koef}\nМногочлен: {result}')

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# Решение

# import random

# # запись в файл


# def write_file(name, st):
#     with open(name, 'w') as data:
#         data.write(st)

# # создание случайного числа от 0 до 100


# def rnd():
#     return random.randint(0, 101)

# # создание коэффициентов многочлена


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst

# # создание многочлена в виде строки


# def create_str(sp):
#     lst = sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# # получение степени многочлена


# def sq_mn(k):
#     if 'x^' in k:
#         i = k.find('^')
#         num = int(k[i+1:])
#     elif ('x' in k) and ('^' not in k):
#         num = 1
#     else:
#         num = -1
#     return num

# # получение коэффицента члена многочлена


# def k_mn(k):
#     if 'x' in k:
#         i = k.find('x')
#         num = int(k[:i])
#     return num

# # разбор многочлена и получение его коэффициентов


# def calc_mn(st):
#     st = st[0].replace(' ', '').split('=')
#     st = st[0].split('+')
#     lst = []
#     l = len(st)
#     k = 0
#     if sq_mn(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1  # степень
#     ii = l-1  # индекс
#     while ii >= 0:
#         if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
#             lst.append(k_mn(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1

#     return lst


# # создание двух файлов
# k1 = int(input("Введите натуральную степень для первого файла k = "))
# k2 = int(input("Введите натуральную степень для второго файла k = "))
# koef1 = create_mn(k1)
# koef2 = create_mn(k2)
# write_file("file34_1.txt", create_str(koef1))
# write_file("file34_2.txt", create_str(koef2))

# # нахождение суммы многочлена

# with open('file34_1.txt', 'r') as data:
#     st1 = data.readlines()
# with open('file34_2.txt', 'r') as data:
#     st2 = data.readlines()
# print(f"Первый многочлен {st1}")
# print(f"Второй многочлен {st2}")
# lst1 = calc_mn(st1)
# lst2 = calc_mn(st2)
# ll = len(lst1)
# if len(lst1) > len(lst2):
#     ll = len(lst2)
# lst_new = [lst1[i] + lst2[i] for i in range(ll)]
# if len(lst1) > len(lst2):
#     mm = len(lst1)
#     for i in range(ll, mm):
#         lst_new.append(lst1[i])
# else:
#     mm = len(lst2)
#     for i in range(ll, mm):
#         lst_new.append(lst2[i])
# write_file("file34_res.txt", create_str(lst_new))
# with open('file34_res.txt', 'r') as data:
#     st3 = data.readlines()
# print(f"Результирующий многочлен {st3}")