#2) Создайте декоратор класса с параметром. Параметром должна быть
#строка, которая должна дописываться (слева) к результату работы метода
#__str__.


def decorator(name):
    class Wrapped:
        def __init__(self, cls):
            self.cls = cls

        def __call__(self):
            self.string = self.cls.__str__(self.cls)
            self.cls.__str__ = self.__str__

            return self.cls()

        def __str__(self):
            return f"{name}{self.string}"
    return Wrapped


@decorator("Mihail")
class Hello:
    def __str__(self):
        return " - Hello!"

@decorator("Ivan")
class Bye:
    def __str__(self):
        return " - Bye!"


h = Hello()
print(h)

b = Bye()
print(b)


