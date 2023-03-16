# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, A, B, C):
        # вычисляем длину стороны по координатам точек
        def side_length(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        self.AB = side_length(self.A, self.B)   # длина стороны AB
        self.BC = side_length(self.B, self.C)   # длина стороны BC
        self.CA = side_length(self.C, self.A)   # длина стороны CA

    # вычисляем периметр
    def perimeter_triangle(self):
        return self.AB + self.BC + self.CA

    # вычисляем площадь треугольника по формуле Герона
    def area_triangle(self):
        p_2 = self.perimeter_triangle() / 2 # полупериметр
        return math.sqrt(p_2 * (p_2 - self.AB) * (p_2 - self.BC) * (p_2 - self.CA))

    # вычисляем высоту
    def height_triangle(self):
        return self.area_triangle() / self.AB


tr = Triangle((5, 5), (6, 6), (9, 15))

print(f"Периметр треугольника = {tr.perimeter_triangle()}")
print(f"Площадь треугольника = {tr.area_triangle()}")
print(f"Высота треугольника = {tr.height_triangle()}")
print("")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
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

    # проверяем, является ли фигура равнобокой трапецией, а не простой трапецией или параллерограммом или треугольником
    def check_trapezoid(self):
        return (self.AB == self.CD) and (self.BC != self.DA) and (self.B != self.C)

    # вычисляем периметр
    def perimeter_trapezoid(self):
        return self.AB + self.BC + self.CD + self.DA

    # вычисляем площадь трапеции по формуле Брахмапутры
    def area_trapezoid(self):
        p_2 = self.perimeter_trapezoid() / 2    # полупериметр
        return math.sqrt((p_2 - self.DA) * (p_2 - self.BC) * (p_2 - self.AB) ** 2)


tr = Trapezoid((2, 2), (4, 6), (6, 6), (8, 2))  # равнобокая трапеция

if tr.check_trapezoid():
    print("Это равнобокая трапеция")
    print(f"Сторона AB = {tr.AB}")
    print(f"Сторона BC = {tr.BC}")
    print(f"Сторона CD = {tr.CD}")
    print(f"Сторона DA = {tr.DA}")
    print(f"Периметр трапеции = {tr.perimeter_trapezoid()}")
    print(f"Площадь трапеции = {tr.area_trapezoid()}")
else:
    print("Это не равнобокая трапеция, проверь координаты")