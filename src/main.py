from voice_recording import voice_rec as VR
from PIL import Image
import Models

def OpenSesame(username,filename):
    print("openSesame")

def CheckName(username):
    print("Checking name")

def AddName(username):
    print("add name")


time_reg = 12
time_sign = 3.8

print(" Welcome to great service, dear friend")
print("Have you got an account ?  1  = YES, 0 = NO  ")


ans = input()

if ans == 1:
    print ("What is your name?")
    username = input()
    if CheckName(name) == 1:
        print ("Your nickname is not found :(")
    else:
        print ("Tap enter to record your password")
        input()

        print("*recording")
        sound = VR(time_sign)
        print("done")

        if OpenSesame(username,sound) == 0:
            print ("Logged in")
            img = Image.open('D:\picture.jpg')
            img.show()
else:
    print ("What is your name?")
    username = input()

    print ("Tap enter to read our rules and record it ")
    input()
    print("*recording")

    print("Все, что вы скажите не будет использоваться против вас, даже наоборот это поможет входить в нашу систему. Я на правах владельца этого голоса соглашаюсь на хранение данных.")
    sound = VR(time_reg)
    print("done")

    AddUser(username, sound)



