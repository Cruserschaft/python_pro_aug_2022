import random

"""1) Реализуйте генераторную функцию, которая будет возвращать по одному
члену числовой последовательности, закон которой задается с помощью
пользовательской функции. Кроме этого параметром генераторной функции
должны быть значение первого члена прогрессии и количество выдаваемых
членов последовательности (n). Генератор должен остановить свою работу
или по достижению n — го члена , или при передаче команды на завершение."""


def generator(start, end, func):
    count = 0
    while count < end:

        command = yield start
        if command and command.lower() == "stop":
            return None
        start = func(start)
        count += 1




def square(value):
    if value < 2:
        return value+1
    return value ** 2


def plus_random(value):
    return value + (random.randint(1, 30))


def plus_self(value):
    return value + value


a = generator(1, 10, square)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


b = generator(1, 10, plus_random)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))


c = generator(1, 10, lambda x: x * 4)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

d = generator(6, 10, plus_self)
print(d)
for i in range(20):
    tmp = next(d)
    if tmp > 100:
        try:
            d.send("stop")
        except StopIteration:
            break
    print(tmp)







