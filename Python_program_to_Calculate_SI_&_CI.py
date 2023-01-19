print("Python program to Calculate Simple interest and compound interest.")
def si():
    p=int(input("Enter principle amount>>"))
    r=float(input("Enter the rate of interest>>"))
    t=int(input("Enter the time in years>>"))
    print(p*r*t/100)
def ci():
    