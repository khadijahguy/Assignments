# Author : Khadija Gueye

"""
This code uses a users input to then determine if it is a right, acute, or obtuse triangle.
"""

import math

#Ask for the lengths of each side to the user.
side_a =  int(input('Please enter the length side A of the triangle (in meters): '))
side_b =  int(input('Please enter the length side B of the triangle (in meters): '))
side_c =  int(input('Please enter the length side C of the triangle (in meters): '))

#Formulas for solving for the perimeter and area.
p = (side_a + side_b + side_c)#/2
s = (side_a + side_b + side_c)/2
area = math.sqrt (s * (s - side_a) * (s - side_b) * (s - side_c))

#Print the perimeter and area.
print(f'The perimeter of the triangle is {p}m')
print(f'The area of the triangle is {area}m^2')


#Sqare root the side provided, so we can use pythagorean theorem to determine the type of triangle it is.
sqrt_a = side_a ** 2
sqrt_b = side_b ** 2
sqrt_c = side_c ** 2

if sqrt_a + sqrt_b == sqrt_c:
    triangle_type = "Right Triangle"
elif sqrt_a + sqrt_b > sqrt_c:
    triangle_type = "Acute Triangle"
else:
    triangle_type = "Obtuse Triangle"

print('It is a', triangle_type)