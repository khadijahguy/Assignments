# Creator : Khady Gueye

""" This program will return the next greater elemnt for each element in the given array. """

def next_greater_elements(arr):
    # Stack to track next greater elements
    stack = []
    # Result initialized with -1
    result = [-1] * len(arr)

    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        # Remove elements ≤ current
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        # Top of stack is next greater
        if stack:
            result[i] = stack[-1]
        # Add current to stack
        stack.append(arr[i])

    return result

# Driver Code
if __name__ == "__main__":
    arr = [2, 1, 4, 3]
    print("Sample Input:", arr)
    print("Sample Output:", next_greater_elements(arr))
