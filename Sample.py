class Sample:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    def Add(self , a, b):
        return a + b

    def Sub(self, a, b):
        return a - b

    def Mul(self, a, b):
        return a * b

    def Div(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b