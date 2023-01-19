input=input("Enter a Number: ")
n_d={# Number Dictionary
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
}
for i in range(len(input)):
    in_n=int(input[i])# Individual number
    print(n_d[in_n],end=" ")