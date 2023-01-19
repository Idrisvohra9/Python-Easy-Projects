rows=5
for i in range(rows):
     for x in range(i+1):
          print("*",end=" ")
     for y in range(rows-i,1,-1):
          print(" ",end=" ") # This is for inverted space
     for z in range(rows-i,1,-1):
          print(" ",end=" ") # This is for inverted space
     for x in range(i+1):
          print("*",end=" ")
     print()
# print()
for j in range(rows):
     for x in range(4-j):
          print("*",end=" ")
     for y in range(j+1):
          print(" ",end=" ") # This is for inverted space
     for z in range(j+1):
          print(" ",end=" ") # This is for inverted space
     for x in range(4-j):
          print("*",end=" ")
     print()