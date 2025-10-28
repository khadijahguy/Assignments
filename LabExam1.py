# Creator : Khady Gueye

""" This is ternary search algorithm program."""

def ternary_search(arr, target):
    def search(left, right):

        # If target is not found print this
        if left > right:
            return -1 
        
        # Dividing the range into 3 equal parts
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third
        
        # Checks for which midpoint the target is in
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Searches each segment
        if target < arr[mid1]:
            return search(left, mid1 - 1) # LEFT
        elif target > arr[mid2]:
            return search(mid2 + 1, right) # RIGHT
        else:
            return search(mid1 + 1, mid2 - 1) # MIDDLE
    
    return search(0, len(arr) - 1) # Search full range of the array

# Example
arr = [1,4,5,6,7,8,9,11,17,202,231,333,339,443]
print(ternary_search(arr, 11))
print(ternary_search(arr, 111)) 
