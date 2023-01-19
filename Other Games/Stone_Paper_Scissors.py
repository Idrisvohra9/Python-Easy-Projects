import random
import os
os.system("cls")
print("The game of stone🪨 , paper🗞️  and scisors✂️ :")
gamestarter=True
while gamestarter==True:
    choice=random.randint(1,3)
    t=-1
    w=-1
    countc=0
    countp=0

    print("\nPlayer 1's Turn:-")
    p1=input("Stone(s) Paper(p) or Scissors(x)?: ")

    if p1=='s' and choice==1 or p1=='p' and choice==2 or p1=='x' and choice==3:
        t=0

    elif p1=='s' and choice==3 or p1=='p' and choice==1 or p1=='x' and choice==2:
        w=1

    elif p1=='s' and choice==2 or p1=='p' and choice==3 or p1=='x' and choice==1:
        w=2
    print("\nComputer's Turn:-")
    print("Stone(s) Paper(p) or Scissors(x)?: ",end='')
    # print(choice)
    if choice==1:
        print("Stone")
    if choice==2:
        print("Paper")
    if choice==3:
        print("Scissors")

    if t==0:
        print("\nIt's a Tie!!")
    elif w==1:
        print("\nPlayer 1 won the Round!!")
        countp+=1
    elif w==2:
        print("\nComputer won the Round!!")
        countc+=1
    
    if countc <=9 or countp <=9:
        if countc == 9:
            print("The Game has been won by The Computer!!!")
            gamestarter=False
        elif countp == 9:
            print("The Game has been won by The Player!!!")
            gamestarter=False