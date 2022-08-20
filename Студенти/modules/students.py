import sqlite3
import random
import settings
from person import Person
from logger import *


con = sqlite3.connect("sqlite.db")
cursor = con.cursor()




class Student(Person):
    def __init__(self, name, subname, parent, birthday, my_group):
        super().__init__(name, subname, parent, birthday)
        self.my_group = my_group

    def __str__(self):
        return f"Студент: {self.name} {self.subname}\n"




class Group:
    """
    Має типи данних:
    students_list: Відповідає за збереження посилання на об'єкти классу Student,
                   які знаходяться в базі даних
    group_name: Відповідає за назву групи
    
    Має методи:
    get_stud: Вводить в змінну students_list посилання на створені об'єкти класу Student
    get_all: Виводить всі ім'я та прізвища студентів в групі
    find: Повертає посилання на знайдений по прізвищу об'єкт класу Student
    del_stud: Видаляє студента по прізвищу з бази даних

    add_stud: Додає студента в групу

    """

    
    def __init__(self, group:str):
        self.students_list = []
        self.get_stud(group)
        self.group_name = group
        

    def get_stud(self, group:str):
        list_stud = cursor.execute(f"SELECT * FROM {group}").fetchall()
        for i in list_stud:
            self.students_list.append(Student(i[0], i[1], i[2], i[3], group))

    def get_all(self):
        res = f"Студенти групи {self.group_name}:\n"
        return res+"".join(map(str, self.students_list))


    def find(self, familie:str):
        for i in self.students_list:
            if i.subname == familie:
                return i
        

    
    def del_stud(self, familie:str):
        if self.find(familie):
            cursor.execute(f"DELETE FROM {self.group_name} WHERE subname = '{familie}'")
            #con.commit() #Змінює файл бази данних після закриття
            logger.info(f"Видалено студента {familie} з групи {self.group_name}")
            self.__init__(self.group_name) #Перезавантаження групи зі змінами
            
    def add_stud(self, name:str, subname:str, parent:str, birthday:str):
        if len(self.students_list)<settings.MAX_STUDENTS:
            if not self.find(subname):
                cursor.execute(f"INSERT INTO {self.group_name} (name, subname, parent, birthday) VALUES ('{name}','{subname}','{parent}','{birthday}')")
                #con.commit()
                logger.info(f"Додано студента {name} {subname} до групи {self.group_name}")
                self.__init__(self.group_name)
            else:
                logger.warning(f"Студент {name} {subname} вже є в групі {self.group_name}")
        else:
            logger.warning(f"Неможливо додати студента. Кількість місць - {settings.MAX_STUDENTS}")
        
                
              
        












