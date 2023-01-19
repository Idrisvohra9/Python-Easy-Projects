"""
Magic operator for binary Operators:

+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)*/
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
"""

"""
Magic Comparison Operators :

<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
"""

class Num_processing:
    def __init__(self,n):
        self.n = n
    # Arithmatic magical Methods:
    def __add__(self,other):
        self.other = other
        return self.n + other.n

    def __sub__(self,other):
        self.other = other
        return self.n - other.n

    def __mul__(self,other):
        self.other = other
        return self.n * other.n

    def __truediv__(self,other):
        self.other = other
        return self.n / other.n

    def __floordiv__(self,other):
        self.other = other
        return self.n // other.n

    def __mod__(self,other):
        self.other = other
        return self.n % other.n
    def __pow__(self,other):
        self.other = other
        return self.n ** other.n

    # Comparison magical Methods:

    def __eq__(self,other):
        self.other = other
        if (self.n == other.n):
            return f"Yes, {self.n} == {other.n}"
        
        else:
            return f"No, {self.n} != {other.n}"

    def __lt__(self,other):
        self.other = other
        if (self.n < other.n):
            return f"{self.n} < {other.n}"
    
    def __gt__(self,other):
        self.other = other
        if (self.n > other.n):
            return f"{self.n} > {other.n}"

    def __le__(self,other):
        self.other = other
        if (self.n <= other.n):
            return f"{self.n} <= {other.n}"

    def __ge__(self,other):
        self.other = other
        if (self.n >= other.n):
            return f"{self.n} >= {other.n}"
        
n1=Num_processing(50)
n2=Num_processing(10)
add=n1 + n2
sub=n1 - n2
mul=n1 * n2
div=n1 / n2
flr_div=n1 // n2
mod=n1 % n2
pow =n1 ** n2
are_equal= n1 == n2
are_not_equal= n1 != n2
is_less= n1 < n2
is_greater= n1 > n2
is_less_equal= n1 <= n2
is_greater_equal= n1 >= n2

print("Addition =",add)
print("Subtraction =",sub)
print("Multiplication =",mul)
print("Division =",div)
print("Floor division =",flr_div)
print("Modulus =",mod)
print("Pow =",pow)
print(are_equal)
print(are_not_equal)
print(is_less)
print(is_greater)
print(is_less_equal)
print(is_greater_equal)