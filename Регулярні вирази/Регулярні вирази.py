import re

# 1. Напишите регулярное выражение, которое будет находить в тексте фрагменты, состоящие из одной буквы R, за которой
# следует одна или более букв b, за которой одна r. Учитывать верхний и нижний регистр.
print(1, "*" * 20)

st = "dgfeagkoaep'geagRbbbraker'golw m'g;pawrmasdbaew 01r i910irbbbbbbbbr'rBBr a"

search = re.findall(r"[Rr][bB]{1,}[Rr]", st)
print(search)


# 2. Напишите функцию, выполняющую валидацию номера банковской карты (9999-9999-9999-9999).
print(2, "*" * 20)

def bank_card_verification(val):
    return len(re.findall(r"[0-9]{4}", st)) == 4


st = "2432-2562-1256-1257"
print(bank_card_verification(st))

st = "234a-2341-6332-2333"
print(bank_card_verification(st))


# 3. Напишите функцию, принимающую строковые данные и выполняющую проверку на их соответствие мейлу.
# Требования:
# -цифры (0-9).
# -только латинские буквы в большом (A-Z) и малом (a-z) регистрах.
# -в теле мейла допустимы только символы “_” и “-”. Но они не могут быть первым символом мейла.
# -символ “-” не может повторяться.
print(3, "*" * 20)


def mail_verify(val):
    tmp = re.split("@", val)[0]
    if len(re.findall(r"[-_]", tmp)) > 1 or re.search(r"^[-_]", tmp):
        return False

    if re.findall(r"[^a-zA-Z0-9-.]", tmp) or len(re.findall(r"@", val)) > 1:
        return False

    return True


st = "fsfQee-f2341@gmail.com"
print(mail_verify(st))
st = "fsdfwf--adaw@gmail.com"
print(mail_verify(st))
st = "fagf5dgae@@gmail.com"
print(mail_verify(st))
st = "-dsfsafa@gmail.com"
print(mail_verify(st))


# 4. Напишите функцию, проверяющую правильность логина. Правильный логин – строка от 2 до 10 символов, содержащая только буквы и цифры.
print(4, "*"*20)

def login_verify(val):
    if len(re.findall("[^a-zA-Z0-9]", val)):
        return False
    if 2 > len(val) or len(val) > 10:
        return False
    return True

st = "Boris"
print(login_verify(st))
st = "a"
print(login_verify(st))
st = "a dwd"
print(login_verify(st))
st = "123borya123123123121233"
print(login_verify(st))