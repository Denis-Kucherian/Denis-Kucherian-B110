# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_list = [1, 1]  # начало ряда не с "0"
    for i in range(0, (m - 1)):
        fib_list.append(fib_list[i] + fib_list[i + 1])
    return fib_list[n:(m + 1)]


print(fibonacci(5, 15))  # ряд Фибоначчи с n по m


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):  # внешний цикл от 1 до (длина списка - 1)
        for i in range(len(origin_list) - n):  # внутренний от 0 до (длина списка - n -1)
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]  # сдвигаем наибольшее в конец
        n += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_numb(func, input_list):
    output_list = []
    for i in range(len(input_list)):
        if func(input_list[i]) == True:
            output_list.append(input_list[i])  # если элемент нечётный - добавляем в возвращаемый список
    return output_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

func = lambda n: n % 2 != 0  # проверка на нечётность

print(filter_numb(func, input_list))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('Введите координаты вершин параллерограмма: \n'
      'А1(х1 ,у1), А2(х2 ,у2), А3(x3, у3), А4(x4, у4))')

x = [int(input('x{} = '.format(x))) for x in range(1, 5)]  # сначала абцисы
y = [int(input('y{} = '.format(y))) for y in range(1, 5)]  # потом ординаты

if ((x[0] + x[2]) / 2) == ((x[1] + x[3]) / 2) and ((y[0] + y[2]) / 2) == (
        (y[1] + y[3]) / 2):  # проверяем точку пересечения диагоналей
    print('Это параллерограмм!')
else:
    print('Это не параллерограмм!')
