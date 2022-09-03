#2) Создайте декоратор, который зарегистрирует декорируемую функцию в
#списке функций, для обработки последовательности.

funcs = []
class Adder:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        funcs.append(self.func)
        res = self.func()
        return res


@Adder
def hello():
    return f"Hello"


@Adder
def bye():
    return f"Bye"


print(hello())
print(bye())

print(funcs)

for i in funcs:
    print(i())



