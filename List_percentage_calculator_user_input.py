total=0
n=1
mlist=[total]
while(True):
    marks=int(input("Enter marks and the percentage will be calculated:\n to exit press 'e'"))
    while marks!='e':
        total=total+marks
        n+=1
    p=mlist/n
    print("The total percentage is {}".format(p))