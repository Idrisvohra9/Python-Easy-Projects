# 1st simple star pyramid->
# rows=5
# for x in range(rows):
#     for space in range(5-x):
#         print(" ",end="")
#     for rows in range(x+1):
#         print("*",end=' ')
#     print()

# Output:
#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *

#______________________________________________________________________________________________#
# 2nd The original big boy pyramid->
# rows=5
# num=1
# for x in range(rows):
#     for space in range(5-x):
#         print("  ",end="")
#     for s in range(x+1):
#         print("* ",end="")
#     for s in range(x):
#         print("* ",end="")
#     print()

# Output:
#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#______________________________________________________________________________________________#
# 3rd Numerical column wise pyramid->
# rows=5
# for x in range(rows):
#     for space in range(5-x,0,-1):
#         print(" ",end="")
#     for rows in range(x+1):
#         print(x+1,end=' ')
#     print()

# Output:
#      1 
#     2 2
#    3 3 3
#   4 4 4 4
#  5 5 5 5 5
#______________________________________________________________________________________________#
# 4th Numerical column wise big boy pyramid->
# rows=5
# for x in range(rows):
#     for space in range(5-x):
#         print("  ",end="")
#     for s in range(x+1):
#         print(x+1,end=" ")
#     for s in range(x):
#         print(x+1,end=" ")
#     print()

# Output:
#           1 
#         2 2 2
#       3 3 3 3 3
#     4 4 4 4 4 4 4
#   5 5 5 5 5 5 5 5 5
#______________________________________________________________________________________________#
# 5th Continious numerical pyramid->
# rows=5
# n=1
# for x in range(rows):
#     for space in range(5-x):
#         print(" ",end="")
#     for rows in range(x+1):
#         print(n,end=" ")
#         n+=1
#     print()

# Output:
#      1
#     2 3
#    4 5 6
#   7 8 9 10
#  11 12 13 14 15
#______________________________________________________________________________________________#
# 6th continious numerical big boy pyramid->
# rows=5
# num=1
# for x in range(rows):
#     for space in range(5-x):
#         print("  ",end="")
#     for s in range(x+1):
#         print(num,end=" ")
#         num+=1
#     for s in range(x):
#         print(num,end=" ")
#         num+=1
#     print() 

# Output:
#           1 
#         2 3 4
#       5 6 7 8 9
#     10 11 12 13 14 15 16 
#   17 18 19 20 21 22 23 24 25
#______________________________________________________________________________________________#
# 7th continious alphabetic pyramid:
# rows=5
# a=65
# for x in range(rows):
#     for space in range(5-x):
#         print(" ",end="")
#     for rows in range(x+1):
#         print(chr(a),end=" ")
#         a+=1
#     print()

# Output:
#      A
#     B C
#    D E F
#   G H I J
#  K L M N O
#______________________________________________________________________________________________#
# 8th Continuous alphabetic big boy pyramid->
# rows=5
# a=65
# for x in range(rows):
#     for space in range(5-x):
#         print("  ",end="")
#     for s in range(x+1):
#         print(chr(a),end=" ")
#         a+=1
#     for s in range(x):
#         print(chr(a),end=" ")
#         a+=1
#     print()

# Output:
#           A
#         B C D
#       E F G H I
#     J K L M N O P
#   Q R S T U V W X Y
#______________________________________________________________________________________________#
# 9th inverted Continuous alphabetic big boy pyramid->
# rows=4
# a=65
# for x in range(rows,-1,-1):
#     for space in range(5-x):
#         print("  ",end="")
#     for s in range(x+1):
#         print(chr(a),end=" ")
#         a+=1
#     for s in range(x):
#         print(chr(a),end=" ")
#         a+=1
#     print()

# Output:
#   A B C D E F G H I
#     J K L M N O P
#       Q R S T U
#         V W X
#           Y
#______________________________________________________________________________________________#
# 10th continious inverted connected alphabetical pyramid->
# rows=4
# a=65
# for x in range(rows,-1,-1):
#     for space in range(5-x):
#         print("  ",end="")
#     for s in range(x+1):
#         print(chr(a),end=" ")
#         a+=1
#     for s in range(x):
#         print(chr(a),end=" ")
#         a+=1
#     print()
# rows=5
# a=89
# for x in range(rows):
#     for space in range(5-x):
#         print("  ",end="")
#     for s in range(x+1):
#         print(chr(a),end=" ")
#         a-=1
#     for s in range(x):
#         print(chr(a),end=" ")
#         a-=1
#     print()
# Output:
#   A B C D E F G H I 
#     J K L M N O P
#       Q R S T U
#         V W X
#           Y
#           Y
#         X W V
#       U T S R Q
#     P O N M L K J
#   I H G F E D C B A