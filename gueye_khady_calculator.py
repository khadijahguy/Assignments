# Creator: Khady Gueye

"""
This program is a calculator you can use to help solve math problems you may have.
"""
import math 

print('Please enter an Expression')
print(' ')

while True:
    problem = input(f':> ')
    if problem.lower() in ['quit', 'q', 'stop']:
            break

    try:
        parts = problem.split()
        num1 = float(parts[0])  
        operand = parts[1]
        num2 = float(parts[2]) 

        if operand == "+":
            results = num1 + num2
        elif operand == "-":
            results = num1 - num2
        elif operand == "*":
            results = num1 * num2
        elif operand == "/":
            results = num1 / num2
        elif operand == "//":
            results = num1 // num2
        elif operand == "%":
            results = num1 % num2
        elif operand == "**":
            results = num1 ** num2
        else:
            continue

        if results.is_integer():
            results = round(results)

        if num1.is_integer():
            num1 = round(num1)

        if num2.is_integer():
            num2 = round(num2)

        print(f'Result: {num1} {operand} {num2} = {results}')
        print(" ")

    except (ValueError, IndexError):
        print(f'Error: Invalid Expression - ({problem})')
        print(" ")