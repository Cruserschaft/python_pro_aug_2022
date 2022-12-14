import datetime
from itertools import chain


class Product:
    """
    Класс Product

    переменные класса:

    name: Название продукта

    cose: Цена продукта
    
    """
    def __init__(self, name:str, cost:int):
        self.name = name
        self.cost = cost


    def __str__(self):
        return f"{self.name}"




dough = Product("Тесто", 30)
dough_cheese = Product("Тесто с сырной коркой", 40)

cheese = Product("Сыр", 12)
salami = Product("Салями", 15)
meat = Product("Мясо", 20)
pineapple = Product("Ананас", 15)
apple = Product("Яблоки", 10)
fish = Product("Рыба", 12)
potato = Product("Картошка", 8)
tomato = Product("Помидор", 8)
#Автору очень жаль за испорченый аппетит :C


class Pizza:
    """
    Класс Pizza

    Переменные:
    dough: Вид теста для пиццы
    
    prod: Список со всеми ингридиентами
    
    today: Переменная, отвечающая для проверки, блюдо ежедневное или нет

    """
    def __init__(self, dough, *args, today = False):
        self.dough = dough
        self.prod = list(args)
        self.today = today


    def __str__(self):
        return f"Пицца\nОснова:{self.dough.name}\nДобавки: {self.get_all_additions()}\nВсего: {self.get_cost()} грн.\n"


    def get_all_additions(self):
        if not self.prod:
            return None
        return ",".join(map(str, self.prod))


    def get_cost(self):
        tmp = self.dough.cost
        for i in self.prod:
            tmp+=i.cost
            
        if self.today:
            return tmp/2
        return round(tmp)

            
        
#Запись пиццы на каждый день недели
today_pizzas = [Pizza(dough, cheese, cheese, cheese, today = True),
                Pizza(dough, cheese, meat, pineapple, tomato, today = True),
                Pizza(dough_cheese, cheese, cheese, pineapple, potato, today = True),
                Pizza(dough, apple, pineapple, cheese, fish, today = True),
                Pizza(dough_cheese, fish, cheese, cheese, today = True),
                Pizza(dough, apple, meat, fish, potato, today = True),
                Pizza(dough_cheese, pineapple, fish, today = True)
                ]


def get_me_today_pizza():
    return today_pizzas[(datetime.datetime.weekday(datetime.datetime.now()))]






piz1 = Pizza(dough_cheese, cheese, salami, meat)
print(piz1)

piz2 = Pizza(dough, cheese, fish, meat)
print(piz2)

piz3 = get_me_today_pizza()
print(piz3)


