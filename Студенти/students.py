import sqlite3
import random


con = sqlite3.connect("sqlite.db")
cursor = con.cursor()


class Person:
    """
    Має типи даних:

    name: Ім'я

    subname: Прізвище

    parent: Ім'я по-батькові

    birthday: День нарождення

    """


    
    def __init__(self, name:str, subname:str, parent:str, birthday:str):
        self.name = name
        self.subname = subname
        self.birthday = birthday

    def __str__(self):
        return f"Тип: Людина\nІм'я: {self.name}\nПрізвище: {self.subname}"




class Student(Person):
    def __init__(self, name, subname, parent, birthday, my_group):
        super().__init__(name, subname, parent, birthday)
        self.my_group = my_group

    def __str__(self):
        return f"Тип: Людина\nСпеціалізація: Студент\nІм'я: {self.name}\nПрізвище: {self.subname}\nГрупа: {self.my_group}"




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
        return res.join(map(str, self.students_list))


    def find(self, familie:str):
        for i in self.students_list:
            if i.subname == familie:
                return i
        return None
    
    def del_stud(self, familie:str):
        if self.find(familie):
            cursor.execute(f"DELETE FROM {self.group_name} WHERE subname = '{familie}'")
            #con.commit() #Змінює файл бази данних після закриття
            self.__init__(self.group_name) #Перезавантаження групи зі змінами
            
    def add_stud(self, name:str, subname:str, parent:str, birthday:str):
        if not self.find(subname):
            cursor.execute(f"INSERT INTO {self.group_name} (name, subname, parent, birthday) VALUES ('{name}','{subname}','{parent}','{birthday}')")
            #con.commit()
            self.__init__(self.group_name)
        
        


a = Group("group2")
#print(a.get_all())
#print(a.find("Лютий"))
#print(a.find("ААААААААААААА"))
#print(a.del_stud("Лютий"))
print(a.get_all())


#a.add_stud("Олексій", "Вишневський", "Олександрович", "03.02.1896")
#print(a.find("Вишневський").name)
#print(a.get_all())



#b = Group("group1")
#print(b.get_all())
#print(b.find("Деркач"))












