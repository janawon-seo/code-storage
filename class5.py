class Calc():
    
    def set_number(self, a, b):
        self.a = int(a)
        self.b = int(b)
        
    def plus(self):
        return f"더하기 : {self.a + self.b}"
    def minus(self):
        return f"빼  기 : {self.a - self.b}"
    def multiple(self):
        return f"곱하기 : {self.a * self.b}"
    def divide(self):
        return f"나누기 : {self.a / self.b}"
    
calc = Calc()   
calc.set_number(20, 10)
    
print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide())
