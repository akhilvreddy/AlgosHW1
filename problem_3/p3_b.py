'''
Problem 3b

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n. 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n log n) as described in the homework.
'''

def merge_and_count_large_inversions(arr, temp_arr, left, right, delta):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inv_count = 0
    
    inv_count += merge_and_count_large_inversions(arr, temp_arr, left, mid, delta)
    inv_count += merge_and_count_large_inversions(arr, temp_arr, mid + 1, right, delta)
    
    inv_count += merge_and_count(arr, temp_arr, left, mid, right, delta)
    
    return inv_count

def merge_and_count(arr, temp_arr, left, mid, right, delta):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0
    
    # Merge the two subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j] + delta:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There is a large inversion
            inv_count += (mid-i + 1)
            temp_arr[k] = arr[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def parse_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
    return n,arr


def number_of_large_inversions_3b(file_path, delta):
    n, arr = parse_input(file_path)
    temp_arr = [0]*n
    return merge_and_count_large_inversions(arr, temp_arr, 0, n-1, delta)
