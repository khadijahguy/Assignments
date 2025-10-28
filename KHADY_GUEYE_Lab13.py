# Creator : Khady Gueye

import numpy as np

# Step-1:
arr = np.zeros((4, 6), dtype=int)

# Step-2:
print("Shape of the array: ", arr.shape)
print("Size of the array: ", arr.size)

# Step-3: 
new_row = np.full((1, 6), 7)
arr = np.insert(arr, 2, new_row, axis=0)
print("\nArray after step-3:\n", arr)

# Step-4: Insert a new column as the 1st column where each element is 2.
new_col = np.full((arr.shape[0], 1), 2)
arr = np.insert(arr, 0, new_col, axis=1)
print("\nArray after step-4:\n", arr)

# Step-5: Sort the array row-wise
arr = np.sort(arr, axis=1)
print("\nArray after step-5:\n", arr)

# Step-6: Resize the array to shape (7,5) in row-major order
arr.resize((7, 5))
print("\nArray after step-6:\n", arr)

# Step-7: Flatten the array in column-major order
flat_arr = arr.flatten(order='F')
print("\nArray after step-7:", flat_arr)

# Step-8: Create a new one-dimensional array of shape (35) with all ones and add it
ones_arr = np.ones(35, dtype=int)
result = flat_arr + ones_arr
print("\nAfter step-8:", result)
