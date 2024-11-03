# ЗАДАНИЕ ПО ТЕМЕ "Наследование классов"

import math


class Figure:
    sides_count = 0  # количество сторон фигуры

    def __init__(self, color, *sides):
        self.__color = list(color)  # цвет фигуры в RGB-формате (три целых числа от 0 до 255)
        self.__sides = [*sides]  # список длин сторон (ребер) фигуры
        # Если цвет в RGB-формате указан корректно, то filled = ИСТИНА (цвет задан),
        # если не корректно, то filled = ЛОЖЬ (цвет не задан)
        if len(list(color)) == 3 and all((isinstance(rgb, int) | rgb in list(range(0, 256))) for rgb in list(color)):
            self.filled = True
        else:
            self.filled = False
        # Если список длин сторон задан только целыми числами, то constructed = ИСТИНА (фигура может быть создана),
        # если не корректно, то constructed = ЛОЖЬ (фигура не может быть создана)
        if all((isinstance(side, int) for side in [*sides])):
            self.constructed = True
        else:
            self.constructed = False

    # Получение списка цветов фигуры в RGB-формате
    def get_color(self):
        if self.filled:
            return self.__color
        else:
            return f'Цвет не задан. Список {self.__color} не соответствует RGB-формату'

    # Проверка набора цветов на соответствие RGB-формату,
    # все аргументы r, g, b - целые числа от 0 до 255 включительно
    def __is_valid_color(self, r, g, b):
        rgb_color = [r, g, b]
        # Флаг ИСТИНА - если набор переданных значений корректен
        # Флаг ЛОЖЬ - если набор переданных значений не корректен
        rgb_flag = False
        if all((isinstance(rgb, int) and rgb in list(range(0, 256))) for rgb in rgb_color):
            rgb_flag = True
        return rgb_flag

    # Меняем цвет фигуры только в том случае, если передан корректный набор цветов RGB
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True

    # Проверка корректности списка сторон (ребер) фигуры
    def __is_valid_sides(self):
        # Флаг ИСТИНА - если количество переменных равно sides_count и все они целые числа
        # Флаг ЛОЖЬ - если количество переменных не равно sides_count или хотя бы одна из них не целое число
        sides_flag = False
        # if len(self.__sides) == self.sides_count and all(isinstance(side, int) for side in self.__sides):
        if len(self.__sides) == self.sides_count and self.constructed:
            sides_flag = True
        return sides_flag

    # Получение списка длин сторон (ребер) фигуры
    def get_sides(self):
        # Если количество элементов переданного списка сторон не равно sides_count или
        # хотя бы один из них не является целым числом
        if not self.__is_valid_sides():
            # if all(isinstance(side, int) for side in self.__sides):
            if self.constructed:
                if len(self.__sides) == 1:
                    self.__sides = list(self.__sides * self.sides_count)
                else:
                    self.__sides = list([1] * self.sides_count)
            else:
                self.__sides = f'Фигура не может быть построена. Список {self.__sides} задан некорректно'
        return self.__sides

    # Изменение списка длин сторон (ребер) фигуры
    def set_sides(self, *new_sides):
        sides = [*new_sides]
        if len(sides) == self.sides_count and all((isinstance(side, int) for side in sides)):
            self.__sides = sides
            self.constructed = True

    # Сумма длин сторон / ребер фигуры (периметр фигуры)
    def __len__(self):
        if self.constructed:
            return sum(self.get_sides())
        else:
            return f'Сумма длин сторон не найдена. Длины сторон заданы не целыми числами'


class Circle(Figure):
    sides_count = 1  # количество сторон фигуры - круг

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.constructed:
            self.__radius = super().get_sides()[0] / (2 * math.pi)  # Радиус круга
        else:
            self.__radius = None
        # print(f'радиус - {self.__radius}')

    # Площадь круга (с округлением до двух знаков после запятой)
    def get_square(self):
        if self.constructed:
            square = round(math.pi * self.__radius ** 2, 2)
            return square
        else:
            return f'Площадь не найдена. Длины сторон заданы не целыми числами'


class Triangle(Figure):
    sides_count = 3  # количество сторон фигуры - треугольник

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    # Площадь треугольника (с округлением до двух знаков после запятой)
    # Формула Герона - s = (p*(p-a)*(p-b)*(p-c))**0.5, где p - половина периметра
    def get_square(self):
        if self.constructed:
            sides = self.get_sides()  # Список сторон треугольника [a, b, c]
            p = sum(sides) / 2  # p = (a + b + c) / 2
            square = round((p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5, 2)
            return square
        else:
            return f'Площадь не найдена. Длины сторон заданы не целыми числами'


class Cube(Figure):
    sides_count = 12  # количество ребер фигуры - куб

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    # Объем куба (с округлением до двух знаков после запятой) / v = side ** 3
    def get_volume(self):
        if self.constructed:
            sides = self.get_sides()
            volume = round(sides[0] ** 3, 2)
            return volume
        else:
            return f'Объем не найден. Длины сторон заданы не целыми числами'


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# ПРИМЕРЫ ДЛЯ ПРОВЕРКИ ВСЕХ ФУНКЦИЙ (get, set, len, площадь, объем)
# circle2 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# # circle2 = Circle((300, 200, 100), 10, 5.5)
# print(circle2.get_color())
# circle2.set_color(0, 0, 0)  # изменится
# print(circle2.get_color())
# print(circle2.get_sides())
# circle2.set_sides(15)  # изменится
# print(circle2.get_sides())
# print(circle2.get_square())
# print(len(circle2))
# print()
# triangle2 = Triangle((100, 15, 235), 3, 2)
# # triangle2 = Triangle((100, 15, 235), 4, 5.1, 6)
# print(triangle2.get_color())
# triangle2.set_color(0, 15, 256)  # не изменится
# print(triangle2.get_color())
# print(triangle2.get_sides())
# triangle2.set_sides(5, 5, 5)  # изменится
# print(triangle2.get_sides())
# print(triangle2.get_square())
# print(len(triangle2))
# print()
# cube2 = Cube((222, 35, 130), 4, 5)
# # cube2 = Cube((222, 35, 430), 8, 9, 10)
# print(cube2.get_color())
# cube2.set_color(255, 255, 255)  # изменится
# print(cube2.get_color())
# print(cube2.get_sides())
# cube2.set_sides(10)  # не изменится
# print(cube2.get_sides())
# print(cube2.get_volume())
# print(len(cube2))
