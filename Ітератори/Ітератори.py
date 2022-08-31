#1 Завдання
#1) Реализуйте генераторную функцию, которая будет возвращать по
#одному члену геометрической прогрессии с указанным множителем.
#Генератор должен остановить свою работу или по достижению указанной
#границы, или при передаче команды на завершение.


def geom_progression(value, start = 1, end = 100):    
    while start < end:
        yield start
        start*=value
        
        
x = geom_progression(3)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

y = geom_progression(5)
print(x)
print(next(y))
print(next(y))
print(next(y))
#print(next(y)) #Stop iteration



#2 Завдання
##2) Реализуйте свой аналог генераторной функции range(). Да, вы теперь
##знаете, что это - генератор.


def my_range(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1

    if len(args) == 2:
        start, stop, step = args[0], args[1], 1

    if len(args) == 3:
        start, stop, step = args[0], args[1], args[2]

    if step >= 0 and start > stop:
        raise ValueError()


    while start < stop:
        yield start
        start += step


x = my_range(10)
print(x)
print(next(x))

y = my_range(2, 10)
print(y)
print(next(y))
print(next(y))
print(next(y))

z = my_range(2, 10, 2)
print(z)
print(next(z))
print(next(z))
print(next(z))
print(next(z))


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


