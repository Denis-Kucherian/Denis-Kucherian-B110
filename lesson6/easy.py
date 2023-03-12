# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Вводите положительные числа")


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as error:
    print("Ошибка:", error, ". Проверьте введенные числа.")


# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def create_dir():
    for i in range(1, 10):
        dir_name = ("dir_" + str(i))
        try:
            os.mkdir(dir_name)
        except:
            print(f"Папка {dir_name} существует")


def delete_dir():
    for i in range(1, 10):
        dir_name = ("dir_" + str(i))
        try:
            os.rmdir(dir_name)
        except:
            print(f"Папка {dir_name} не существует")


inp = input("Введите 1 для создания папок, 2 - для удаления: ")
if inp == "1":
    create_dir()
elif inp == "2":
    delete_dir()
else:
    print("Неправильный ввод")

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

def dir_view():
    d = os.listdir()
    print('Список папок:')
    for index, element in enumerate(d, start=1):
        if os.path.isdir(element):
            print(f'{index}. {element}')


if __name__ == '__main__':
    dir_view()

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

new_file ="copy___" + os.path.split(__file__)[1]
shutil.copy(__file__, new_file)
