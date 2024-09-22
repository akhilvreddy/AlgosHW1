'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n^2).
'''
def most_frequent_difference_a(values, d_mode) -> int:
    n = len(values)
    count = 0

    for i in range(n):
        for j in range(n):
            if i == j: 
                continue
            delta = values[i] - values[j]
            if delta == d_mode:
                count += 1

    return count