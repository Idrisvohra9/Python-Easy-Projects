import random

smallalpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bigalpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['!', '<', '>', '@','#','$','%','&','*','/',':','=','.','-','+','~','?','{','}']
passw=[]
length=int(input("Enter the length of the password: "))
characters=(smallalpha + bigalpha + numbers + symbols)
random.shuffle(characters) # This shuffles the password characters

for i in range(length):
    passw.append(random.choice(characters))
password = ''.join([str(elem) for elem in passw])
# password.join(passw) This generates an error

print(password)