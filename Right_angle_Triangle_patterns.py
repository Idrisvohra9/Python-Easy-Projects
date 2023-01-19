# 1st Normal star pattern->

# rows=5
# for x in range(rows):
#     for rows in range(x+1):
#         print("* ",end="")
#     print()

"""
Output:
  * 
  * *
  * * *
  * * * *
  * * * * *
"""#____________________________________________________________________________________________#
# 2nd Inverted star pattern->

# rows=5
# for x in range(rows,0,-1):
#     for rows in range(x,0,-1):
#         print("* ",end="")
#     print()

"""Output:
  * * * * * 
  * * * *
  * * *
  * *
  *
"""#______________________________________________________________________________________________#
# 3rd Row Number counting triangle ->

# rows=5
# for x in range(rows):         
#     for rows in range(x+1):    
#         print(rows+1,end=" ")
#     print()

"""
Output:
  1 
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5
"""#______________________________________________________________________________________________#
# 4th Column number counting triangle ->

# rows=5
# for x in range(rows):
#     for rows in range(x+1):
#         print(x+1,end=" ")
#     print()

"""
Output:
  1 
  2 2
  3 3 3
  4 4 4 4
  5 5 5 5 5
"""#______________________________________________________________________________________________#
# 5th Continuous number triangle->

# rows=5
# n=1
# for x in range(rows):
#     for rows in range(x+1):
#         print(n,end=" ")
#         n+=1
#     print()

"""
Output:
  1 
  2 3
  4 5 6
  7 8 9 10
  11 12 13 14 15
"""#______________________________________________________________________________________________#
# 6th indented number triangle in 1->
# rows=5
# for x in range(rows):
#     for space in range(4-x):
#         print("1 ",end="")
#     for rows in range(x+1):
#         print(x+1,end=" ")
#     print()

"""
Output:
  1 1 1 1 1 
  1 1 1 2 2
  1 1 3 3 3
  1 4 4 4 4
  5 5 5 5 5
"""#______________________________________________________________________________________________#
# 7th Row Wise Alphabetic triangle->

# for x in range(65,70):
#     for rows in range(65,x+1):
#         print(chr(rows),end=" ")
#     print()

"""
Output:
  A 
  A B
  A B C
  A B C D
  A B C D E
"""#______________________________________________________________________________________________#
# 8th Column Wise Alphabetic triangle->

# for x in range(65,70):
#     for rows in range(65,x+1):
#         print(chr(x),end=" ")
#     print()

"""
Output:
  A 
  B B
  C C C
  D D D D
  E E E E E
"""#______________________________________________________________________________________________#
# 9th Continuous Alphabetic triangle->

# a=65
# rows=5
# for i in range(rows):
#     for rows in range(i+1):
#         print(chr(a),end=' ')
#         a+=1
#     print()

"""
Output:
  A 
  B C
  D E F
  G H I J
  K L M N O
"""#______________________________________________________________________________________________#
# Misc patterns->

# 1st inverted numeric rows and columns based triangle->

# rows=5
# for i in range(rows+1):
#     for rows in range(5 - i, 0 , -1):  
#         print(rows, end=' ')  
#     print()

"""
Output:
  5 4 3 2 1
  4 3 2 1
  3 2 1
  2 1
  1
"""
# 2nd binary triangle->

# rows=5
# num=1
# for x in range(rows):
#     for rows in range(x+1):
#         if (num%2==0):
#             binary=0
#         else:
#             binary=1
#         num+=1
#         print(binary,end=" ")
#     print()

"""
Output:
  1 
  0 1
  0 1 0
  1 0 1 0
  1 0 1 0 1
"""
# 3rd inverted binary triangle->
# rows=5
# num=1
# for x in range(rows,0,-1):
#     for rows in range(x,0,-1):
#         if (num%2==0):
#             binary=0
#         else:
#             binary=1
#         num+=1
#         print(binary,end=" ")
#     print()

"""
Output:
  1 0 1 0 1 
  0 1 0 1 
  0 1 0 
  1 0 
  1 
  """

# 4th 90 degree rotated pyramid->
# rows=5
# for x in range(rows):
#     for rows in range(x+1):
#         print("* ",end="")
#     print()
# rows2=4
# for y in range(rows2,0,-1):
#     for rows2 in range(y,0,-1):
#         print("* ",end="")
#     print()

"""
Output:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""