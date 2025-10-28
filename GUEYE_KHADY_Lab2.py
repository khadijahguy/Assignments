# Creator: Khady Gueye

""" This program finds the unique numbers in a list using brute force, dictionary, and XOR"""

def find_unique_brute_force(arr):
    # Define a function that takes a list 'arr'
    for i in range(len(arr)):
        # Loop each index i
        count = 0

        for j in range(len(arr)):
            # Loop again for j
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            # If appear once return it
            return arr[i]
    # If no matches, return none
    return None

def find_unique_ON_ON(arr):
    # Define a function that uses a dictionary to count frequencies.
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    # Loop over pairs in the disctionary 
    # if the count comes up once then it's unique, return it
    for num, count in freq.items():
        if count == 1:
            return num

    return None

def find_unique_ON_O1(arr):
    # Define a function that uses XOR to cancel out pairs.
    unique = 0
    # (x ^ 0 = x)
    for num in arr:
        unique ^= num
        # XOR it into unique and the pairs should cancel out
    return unique
    # Return the  unpaired numbers


# Driver Code
if __name__ == "__main__":

    test_cases = [
        [0, 2, -4, 5, 2, 0, -4],    # 5
        [3, 3, 3, 3, 6, 6, 7],      # 7
        [1, 1, 1, 1, 1, 1, 1, 1, 2],# 2
        [1, 0, 1, 2, 4, 2, 4],      # 0
        [3]                         # 3
    ]

    for arr in test_cases:
        # Loop through each test
        print("Array:", arr)
        print("Brute Force:", find_unique_brute_force(arr))
        print("O(n) with O(n):", find_unique_ON_ON(arr))
        print("O(n) with O(1):", find_unique_ON_O1(arr))
        print("-" * 40)