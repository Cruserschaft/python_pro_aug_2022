import os
#3) Предположим, в классе определен метод __str__, который возвращает
#строку на основании класса. Создайте такой декоратор для этого метода,
#чтобы полученная строка сохранялась в текстовый файл, имя которого
#совпадает с именем класса, метод которого вы декорировали.



def to_file(func):
    def get_func(*args):
        tmp = func(*args)
        file = str(func).split()[1].split(".")[0]
        if not os.path.exists(f"{file}.txt"):
            with open(f"{file}.txt", "w"):
                pass
        with open(f"{file}.txt", "a") as f:
            f.write(f"{tmp}\n")



        return tmp

    return get_func




class Hello:
    def __init__(self, name):
        self.name = name

    @to_file
    def __str__(self):
        return f"{self.__class__.__name__}, {self.name}"




a = Hello("Misha")
print(a)

b = Hello("Vitaly")
print(b)