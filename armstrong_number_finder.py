# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
print("Python program to find if a number is armstrong number or not.\n\n")
sum=0
num=input("Enter a number:")
snum=num
temp=int(num)
while temp>0:
    digit=temp%10
    sum=sum+ digit**3
    temp=temp//10
if num==sum:
    print(num,"is an armstrong number.")
else:
    print(num,"is not an armstrong number.")