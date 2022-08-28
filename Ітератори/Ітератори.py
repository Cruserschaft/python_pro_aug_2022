#1 Завдання
##1) Реализуйте генераторную функцию, которая будет возвращать по
##одному члену геометрической прогрессии с указанным множителем.
##Генератор должен остановить свою работу или по достижению указанной
##границы, или при передаче команды на завершение.


stop = 100
def geom_progression(value):
    if isinstance(value, int|float):
        return (i * value for i in range(1, stop))



x = geom_progression(3)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

y = geom_progression(17.5)
print(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))

#2 Завдання
##2) Реализуйте свой аналог генераторной функции range(). Да, вы теперь
##знаете, что это - генератор.


def my_range(start, stop):
    if not isinstance(start, int) and not isinstance(stop, int):
        raise ValueError("Must be integer")
    return (i for i in range(start, stop))

x = my_range(10, 20)
print(x)
print(next(x))
print(next(x))
print(next(x))


#3 Завдання
##3) Напишите функцию-генератор, которая будет возвращать простые числа.
##Верхняя граница этого диапазона должна быть задана параметром этой
##функции.


def prime_num(value):
    for i in range(1, value + 1):
        for j in range(2, i):
            if not i % j:
                break
        else:
            yield i

x = prime_num(20)

print(x)

for i in x:
    print(i)

#4 Завдання
##4) Напишите выражение-генератор для заполнения списка. Список должен
##быть заполнен кубами чисел от 2 и до указанной вами величины.

def sq_list(value):
    return (i*i for i in range(1, value))

x = sq_list(30)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


