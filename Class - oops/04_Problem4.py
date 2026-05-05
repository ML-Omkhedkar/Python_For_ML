class Calculator:

    def __init__(self, n):
        self.n = n

    def squre(self):
        print(f"the squre is {self.n*self.n}")

    def cube(self):
        print(f" the cube is {self.n*self.n*self.n}")

    def root(self):
        print(f"the Squreroot is {self.n**1/2}")

    @staticmethod
    def greet():
        print("hello there! nice to meet you")    

p = Calculator(4)
p.greet()
p.squre()
p.cube()
p.root()