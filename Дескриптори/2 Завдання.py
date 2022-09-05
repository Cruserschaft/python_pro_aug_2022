#2) Реализуйте функционал, который будет запрещать установку полей класса
#любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
#попытаться присвоить, например, строку, то должно быть возбужденно
#исключение.

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Coords must be integer")
        self.__dict__[key] = value

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

b = Box(1, 2, 3)
print(b)

c = Box("hu", 3, 5)