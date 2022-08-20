import sys
sys.path.append("modules")
from students import *


a = Group("group2")
print(a.get_all())
print(a.find("Лютий"))
print(a.find("ААААААААААААА"))
a.del_stud("Лютий")
print(a.get_all())


a.add_stud("Олексій", "Вишневський", "Олександрович", "03.02.1896")
print(a.find("Вишневський").name)
print(a.get_all())



b = Group("group1")
print(b.get_all())
print(b.find("Деркач"))

a.del_stud("Забуга")
a.add_stud("Василь", "Серпень", "Олекційович", "22.01.1978")
a.add_stud("Олексій", "Вишневський", "Олександрович", "03.02.1896")
print(a.get_all())
