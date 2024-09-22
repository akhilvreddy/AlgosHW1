'''
Problem 5

input: List of tuples representing the friend's apartments.
output: List of apartment pairs.

TODO: implement your solution.
'''
from collections import deque
import heapq
# p5.py



def cookies_distrubution_map(apartments):
    n = len(apartments)
    eman_floor = (n + 1) // 2
    eman_index = (n + 1) // 2
    eman_apartment = (eman_floor, eman_index)
    
    all_apartments = [eman_apartment] + apartments
    
    visited = set()
    visited.add(eman_apartment)
    edges = []
    parent = {}
    
    # Add edges from Eman's apartment to all other apartments
    for apt in apartments:
        distance = abs(eman_apartment[0] - apt[0]) + abs(eman_apartment[1] - apt[1])
        heapq.heappush(edges, (distance, eman_apartment[0], eman_apartment[1], eman_apartment, apt[0], apt[1], apt))
    
    while edges and len(visited) < len(all_apartments):
        item = heapq.heappop(edges)
        distance = item[0]
        frm = item[3]
        to = item[6]
        if to in visited:
            continue
        visited.add(to)
        parent[to] = frm
        # Add edges from 'to' to unvisited apartments
        for apt in all_apartments:
            if apt not in visited:
                dist = abs(to[0] - apt[0]) + abs(to[1] - apt[1])
                heapq.heappush(edges, (dist, to[0], to[1], to, apt[0], apt[1], apt))
                
    delivery_plan = []
    for child, par in parent.items():
        delivery_plan.append((par, child))
    
    return delivery_plan
