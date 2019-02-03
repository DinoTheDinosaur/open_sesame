import datetime

# -*- coding: utf-8 -*-

ALPHA = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encoding(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decoding(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))

def dnev():
    history = open("file.txt", "r")
    temp = history.read()
    temp1 = decoding(temp, 2)
    print('\n' + temp1 + '\n')
    history.close()

    time = datetime.datetime.now()
    time1 ="{:%B %d, %Y}".format(time)

    temp = input('\n' + time1 + '\r' + '\n')
    time1 = encoding(time1, 2)
    temp1 = encoding(temp, 2)

    filehandle = open('file.txt', 'a')
    filehandle.write('\n' + time1 + '\n')
    filehandle.write(str(str(temp1) + str('\n')))
    filehandle.close()
    print("end")

