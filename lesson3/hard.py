hw03_hard.py
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
print('y = ', float(equation[4:7]) * x + float(equation[11:24]))


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

date = input('Введите дату: ')
date_list = date.split('.')
day = int(date_list[0])
month = int(date_list[1])
year = int(date_list[2])

if year > 0 and year < 10000 and month > 0 and month < 13:
    if day > 0 and day < 31:
        print('Дата введена корректно')
    elif day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or
                        month == 8 or month == 10 or month == 12):
        print('Дата введена корректно')
    else:
        print('Дата введена некорректно !!!')
else:
    print('Дата введена некорректно !!!')


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
def get_floor(flat_number):
    # функция по номеру квартиры возвращает этаж и порядковый номер на этаже (кортеж из двух значений.
    # Квартиры расположены следующим образом: первый "блок" образует один этаж с одной квартирой
    # следующий блок - два этажа по две квартиры на каждом, третий блок - три этажа по три квартиры на каждом,
    # N-ный блок - N этажей по N квартир на каждом
    # эту законмерность и будем использовать: будем считать блоки по N*N квартир
    # пока искомая квартира не окажется внутри блока

    floor_block = 0  # номер "блока"
    floor = 0  # номер этажа
    max_flat = 0  # максимальный номер квартиры в блоке

    # отсчитываем квартиры блоками по N*N штук в каждой итерации, пока искомый номер не окажется внутри
    while max_flat < flat_number:
        floor_block += 1  # порядковый номер "блока" квартир, заодно это количество квартир на этаже
        floor += floor_block  # номер последнего этажа в блоке
        max_flat += floor_block ** 2

    # от последнего этажа отсчитываем вниз целые этажи до этажа с искомой квартирой
    floor -= (max_flat - flat_number) // floor_block

    return floor, floor_block - (max_flat - flat_number) % floor_block  # возвращаем номер этажа и "смещение"


if __name__ == '__main__':
    while True:
        print(*get_floor(int(input('Введите номер квартиры:\t'))))