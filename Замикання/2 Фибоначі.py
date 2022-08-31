import timeit

"""2) Используя функцию замыкания реализуйте такой прием программирования
как Мемоизация - https://en.wikipedia.org/wiki/Memoization
Используйте полученный механизм для ускорения функции рекурсивного
вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
просто рекурсивным подходом."""


def fibonacci():
    results = [0, 1, ]

    def get_fib(n):
        if n < len(results):
            return results[n-1]
        for i in range (n-len(results)):
            results.append(results[-1]+results[-2])
        return results[-1]

    return get_fib


x = fibonacci()

print(x(5))
print(x(7))
print(x(3))
print(x(20))
print(x(4))


def recurse_fibonacci():
    def get_fib(n):
        results = [0, 1]
        for i in range (n-len(results)):
            results.append(results[-1]+results[-2])
        return results[-1]

    return get_fib


y = recurse_fibonacci()

print(y(5))
print(y(7))
print(y(3))
print(y(20))
print(y(4))






first = """
def fibonacci():
    results = [0, 1, ]

    def get_fib(n):
        if n < len(results):
            return results[n-1]
        for i in range (n-len(results)):
            results.append(results[-1]+results[-2])
        return results[-1]

    return get_fib


x = fibonacci()

x(5)
x(7)
x(3)
x(20)
x(4)
"""

second = """
def recurse_fibonacci():
    def get_fib(n):
        results = [0, 1]
        for i in range (n-len(results)):
            results.append(results[-1]+results[-2])
        return results[-1]

    return get_fib


y = recurse_fibonacci()

y(5)
y(7)
y(3)
y(20)
y(4)
"""



print(timeit.timeit(first, number=1000000)) #4.6
print(timeit.timeit(second, number=1000000)) #6.2







