import abc

#1) Создайте ABC класс с абстрактным методом проверки целого числа на
#простоту. Т.е., если параметром этого метода является целое число и оно
#простое, то метод должен вернуть True, а в противном случае False.
#2) Создайте класс его наследующий.
#3) Создайте класс, который не наследует пользовательский ABC класс, но
#обладает нужным методом. Зарегистрируйте его в качестве виртуального
#подкласса.
#4) Проверьте работоспособность проекта.


class Validator(abc.ABC):
    @abc.abstractmethod
    def validate(self):
        pass


class Rational(Validator):
    def __init__(self, number):
        self.number = number

    def validate(self):
        for i in range(2, (self.number // 2) + 1):
            if self.number % i == 0:
                return False
        return True


class Rational2(Validator):
    def __init__(self, number):
        self.number = number

    def validate(self):
        for i in range(2, (self.number // 2) + 1):
            if self.number % i == 0:
                return False
        return True



r = Rational(10)
print(r.validate())
r2 = Rational(3)
print(r2.validate)


print("*"*20)
r3 = Rational2(5)
Validator.register(Rational2)
print(isinstance(r3, Validator))



