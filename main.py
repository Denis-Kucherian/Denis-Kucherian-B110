# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random
n = int(input("введите количество целых чисел в списке: "))
random_list = []
for i in range (n):
    random_list.append(int(random.randint(0, 10)))
print("Ваш список: ", random_list)
new_list = []
for i in random_list:
    if i % 2 == 0:
        new_list.append(i / 4) # получаемые значения - тип float
    else:
        new_list.append(i * 2) # получаемые значения - тип int
print("Новый список: ", new_list)