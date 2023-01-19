class Calculator:
     def Sqr(self,n):
          self.square=n**2
          print(f"The square of {n} is {self.square}")
     def Cube(self,n):
          self.cube=n**3
          print(f"The cube of {n} is {self.cube}")
     def Sqr_Root(self,n):
          self.root=n**0.5
          print(f"The square root of {n} is {self.root}")
c=Calculator()
c.Sqr(90)
c.Cube(90)
c.Sqr_Root(90)