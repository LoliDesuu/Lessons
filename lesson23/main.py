from math import pi
from math import sqrt


class Figure:
    sides_count = 0
    def __init__(self, sides:list, color:list , filled:bool = True):
        if isinstance(sides, list) or isinstance(sides, int) and isinstance(color, list) and isinstance(filled, bool):
            self.__color = color
            self.filled = filled
            if isinstance(sides, list):
                if len(sides) == self.sides_count:
                    self.__sides = sides
                else:
                    i = 0
                    self.__sides = []
                    while i < self.sides_count:
                        self.__sides.append(1)
                        i += 1
            if isinstance(sides, int):
                if sides == self.sides_count:
                    self.__sides = sides
                elif len(str(sides)) == 1:
                    i = 0
                    self.sides = sides
                    elem = self.sides
                    self.__sides = []
                    while i < self.sides_count:
                        self.__sides.append(elem)
                        i += 1
        else:
            raise ValueError('Указан неверный тип данных.')

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for elem in self.__sides:
            perimeter += elem
        return perimeter

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides) == True:
            self.__sides = list(new_sides)

    def __is_valid_color(self, r, g, b):
        if r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
            return True

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            is_valid = True
            for elem in args:
                if isinstance(elem, int) and elem > 0:
                    continue
                else:
                    is_valid = False
                    return is_valid
            return is_valid
        else:
            return False


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        radius = self.__sides / (pi * 2)
        return radius

    def get_square(self):
        square = self.__sides ** 2 * pi
        return square


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = 0.5 * (self.__sides[0] + self.__sides[1] + self.__sides[2])
        square = sqrt(p*(self.__sides[0] - p)*(self.__sides[1] - p)*(self.__sides[2] - p))


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        volume = self.sides ** 3
        return volume


circle1 = Circle(10, [200, 200, 100])
cube1 = Cube(6, [222, 35, 130])

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())