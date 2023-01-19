def program():#to make a program repeating indefinite amount of times one way is to define the program on a function and call it where you want it to repeat itself.
    op=(input("Enter a Mode of calculation \n'+'\n'-'\n'/'\n'Power=(**)'\n'Sq. root=(~)'\n|To exit Press 'E'\n"))
    if (op=='+'):
        n1=int(input("Enter No. 1:"))
        n2=int(input("Enter No. 2:"))
        print("{}+{}={}".format(n1,n2,n1+n2))
        program()
    if (op=='-'):
        n1=int(input("Enter No. 1:"))
        n2=int(input("Enter No. 2:"))
        print("{}-{}={}".format(n1,n2,n1-n2))
        program()
    if (op=='**'):
        n1=int(input("Enter No. 1:"))
        n2=int(input("Enter No. 2:"))
        print("{}*{}={}".format(n1,n2,n1**n2))
        program()
    if (op=='/'):
        n1=int(input("Enter No. 1:"))
        n2=int(input("Enter No. 2:"))
        print("{}/{}={}".format(n1,n2,n1/n2))
        program()
    if (op=='*'):
        n1=int(input("Enter No. 1:"))
        n2=int(input("Enter No. 2:"))
        print("{}*{}={}".format(n1,n2,n1*n2))
        program()
    if (op=='~'):
        n1=int(input("Enter The number:"))
        print("square root of {} = {}".format(n1,n1**0.5))
        program()
    if (op=='E' or 'e'):
        print("you exited.")
        exit()

program()