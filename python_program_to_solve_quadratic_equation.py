import cmath
print("Type according to the quadratic equation ax**2 + bx + c = 0\n\n")
a =int(input("Type a =>"))
b =int(input("Type b =>"))
c =int(input("Type c =>"))
  
# calculating the discriminant
dis = (b**2) - (4 * a*c)
  
# find two results
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)
  
# printing the results
print('The roots are')
print(ans1)
print(ans2)