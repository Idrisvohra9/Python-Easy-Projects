import os; os.system("cls")
import time
import datetime as dt
import Random_clr_gen as rcg
import colors as clr


while True:
    time.sleep(1)
    x=dt.datetime.now()

    rcg.Random_Color_Gen(True,True)# All will be there
    print(f"{x.hour}",end="")

    rcg.Random_Color_Gen(False)# Strike through and underline will not be there
    print(" : ",end="")

    rcg.Random_Color_Gen(True,False)# Bgcolors will not be there
    print(f"{x.minute}",end="")

    rcg.Random_Color_Gen(False,False) # only normal colors will be there
    print(" : ",end="")

    rcg.Random_Color_Gen()
    print(f"{x.second}")

    clr.reset()