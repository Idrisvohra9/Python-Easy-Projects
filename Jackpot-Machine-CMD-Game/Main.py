import pygame as pg
import trmnl_colors as clr
import time
import random
import os
os.system("cls")
os.environ["TMPDIR"] = "/"
pg.init()

# Making the path compatible for downloads:
current_script_path = os.path.dirname(os.path.abspath(__file__))
# print(os.path.join(current_script_path, "sounds","spin.wav"))


def insertSymbol(int):
    if int == 1:
        return "💰"
    if int == 2:
        return "🍒"
    if int == 3:
        return "❤️ "
    if int == 4:
        return "💎"
    if int == 5:
        return "🍓"
    if int == 6:
        return "👑"


def getSound(name):
    return os.path.join(current_script_path, "sounds", f"{name}.wav")


def sound(which):
    sound = pg.mixer.Sound(getSound(which))
    sound.play()
    pg.time.delay(1000)
    sound.stop()


count = 1
print("'↩' to Spin and 'n' to exit: ")
s1 = random.randrange(1, 7)
s3 = random.randrange(1, 7)
s2 = random.randrange(1, 7)
time.sleep(2)
print("{}".format(insertSymbol(s1)), end=" |")
print("{}".format(insertSymbol(s2)), end=" |")
print("{}".format(insertSymbol(s3)), end=" /*")
print()
spin = ""
while spin != 'n':
    clr.redB()
    spin = input("Spinn: ")
    print()
    clr.reset()
    s1 = random.randrange(1, 7)
    s3 = random.randrange(1, 7)
    s2 = random.randrange(1, 7)
    if spin == '':
        sound("spin")
        clr.whitefill()
        print("{}".format(insertSymbol(s1)), end=" |")
        print("{}".format(insertSymbol(s2)), end=" |")
        print("{}".format(insertSymbol(s3)), end=" /*")
        clr.reset()
        print()
    if s1 > s2 > s3:
        clr.yellowD()
        print("\nNot quite there!")
        sound("coins")
        count += 1
        clr.reset()

    elif s1 > s3 > s2:
        clr.yellowI()
        print("\nNot quite there!")
        sound("coins")
        count += 1
        clr.reset()

    elif s2 > s1 > s3:
        clr.greenU()
        print("\nYou can do it!")
        sound("coins")
        count += 1
        clr.reset()

    elif s2 > s3 > s1:
        clr.magentaB()
        print("\nA for Effort!")
        sound("coins")
        count += 1
        clr.reset()

    elif s3 > s1 > s2:
        clr.blueD()
        print("\nJust do it!!")
        sound("coins")
        count += 1
        clr.reset()

    elif s3 > s2 > s1:
        clr.cyanD()
        print("\nNope")
        sound("coins")
        count += 1
        clr.reset()

    elif s1 == s2 == s3:
        clr.yellowB()
        print("You have done it!!")
        print("Total spins: {}".format(count))
        sound("payout")
        clr.reset()
        break
    else:
        clr.magentaI()
        print("\n...")
        sound("coins")
        count += 1
        clr.reset()
