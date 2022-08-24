import settings
from logger import *


class Shop:
    def __init__(self, my_money:int):
        self._my_money = my_money
        self.all_thing = []


        
    def get_all(self):
        result = ""
        if len(self.all_thing)!= 0:
            for i in self.all_thing:
                result+= f"{i.name} - {i.amount} шт.\n"

            return result
    @property
    def my_money(self):
        return self._my_money

    @my_money.setter
    def my_money(self, value):
        if isinstance(value, int|float):
            logger.info(f"Начислено {value} грн.")
            self._my_money = value


My_shop = Shop(0)

#Проверка gettera and settera
#print(My_shop.my_money)
#My_shop.my_money = 2



class Thing:
    def __init__(self, name:str, cost:int, description:str, weight:list, amount:int):
        self.name = name
        self.cost = cost
        if not isinstance(self.cost, int|float) or self.cost<=0:
            logger.warning(f"Неправильная ціна товару {self.name}")
            raise ValueError(f"Неправильная ціна товару {self.name}")
        self.description = description
        self.weight = weight
        self.amount = amount
        My_shop.all_thing.append(self)

    def __str__(self):
        return f"{self.name}"


    def get_cost(self):
        return f"Ціна на {self.name} - {self.cost} гривень"








class Buyer:

    def __init__(self, pib:list, phone_number:str, buyer_id = None):
        self.subname = pib[0]
        self.name = pib[1]
        self.patr = pib[2]
        self.phone_number = phone_number
        self.phone_number = self._validate_phone_number(self.phone_number)
        self.buyer_id = self.name[0] + self.subname + self.phone_number[-4:]
        self.purchases = Cart()

    def __str__(self):
        return f"{self.name} {self.subname}\n{self.buyer_id}\n{self.purchases}"

    def to_purchase(self, item):
        self.purchases.add_item(item)
        

                     
    def to_buy(self):
        My_shop.my_money += self.purchases.get_all("cost")
        logger.info(f"{self.name} {self.subname} придбав {self.get_all_purchases()}")
        return f"Ви придбали: \n{self.get_all_purchases()}\nЗверніться в найближче відділення і укажіть свій ID: {self.buyer_id}"
        
            

    def get_all_purchases(self):
        return self.purchases.get_all()
        

    def _validate_phone_number(self, phone_number):
        if len(phone_number) == 13:
            if phone_number[0:4] == "+380":
                return phone_number
            else:
                self._error_phone_number()
        else:
            if len(phone_number) == 10:
                phone_number = f"+38{phone_number}"
                return phone_number
            else:
                self._error_phone_number

    def _error_phone_number(self):
        print(f"Введіть правильно номер телефону")




class Cart:
    def __init__(self):
        self.purchases = {}

    def __str__(self):
        tmp = ""
        for i in self.purchases:
            tmp+=f"\n{i.name}: {self.purchases[i]}"
        return tmp


    def add_item(self, item: Thing):
        for i in My_shop.all_thing:
            if i.amount==0:
                return f"Вибачте, торвар закінчився"
            i.amount-=1

            if len(self.purchases) == 0:
                self.purchases[item] = 1
                return f"{item.name} занесено до кошика"

            else:
                if item in self.purchases:
                    self.purchases[item]+=1
                    return f"{item.name} занесено до кошика"
                else:
                    self.purchases[item] = 1
                    return f"{item.name} занесено до кошика"
                
    def __len__(self):
        return len(self.purchases)

    
    def __getitem__(self, item):
        if isinstance(item, int):
            return list(self.purchases.keys())[item]

        if isinstance(item, slice):
            return "\n".join(map(str, list(self.purchases.keys())[item]))

    def __iter__(self):
        return CartIter(list(self.purchases.keys()))

    def get_all(self, name = "all"):
        all_cost = 0
        if len(self.purchases)==0:
            return f"У вас нет покупок"
        
        for i in self.purchases:
            all_cost+=i.cost*self.purchases[i]

        if name == "cost":
            return all_cost
        return f"{str(self)}\nЗагальна вартість - {all_cost}"




class CartIter:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __str__(self):
        return "\n".join(map(str, self.wrapped))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        raise StopIteration











try:
    pen = Thing("Ручка", 10, "Масляна ручка, дуже добре пише", [20, "g"], 153)
    perfume = Thing("Духи", 120, "А пахне, наче газовий гігант Юпітер", [100, "g"], 31)
    mazda6 =Thing("Мазда 6", 100000, "Мазда 6 150 к.с.", [1578, "kg"], 5)
    pencil = Thing("Олівець", 7, "Звичайний олівець B2", [20, "g"], 20)

except Exception as err:
    print(err)
    

buyer1 = Buyer(["Василенко", "Петро", "Олексійович"], "0935678456")
buyer2 = Buyer(["Іваненко", "Іван", "Степанович"], "+380993135745")
buyer3 = Buyer(["Чепурна", "Оксана", "Василівна"], "0501255345")




##print(My_shop.get_all())
##print(pen.get_cost())
##print(perfume.description)
##print(My_shop.all_thing[0].cost)
##print(pen)
##
##
##
##
###Перевірка
##print(buyer1.to_purchase(pen))
##print(buyer1.to_purchase(pen))
##print(buyer1.to_purchase(pen))
##print(buyer1.to_purchase(perfume))
##print(buyer1.to_purchase(pen))
##print(buyer1.get_all_purchases())
##print(buyer1.to_buy())
##print(f"Мої гроші - {My_shop.my_money}")
##
##
##
##
##
##print(buyer2.to_purchase(perfume))
##print(buyer2.to_purchase(perfume))
##print(buyer2.to_purchase(perfume))
##print(buyer2.to_purchase(perfume))
##print(buyer2.to_purchase(perfume))
##print(buyer2.to_buy())
##print(f"Мої гроші - {My_shop.my_money}")
##
##
##
##





###Перевірка ітератора
##
##buyer1.to_purchase(pen)
##buyer1.to_purchase(pen)
##buyer1.to_purchase(pen)
##buyer1.to_purchase(perfume)
##buyer1.to_purchase(perfume)
##buyer1.to_purchase(mazda6)
##buyer1.to_purchase(pencil)
##buyer1.to_purchase(pencil)
##buyer1.get_all_purchases()
##
##
##print(buyer1)
##
##print(len(buyer1.purchases))
##print(buyer1.purchases[1])
##print(buyer1.purchases[:3])
##
##it = iter(buyer1.purchases)
##
##
##print(it)
##
##while True:
##    try:
##        item = next(it)
##        print(item)
##    except StopIteration:
##        break

