# example of Empirical Performance analysis
import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

import random
# Benchmarking function
def measure_time(algorithm, n):
    times = []
    for _ in range(10):  # Run 10 iterations and take the median
        start = time.time()
        algorithm(n)
        times.append(time.time() - start)
    return np.median(times)

def stable_matching_1b(file) -> dict:
    n = 0
    doctors_pref = []
    hospitals_pref = []

    with open(file, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
    # doctors to hospitals map
    pairs = {} 
    matched_hospitals = set()

    # continues until all hospitals are matched 
    # For each hospital, it finds doctor they prefer and checks doctor's preference
    # Does this for n hospitals, iterates over n doctors, and then conducts pop and index functions which take O(n) so O(n^3)
    while len(matched_hospitals) < n:
        for h in range(n):
            if h not in matched_hospitals:

                # # operation below takes O(n) time 
                doc_preference = hospitals_pref[h].pop(0)

                # If the hospital's preference hasn't been matched
                if doc_preference not in pairs:
                    pairs[doc_preference] = h
                    matched_hospitals.add(h)

                # If the hospital's preference already has a match
                else:
                    h2 = pairs[doc_preference]
                    h1_idx = doctors_pref[doc_preference].index(h)
                    h2_idx = doctors_pref[doc_preference].index(h2)
                    ##^These lines use index function, which has time complexity of O(n)
                    if h1_idx < h2_idx:
                        pairs[doc_preference] = h
                        matched_hospitals.add(h)
                        matched_hospitals.remove(h2)

    return pairs


# Function for stable_matching_1c (Optimized)
def stable_matching_1c(file):
    n = 0
    doctors_pref = []
    hospitals_pref = []
    proposals = []
    doc_rankings = []

    with open(file, "r") as f:
        n = int(f.readline())
        proposals = [0] * n
        doc_rankings = [{} for _ in range(n)]

        for i in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])
            for rank, hospital in enumerate(doctors_pref[i]):
                doc_rankings[i][hospital] = rank

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])

    pairs = {}
    unmatched_hospitals = list(range(n))

    while unmatched_hospitals:
        h = unmatched_hospitals.pop(0)
        doc_preference = hospitals_pref[h][proposals[h]]
        proposals[h] += 1

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
# emperical analysis
# generaten_values that works for that sepecific question
# Function to generate random test input files for matching
def generate_test_file(n, filename):
    with open(filename, "w") as f:
        f.write(f"{n}\n")
        for _ in range(n):
            f.write(" ".join(map(str, random.sample(range(n), n))) + "\n")
        for _ in range(n):
            f.write(" ".join(map(str, random.sample(range(n), n))) + "\n")



# Instance sizes
n_values = np.logspace(1, 2, 10, dtype=int)  # Vary n from 10 to 100

# Generate test files for each n
for n in n_values:
    generate_test_file(n, f"test_{n}.txt")

# Measure performance for both implementations
times_1b = [measure_time(stable_matching_1b, f"test_{n}.txt") for n in tqdm(n_values, desc="1b Algorithm (Unoptimized)")]
times_1c = [measure_time(stable_matching_1c, f"test_{n}.txt") for n in tqdm(n_values, desc="1c Algorithm (Optimized)")]

# Plotting the results
plt.plot(n_values, times_1b, label='1b Algorithm (Unoptimized)', marker='o')
plt.plot(n_values, times_1c, label='1c Algorithm (Optimized)', marker='x')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Instance Size (n) - Log Scale')
plt.ylabel('Median Runtime (seconds)')
plt.title('Performance Analysis: 1b vs 1c Gale-Shapley Algorithm')
plt.legend()
plt.grid(True)
plt.show()
