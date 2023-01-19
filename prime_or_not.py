# Program to check if a number is prime or not

num =int(input("Enter a number:"))
if num > 1:
    # check for factors
    for i in range(2,num):
        if num % i == 0:
            print(num,"is a composite number")
            break
    else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")