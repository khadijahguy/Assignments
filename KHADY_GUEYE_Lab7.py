file = open('lab7_words.txt')
words = file.read().splitlines()
file.close()
print('Number of words read:', len(words))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            print(f"Target = {target}, Found at index = {mid}, Number of iterations = {iterations}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print(f"Target = {target}, Found at index = -1, Number of iterations = {iterations}")
    return -1

target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()
