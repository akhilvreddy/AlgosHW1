'''
Problem 1a

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README). 
output: Dictionary mapping students to hospitals. 
'''
def stable_matching_1a(file) -> dict:

    
    n = 0  # of docs and hospitals
    doctors_pref = [] 
    hospitals_pref = []

    #Extract doctor and hospital preferences
    with open(file, "r") as f:
        n = int(f.readline()) # # of docs and hospitals
        for _ in range(n):
            d_pref = f.readline().split() #read doc prefs and convert to integer 
            doctors_pref.append([int(x) for x in d_pref])

        # ^same process for hospitals 
        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
    # doctors to hospitals map
    pairs = {} 
    # SET of matched hospitals
    matched_hospitals = set()

    #while loop iterates over hospitals instead of doctors 
    while len(matched_hospitals) < n:
        # no for loops in lecture notes Gale-Shapley and other versions
        # loops through each hospital
        for h in range(n):
            if h not in matched_hospitals:  # looks at unmatched hospitals
                # hospital h requests next doctor on its list
                doc_preference = hospitals_pref[h].pop(0)

                # If the hospital's preference hasn't been matched
                if doc_preference not in pairs:
                    pairs[doc_preference] = h # match doc to hosp
                    matched_hospitals.add(h) # mark hosp as matched

                # If the hospital's preference already has a match
                else:
                    h2 = pairs[doc_preference] # current hospital doc is matched to
                    # indices of hospitals in doc's list 
                    h1_idx = doctors_pref[doc_preference].index(h) # index of new hospital
                    h2_idx = doctors_pref[doc_preference].index(h2) # index of current match
                    
                    # this might be backwards
                    #h1_idx and h2idx are indexing hospitals in doctor's perference list
                    #lower index would be more preferred
                    # formatting of input file means that the higher the index the less you prefer it
                    # Right now it is checking whether the doctor mathes their currently matched hospital but you should check if doctor prefers new hospital
                    # So h1idx < h2idx so doc switches to new assuming they prefer it
    
                    if h1_idx > h2_idx:
                        pairs[doc_preference] = h
                        matched_hospitals.add(h)
                        matched_hospitals.remove(h2)

    return pairs
