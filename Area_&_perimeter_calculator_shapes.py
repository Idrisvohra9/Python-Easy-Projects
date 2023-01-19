pi=3.14
shape=input("Select a shape:\n Circle='c'\n Rectangle='r'\n Square='s'\n")
if (shape=='c'):
    r=int(input("Radius:"))
    work=input("Select What output \nPerimeter= 'p'\n Area = 'a'\n")
    if (work=='p'):
        peri=2*pi*r
        print("Perimeter=",peri)
    else:
        area=pi*r**2
        print("Area=",area)

if (shape=='r'):
    l=int(input("Length:"))
    b=int(input("Breadth:"))
    work=input("Select What output \nPerimeter= 'p'\n Area = 'a'\n")
    if (work=='p'):
        peri=2*(l+b)
        print("Perimeter=",peri)
    else:
        area=l*b
        print("Area=",area)
if (shape=='s'):
    x=int(input("Side:"))
    work=input("Select What output \nPerimeter= 'p' Area = 'a'\n")
    if (work=='p'):
        peri=4*x
        print("Perimeter=",peri)
    else:
        area=x**2
        print("Area=",area)

