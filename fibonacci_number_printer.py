n1=0
n2=1
count=0
num=int(input("Enter the number till the fibonacci numbers should go->"))
if num<=0:
    print("Enter a number greater than 0.")
else:
    print(n1)
    print(n2)
    while count!=num:
        sum=n1+n2
        print(sum)
        n1=n2
        n2=sum
        count+=1
        
