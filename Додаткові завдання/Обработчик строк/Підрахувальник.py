from collections import Counter



class File:

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return self.readlines()


    def readlines(self):
        with open(self.file, "r", encoding = "utf-8") as tmp:
            return "".join(map(str,tmp.readlines()))


    def amount_words(self):
        tmp = self.readlines()
        for i in [":",",",".",";","-"]:
            tmp = tmp.replace(i, "")
        
        return len(tmp.split())

    def amount(self, other):
        return Counter(self.readlines())[other]


    def amount_pred(self):
        return Counter(self.readlines())["."]
    




f = File("file.txt")
print(f.amount_words())
print(f.amount("а"))
print(f.amount("-"))
print(f.amount_pred())

print("*"*20)
print(f)
