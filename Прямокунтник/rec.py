import random
import math

"""
1) Создайте класс «Прямоугольник», у которого присутствуют два поля
(ширина и высота). Реализуйте метод сравнения прямоугольников по
площади. Также реализуйте методы сложения прямоугольников (площадь
суммарного прямоугольника должна быть равна сумме площадей
прямоугольников, которые вы складываете). Реализуйте методы
умножения прямоугольника на число n (это должно увеличить площадь
базового прямоугольника в n раз).
"""


class Rectangle:
    def __init__(self, height:int, width:int):
        self.height = height
        self.width = width

    def value(self):
        return self.width*self.height

    def __str__(self):
        return f'{self.width} x {self.height}'

    def __add__(self, other):
        tmp = Rectangle(self.width, (self.value()+other.value())/self.width)
        return tmp

    def __iadd__(self, other):
        tmp = Rectangle(self.width, (self.value()+other)/self.width)
        return tmp

    def __rmul__(self, other):
        tmp = Rectangle(self.width, (self.value()*other)/self.width)
        return tmp

    def __mul__(self, other: int):
        if not isinstance(other, int):
            return NotImplemented
        tmp = Rectangle(self.width, self.value()*other/self.width)
        return tmp

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.value() < other.value()

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.value() <= other.value()

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.value() > other.value()

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.value() >= other.value()



"""
#Перевірка складання
rec1 = Rectangle(1, 2)
rec2 = Rectangle(2, 2)
rec3 = rec1+rec2
print(rec3)
rec4 = rec3
rec4+=2
print(rec4)
"""

"""
#min max перевірка
recs = [Rectangle(random.randint(1, 100), random.randint(1, 100)) for i in range(10)]
print('\n'.join(map(str, recs)))
print("*"*20)
print(min(recs))
print(max(recs))
print("*"*20)
a = sorted(recs)
print('\n'.join(map(str, a)))
print("*"*20)
recs1 = recs[0]+recs[1]
print(recs1)
"""

"""
#Перевірка множення
print("*"*20)
rec10 = Rectangle(7, 7)
rec11 = rec10*2
print(rec11)

print("*"*20)
rec12 = Rectangle(10, 8)
rec13 = 5*rec12
print(rec13)
"""






