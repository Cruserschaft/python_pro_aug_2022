#1) Создайте декоратор, который зарегистрирует декорируемый класс в
#списке классов.




classes = []
class Adder:
    def __init__(self, cl):
        self.cl = cl

    def __call__(self):
        classes.append(self.cl)



@Adder
class Hello:
    def __str__(self):
        return "Hello from Hello"


@Adder
class Bye:
    def __str__(self):
        return "Hello from Bye"



a = Hello()
print(a)
b = Bye()
print(b)
print(classes)