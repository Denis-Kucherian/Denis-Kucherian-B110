# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class R_trapezoid:
    def __init__(self, A, B, C, D):
        # вычисляем длину стороны по координатам точек
        def side_length(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = side_length(self.A, self.B)   # длина стороны AB
        self.BC = side_length(self.B, self.C)   # длина стороны BC
        self.CD = side_length(self.C, self.D)   # длина стороны CD
        self.DA = side_length(self.D, self.A)   # длина стороны DA

    # проверка, является ли фигура равнобочной трапецией


    # вычисляем периметр
    def perimeter_triangle(self):
        return self.AB + self.BC + self.CA

    # вычисляем площадь треугольника по формуле Герона
    def area_triangle(self):
        p_2 = self.perimeter_triangle() / 2
        return math.sqrt(p_2 * (p_2 - self.AB) * (p_2 - self.BC) * (p_2 - self.CA))

    # вычисляем высоту
    def height_triangle(self):
        return self.area_triangle() / self.AB


# tr = Triangle((5, 5), (6, 6), (9, 15))
#
# print(tr.perimeter_triangle())
# print(tr.area_triangle())
# print(tr.height_triangle())
