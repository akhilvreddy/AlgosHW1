'''
Problem 1c

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README).
output: Dictionary mapping students to hospitals. 

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
'''
def stable_matching_1c(file) -> dict:
    n=0
    doctors_pref = []
    hospitals_pref = []

    proposals = [] # Track next "proposal" for each hospital
    doc_rankings = [] #Ranks of hospitals for each doctor

    # Open File to Read
    
    with open(file,"r") as f:

        #Read # of docs/hospitals
        n = int(f.readline()) 
        #Initialize index for hospital "proposals"
        proposals = [0] * n
        #dictionaries to rank doctors
        doc_rankings = [{} for _ in range(n)]

        for i in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])
            #Compute doctor's rankings of hospitals 
            for rank, hospital in enumerate(doctors_pref[i]):
                doc_rankings[i][hospital] = rank

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
   # doctors to hospitals map
    pairs = {}
    unmatched_hospitals = list(range(n))

    

    while unmatched_hospitals:

        #unmatched hospital attempts to match w doctor
        h = unmatched_hospitals.pop(0)
        #increment so hospital tries to match with next doctor 
        doc_preference = hospitals_pref[h][proposals[h]]
        proposals[h] += 1

        #Doctor is not matched yet
        if doc_preference not in pairs:
                    pairs[doc_preference] = h

        else:
            h2 = pairs[doc_preference]
            
            h1_idx = doc_rankings[doc_preference][h]
            h2_idx = doc_rankings[doc_preference][h2]

            if h1_idx < h2_idx:
                pairs[doc_preference] = h
                unmatched_hospitals.append(h2)

    return pairs