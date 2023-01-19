import os; os.system("cls")
import random
import time
import colors as clr
from pydub import *
from pydub.playback import play


def ColorAccord(int):
    if int==1:
        print("💰",end="")
        return ""
    if int==2:
        print("🍒",end="")
        return ""
    if int==3:
        print("❤️ ",end="")
        return ""
    if int==4:
        print("💎",end="")
        return ""
    if int==5:
        print("🍓",end="")
        return ""
    if int==6:
        print("👑",end="")
        return ""

def sound(which):
    if which=="spin":
        sound = AudioSegment.from_wav("")
        play(sound)


    elif which=="coin":
        sound = AudioSegment.from_wav("")
        play(sound)


    elif which=="win":
        sound = AudioSegment.from_wav("")
        play(sound)


        
count=1
print("'↩' to Spin and 'n' to exit: ")
s1=random.randrange(1,7)
s3=random.randrange(1,7)
s2=random.randrange(1,7)
time.sleep(2)
print("{}".format(ColorAccord(s1)),end=" |")
print("{}".format(ColorAccord(s2)),end=" |")
print("{}".format(ColorAccord(s3)),end=" /*")
print()
spin=""
while spin!='n':
    clr.redB()
    spin=input("Spinn: ")
    print()
    clr.reset()
    s1=random.randrange(1,7)
    s3=random.randrange(1,7)
    s2=random.randrange(1,7)
    if spin=='':
        sound("spin")
        # time.sleep(3)
        print("{}".format(ColorAccord(s1)),end=" |")
        print("{}".format(ColorAccord(s2)),end=" |")
        print("{}".format(ColorAccord(s3)),end=" /*")
        print()

    if s1>s2>s3:
        clr.yellowD()
        print("\nNot quite there!")
        sound("coin")
        count+=1
        clr.reset()

    elif s1>s3>s2:
        clr.yellowI()
        print("\nNot quite there!")
        sound("coin")
        count+=1
        clr.reset()

    elif s2>s1>s3:
        clr.greenU()
        print("\nYou can do it!")
        sound("coin")
        count+=1
        clr.reset()

    elif s2>s3>s1:
        clr.magentaB()
        print("\nA for Effort!")
        sound("coin")
        count+=1
        clr.reset()

    elif s3>s1>s2:
        clr.blueD()
        print("\nJust do it!!")
        sound("coin")
        count+=1
        clr.reset()

    elif s3>s2>s1:
        clr.cyanD()
        print("\nNope")
        sound("coin")
        count+=1
        clr.reset()

    elif s1==s2==s3:
        clr.yellowB()
        print("You have done it!!")
        print("Total spins: {}".format(count))
        sound("win")
        clr.reset()
        break
    else:
        clr.magentaI()
        print("\n...")
        sound("coin")
        count+=1
        clr.reset()