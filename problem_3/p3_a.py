'''
Problem 3a

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n.
    example of file content:
    4
    2 4 1 3

    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n^2) as described in the homework.
'''
def number_of_large_inversions_3a(file, delta) -> int:
    
    with open(file, "r") as f:
        n = int(f.readline().strip()) # checking first line
        #parsing second line of file
        rankj = list(map(int,f.readline().split()))
    
   #For Debugging
    print(f"Input n = {n}, delta = {delta}")
    large_inversion_limit = 10  # Set a limit to print only a few inversions for debugging
    logged_inversions = 0


    # count # of large inversions 
    nli = 0
    
    #loop over pairs (x,y) s.t x <y
    for x in range(n):
        for y in range(x+1,n):
            # Check condition for large inversion
            if rankj[x] > (rankj[y] + delta ):
                nli += 1 #increment
     #           print(f"Large inversion found: rankj[{x}] = {rankj[x]}, rankj[{y}] = {rankj[y]} with delta = {delta}")
                # Only log the first few large inversions for debugging
                if logged_inversions < large_inversion_limit:
                    print(f"Large inversion: rankj[{x}] = {rankj[x]}, rankj[{y}] = {rankj[y]}")
                    logged_inversions += 1

                # Batch logging after every 1000 large inversions
                if nli % 1000 == 0:
                    print(f"Found {nli} large inversions so far...")


    # Final output of large inversions
    print(f"Total large inversions: {nli}")
    return nli