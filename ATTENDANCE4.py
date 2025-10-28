# Creator : Khady Gueye


""" Task 1 """
import numpy as np
arr = np.arange(11)
odd_numbers = arr[arr % 2 != 0]
greater_than_2 = arr[arr > 2]

print("Odd numbers:", odd_numbers)
print("Numbers greater than 2:", greater_than_2)






""" Task 2 """
arr2 = np.arange(100, 201, 10).reshape(5, 2)
print("5x2 array with a difference of 10 between elements:\n", arr2)



""" Task 3 """
# NumPy array
Arr = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
third_column = Arr[:, 2]

print("Third column from all rows:", third_column)





""" Task 4 """
# NumPy array
sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
sub_array = sampleArray[0:3, 1:4]

print("Array from second to fourth column, first to third row:\n", sub_array)
