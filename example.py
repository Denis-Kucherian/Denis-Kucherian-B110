import os, shutil
import sys

#
# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# def create_main_copy():
#     src_path = os.path.join(os.getcwd(), os.path.split(__file__)[1])
#     print(src_path)
#     des_path = os.path.join(os.getcwd(), "copy_" + os.path.split(__file__)[1])
#     print(des_path)
#     shutil.copy(src_path, des_path)
#
#
# if __name__ == '__main__':
#     create_main_copy()

new_file ="copy___" + os.path.split(__file__)[1]
shutil.copy(__file__, new_file)
