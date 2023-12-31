class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Example usage:
calculator = Calculator()

result_add = calculator.add(5, 3)
print("5 + 3 =", result_add)

result_subtract = calculator.subtract(10, 4)
print("10 - 4 =", result_subtract)

result_multiply = calculator.multiply(6, 2)
print("6 * 2 =", result_multiply)

result_divide = calculator.divide(8, 2)
print("8 / 2 =", result_divide)
