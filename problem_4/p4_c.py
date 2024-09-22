'''
Problem 4c

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n).
'''
def most_frequent_difference_c(values, d_mode) -> int:
    from collections import Counter

    freq = Counter(values)
    count = 0

    if d_mode != 0:
        for x in freq:
            complement = x - d_mode
            if complement in freq:
                count += freq[x] * freq[complement]
    else:
        for x in freq:
            n = freq[x]
            count += n * (n - 1)

    return count