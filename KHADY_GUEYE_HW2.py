import time

def num_paths(m, n):
    # TODO: Task 1 of the assignment
    if m == 1 or n == 1:
        return 1
    return num_paths(m - 1, n) + num_paths(m, n - 1)

def num_paths_memo(m, n, memo={}):
    # TODO: Task 2 of the assignment
    if m == 1 or n == 1:
        return 1
    
    if (m, n) in memo:
        return memo[(m, n)]
    
    memo[(m, n)] = num_paths_memo(m - 1, n, memo) + num_paths_memo(m, n - 1, memo)
    return memo[(m, n)]


#driver code - you do not need to make any changes after this line.
#However, submit a screenshot of the output to report the execution time/elapsed time.
start_time = time.time()
print(num_paths(15,14))
end_time = time.time()

start_time_memo = time.time()
print(num_paths_memo(15,14))
end_time_memo = time.time()

print(f"Elapsed time (no memoization): {end_time - start_time} seconds")
print(f"Elapsed time (memoization): {end_time_memo - start_time_memo} seconds")
