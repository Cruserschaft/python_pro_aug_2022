#3) Реализуйте свойство класса, которое обладает следующим
#функционалом: при установки значения этого свойства в файл с заранее
#определенным названием должно сохранятся время (когда устанавливали
#значение свойства) и установленное значение.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        with open("file.txt", "a") as f:
            f.write(f"{key} was change to {value}\n")
        self.__dict__[key] = value



c = Cat("Barsik", 5)
c.name = "Murzik"
