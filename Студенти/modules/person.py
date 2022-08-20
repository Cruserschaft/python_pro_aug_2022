
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
