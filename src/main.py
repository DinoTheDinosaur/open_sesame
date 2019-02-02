from voice_recording import voice_rec as VR
from PIL import Image
from models import *
import os
from time import sleep

time_reg = 12
time_sign = 3.8

os.system('cls' if os.name == 'nt' else 'clear')

print("___________________OPEN__SESAME_____________________")
print("    A Python module for speech authentification")

print('\n\n')
print("Welcome to great service, dear friend!")
print("Have you got an account?   1  = YES, 0 = NO  ")

ans = input()

if ans == '1':
    print ("What is your name?")
    username = input()
    if not user_exist(username):
        print ("Your nickname is not found :(")
    else:
        print ("Tap enter to record your voice")
        input()

        sound = VR(time_sign)
        print("done")
        authorization(username, sound)

        # print("Logged in")
        # img = Image.open("/home/somnoynadno/Pictures/gunter-adventure-time-at.jpg")
        # img.show()

elif ans == '0':
    print ("What is your name?")
    username = input()

    print ("Tap enter to record your voice")
    input()

    sound = VR(time_reg)

    add_user(username, sound)
    print("New account created!")
    print("Your username to log in:", username)

sleep(0.5)
print("exiting...")
sleep(1.5)

