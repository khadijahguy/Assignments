# Creator : Khady Gueye

""" THis is calulator that solves equation using class objects."""

# Define Class

class Number:

    # Define Class Object
    def __init__(self, num):
        self.num = int(num)

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return Number(self.num + other.num)
    
    def __sub__(self, other):
        return Number(self.num - other.num)
    
    def __mul__(self, other):
        return Number(self.num * other.num)
    
    def __truediv__(self, other):
        return Number(self.num // other.num)  
 

def main():
    # Assign numbers to value
    num1 = Number(25)
    num2 = Number(5)
    num3 = Number(30)
    num4 = Number(20)
    num5 = Number(125)

    # Addition
    result_add = num1 + num2
    print(f"{num1} + {num2} = {result_add}")

    # Subtraction
    result_sub = num1 - num2
    print(f"{num1} - {num2} = {result_sub}")

    # Multiplication
    result_mul = num1 * num2
    print(f"{num1} * {num2} = {result_mul}")

    # Division
    result_div = num1 / num2
    print(f"{num1} / {num2} = {result_div}")

    # Long Expression
    result_combined = (num3 + (num4 * num2)) / num5
    print(f"({num3} + {num4} * {num2}) / {num5} = {result_combined}")

# Call main function
if __name__ == "__main__":
    main()