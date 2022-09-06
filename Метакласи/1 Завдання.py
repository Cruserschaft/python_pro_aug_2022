#1) Реализуйте метакласс, который обладает следующим функционалом: при
#его использовании в файл с заранее определенным названием нужно
#сохранить имя класса и список его полей.
file = "file.txt"

class MetaFileSaver(type):
    def __init__(cls, classname, supers, classdict):
        res = ", ".join(map(str, list(cls.__dict__)))
        res = f"{cls.__name__}:\n {res}\n"
        with open(file, "a") as f:
            f.write(res)




class Circle(metaclass=MetaFileSaver):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"{self.radius}"

c = Circle(10)

class Box(metaclass=MetaFileSaver):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        if isinstance(other, int|float):
            self.x += other
            self.y += other
            self.z += other

b = Box(1, 1, 1)