__author__ = 'Кучерян Денис Александрович'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

name = input("Введите Ваше имя:")
age = int(input("Введите Ваш возраст:"))
delta_age = age - 18
if delta_age > 0:
    print(name, "Вы старше восемнадцати на", delta_age, "года/лет")
elif delta_age < 0:
    print(name, "Вы младше восемнадцати на", abs(delta_age), "года/лет")
else:
    print(name, "Вам 18 лет")


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

var_1 = input("Введите количество солнечных дней в январе 2023 года:")
var_2 = input("Введите количество пасмурных дней в январе 2023 года:")
var_temp = var_1
var_1 = var_2
var_2 = var_temp
print("Количество солнечных дней в январе 2023 года:", var_1)
print("Количество пасмурных дней в январе 2023 года:", var_2)
print("Всё перемешалось ;)")

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

a = float(input("Введите коэффициэнты квадратного уравнения, сначала a:"))
b = float(input("теперь b:"))
c = float(input("и, наконец, c:"))
diskrim = b * b - (4 * a * c)
print("вычисляем дискриминант:", diskrim)
if diskrim < 0:
    print("Уравнение не имеет действительных корней")
elif diskrim == 0:
    print("Единственный корень уравнения = ", -b / (2 * a))
else:
    import math
    x1 = (-b + math.sqrt(diskrim)) / (2 * a)
    x2 = (-b - math.sqrt(diskrim)) / (2 * a)
    print("Первый корень уравнения = ", x1)
    print("Второй корень уравнения = ", x2)

# ну, как-то так