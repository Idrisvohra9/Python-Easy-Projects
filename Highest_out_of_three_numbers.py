n1=int(input("1st number=>"))
n2=int(input("2nd number=>"))
n3=int(input("3rd number=>"))

if n1>n2>n3:
    print(n1,"Is the largest number.")
if n3>n2>n1:
    print(n3,"Is the largest number.")
if n2>n3>n1:
    print(n2,"Is the largest number.")
else:
    print("All the numbers are equal.")
