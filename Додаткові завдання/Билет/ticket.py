from datetime import *
import random
import settings


class RegularTicket:
    """
    Класс Ticket

    Переменные класса:

    name: Имя, на которое записан билет

    date: Дата мероприятия

    cost: Расчетная переменная, если > 60 дней - скидка до 0.4 от стоимости, если < 10 дней - 110% грн.

    dis_stud: Входящая переменная, отвечает за проверку, нужно ли покупателю студенческий дисконт
    """
    def __init__(self, name:str, date:"dd.mm.yyyy"):
        self.name = name
        self.date = date
        self.cost = settings.COST_TICKET
        

    def __str__(self):
        return f"Билет на {self.date}\nна имя {self.name}\nНомер билета: {self.rand_ticket()}\nСумма оплаты: {self.cost}\n"

    
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

class StudTicket(RegularTicket):
    def __init__(self, name:str, date:"dd.mm.yyyy"):
        super().__init__(name, date)
        self.cost = round(settings.COST_TICKET * settings.DISCONT_STUD)

    def __str__(self):
        return f"{super().__str__()}Студенческий билет"




class DiscontTicket(RegularTicket):
    def __init__(self, name:str, date:"dd.mm.yyyy"):
        super().__init__(name, date)
        self.cost = round(settings.COST_TICKET * settings.DISCONT_PRE)
        
    def __str__(self):
        return f"{super().__str__()}Предварительный билет"




class UnluckyTicket(RegularTicket):
    def __init__(self, name:str, date:"dd.mm.yyyy"):
        super().__init__(name, date)
        self.cost = round(settings.COST_TICKET * settings.DISCONT_UNLUCKY)

    def __str__(self):
        return f"{super().__str__()}Опоздавший билет"








#Перевірки
tic1 = StudTicket("Микола", "12.03.2023")
print(tic1)
print("*"*20)
tic2 = DiscontTicket("Василь", "19.08.2022")
print(tic2)
print("*"*20)
tic3 = UnluckyTicket("Сашко", "19.08.2022")
print(tic3)





