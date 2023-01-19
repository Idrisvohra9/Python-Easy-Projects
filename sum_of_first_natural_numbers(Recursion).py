def sum_n_no(n):
    if n == 0:
        return 0
    else:
        return n + sum_n_no(n-1)
n= sum_n_no(5)
print(n)