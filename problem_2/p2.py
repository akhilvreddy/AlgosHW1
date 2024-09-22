'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
    # Sort intervals by finish time
    intervals.sort(key=lambda x: x[1])
    
    # Initialize J as all intervals
    J = intervals.copy()
    
    # Function to check if an interval is redundant
    def is_redundant(interval, others):
        start, end = interval
        coverage = set(range(start, end + 1))
        for other in others:
            if other != interval:
                other_start, other_end = other
                coverage -= set(range(other_start, other_end + 1))
            if not coverage:
                return True
        return False
    
    # Remove redundant intervals
    i = 0
    while i < len(J):
        if is_redundant(J[i], J):
            J.pop(i)
        else:
            i += 1
    
    # Check if J covers [0, M]
    coverage = set()
    for start, end in J:
        coverage.update(range(start, end + 1))
    
    if coverage != set(range(M + 1)):
        return None  # J doesn't cover [0, M]
    
    return J