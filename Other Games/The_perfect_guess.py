import random
import os
os.system("cls")
import trmnl_colors as colors
n=random.randint(0,100)
count=1
while True:
    colors.reset()
    print("Guess the number! : ",end="")
    num=int(input())

    if num<n:
        colors.greenD()
        print("Go for a bigger number!")
        count+=1

    if num>n:
        colors.yellowI()
        print("Go for a smaller number!")
        count+=1

    if num==n:
        colors.blueB()
        print("You guessed it! the number was {}!".format(n))
        colors.cyanL()
        print("Total guesses {}".format(count))
        break