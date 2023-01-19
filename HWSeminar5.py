# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Решение:

# Вариант с семинара:

# st = 'лдофы фдылабв аБв дловфы абвыдфлоф'.split()
# print(st)
# st = list(filter(lambda x: not 'абв' in x.lower(), st))
# print(' '.join(st))

# Свой вариант:

# my_text = 'абви аку дзщабв куку абв дада'
# my_list = [i for i in my_text.split() if 'абв' not in i]
# print(' '.join(my_list))




# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# total = 2021
# max_step = 28
# # Функция жеребьевки, рандомно задает значение для определения игрока, который будет ходить первым.
# def who_is_first():
#     motion = bool(randint(0,1))
#     return motion
# # Функция запуска игры, на основании выбора кол-ва игроков.
# def start_game():                       
#     game = int(input('Введите колличество игроков, 1 или 2: '))
#     if game == 1:
#         player_vs_bot()
#     if game == 2:
#         two_players()
# # Функция игры для 2х игроков
# def two_players():
#     global total
#     global max_step
#     player_1 = input('Игрок 1 введите ваше имя: ')
#     player_2 = input('Игрок 2 введите ваше имя: ')
#     motion = who_is_first()
#     if motion:
#         print(f'\nПервым ходит {player_1}')
#     else:
#         print(f'\nПервым ходит {player_2}')

#     print(f'''\nИгра начинается. Берите не более {max_step} конфет.
#     Побеждает игрок, сделавший последний ход.''')
#     while total > 0:
#         if motion:
#             step = int(input(f'\nХодит {player_1}. Сколько возьмете конфет?: '))
#             while step > max_step or step > total:
#                 step = int(input('Не правильное значение, попробуйте еще. Сколько возьмете конфет?: '))
#         else:
#             step = int(input(f'\nХодит {player_2}. Сколько возьмете конфет?: '))
#             while step > max_step or step > total:
#                 step = int(input('Не правильное значение, попробуйте еще. Сколько возьмете конфет?: '))
#         total -= step
#         print('Осталось', total, 'конфет')
#         motion = not motion

#     if motion:
#         print(f'\nИгра окончена! Победил {player_2}!!!')
#     else:
#         print(f'\nИгра окончена! Победил {player_1}!!!')
# # Функция игры с ботом
# def player_vs_bot():
#     global total
#     global max_step
#     player1 = who_is_first()
#     if player1:
#         print('\nВы ходите первым.')
#     else:
#         print('\nПервым ходит бот')
#     print(f'''\nИгра начинается. На столе всего {total} конфет.\nЗа один ход вы можете взять не более {max_step} конфет.\nПобеждает игрок, сделавший последний ход.''')
#     while total > 0:
#         if player1:
#             step = int(input('\nВаш ход. Сколько возьмете конфет?: '))
#             if step > max_step or step > total:
#                 step = int(input('Не правильное значение, попробуйте еще. Сколько возьмете конфет?: '))
#         else:
#             if total % (max_step + 1) != 0:
#                 step = total % (max_step + 1)
#             else:
#                 step = randint(1, 28)
#             print(f'\nХодит Бот. Он берет {step} конфет.')
#         total -= step
#         print('Осталось', total, 'конфет')
#         player1 = not player1

#     if player1:
#         print('\nИгра окончена! Победил Бот!!!')
#     else:
#         print('\nИгра окончена! ВЫ победили!!!')

# start_game()




# Задача 3. Создайте программу для игры в ""Крестики-нолики"".

# Решение:

# def print_maps():                 # Функция печати игрового поля
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])

# def step_maps(step, symbol):      # Функция хода
#     i = maps.index(step)
#     maps[i] = symbol

# def get_result():                 # Проверка победителя
#     win = ''
#     for i in victories:
#         if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
#             win = 'X'
#         if maps[i[0]] == '0' and maps[i[1]] == '0' and maps[i[2]] == '0':
#             win = '0'
#     return win

# maps = [1, 2, 3,         # Игровое поле
#         4, 5, 6,
#         7, 8, 9]

# victories = [[0,1,2],    # Выигрышные комбинации
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]

# finish = False
# player1 = True
# count = 0          # Счетчик ходов, на случай ничьей
# print_maps()
# while finish == False and count < 9:
#     if player1 == True:
#         symbol = 'X'
#         step = int(input("Ходит 'X': "))
#     else:
#         symbol = '0'
#         step = int(input("Ходит '0': "))
#     if step not in maps:
#         step = int(input('Вы ввели не верное значение, попробуйте снова: '))
#     step_maps(step, symbol)
#     print_maps()
#     win = get_result()
#     if win != '':
#         finish = True
#         print('Игра окончена! Победил', win, '!!!')
#         break
#     else:
#         player1 = not player1
#         count += 1
# else:
#     print('Игра окончена. Победила дружба!!!')



# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def text_compression(text):
    count = 1
    brief_text = ''

    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            brief_text += str(count) + text[i]
            count = 1
    brief_text += str(count) + text[len(text)-1]
    return brief_text

def text_recovery(brief_text):
    text = ''
    num = ''
    for i in range(len(brief_text)):
        if str.isdigit(brief_text[i]):
            num += brief_text[i]
        else:
            text += brief_text[i] * int(num)
            num = ''
    return text

def main():
    with open('TextTask4Sem5.txt', 'w') as data:
        data.write('aaaaaaaaaaabbbbbccddd')
    with open('TextTask4Sem5.txt', 'r') as data:
        my_text = data.read()
    print(my_text)
    zip_text = text_compression(my_text)
    print(zip_text)

    with open('CompressionTask4Sem5.txt', 'w') as data:
        data.write(zip_text)
    with open('CompressionTask4Sem5.txt', 'r') as data:
        new_text = data.read()
    new_text = text_recovery(new_text)
    print(new_text)
    with open('RecoveryTask4Sem5.txt', 'w') as data:
        data.write(new_text)

main()
