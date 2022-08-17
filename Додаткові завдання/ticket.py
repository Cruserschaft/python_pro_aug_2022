from datetime import *
import random
import settings


class Ticket:
    def __init__(self, name:str, date:"dd.mm.yyyy", dis_stud = False):
        self.name = name
        self.date = date
        if not dis_stud:
            self.cost = settings.COST_TICKET * self.check_discont()
        else:
            self.cost = settings.COST_TICKET * settings.DISCONT_STUD
        

    def __str__(self):
        return f"Билет на {self.date}\nна имя {self.name}{self.rand_ticket()}\nСумма оплаты: {self.cost}\n"

    
    def check_discont(self):
        tmp = datetime.strptime(self.date, "%d.%m.%Y")
        if (tmp - datetime.now()).days > 60:
            return settings.DISCONT_PRE
        if (tmp - datetime.now()).days < 10:
            return settings.DISCONT_UNLUCKY
        return 1
        

    def rand_ticket(self):
        tmp = datetime.now()
        return f"{self.name[-1].upper()}{self.name[0].upper()}{random.randint(1,9)}{tmp.strftime('%m')}{random.randint(1,9)}{tmp.strftime('%d')}"


#Перевірки
tic1 = Ticket("Микола", "12.03.2023")
print(tic1)

tic2 = Ticket("Василь", "19.08.2022")
print(tic2)

tic3 = Ticket("Сашко", "19.08.2022", dis_stud = True)
print(tic3)





