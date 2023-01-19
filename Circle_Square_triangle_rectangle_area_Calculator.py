def circle():
    r = int(input(" Enter the radius: "))
    print("     Area of circle =",PI*(r**2))
def square():
    x = int(input(" Side of square:" ))
    print("     Area of square = ",x**2)
def triangle():
    h = int(input(" Height of the triangle: "))
    base = int(input(" Base of the triangle: "))
    print("     Area of triangle = ",0.5*h*base)
def rectangle():
    l = int(input(" Length of rectangle: "))
    b = int(input(" Breadth of rectangle: "))
    print("     Area of rectangle = ",l*b)
PI=3.14
print("For Circle : Square : Triangle : Rectangle = c : s : t : r")
shape=input("Area of which shape? ")
if shape=="c":
    circle()
if shape=="s":
    square()
if shape=="r":
    rectangle()
if shape=="t":
    triangle()