#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Empowered:
    def __init__(self, a=0, b=1):
        a = float(a)
        b = float(b)

        self.__first = a
        self.__second = b

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split('^', maxsplit=1)))

        if parts[1] == 0:
            raise ValueError()

        self.__first = parts[0]
        self.__second = parts[1]

    def display(self):
        print(self.__first ** self.__second)
    
    def power(self):
        a = self.first
        b = self.second
        
        p = a ** b
        return p


if __name__ == '__main__':
    r1 = Empowered(3, 3)
    r1.display()

    r2 = Empowered()
    r2.read("Insert the number and its power: ")
    r2.display()