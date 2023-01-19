n=int(input("Enter a number to check its factors:"))
factors=[]
for i in range(1,n+1):
    if n % i==0:
#In this condition there is one thing to be kept in mind that the main input variable should be placed before the mod and the variable that is iterated is to be placed after. Otherwise the value produced in the output will not be factors. 
        factors.append(i)

print("The factors of {} are {}".format(n,factors))
