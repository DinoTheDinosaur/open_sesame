from voice_recording import voice_rec as VR
from PIL import Image

def OpenSesame():
    print("openSesame")

def CheckName(name):
    print("Checking name")

def AddName():
    print("add name")


print(" Welcome to great service, dear friend")
print("Have you got an account ?  1  = YES, 0 = NO  ")

ans = 0;
ans=input()

if (ans == 1):
    print ("What is your name?")
    name = "name"
    name = input()
    id = CheckName(name);

    print ("Tap enter to record your password")
    input()

    print("*recording")
    VR('../tmp/{}.wav'.format(id))
    print("done")

    if ( OpenSesame(id, ) == 0 ) :
        print ("Logged in")
        img = Image.open('D:\picture.jpg')
        img.show()
else :
    print ("What is your name?")
    name = "name"
    name = input()
    id = AddName(name)

    print ("Tap enter to record your password 3 times")
    input()
    print("*recording")
    for i in range(0,3):
        print(i)
        VR('../tmp/{}.wav'.format(id))
        print("done")




