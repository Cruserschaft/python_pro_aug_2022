import time
import os
#4) Создайте декоратор с параметрами для проведения хронометража работы
#той или иной функции. Параметрами должны выступать то, сколько раз нужно
#запустить декорируемую функцию и в какой файл сохранить результаты
#хронометража. Цель - провести хронометраж декорируемой функции.

def Timer(num, file):
    def wrapped(func):
        if not os.path.exists(file):
            with open(file, "w"):
                pass
        with open(file, "a") as f:
            for i in range(num):
                tmp = time.time()
                res = func()
                f.write(f"{time.time()-tmp}\n")

        return func
    return wrapped



@Timer(10, "file.txt")
def sleep():
    time.sleep(1)
    return 1

a = sleep()


