class Number:
    def __init__(self,n,n2):
        self.n = n
        self.n2 = n2

    def __str__(self):
        return f"Num : {self.n}, {self.n2}" # THE __str__ takes any number of arguments and return a string representation.
    
    def __len__(self):
        return self.n2 # The __len__ takes only numbers as arguments and returns a int representation.

n= Number(100,30)
print(n)
print(len(n))