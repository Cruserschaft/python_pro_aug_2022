#2) Реализуйте функционал, который будет запрещать установку полей класса
#любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
#попытаться присвоить, например, строку, то должно быть возбужденно
#исключение.

class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError
        self.val = value

    def __get__(self, instance, owner):
        return self.val


class Box:
    x = Descriptor()
    y = Descriptor()
    z = Descriptor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __str__(self):
        return f"{self.x * self.y * self.z}"




b1 = Box(1, 2, 3)
print(b1)


#c = Box("hu", 3, 5)