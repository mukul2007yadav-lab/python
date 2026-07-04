class calculator():
   def __init__(self,n):
        self.n=n

   def square(self):
       print(f"The square is {self.n*self.n}")

   def squareroot(self):
       print(f"The square root is {self.n**0.5}")

   def cube(self):
       print(f"The cube is {self.n*self.n*self.n}")
          
a = calculator(25)
a.square()
a.cube()
a.squareroot()
