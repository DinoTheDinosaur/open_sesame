import datetime

# -*- coding: utf-8 -*-

ALPHA = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'


def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))


history = open("file.txt", "r")
temp = history.read()
temp1 = decode(temp, 2)
print('\n' + temp1 + '\n')
history.close()

time = datetime.datetime.now()
time1 = "{:%B %d, %Y}".format(time)
temp = input('\n' + time1 + '\r' + '\n')
while (temp != "на сегодня все"):
    # print('\n')
    temp = input()
    temp1 = encode(temp, 2)

filehandle = open('file.txt', 'a')
filehandle.write('\n' + time1 + '\n')
filehandle.write(temp1 + '\n')
filehandle.close()
print("end")

