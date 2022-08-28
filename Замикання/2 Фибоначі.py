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



