__author__ = 'Кучерян Денис Александрович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruit_list = ["яблоко", "банан", "киви", "арбуз"]
for i in  range(len(fruit_list)):
    print("{}. {:>10}".format(i+1, fruit_list[i]))
print("")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


first_list = [1, 7, 12, 'a', 'c', 3.14, 9.1]
second_list = [2, 5, 9.1, 56, 'o', 7, 'a']
temp_list = first_list
for i in first_list:
    for u in second_list:
        if i == u:
            temp_list.remove(u)
first_list = temp_list
print(first_list)
print("")


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