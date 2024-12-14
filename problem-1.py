class Calculator:
    def fun(self, a:float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    
    def calculate(self):
        if self.operation == "+":
            return self.a + self.b
        elif self.operation == "-":
            return self.a - self.b
        elif self.operation == "*":
            return self.a * self.b
        elif self.operation == "/":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error:Invalid operation. Please choose from addition, subtraction, multiplication, or division."
try:
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operation = input("Enter the type of operation (addition, subtraction, multiplication, division): ")

    calc = Calculator()
    calc.fun(a, b, operation)
    result = calc.calculate()
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")

