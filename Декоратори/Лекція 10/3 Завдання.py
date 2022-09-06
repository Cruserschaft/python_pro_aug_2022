#3) Для класса Box напишите статический метод, который будет подсчитывать
#суммарный объем двух ящиков, которые будут его параметрами.


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def v_two_boxes(box1, box2):
        return box1.x * box1.y * box1.z + box2.x * box2.y * box2.z


b1 = Box(10, 10, 1)
b2 = Box(1, 1, 1)
print(Box.v_two_boxes(b1, b2))