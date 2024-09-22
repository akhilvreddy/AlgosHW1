'''
Problem 4b

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n log n).
'''
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict


def most_frequent_difference_b(values, d_mode) -> int:

    values.sort()
    count = 0
    frequency = {}

    for num in values:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    if d_mode == 0:
        for k in frequency:
            count += frequency[k] * (frequency[k] - 1)
    else:
        x = len(values)
        for i in range(x):
            target = values[i] + d_mode
            index = bisect_left(values, target)
            if index < x and values[index] == target:
                count += frequency[target]
    return count