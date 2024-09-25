#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ModelWindow:
    def __init__(self, a="", b=0, c=0, d=1, e=1, f="Белый", g=1, h=1):
        a = str(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = str(f)
        g = int(g)
        h = int(h)

        if ((g > 1) or (g < 0)) or ((h > 1) or (h < 0)):
            raise ValueError()

        self.__title = a
        self.__coord = [b, c]
        self.__horiz = d
        self.__vert = e
        self.__color = f

        if g == 0:
            self.__isvis = "невидимое"
        elif g == 1:
            self.__isvis = "видимое"

        if h == 0:
            self.__isbor = "отсутствует"
        elif h == 1:
            self.__isbor = "присутствует"

    @property
    def title(self):
        return self.__title

    @property
    def coord(self):
        return self.__coord

    @property
    def horiz(self):
        return self.__horiz

    @property
    def vert(self):
        return self.__vert

    @property
    def color(self):
        return self.__color

    @property
    def isvis(self):
        return self.__isvis

    @property
    def isbor(self):
        return self.__isbor

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(str, line.split(', ')))

        self.__title = parts[0]
        lista = []
        lista.append(int(parts[1]))
        lista.append(int(parts[2]))
        self.__coord = lista
        self.__horiz = abs(int(parts[3]))
        self.__vert = abs(int(parts[4]))
        self.__color = parts[5]
        
        if parts[6] == "0":
            self.__isvis = "невидимое"
        elif parts[6] == "1":
            self.__isvis = "видимое"
        else:
            raise ValueError

        if parts[7] == "0":
            self.__isbor = "отсутствует"
        elif parts[7] == "1":
            self.__isbor = "присутствует"
        else:
            raise ValueError

    def display(self):
        print(f"Заголовок: {self.__title}", "Координаты левого верхнего" + \
        f" угла: {self.__coord}", f"Размер по горизонтали: {self.__horiz}", \
        f"Размер по вертикали: {self.__vert}", f"Цвет: {self.__color}", \
        f"Видимость окна: {self.__isvis}", f"Рамка: {self.__isbor}", \
        sep = "\n")

    def move_horiz(self, x):
        if isinstance(x, int):
            b = self.coord[0] + x
            c = self.coord[1]
            
            self.__coord = [b, c]

            return self.coord
        else:
            raise ValueError()

    def move_vert(self, x):
        if isinstance(x, int):
            b = self.coord[0]
            c = self.coord[1] + x
            
            self.__coord = [b, c]

            return self.__coord
        else:
            raise ValueError()

    def size_horiz(self, x):
        if isinstance(x, int):
            d = self.horiz + x
            
            if d != 0:
                self.__horiz = d
            else:
                raise ValueError()

            return d
        else:
            raise ValueError()

    def size_vert(self, x):
        if isinstance(x, int):
            e = self.vert + x

            if e != 0:
                self.__vert = e
            else:
                raise ValueError()

            return e
        else:
            raise ValueError()

    def change_color(self, x):
        if isinstance(x, str):
            f = x

            self.__color = f

            return f
        else:
            raise ValueError()

    def change_vis(self, x):
        if isinstance(x, int):
            g = x
            
            if g == 0:
                self.__isvis = "невидимое"
            elif g == 1:
                self.__isvis = "видимое"
            else:
                raise ValueError

            return g
        else:
            raise ValueError()

    def change_bor(self, x):
        if isinstance(x, int):
            h = x
            
            if h == 0:
                self.__isbor = "отсутствует"
            elif h == 1:
                self.__isbor = "присутствует"
            else:
                raise ValueError

            return h
        else:
            raise ValueError()

    def check_state(self):
        print(f"Состояние окна: {self.isvis}, рамка {self.isbor}")


if __name__ == '__main__':
    r1 = ModelWindow("Настройки приложения", 150, 200, 600, 400, "Красный", 1, 0)
    r1.check_state()
    r1.move_horiz(100)
    r1.move_vert(-75)
    r1.change_bor(1)
    r1.display()
    
    r2 = ModelWindow()
    r2.read("Введите данные для окна: ")
    r2.size_horiz(50)
    r2.size_vert(-140)
    r2.change_color("Синий")
    r2.change_vis(1)
    r2.display()