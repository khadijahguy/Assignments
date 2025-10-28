# Creator: Khady Gueye

"""
This program will ask you to enter a number of floating point value you have and then ask what they are. After it will give it to you in 2 decimal place form.
"""

# Empty list to hold the values
my_valuelist = []


# Ask the user for the number of values the user has to enter.
amount = int(input("Please enter the number of floating point values: "))


# Ask to enter the values so the program can run them.
for i in range(amount):
    value = float(input('Please enter a floating-point value: '))
    normalized = value / 100
    round_normalized = round(normalized, 2)
    my_valuelist.append(round_normalized)


# Print the normalized values.
print(' ')
print('Normalized Floating-Point Values:')
for val in my_valuelist:
    print(f'{val:.2f}')