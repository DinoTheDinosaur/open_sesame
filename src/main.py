from voice_recording import voice_rec as VR
from PIL import Image
from models import *
import os
from time import sleep

time_reg = 12
time_sign = 3.95

if not os.path.exists('../models/Voice_Profiles.pickle'):
    create_empty_pickle()

os.system('cls' if os.name == 'nt' else 'clear')

print("___________________OPEN__SESAME_____________________")
print("    A Python module for speech authentification")

print('\n\n')
print("Welcome to great service, dear friend!")

ans = None

while(ans != '2'):
    print("Have you got an account?   1  = YES, 0 = NO, 2 = EXIT ")
    ans = input()

    if ans == '1':
        print("What is your name?")
        username = input()
        if not user_exist(username):
            print("Your nickname is not found :(")
            print("0 = create account, 1 = try again, 2 = exit ")
            ans = input()
        else:
            for i in range(3):
                print("Tap enter to record your voice")
                input()

                sound = VR(time_sign)
                print("done")
                if authorization(username, sound):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("You are in system! Welcome.")
                    ans = '2'
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Try again")
                    sleep(2)
            else:
                print("Permission denied")
                break

            # print("Logged in")
            # img = Image.open("/home/somnoynadno/Pictures/gunter-adventure-time-at.jpg")
            # img.show()

    elif ans == '0':
        print("What's your name?")
        username = input()

        if user_exist(username):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sorry, this user already exist")
            continue

        print("Tap enter to record your voice")
        input()

        sound = VR(time_reg)

        add_user(username, sound)
        print("New account created!")
        print("Your username to log in:", username)
        break

sleep(0.5)
print("exiting...")
sleep(1.5)

