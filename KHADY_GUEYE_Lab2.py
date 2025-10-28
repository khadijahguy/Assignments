# Creator: Khady Gueye

""" This program does 2 things, it finds the most frequently number in a list, and returnsthe smallest number. Aswell as, calculates the length of the longest sequence,"""

from collections import Counter

def most_frequent_element(numbers):
    # Returns the most frequently element in the list.
    count = Counter(numbers)
    max_frequency = max(count.values())
    candidates = [key for key, freq in count.items() if freq == max_frequency]
    return min(candidates)

def longest_sequence_length(numbers):
    # Returns the length of the longest sequence.
    if not numbers:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

# Examples
print(most_frequent_element([1, 3, 5, 4, 1, 1]))
print(most_frequent_element([5, 3, 5, 4, 4, 1]))

print(longest_sequence_length([1, 2, 3, 4, 4, 2, 2, 2]))
print(longest_sequence_length([1, 2, 3, 4, 5]))
