#1) Создайте дескриптор, который будет делать поля класса управляемые им
#доступными только для чтения.


class MyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        raise AttributeError("field is read-only")


class Order:
    name = MyDescriptor("Milk")

    def __str__(self):
        return str(self.name)

a = Order()
print(a.name)
a.name = "Coconut"