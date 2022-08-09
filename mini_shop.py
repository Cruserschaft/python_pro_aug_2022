
class Shop:
    def __init__(self, my_money:int):
        self.my_money = my_money
        self.all_thing = []


        
    def get_all(self):
        result = ""
        if len(self.all_thing)!= 0:
            for i in self.all_thing:
                result+= f"{i.name} - {i.amount} шт.\n"

            return result


My_shop = Shop(0)



class Thing:
    def __init__(self, name:str, cost:int, description:str, weight:list, amount:int):
        self.name = name
        self.cost = cost
        self.description = description
        self.weight = weight
        self.amount = amount
        My_shop.all_thing.append(self)

    def __str__(self):
        return f"{self.name}:{self.description}"

    def get_cost(self):
        return f"Ціна на {self.name} - {self.cost} гривень"








pen = Thing("Ручка", 10, "Масляна ручка, дуже добре пише", [20, "g"], 153)
perfume = Thing("Духи", 120, "А пахне, наче газовий гігант Юпітер", [100, "g"], 31)
mazda6 =Thing("Мазда 6", 100000, "Мазда 6 150 к.с.", [1578, "kg"], 5)

print(My_shop.get_all())
print(pen.get_cost())
print(perfume.description)
print(My_shop.all_thing[0].cost)
print(pen)




class Buyer:

    def __init__(self, pib:list, phone_number:str, buyer_id = None, purchases = {}):
        self.subname = pib[0]
        self.name = pib[1]
        self.patr = pib[2]
        self.phone_number = phone_number
        self.phone_number = self._validate_phone_number(self.phone_number)
        self.buyer_id = self.name[0] + self.subname + self.phone_number[-4:]
        self.purchases = purchases



    def to_purchase(self, item):
        for i in My_shop.all_thing:
            if i == item:
                if i.amount!=0:
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
                else:
                    return f"Вибачте, торвар закінчився"
                
            
    def to_buy(self):
        res = f"Вы придбали:\n"
        all_cost = 0
        for i in self.purchases:
            all_cost+=i.cost*self.purchases[i]
            res+=(f"{i.name} - {self.purchases[i]} шт.\n")
        res+=(f"Загальна вартість - {all_cost}\n")
        res+=(f"Зверніться в найближче відділення і укажіть свій ID: {self.buyer_id}")
        My_shop.my_money+=all_cost
        return res
        
            
        

    def get_all_purchases(self):
        all_cost = 0
        if len(self.purchases)==0:
            return f"У вас нет покупок"
        else:
            for i in self.purchases:
                all_cost+=i.cost*self.purchases[i]
                return f"{i.name} - {self.purchases[i]} шт."
            return f"Загальна вартість - {all_cost}"
        

        

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

    


    




buyer1 = Buyer(["Василенко", "Петро", "Олексійович"], "0935678456")
buyer2 = Buyer(["Іваненко", "Іван", "Степанович"], "+380993135745")
buyer3 = Buyer(["Чепурна", "Оксана", "Василівна"], "0501255345")



#Перевірка
print(buyer1.to_purchase(pen))
print(buyer1.to_purchase(pen))
print(buyer1.to_purchase(pen))
print(buyer1.to_purchase(perfume))
print(buyer1.to_purchase(pen))
print(buyer1.get_all_purchases())
print(buyer1.to_buy())
print(f"Мої гроші - {My_shop.my_money}")





print(buyer2.to_purchase(perfume))
print(buyer2.to_purchase(perfume))
print(buyer2.to_purchase(perfume))
print(buyer2.to_purchase(perfume))
print(buyer2.to_purchase(perfume))
print(buyer2.to_buy())
print(f"Мої гроші - {My_shop.my_money}")



























