"""3) Напишите функцию, которая применит к списку чисел произвольную
пользовательскую функцию и вернет суммы элементов полученного списка."""
import random
import timeit


def summ(lis, func):
    return sum(func(i) for i in lis)


def sub_two(value):
    return value // 3


def square(value):
    return value ** 2


def no_action(value):
    return value

a = [random.randint(1, 50) for i in range(20)]
print(summ(a, sub_two))



b = [random.randint(1, 50) for i in range(20)]
print(summ(b, no_action))


c = [random.randint(1, 50) for i in range(20)]
print(summ(b, square))



#Перевірка швидкості праці коду


first = """
def square(value):
    return value ** 2
d = [i for i in range(100)]
def summ2(lis, func):
    res = 0
    for i in d:
        res += func(i)
    return res
summ2(d, square)
"""

second = """
def summ(lis, func):
    return sum(func(i) for i in lis)
    
def square(value):
    return value ** 2
    
e = [i for i in range(100)]
summ(e, square)
"""

print(timeit.timeit(first, number=100000)) #3,7
print(timeit.timeit(second, number=100000)) #3,8