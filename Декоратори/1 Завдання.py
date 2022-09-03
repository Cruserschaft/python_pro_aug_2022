#1) Создайте декоратор, который будет подсчитывать, сколько раз была
#вызвана декорируемая функция.


class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, name):
        self.count += 1
        res = self.func(name)
        return res


@Counter
def func(name):
    return f"Hello, {name}"



print(func("Misha"))
print(func.count)
func("Sasha")
func("Mikola")
print(func.count)
