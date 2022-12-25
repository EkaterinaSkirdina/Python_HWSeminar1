import random
# Задача 1. 
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# РЕШЕНИЕ

def get_list(n):
    new_list = []
    for i in range(n):
        new_list.append(random.randint(-n, n))
    return new_list

def find_sum_el(some_list):
    sum_el = 0
    for i in range(len(some_list)):
        if i % 2 == 0:
            i += 1
        else:
            sum_el += some_list[i]
    return sum_el

my_list = get_list(7)
print(my_list)
print(find_sum_el(my_list))


# Задача 2. 
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# РЕШЕНИЕ

# def get_list(n):
#     new_list = []
#     for i in range(n):
#         new_list.append(random.randint(-n, n))
#     return new_list

# def prod_of_pairs(some_list):
#     new_list = []
#     p = 0
#     for i in range(len(some_list)//2+1):
#         p = some_list[i] * some_list[len(some_list)-i-1]
#         new_list.append(p)
#     return new_list

# my_list = get_list(5)
# print(my_list)
# my_list2 = prod_of_pairs(my_list)
# print(my_list2)


# Задача 3. 
# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# РЕШЕНИЕ

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



# Задача 4. 
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# РЕШЕНИЕ

# def get_bin_from_dec(d):
#     b = ''
#     while d != 0:
#         b = str(d%2) + b
#         d //=2
#     return b

# dec_num = int(input('Введите число: '))
# bin_num = get_bin_from_dec(dec_num)
# print(bin_num)



# Задача 5. 
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# РЕШЕНИЕ

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# def NegaFibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = [0]
# number = int(input('Введите число: '))
# for i in range(1, number + 1):
#     list.append(Fibonacci(i))
#     list.insert(0, NegaFibonacci(i))
# print(list)