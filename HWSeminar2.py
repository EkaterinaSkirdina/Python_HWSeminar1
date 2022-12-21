import random

# Задача 1. Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# РЕШЕНИЕ

# num = input('Введите число: ')
# sum_digits = 0

# for item in num:
#     if item.isdigit():
#         sum_digits += int(item)

# print(sum_digits)


# Задача 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# РЕШЕНИЕ

# n = int(input('Введите число: '))

# k = 1
# for i in range(n):
#     i = i + 1
#     k = i * k
    
#     print(k, end=" ")


# Задача 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# РЕШЕНИЕ:

# n = int(input('Введите число n: '))
# my_list = []
# s = 0

# for i in range(1, n+1):
#     num = round((i + 1/i)**i, 2)
#     my_list.append(num)
#     s += num
# print(my_list)
# print(s)

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

# РЕШЕНИЕ:

# n = int(input('Введите колличество элементов списка, но не менее 6: '))
# my_list = []
# for i in range(n):
#     my_list.append(random.randint(-n, n))
# print(my_list)

# with open('file.txt', 'w') as data:
#     data.write('0 \n')
#     data.write('2 \n')
#     data.write('4 \n')
#     data.write('5 \n')

# prod = 1
# with open('file.txt', 'r') as data:
#     for line in data:
#         prod *= my_list[int(line)]

# print(prod)


# Задача 5. Реализуйте алгоритм перемешивания списка.

# my_list = []
# for i in range(6):
#     num = random.randint(0, 10)
#     my_list.append(num)
# print(my_list)

# new_list = my_list[:]

# for i in range(len(new_list)):
#     j = random.randint(0, len(new_list) - 1)
#     temp = new_list[i]
#     new_list[i] = new_list[j]
#     new_list[j] = temp
    
# print(new_list)
