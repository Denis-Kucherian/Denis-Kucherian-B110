import os


def dir_view():
    d = os.listdir()
    print('Список папок:')
    for index, element in enumerate(d, start=1):
        if os.path.isdir(element):
            print(f'{index}. {element}')


if __name__ == '__main__':
    dir_view()